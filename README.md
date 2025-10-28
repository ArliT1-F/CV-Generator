# CV-Generator
I'm too broke to buy ready made CVs from the internet and visibly too lazy to make new CVs everytime manually. So here it is!

## Features
- Generate professional PDF CVs using Python and ReportLab
- Clean, modern styling with customizable colors
- Placeholder-based template for easy customization
- Professional layout with sections for personal info, education, work experience, skills, and more

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from cv_generator import generate_cv

# Generate a CV with default filename
pdf_path = generate_cv()

# Or specify a custom filename
pdf_path = generate_cv("My_CV.pdf")
```

## Customization
The CV template uses placeholders that you can easily replace with your own information:
- `[FULL NAME]` - Your full name
- `[ADDRESS]` - Your address
- `[PHONE NUMBER]` - Your phone number
- `[EMAIL]` - Your email address
- And many more placeholders throughout the document

Simply edit the `cv_generator.py` file and replace the placeholders with your actual information.
