import importlib
import inspect

# Specify the module and function names as strings
module_name = "os"
function_name = "path"

# Dynamically import the module
module = importlib.import_module(module_name)

try:
    # Get the function object from the module
    function = eval(f"module.{function_name}")

    # Attempt to get the source code of the function
    source_code = inspect.getsource(function)

    # Specify the output file path
    output_file = f"{function_name.replace('.', '_')}_source.py"

    # Write the source code to the file
    with open(output_file, "w") as file:
        file.write(source_code)

    print(f"Source code written to {output_file}")

except OSError as e:
    print(f"Error: {e}")
    print(f"Could not retrieve the source code for {function_name}. It might be implemented in C or be a built-in function.")
