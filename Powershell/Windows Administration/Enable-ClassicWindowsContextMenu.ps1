
function Enable-ClassicWindowsContextMenu(){
    try {
        # Define the path to the new key
        $regPath = "HKCU:\SOFTWARE\CLASSES\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32"
        
        # Create the new key
        New-Item -Path $regPath -Force -ErrorAction Stop
        
        # Set the default value to an empty string
        Set-ItemProperty -Path $regPath -Name "(default)" -Value "" -ErrorAction Stop
    
        # Provide feedback
        Write-Output "Registry keys set successfully."
        Write-Output -ForegroundColor Yellow "Restarting Explorer"
    
        # Restart Windows Explorer to apply changes
        Stop-Process -Name explorer -Force
    
        # Small pause to ensure Explorer has time to stop
        Start-Sleep -Seconds 1
    
        Start-Process explorer
    
        Write-Output "Classic context menu enabled successfully."
    } catch {
        Write-Error "An error occurred: $_"
    }
}

Enable-ClassicWindowsContextMenu()