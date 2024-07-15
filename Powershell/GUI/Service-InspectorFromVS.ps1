Add-Type -AssemblyName PresentationFramework
$xamlFile = "C:\Users\aaron_bawwa88\OneDrive\Documents\GitHub\Public\Powershell\GUI\MainWindow.xaml"
$inputXAML = Get-Content -PAth $xamlFile -Raw
$inputXAML = $inputXAML -replace 'mc:Ignorable="d"','' -replace "x:N","N" -replace '^<Win.*','<Window'
[XML]$XAML = $inputXAML

$reader = New-Object System.Xml.XmlNodeReader $XAML
try{
    $psform = [Windows.Markup.XamlReader]::Load($reader)
} catch {
    Write-Host $_.Exception
    throw
}

$xaml.SelectNodes("//*[@Name]") | ForEach-Object {
    try {
        Set-Variable -Name "var_$($_.Name)" -Value $psform.FindName($_.Name) -ErrorAction Stop
    } catch {
        throw
    }
}

Get-Variable var_*

Get-Service | ForEach-Object {$var_ddlServices.Items.Add($_.Name)}

function GetDetails {
    $ServiceName = $var_ddlServices.SelectedItem
    write-host $ServiceName
    $details = Get-Service -Name $ServiceName | select *
    $var_lblName.Content = $details.name
    $var_lblStatus.Content = $details.Status

    if($var_lblStatus.Content -eq 'Running') {
        $var_lblStatus.Foreground = "Green"
    } else {
        $var_lblStatus.Foreground = "Red"
    }    
}

$var_ddlServices.Add_SelectionChanged({GetDetails})

$psform.ShowDialog()