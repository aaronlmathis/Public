<#
.SYNOPSIS
A function to copy all folders located within the C:\Users directory to a destination directory located on the same USB flash drive the script is run from.

.DESCRIPTION


.PARAMETER Ignore
A list of folders or files to ignore, separated by comma.
For Example: -Ignore "Apps,TMP,hello.txt"

.PARAMETER destFolder
Destination folder on the removeable media in which to copy the files to.



.EXAMPLE
.\Export-UserDir.ps1 -DestFolder 'backups' -Ignore "AppData,TMP" -Verbose

.NOTES

#>


[CmdletBinding()]
param (
    [Parameter(Mandatory = $true, Position = 0, HelpMessage = "Enter the destination directory.")]
    [string]$destFolder,
    [Parameter(Mandatory = $false, Position = 1, HelpMessage = "Enter the path of the directories/files to ignore")]
    [string]$Ignore
)


function Export-UserDir (){
    param (
        [string]$destFolder,
        [string]$Ignore,
        [string]$scriptPath
    )
    
    # Split the ignore parameter into an array
    $ignorePaths = @()
    if ($Ignore) {
        $ignorePaths = $Ignore.Split(",")
    }
    
    # Get the script's location (assuming it's on the USB drive)

    $usbDrive = Split-Path $scriptPath -Parent

    # Define the destination folder on the USB drive
    $destinationFolder = Join-Path $usbDrive $destFolder
    
    # Ensure the destination folder exists
    if (-Not (Test-Path $destinationFolder)) {
        New-Item -Path $destinationFolder -ItemType Directory
    }
    
    # Get all files and directories under C:\Users\
    $sourceFolder = "C:\Users\"
    $itemsToCopy = Get-ChildItem -Path $sourceFolder -Recurse
    
    $count = 1
    $itemsCount = $itemsToCopy.count
    $copiedCount = 0
    $ignoredCount = 0

    write-host -ForegroundColor yellow "Starting transfer of $($itemsCount) items."
    foreach ($item in $itemsToCopy) {
        # Determine the relative path to the item
        $relativePath = $item.FullName.Substring($sourceFolder.Length)
        
        # Check if the item is in the ignore list
        $ignoreItem = $false
        foreach ($ignorePath in $ignorePaths) {
            if ($relativePath -like $ignorePath) {
                $ignoreItem = $true
                Write-Verbose "Skipping Item: $($item.FullName)"
                $ignoredCount++
                break
            }
        }
    
        if (-Not $ignoreItem) {
            # Construct the destination path
            $destinationPath = Join-Path $destinationFolder $relativePath
            
            # Create the directory structure if it doesn't exist
            $destinationDir = Split-Path $destinationPath -Parent
            if (-Not (Test-Path $destinationDir)) {
                New-Item -Path $destinationDir -ItemType Directory -Force
            }
    
            # Copy the item
            Copy-Item -Path $item.FullName -Destination $destinationPath -Force
            Write-Verbose  "Copying Item: $($item.FullName)"
            $copiedCount++
        }

        #Write Progress Bar
        $progress = "[]: Copying: $($item.FullName) [$($count)/$($itemsCount)]"
        Write-Progress -Activity "Copying Users Directory" -Status $progress -PercentComplete (($count / $itemsCount) * 100)
    }
      
    Write-Host -ForegroundColor Green "Backup completed."
    Write-Host -ForegroundColor cyan "$($copiedCount) Items successfully copied."
    Write-Host -ForegroundColor Yellow "$($ignoredCount) Items ignored."
    
}

Export-UserDir -destFolder $destFolder -Ignore $ignore -ScriptPath $MyInvocation.MyCommand.Path 