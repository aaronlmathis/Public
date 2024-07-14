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