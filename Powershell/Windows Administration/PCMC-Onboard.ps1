#Create PCMC account
function New-PCMCAccount(){
    try{
        # Create a secure password
        $password = Read-Host -AsSecureString "Enter the password for the new user"
        # Create the new user with the password, never expires
        New-LocalUser -Name "PCMC" -Description "PCMC Admin Account" -Password $password
        Set-LocalUser -Name "PCMC" -PasswordNeverExpires $true
        # Add the new user to the Administrators group
        Add-LocalGroupMember -Group "Administrators" -Member "PCMC"

        Write-Host -ForegroundColor yellow "PCMC Admin user created..."
    } catch{
        Write-Host "An error occurred: $_" -ForegroundColor Red
    }
}
#Install Updates

function Force-WindowsDriverUpdate(){
    write-host -ForegroundColor Cyan "Starting Windows Update..."
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

function Set-CommonConfigs() {
    try {
        write-host -ForegroundColor yellow "Setting common configurations..."
        write-host -ForegroundColor yellow "Turning off sleep when plugged in..."
        #Set sleep to never
        powercfg -change -standby-timeout-ac 0
        
        # Define the registry path and value name
        $sleepRegistryPath = "HKLM:\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\238C9FA8-0AAD-41ED-83F4-97BE242C8F20\7bc4a2f9-d8fc-4469-b07b-33eb785aaca0"
        $sleepValueName = "Attributes"

        # Set the Attributes value to 2 to disable sleep
        Set-ItemProperty -Path $sleepRegistryPath -Name $sleepValueName -Value 2
        Write-Host -ForegroundColor yellow "Sleep feature disabled by setting $sleepValueName to 2 in $sleepRegistryPath."

        #Disable Hover
        # Define the registry path and value name
        $hoverRegistryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        $hoverValueName = "ExtendedUIHoverTime"

        # Create the DWORD value and set it to 0 to disable hover
        New-ItemProperty -Path $hoverRegistryPath -Name $hoverValueName -PropertyType DWORD -Value 0 -Force | Out-Null
        Write-Host -ForegroundColor yellow "Hover feature disabled by setting $hoverValueName to 0 in $hoverRegistryPath."


    }catch {
        Write-Host -ForegroundColor Red "An error occurred: $_"
    }
}

function Remove-WindowsApps(){
    write-host -ForegroundColor Yellow "Removing windows apps..."

    try {
            # Define a list of app names or partial names to uninstall
        $appsToRemove = @(
            "*xbox*",
            "*yourphone*",
            "*zunevideo*",
            "*zunemusic*"
        )

        # Uninstall apps for the current user
        foreach ($app in $appsToRemove) {
            Get-AppxPackage -Name $app | Remove-AppxPackage
            Write-Host -ForegroundColor yellow "Uninstalled $app for the current user."
        }

        # Remove provisioned apps for all future users
        foreach ($app in $appsToRemove) {
            Get-AppxProvisionedPackage -Online | Where-Object DisplayName -like $app | Remove-AppxProvisionedPackage -Online
            Write-Host -ForegroundColor yellow "Removed $app for all future users."
        }
    }catch {
        Write-Host -ForegroundColor Red "An error occurred: $_"
    }
}

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

write-host -ForegroundColor yellow "Starting PCMC Onboarding Script:"

New-PCMCAccount

Set-CommonConfigs

Remove-WindowsApps

Force-WindowsDriverUpdate


