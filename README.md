# CV Generator - Iliriana Riza Turka

A Python script that generates a professionally styled PDF CV using ReportLab. This project creates a formatted CV document with proper styling, sections, and layout.

## Features

- **Professional Styling**: Clean, modern design with custom colors and typography
- **Structured Layout**: Well-organized sections including personal information, education, work experience, and skills
- **Albanian Language Support**: Full support for Albanian text and special characters
- **PDF Generation**: High-quality PDF output using ReportLab library
- **Customizable**: Easy to modify content, styling, and layout

## Requirements

- Python 3.6+
- ReportLab library

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage
```bash
python cv_generator.py
```

This will generate a PDF file named `CV_Iliriana_Riza_Turka_Styled.pdf` in the current directory.

### Custom Output Path
You can modify the script to specify a custom output path by editing the `generate_cv()` function call:

```python
pdf_path = generate_cv("path/to/your/cv.pdf")
```

## File Structure

- `cv_generator.py` - Main script containing the CV generation logic
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## CV Sections

The generated CV includes the following sections:
- **Personal Information** (Të dhëna personale)
- **Education** (Arsimi)
- **Language Skills** (Aftësi gjuhësore)
- **Qualifications and Certifications** (Kualifikime dhe çertifikata të tjera)
- **Work Experience** (Eksperienca e punës)
- **Computer Skills** (Aftësi kompjuterike)
- **Personal Attributes** (Atribute personale)

## Customization

To customize the CV content:
1. Edit the content within the `generate_cv()` function
2. Modify styles by adjusting the `ParagraphStyle` definitions
3. Change colors by updating the `HexColor` values
4. Adjust layout by modifying margins and spacing

## Dependencies

- **reportlab**: PDF generation library for Python
