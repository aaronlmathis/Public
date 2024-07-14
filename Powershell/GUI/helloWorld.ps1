# Load the Windows Forms assembly
Add-Type -AssemblyName System.Windows.Forms

# Create a form and a label object
$FormObject = [System.Windows.Forms.Form]
$LabelObject = [System.Windows.Forms.Label]
$ButtonObject = [System.Windows.Forms.Button]

# Create a new instance of the form
$HelloWorldForm = New-Object $FormObject

#Set properties of form
$HelloWorldForm.ClientSize='500,300'
$HelloWorldForm.Text = 'Hello World!'
$HelloWorldForm.BackColor="#FFFFFF"

#Create instance of Button
$btnHello = New-Object $ButtonObject
$btnHello.Text = 'Say Hello!'
$btnHello.Autosize = $true
$btnHello.Location = New-Object System.Drawing.Point(185,180)
$btnHello.Font = 'Verdana,14'

#Create instance of Label
$lbltitle = New-Object $LabelObject

#Set properties of Label
$lbltitle.Text = 'Hello World!'
$lbltitle.Autosize = $true
$lbltitle.Font = "Verdana,24,Style=Bold"
$lbltitle.ForeColor = 'Black'
$lbltitle.location = New-Object System.Drawing.Point(120,110)

#Add Controls
$HelloWorldForm.Controls.AddRange(@($lbltitle,$btnHello))

#LOGIC section / functions
function Say-Hello(){
    if($lbltitle.ForeColor -eq 'Black'){
        $lbltitle.ForeColor = "Red"
    } else {
        $lbltitle.ForeColor = "Black"
    }
}

$btnHello.Add_Click({Say-Hello})

#Display Form
$HelloWorldForm.ShowDialog()

#Cleans up Form
$HelloWorldForm.dispose()

