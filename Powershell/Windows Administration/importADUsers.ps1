# Path to the CSV file
$csvFile = "C:\ADUsersExport.csv"

# Default password for all new users
$defaultPassword = ConvertTo-SecureString "PassforDHC@1" -AsPlainText -Force

# Import the CSV file
$users = Import-Csv -Path $csvFile

# Initialize progress bar
$totalUsers = $users.Count
$currentUser = 0

foreach ($user in $users) {
    # Generate the user's name and other AD fields
    $samAccountName = $user.SamAccountName
    $displayName = $user.DisplayName
    $emailAddress = $user.EmailAddress
    $department = $user.Department
    $title = $user.Title

    # Set the user account properties
    $userParams = @{
        SamAccountName            = $samAccountName
        Name                      = $displayName
        DisplayName               = $displayName
        UserPrincipalName         = "$samAccountName@yourdomain.com"  # Replace with your domain
        EmailAddress              = $emailAddress
        Department                = $department
        Title                     = $title
        AccountPassword           = $defaultPassword
        PasswordNeverExpires      = $false
        ChangePasswordAtLogon     = $true
        Enabled                   = $true
        Path                      = "OU=Users,DC=yourdomain,DC=com"  # Replace with your OU and domain
    }

    # Create the user in AD
    try {
        New-ADUser @userParams
        Write-Host "Created user: $displayName ($samAccountName)"
    } catch {
        Write-Host "Failed to create user: $displayName ($samAccountName) - $_" -ForegroundColor Red
    }

    # Update the progress bar
    $currentUser++
    Write-Progress -Activity "Creating Users" -Status "Processing $currentUser of $totalUsers" -PercentComplete (($currentUser / $totalUsers) * 100)
}

Write-Host "User creation process completed."
