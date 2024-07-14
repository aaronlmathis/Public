class Person {

    [string] $Name
    [int] $Age
   
    Person([string] $name, [int] $age) {
        $this.Name = $name
        $this.Age = $age
    }

    [void] Display() {
        Write-Host "Hello, My name is $($this.Name) and $($this.Age) years old."
    }
}

Class Employee : Person {
    [int]$Salary

    Employee([string]$name, [int]$age, [int]$salary) : base($name, $age){ 
        $this.Salary = $salary
    }

    [void] Display() {
        Write-Host "Hello, my name is $($this.Name). I am $($this.Age) years old and I make $($this.Salary) dollars a year."
    }   
}

$employee = New-Object Employee -ArgumentList "Prashanth ", 40, 50000

$employee.Display()