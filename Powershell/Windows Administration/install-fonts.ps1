# Define the download URL and target paths
$DownloadUrl = "https://download.microsoft.com/download/8/6/0/860a94fa-7feb-44ef-ac79-c072d9113d69/Microsoft%20Aptos%20Fonts.zip"
$DownloadPath = "$env:TEMP\MicrosoftAptosFonts.zip"
$ExtractPath = "$env:TEMP\MicrosoftAptosFonts"
$FontsPath = "$env:SystemRoot\Fonts"

# Download the ZIP file
Write-Host "Downloading the font package..." -ForegroundColor Cyan
Invoke-WebRequest -Uri $DownloadUrl -OutFile $DownloadPath -UseBasicParsing

# Check if the file downloaded successfully
if (-not (Test-Path $DownloadPath)) {
    Write-Error "Failed to download the font package. Please check the URL."
    exit 1
}

# Unzip the file
Write-Host "Extracting the font files..." -ForegroundColor Cyan
if (-not (Test-Path $ExtractPath)) {
    New-Item -ItemType Directory -Path $ExtractPath | Out-Null
}
Expand-Archive -Path $DownloadPath -DestinationPath $ExtractPath -Force

# Get all font files from the extracted folder
$FontFiles = Get-ChildItem -Path $ExtractPath -Recurse -Include *.ttf, *.otf

if ($FontFiles.Count -eq 0) {
    Write-Error "No font files were found in the extracted package."
    exit 1
}

# Install the fonts by copying them to the Fonts folder and registering them
Write-Host "Installing fonts..." -ForegroundColor Cyan
foreach ($FontFile in $FontFiles) {
    $DestinationFontPath = Join-Path -Path $FontsPath -ChildPath $FontFile.Name

    if (-not (Test-Path $DestinationFontPath)) {
        Copy-Item -Path $FontFile.FullName -Destination $DestinationFontPath
        # Add the font to the registry to make it available system-wide
        $FontName = $FontFile.BaseName
        $RegistryPath = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"
        Set-ItemProperty -Path $RegistryPath -Name "$FontName (TrueType)" -Value $FontFile.Name
        Write-Host "Installed $FontName" -ForegroundColor Green
    } else {
        Write-Host "Font $($FontFile.Name) is already installed." -ForegroundColor Yellow
    }
}

# Cleanup temporary files
Write-Host "Cleaning up..." -ForegroundColor Cyan
Remove-Item -Path $DownloadPath -Force
Remove-Item -Path $ExtractPath -Recurse -Force

Write-Host "Font installation completed!" -ForegroundColor Green
