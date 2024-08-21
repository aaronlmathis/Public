# Define the output CSV file
$outputFile = "C:\ADUsersExport.csv"

# Get all users from Active Directory
$users = Get-ADUser -Filter * -Property DisplayName, SamAccountName, EmailAddress, Department, Title

# Initialize the progress bar
$totalUsers = $users.Count
$currentUser = 0

# Create an array to store the user data
$userData = @()

# Iterate over each user and add their details to the array
foreach ($user in $users) {
    $userData += New-Object PSObject -Property @{
        DisplayName     = $user.DisplayName
        SamAccountName  = $user.SamAccountName
        EmailAddress    = $user.EmailAddress
        Department      = $user.Department
        Title           = $user.Title
    }
    
    # Update the progress bar
    $currentUser++
    Write-Progress -Activity "Exporting Users" -Status "Processing $currentUser of $totalUsers" -PercentComplete (($currentUser / $totalUsers) * 100)
}

# Export the data to a CSV file
$userData | Export-Csv -Path $outputFile -NoTypeInformation

Write-Host "Export complete. File saved to $outputFile"