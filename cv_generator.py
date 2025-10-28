from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_cv(output_path="CV_Styled.pdf"):
    """
    Generate a styled CV PDF document with placeholders.
    
    Args:
        output_path (str): Path where the PDF will be saved
        
    Returns:
        str: Path to the generated PDF file
    """
    # Create styled PDF
    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=60, rightMargin=60, topMargin=50, bottomMargin=50
    )

    # Styles
    styles = getSampleStyleSheet()
    header_style = ParagraphStyle('HeaderStyle', fontSize=22, leading=26, alignment=1, textColor=colors.HexColor("#1C3D5A"), spaceAfter=10)
    subheader_style = ParagraphStyle('SubHeaderStyle', fontSize=12, leading=14, alignment=1, textColor=colors.HexColor("#555555"), spaceAfter=20)
    section_title = ParagraphStyle('SectionTitle', fontSize=13, leading=16, textColor=colors.HexColor("#1C3D5A"), spaceBefore=16, spaceAfter=8, underlineWidth=0.5)
    text_style = ParagraphStyle('TextStyle', fontSize=11, leading=15, textColor=colors.black)

    elements = []

    # Header
    elements.append(Paragraph("[FULL NAME]", header_style))
    elements.append(Paragraph("[ADDRESS] | Tel: [PHONE NUMBER] | Email: [EMAIL]", subheader_style))
    elements.append(HRFlowable(width="100%", color=colors.HexColor("#1C3D5A"), thickness=1))
    elements.append(Spacer(1, 12))

    # Personal Information
    elements.append(Paragraph("PERSONAL INFORMATION", section_title))
    elements.append(Paragraph("Date of Birth: [DATE OF BIRTH]<br/>"
                              "Place of Birth: [PLACE OF BIRTH]<br/>"
                              "Nationality: [NATIONALITY]", text_style))

    # Education
    elements.append(Paragraph("EDUCATION", section_title))
    elements.append(Paragraph("[YEAR] – [DEGREE] in [FIELD OF STUDY]<br/>"
                              "[UNIVERSITY/INSTITUTION NAME], [LOCATION]<br/><br/>"
                              "[YEAR] – [DEGREE] in [FIELD OF STUDY]<br/>"
                              "[UNIVERSITY/INSTITUTION NAME], [LOCATION]<br/><br/>"
                              "[YEAR] – [HIGH SCHOOL NAME]", text_style))

    # Language Skills
    elements.append(Paragraph("LANGUAGE SKILLS", section_title))
    elements.append(Paragraph("• [LANGUAGE 1] – [PROFICIENCY LEVEL] ([CERTIFICATION/YEAR])<br/>"
                              "• [LANGUAGE 2] – [PROFICIENCY LEVEL]<br/>"
                              "• [LANGUAGE 3] – [PROFICIENCY LEVEL]", text_style))

    # Certifications
    elements.append(Paragraph("CERTIFICATIONS AND QUALIFICATIONS", section_title))
    elements.append(Paragraph("• [YEAR] – [CERTIFICATION NAME]<br/>"
                              "• [YEAR] – [CERTIFICATION NAME]<br/>"
                              "• [YEAR] – [CERTIFICATION NAME]<br/>"
                              "• [YEAR] – [CERTIFICATION NAME]<br/>"
                              "• [YEAR] – [CERTIFICATION NAME]", text_style))

    # Work Experience
    elements.append(Paragraph("WORK EXPERIENCE", section_title))
    work_data = [
        ["[START DATE] – [END DATE]", "[COMPANY NAME], [LOCATION] – [JOB TITLE]"],
        ["[START DATE] – [END DATE]", "[COMPANY NAME], [LOCATION] – [JOB TITLE]"],
        ["[START DATE] – [END DATE]", "[COMPANY NAME], [LOCATION] – [JOB TITLE]"],
        ["[START DATE] – [END DATE]", "[COMPANY NAME], [LOCATION] – [JOB TITLE]"],
        ["[START DATE] – [END DATE]", "[COMPANY NAME], [LOCATION] – [JOB TITLE]"],
        ["[START DATE] – [END DATE]", "[COMPANY NAME], [LOCATION] – [JOB TITLE]"],
        ["[START DATE] – [END DATE]", "[COMPANY NAME], [LOCATION] – [JOB TITLE]"],
        ["[START DATE] – [END DATE]", "[COMPANY NAME], [LOCATION] – [JOB TITLE]"],
        ["[START DATE] – [END DATE]", "[COMPANY NAME], [LOCATION] – [JOB TITLE]"],
        # Add more if needed
    ]
    work_table = Table(work_data, colWidths=[130, 340])
    work_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.white),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10.5),
        ("ALIGN", (0, 0), (0, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#CCCCCC")),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(work_table)

    # Computer Skills
    elements.append(Paragraph("COMPUTER SKILLS", section_title))
    elements.append(Paragraph("[SKILL 1], [SKILL 2], [SKILL 3], [SKILL 4], [SKILL 5]", text_style))

    # Personal Attributes
    elements.append(Paragraph("PERSONAL ATTRIBUTES", section_title))
    elements.append(Paragraph("• [ATTRIBUTE 1], [ATTRIBUTE 2] and [ATTRIBUTE 3]<br/>"
                              "• [ATTRIBUTE 4] and [ATTRIBUTE 5]<br/>"
                              "• [ATTRIBUTE 6] and [ATTRIBUTE 7]", text_style))

    # Build PDF
    doc.build(elements)
    return output_path

if __name__ == "__main__":
    # Generate the CV
    pdf_path = generate_cv()
    print(f"CV generated successfully: {pdf_path}")