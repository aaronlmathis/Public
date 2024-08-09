<#
.SYNOPSIS
A script to grant an O365 User FullAccess and Send As permissions to a group of mailboxes with Auto-Mapping disabled to prevent Outlook auto-mapping

.DESCRIPTION
A script to grant an O365 User FullAccess and Send As permissions to a group of mailboxes with Auto-Mapping disabled to prevent Outlook auto-mapping

.PARAMETER AdminUPN
UPN of an administrative account

.PARAMETER accessUPN
UPN of the account that needs FullAccess and Send As permissions

.PARAMETER Ignore
List of UPN's of mailboxes to ignore.

.EXAMPLE
./Grant-MailboxFullAccessAndSendAs.ps1 -AdminUPN admin@contoso.org -accessUPN john@contoso.org -Ignore eric@contoso.org,jane@contoso.org,mary@contoso.org

.NOTES

#>
# Call the function with parameters from the command line
[CmdletBinding()]
param (
    [Parameter(Mandatory = $true, Position = 0, HelpMessage = "Enter the admin user's UserPrincipalName")]
    [ValidateScript({
        if ($_ -match '^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$') {
            $true
        } else {
            throw "The AdminUPN value '$_' is not a valid email address."
        }
    })]
    [string]$AdminUPN,

    [Parameter(Mandatory = $true, Position = 1, HelpMessage = "Enter the UPN of the user that should have access to all mailboxes")]
    [ValidateScript({
        if ($_ -match '^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$') {
            $true
        } else {
            throw "The accessUPN value '$_' is not a valid email address."
        }
    })]
    [string]$accessUPN,

    [Parameter(Mandatory = $false, Position = 2, HelpMessage = "Enter a list of mailboxes to ignore")]
    [string[]]$Ignore
)


Function Grant-MailboxFullAccessAndSendAs(){

    param (
        [string]$AdminUPN,
        [string]$accessUPN,
        [string[]]$Ignore
    )

    try {

        if (!(Get-Module -ListAvailable -Name ExchangeOnlineManagement)) {
            Write-Host -ForegroundColor Yellow "ExchangeOnlineManagement module is not installed. Installing now..."
            Install-Module -Name ExchangeOnlineManagement -Force -Scope CurrentUser
        }

        Import-Module ExchangeOnlineManagement

        Write-Host -ForegroundColor Yellow "Connecting to Exchange Online"
        Connect-ExchangeOnline -UserPrincipalName $AdminUPN -ShowBanner:$false

        # Get all mailboxes
        $mailboxes = Get-Mailbox -ResultSize Unlimited
        $mailBoxCount = $mailboxes.count
        $count = 1
        foreach ($mailbox in $mailboxes) {
            # Skip if the mailbox is the admin's own mailbox
            if ($mailbox.PrimarySmtpAddress -ne $AdminUPN -and -not ($Ignore -contains $mailbox.PrimarySmtpAddress)) {
                # Add Full Access permissions with auto-mapping disabled
                Add-MailboxPermission -Identity $mailbox.PrimarySmtpAddress -User $accessUPN -AccessRights FullAccess -AutoMapping:$false
                Write-Host -ForegroundColor Cyan "Granted Full Access (with auto-mapping disabled) to $accessUPN for mailbox: $($mailbox.PrimarySmtpAddress) [$($count)/$($mailBoxCount)]"

                # Add Send As permissions
                Add-RecipientPermission -Identity $mailbox.PrimarySmtpAddress -Trustee $accessUPN -AccessRights SendAs -Confirm:$false
                Write-Host -ForegroundColor Cyan "Granted Send As permissions to $accessUPN for mailbox: $($mailbox.PrimarySmtpAddress) [$($count)/$($mailBoxCount)]"
            } else {
                Write-Host -ForegroundColor DarkYellow "Skipping mailbox: $($mailbox.PrimarySmtpAddress) [$($count)/$($mailBoxCount)]"
            }
            $count++
        }
        
        Write-Host -ForegroundColor Green "Script completed successfully."
    }
    catch {
        Write-Host -ForegroundColor Red "An error occurred: $_"
    }

    # Disconnect from Exchange Online
    Disconnect-ExchangeOnline -Confirm:$false
}

Grant-MailboxFullAccessAndSendAs -AdminUPN $AdminUPN -accessUPN $accessUPN -Ignore $Ignore
