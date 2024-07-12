Function Enable-AutoEnrollMDM(){

    # Define the registry path and value
    $RegistryPath = "HKLM:\Software\Policies\Microsoft\Windows\CurrentVersion\MDM"
    $ValueName = "AutoEnrollMDM"
    $Value = 1

    # Check if the registry path exists, if not, create it
    if (-not (Test-Path $RegistryPath)) {
        New-Item -Path $RegistryPath -Force
    }

    # Set the registry value
    Set-ItemProperty -Path $RegistryPath -Name $ValueName -Value $Value

    # Verify the registry value is set
    Get-ItemProperty -Path $RegistryPath -Name $ValueName
}

Enable-AutoEnrollMDM