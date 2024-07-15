[CmdletBinding()]
param (
        [Parameter(Mandatory = $true, Position = 0, HelpMessage = "Enter the full path to the CSV file containing VM information")]
        [string]$FilePath
)
function Create-VMFromCSV {
    param (
        [Parameter(Mandatory=$true)]
        [System.Collections.ArrayList]$vms
    )

    foreach($VmObject in $vms){
        # Create a new VM
        write-host -ForegroundColor Yellow "Creating new Virtual Machine: $($VmObject.name)"
       
        New-VM  $VmObject.Name
        # Set the CPU and start-up RAM
        Set-VM $VmObject.Name -ProcessorCount $VmObject.Cpu -MemoryStartupBytes $VmObject.Ram 

        # Create the new VHDX disk - the path and size.
        New-VHD -Path "$($VmObject.PathToDisk)\$($VmObject.Name)-disk1.vhdx" -SizeBytes $VmObject.DiskSize
        # Add the new disk to the VM
        Add-VMHardDiskDrive -VMName $VmObject.Name -Path "$($VmObject.PathToDisk)\$($VmObject.Name)-disk1.vhdx"
        # Assign the OS ISO file to the VM
        Set-VMDvdDrive -VMName $VmObject.Name -Path $VmObject.Image
        # Remove the default VM NIC named 'Network Adapter'
        Remove-VMNetworkAdapter -VMName $VmObject.Name
        # Add a new NIC to the VM and set its name
        Add-VMNetworkAdapter -VMName $VmObject.Name -Name $VmObject.Port
        # Configure the NIC as access and assign VLAN
        Set-VMNetworkAdapterVlan -VMName $VmObject.Name -VMNetworkAdapterName $VmObject.Port -Access -AccessVlanId $VmObject.Vlan
        # Connect the NIC to the vswitch
        Connect-VMNetworkAdapter -VMName $VmObject.Name -Name $VmObject.Port -SwitchName $VmObject.VSwitch
        # Fire it up
        Start-VM $VmObject.Name

    }
    Write-Host -ForegroundColor Green "Successfully create all virtual machines."
}

Create-VMFromCSV((Import-Csv -Path $FilePath))