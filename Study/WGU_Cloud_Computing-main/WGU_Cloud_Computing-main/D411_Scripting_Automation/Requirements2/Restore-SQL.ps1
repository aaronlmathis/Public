# Bryon Smith 011185815

$dbType = "Microsoft.SqlServer.Management.Smo.Database"
$dbName = "ClientDB"
$sqlInstanceName = "SRV19-PRIMARY\SQLEXPRESS"
$tableName = "Client_A_Contacts"
try {
  # Remove old sql module due to function conflicts.
  if (Get-Module -Name sqlps) { Remove-Module sqlps }
  # install new sql module.
  Import-Module -Name SqlServer

  # If database exist, drop it.
  if (Get-SqlDatabase -Name $dbName -ServerInstance $sqlInstanceName -ErrorAction SilentlyContinue) {
    # Drop Database.
    $dropQuery = "ALTER DATABASE $($dbName) SET SINGLE_USER WITH ROLLBACK IMMEDIATE; `
                      USE master; `
                      DROP DATABASE $($dbName)"
    Invoke-Sqlcmd -ServerInstance $sqlInstanceName -Database $dbName -Query $dropQuery
    Write-Host -ForegroundColor Red "$($dbName) exist and has been dropped!"
  } else {
    Write-Host "$($dbName) does not exist. Creating..."
  }
  # Create SQL database
  $dbObject = New-Object -TypeName $dbType -ArgumentList $sqlInstanceName, $dbName
  $dbObject.Create()
  Write-Host -ForegroundColor Cyan "$($dbName) databse was created."
  # Create the table from SQL file
  Invoke-Sqlcmd -ServerInstance $sqlInstanceName -Database $dbName -InputFile $PSScriptRoot\CreateTable_CreateCustomerLeads.sql
  Write-Host -ForegroundColor DarkYellow "$($tableName) table was created."
  # Get Customer_Leads data from csv
  $customer_leads = Import-Csv $PSScriptRoot\NewClientData.csv
  $AllUsers = $customer_leads.count
  $count = 1
  $Insert = "INSERT INTO [$($tableName)] (first_name, last_name, city, county, zip, officePhone, mobilePhone)"
  ForEach ($u in $customer_leads) {
    # Show progress indeicator.
    $progress = "[SQL]: Adding new SQL user $($u.first_name) $($u.last_name). $($count) of $($AllUsers)"
    Write-Progress -Activity "D411 Restore SQL DB" -Status $progress -PercentComplete (($count / $AllUsers) * 100)
    $Values = "VALUES ( `
                '$($u.first_name)', `
                '$($u.last_name)', `
                '$($u.city)', `
                '$($u.county)', `
                '$($u.zip)', `
                '$($u.officePhone)', `
                '$($u.mobilePhone)')"
        
    # Add Insert statement to database.
    $query = $Insert + $Values
    Invoke-Sqlcmd -Database $dbName -ServerInstance $sqlInstanceName -Query $query
    $count++
  }

  Invoke-Sqlcmd -Database $dbName –ServerInstance $sqlInstanceName -Query "SELECT * FROM dbo.$($tableName)" > .\SqlResults.txt
  Write-Host -ForegroundColor Green "$($dbName) database has been built with no errors! SqlResults file has been created."
}
catch {
  Write-Host "Something went wrong!"
  Write-Host $_
}