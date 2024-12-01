# Amazon Worst-Rated Product Finder

This script searches Amazon to find the lowest-rated products in a given category, considering only products with a significant number of reviews.

## Prerequisites

1. **Python 3.7+**
   - Download from [Python.org](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python --version  # or python3 --version
     ```

2. **Chrome Browser**
   - Windows: Download from [Google Chrome](https://www.google.com/chrome/)
   - macOS: Download from [Google Chrome](https://www.google.com/chrome/) or use Homebrew:
     ```bash
     brew install --cask google-chrome
     ```
   - Linux:
     ```bash
     # Ubuntu/Debian
     sudo apt install google-chrome-stable
     
     # Fedora
     sudo dnf install google-chrome-stable
     
     # Arch Linux
     yay -S google-chrome
     ```

3. **Required Python Packages**
   ```bash
   pip install selenium requests
   ```

## Installation

1. Clone or download this repository:
   ```bash
   git clone [repository-url]
   # or download amazon.py directly
   ```

2. Navigate to the directory:
   ```bash
   cd [directory-name]
   ```

## Usage

1. Run the script:
   ```bash
   python amazon.py  # or python3 amazon.py
   ```

2. Enter a product keyword when prompted (e.g., "headphones", "deodorant", etc.)

3. Wait for the script to search through Amazon's listings. It will:
   - Search multiple pages
   - Consider only products with 10+ reviews
   - Show progress as it finds lower-rated products
   - Display the final worst-rated product with its details

## Features

- Automatically downloads correct ChromeDriver version
- Works across Windows, macOS, and Linux
- Searches multiple Amazon pages and sorting methods
- Filters out products with too few reviews
- Shows product title, rating, number of reviews, and link

## Troubleshooting

1. **ChromeDriver Issues**
   - The script automatically downloads the correct ChromeDriver version
   - If you get version mismatch errors, update Chrome to the latest version

2. **Permission Issues (Linux/macOS)**
   ```bash
   # Add execute permission to ChromeDriver
   chmod +x chromedriver/chromedriver-win64/chromedriver
   ```

3. **Chrome Not Found**
   - Ensure Chrome is installed in the default location
   - For custom Chrome locations, modify the script's Chrome path

4. **Python Package Issues**
   ```bash
   # Upgrade pip
   python -m pip install --upgrade pip
   
   # Install/reinstall packages
   pip install --upgrade selenium requests
   ```

## Notes

- The script uses headless Chrome (no visible browser window)
- Amazon may occasionally block requests if too many are made
- Results may vary based on your region and Amazon's sorting algorithm
- Minimum review threshold is set to 10 reviews by default

## Legal

This script is for educational purposes only. Ensure you comply with Amazon's terms of service and robots.txt when using this script.

## Contributing

Feel free to fork, submit issues, or propose improvements through pull requests.

## License

MIT License with Attribution Requirement

Copyright (c) 2024 Armad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

2. All copies or substantial portions of the Software must include the following
   attribution: "Based on work by Armad (https://github.com/xArmad)"

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
