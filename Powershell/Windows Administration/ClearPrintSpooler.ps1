# Ensure the script is running as Administrator
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)) {
    Write-Host "This script must be run as Administrator. Exiting..."
    Pause
    Exit
}

Write-Host "`n=== Stopping the Print Spooler service... ==="
try {
    Stop-Service -Name spooler -Force -ErrorAction Stop
    Write-Host "Print Spooler service stopped successfully."
}
catch {
    Write-Host "ERROR: Failed to stop the Print Spooler service."
    Pause
    Exit
}

# Define the spool directory
$spoolDir = "C:\Windows\System32\spool\PRINTERS"

Write-Host "`n=== Deleting files from $spoolDir ==="
try {
    # Remove all files from the directory
    Get-ChildItem -Path $spoolDir -File | ForEach-Object {
        Write-Host "Deleting file: $($_.FullName)"
        Remove-Item -Path $_.FullName -Force -ErrorAction Stop
    }
    Write-Host "All files successfully deleted."
}
catch {
    Write-Host "ERROR: Some files could not be deleted. Ensure no processes are locking them."
}

Write-Host "`n=== Print Spooler cleanup complete. ==="

# Uncomment the next two lines to automatically restart the Print Spooler
# Write-Host "`nRestarting Print Spooler service..."
# Start-Service -Name spooler -ErrorAction SilentlyContinue
# Write-Host "Print Spooler service restarted successfully."

Write-Host "`nProcess complete."
Pause