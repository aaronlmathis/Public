function Force-WindowsDriverUpdate(){
    try{
        if (!(Get-Module -ListAvailable -Name PSWindowsUpdate)) {
            Write-Host -ForegroundColor Yellow "PSWindowsUpdate module is not installed. Installing now..."
            Install-Module -Name PSWindowsUpdate -Force -SkipPublisherCheck 
        }
        Get-WindowsUpdate
        Install-WindowsUpdate -AcceptAll -AutoReboot
    }catch {
        Write-Host -ForegroundColor Red "An error occurred: $_"
    }
}
