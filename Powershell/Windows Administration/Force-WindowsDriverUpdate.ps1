function Force-WindowsDriverUpdate(){
    # Set the execution policy temporarily to allow script execution
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine -Force
    try{
        if (!(Get-Module -ListAvailable -Name PSWindowsUpdate)) {
            Write-Host -ForegroundColor Yellow "PSWindowsUpdate module is not installed. Installing now..."
            Install-Module -Name PSWindowsUpdate -Force -SkipPublisherCheck 
        }
        Get-WindowsUpdate -AcceptAll -Install -IgnoreReboot
    }catch {
        Write-Host -ForegroundColor Red "An error occurred: $_"
    }
    Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope LocalMachine -Force
}



# Check if the PSWindowsUpdate is installed
if (Get-Module -ListAvailable | Where-Object { $_.Name -eq "PSWindowsUpdate" }) {
} else {
    Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
    Install-Module -Name PSWindowsUpdate -Force
    Import-Module PSWindowsUpdate
}

# Install Windows updates, accepting all updates and ignoring reboots


# Restore the original execution policy
