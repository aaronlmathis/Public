<#
.SYNOPSIS
A function to effectively remove every trace of Webroot from a Windows 10/11 machine.

.DESCRIPTION
This function checks for the presence of Webroot in common installation directories,
runs the silent uninstaller if found, and cleans up any remaining entries in the SecurityCenter2 namespace.

.PARAMETER Name
No parameters are required for this function.

.EXAMPLE
Remove-Webroot
This will remove Webroot from the machine if it is installed.

.NOTES
This script requires administrative privileges.
#>

function Remove-Webroot {
    # Check for the presence of Webroot in possible directories
    $webrootPaths = @(
        "C:\Program Files\Webroot\WRSA.exe",
        "C:\Program Files (x86)\Webroot\WRSA.exe"
    )

    $webrootPath = $webrootPaths | Where-Object { Test-Path $_ }

    if ($webrootPath) {
        Write-Output "Webroot found at $webrootPath"

        try {
            # Run the silent uninstaller
            Write-Output "Running the silent uninstaller..."
            & "$webrootPath" -uninstall /silent

            # Wait for a few moments to allow the uninstallation to complete
            Start-Sleep -Seconds 30

            # Check if Webroot is still present
            if (Test-Path $webrootPath) {
                Write-Output "Uninstallation might have failed or is still in progress."
            } else {
                Write-Output "Webroot uninstalled successfully."
            }
        } catch {
            Write-Output "An error occurred during the uninstallation: $_"
        }
    } else {
        Write-Output "Webroot not found on this machine."
    }

    # Clean up SecurityCenter regardless of whether WRSA.exe was found.
    try {
        # Run CIM instance to check for remaining Webroot entries
        $avProducts = Get-CimInstance -Namespace root\SecurityCenter2 -Class AntiVirusProduct
        $webrootProduct = $avProducts | Where-Object { $_.displayName -eq "Webroot SecureAnywhere" }

        if ($webrootProduct) {
            Write-Output "Webroot SecureAnywhere found in SecurityCenter2. Removing..."
            $webrootProduct | ForEach-Object { 
                Remove-CimInstance -InputObject $_
            }
            Write-Output "Webroot SecureAnywhere entry removed from SecurityCenter2."
        } else {
            Write-Output "No Webroot SecureAnywhere entry found in SecurityCenter2."
        }
    } catch {
        Write-Output "An error occurred while cleaning up SecurityCenter: $_"
    }
}

# Call the function to remove Webroot
Remove-Webroot
