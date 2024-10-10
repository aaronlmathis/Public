# Install Microsoft Graph if not already installed
#Install-Module Microsoft.Graph -Force -AllowClobber

# Connect to Microsoft Graph
Connect-MgGraph -Scopes User.ReadWrite.All

# Path to your CSV file
$csvFilePath = ""

# Read the CSV file
$fullNames = Import-Csv -Path $csvFilePath

# Initialize counters for the summary
$licensesRemovedCount = 0
$usersNotFoundCount = 0
$usersWithNoLicenseCount = 0
$totalNamesRead = $fullNames.Count

# Loop through each full name and remove licenses
foreach ($user in $fullNames) {
    $fullName = $user.'full name'

    # Get the user by Display Name
    $userAccount = Get-MgUser -Filter "displayName eq '$fullName'"

    if ($userAccount) {
        # Get all assigned licenses
        $assignedLicenses = Get-MgUserLicenseDetail -UserId $userAccount.Id

        if ($assignedLicenses) {
            # Extract all SkuIds to remove
            $removeLicenses = $assignedLicenses | ForEach-Object { $_.SkuId }

            # Remove all licenses (addLicenses must be an empty array)
            Set-MgUserLicense -UserId $userAccount.Id -AddLicenses @() -RemoveLicenses $removeLicenses

            Write-Host "Removed all licenses from $($userAccount.DisplayName)"
            $licensesRemovedCount++
        } else {
            Write-Host "No licenses found for $($userAccount.DisplayName)."
            $usersWithNoLicenseCount++
        }
    } else {
        Write-Host "User with Display Name '$fullName' not found."
        $usersNotFoundCount++
    }
}

# Disconnect from Microsoft Graph
Disconnect-MgGraph

# Display summary
Write-Host "Summary:"
Write-Host "Total names read from CSV: $totalNamesRead"
Write-Host "Total licenses removed: $licensesRemovedCount"
Write-Host "Users not found: $usersNotFoundCount"
Write-Host "Users with no licenses: $usersWithNoLicenseCount"
