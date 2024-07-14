Add-Type -AssemblyName System.Windows.Forms

$FormObject = [System.Windows.Forms.Form]
$LabelObject = [System.Windows.Forms.Label]
$ComboBoxObject = [System.Windows.Forms.ComboBox]

$DefaultFont = 'Verdana, 12'

$AppForm = New-Object $FormObject

## Set Up Base Form
$AppForm.ClientSize = '500, 300'
$AppForm.Text = 'DeepThought - Service Inspector'
$AppForm.BackColor = "#FFFFFF"
$AppForm.Font = $DefaultFont

#Building the Label
$lblService = New-Object $LabelObject
$lblService.Text = "Services :"
$lblService.Autosize = $true
$lblService.Location  = New-Object System.Drawing.Point(20,20)



#Building Combo Box
$ddlService = New-Object $ComboBoxObject
$ddlService.width = '300'
$ddlService.Location = New-Object System.Drawing.Point(125,20)

#Load Drop Down List for Services
Get-Service | ForEach-Object {$ddlService.Items.Add($_.Name)}

$ddlService.Text = 'Pick a service'

#Building the Label
$lblForName = New-Object $LabelObject
$lblForName.Text = "Service Friendly Name :"
$lblForName.Autosize = $true
$lblForName.Location  = New-Object System.Drawing.Point(20,80)

#Building the Label
$lblName = New-Object $LabelObject
$lblName.Text = ""
$lblName.Autosize = $true
$lblName.Location  = New-Object System.Drawing.Point(240,80)

#Building the Label for Status
$lblForStatus = New-Object $LabelObject
$lblForStatus.Text = "Status :"
$lblForStatus.Autosize = $true
$lblForStatus.Location  = New-Object System.Drawing.Point(20,120)

#Building the Label status
$lblStatus= New-Object $LabelObject
$lblStatus.Text = ""
$lblStatus.Autosize = $true
$lblStatus.Location  = New-Object System.Drawing.Point(240,120)


$AppForm.Controls.AddRange($($lblService,$ddlService,$lblForName,$lblName,$lblForStatus,$lblStatus))

#Add Functions to the form
function GetServiceDetails {
    $ServiceName = $ddlService.SelectedItem
    $details = Get-Service -Name $ServiceName | Select DisplayName,Status
    $lblname.Text = "$($details.DisplayName)"
    $lblStatus.Text = "$($details.Status)"
    if($details.Status -eq 'Running') {
        $lblStatus.ForeColor = "Green"
    } else {
        $lblStatus.ForeColor = "Red"
    }
}

#Add Function to controls.
$ddlService.Add_SelectedIndexChanged({GetServiceDetails})

#Show Form
$AppForm.ShowDialog()

#Clean Up Form
$AppForm.dispose()
