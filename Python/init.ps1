# Define the base directory
$baseDir = "pySQLBrowser"

# Create directories
$dirs = @(
    "$baseDir",
    "$baseDir/pySQLBrowser",
    "$baseDir/pySQLBrowser/resources",
    "$baseDir/pySQLBrowser/resources/icons",
    "$baseDir/pySQLBrowser/resources/styles",
    "$baseDir/pySQLBrowser/resources/templates",
    "$baseDir/pySQLBrowser/tests",
    "$baseDir/docs"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path $dir
}

# Create files
$files = @(
    "$baseDir/main.py",
    "$baseDir/requirements.txt",
    "$baseDir/README.md",
    "$baseDir/pySQLBrowser/__init__.py",
    "$baseDir/pySQLBrowser/gui.py",
    "$baseDir/pySQLBrowser/database.py",
    "$baseDir/pySQLBrowser/config.py",
    "$baseDir/pySQLBrowser/utils.py",
    "$baseDir/pySQLBrowser/resources/__init__.py",
    "$baseDir/pySQLBrowser/tests/__init__.py",
    "$baseDir/pySQLBrowser/tests/test_gui.py",
    "$baseDir/pySQLBrowser/tests/test_database.py",
    "$baseDir/pySQLBrowser/tests/test_utils.py",
    "$baseDir/docs/index.md",
    "$baseDir/docs/usage.md",
    "$baseDir/docs/api_reference.md"
)

foreach ($file in $files) {
    New-Item -ItemType File -Force -Path $file
}

# Add some initial content to README.md and main.py
$content = @"
# pySQLBrowser

This project is a graphical Python SQL browser.

## Installation

To install the required dependencies, run:

\`\`\`
pip install -r requirements.txt
\`\`\`

## Usage

To start the application, run:

\`\`\`
python main.py
\`\`\`
"@

Set-Content -Path "$baseDir/README.md" -Value $content

$content = @"
# main.py
# Entry point of the pySQLBrowser application.

def main():
    print('Starting pySQLBrowser...')

if __name__ == '__main__':
    main()
"@

Set-Content -Path "$baseDir/main.py" -Value $content
