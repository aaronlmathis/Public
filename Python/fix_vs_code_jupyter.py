import os
import subprocess
import winreg

def enable_long_paths():
    try:
        # Open the registry key
        registry_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Control\FileSystem",
            0,
            winreg.KEY_SET_VALUE
        )

        # Set the LongPathsEnabled value to 1
        winreg.SetValueEx(registry_key, "LongPathsEnabled", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(registry_key)

        print("Long paths have been enabled successfully.")
    except PermissionError:
        print("Permission denied: Please run this script as an administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")

def manage_pyzmq():
    try:
        # Uninstall pyzmq
        subprocess.check_call([os.sys.executable, '-m', 'pip', 'uninstall', 'pyzmq', '-y'])
        print("Uninstalled pyzmq successfully.")

        # Install specific version of pyzmq
        subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', 'pyzmq==25.1.2'])
        print("Installed pyzmq version 25.1.2 successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while managing pyzmq: {e}")

if __name__ == "__main__":
    enable_long_paths()
    manage_pyzmq()
