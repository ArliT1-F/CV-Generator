#!/usr/bin/env python3
"""
CV Generator for Iliriana Riza Turka
Generates a styled PDF CV using ReportLab
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
import os

def generate_cv(output_path="CV_Iliriana_Riza_Turka_Styled.pdf"):
    """
    Generate a styled PDF CV for Iliriana Riza Turka
    
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
    elements.append(Paragraph("ILIRIANA RIZA TURKA", header_style))
    elements.append(Paragraph("Rr. \"Ibrahim Rugova\", Pll. Shallvare, Shk. 4, Tiranë | Tel: +355 676060723", subheader_style))
    elements.append(HRFlowable(width="100%", color=colors.HexColor("#1C3D5A"), thickness=1))
    elements.append(Spacer(1, 12))

    # Të dhëna personale
    elements.append(Paragraph("TË DHËNA PERSONALE", section_title))
    elements.append(Paragraph("Datëlindja: 15 Janar 1976<br/>"
                              "Vendlindja: Durrës, Shqipëri", text_style))

    # Arsimi
    elements.append(Paragraph("ARSIMI", section_title))
    elements.append(Paragraph("2013–2015 – Master Profesional në Edukatë Qytetare – Histori<br/>"
                              "Universiteti \"Aleksandër Xhuvani\", Elbasan<br/><br/>"
                              "2009–2013 – Bachelor në Edukim Qytetar<br/>"
                              "Universiteti \"Aleksandër Xhuvani\", Elbasan<br/><br/>"
                              "1993–1997 – Shkollë e Mesme e Përgjithshme \"Kamëz\"", text_style))

    # Aftësi Gjuhësore
    elements.append(Paragraph("AFTËSI GJUHËSORE", section_title))
    elements.append(Paragraph("• Anglisht – Certifikatë TOEIC (2014)<br/>"
                              "• Italisht – Njohuri të mira në të folur", text_style))

    # Kualifikime
    elements.append(Paragraph("KUALIFIKIME DHE ÇERTIFIKATA TË TJERA", section_title))
    elements.append(Paragraph("• 2019 – Çertifikatë për formimin dhe kualifikimin e punonjësve të Policisë Bashkiake<br/>"
                              "• 2017 – Dëshmi aftësie për punonjës shërbimi në SHPSF<br/>"
                              "• 2017 – Trajnim bazë dhe Çertifikatë e Lotarisë Kombëtare<br/>"
                              "• 2014 – Çertifikatë për Edukimin e Qytetarisë Demokratike në Shekullin e Ri<br/>"
                              "• 2011 – Çertifikatë bazë e formimit të kompjuterit – Qendra Didaktike \"IRISOFT\"", text_style))

    # Eksperienca e Punës
    elements.append(Paragraph("EKSPERIENCA E PUNËS", section_title))
    work_data = [
        ["2019 – Vazhdon", "Policia Bashkiake, Tiranë – Punonjëse Policie"],
        ["Qershor 2018 – Korrik 2019", "Toni Security SH.P.K. – Punonjëse Sigurie"],
        ["Korrik 2017 – Shtator 2018", "Multi Parking Management – Mbikëqyrëse / Punonjëse Parkimi"],
        ["Qershor 2016 – Mars 2017", "Albion-R2015 – Punonjëse Sigurie"],
        ["Shtator 2012 – Janar 2013", "FastCall – Operatore Call Center"],
        ["2011 – 2012", "Shitëse Butiku"],
        ["2007 – 2011", "Shitëse"],
        ["2002 – 2005", "Fabrikë Këpucësh – Përgjegjëse"],
        ["1998 – 1999", "Firma \"Ital Shoes\" – Punëtore / Operatore"],
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

    # Aftësi Kompjuterike
    elements.append(Paragraph("AFTËSI KOMPJUTERIKE", section_title))
    elements.append(Paragraph("Njohuri bazë në përdorimin e kompjuterit (Windows, Microsoft Office, Internet, Email)", text_style))

    # Atribute Personale
    elements.append(Paragraph("ATRIBUTE PERSONALE", section_title))
    elements.append(Paragraph("• E përgjegjshme, e organizuar dhe bashkëpunuese<br/>"
                              "• Aftësi të mira komunikimi dhe pune në grup<br/>"
                              "• E përkushtuar ndaj zhvillimit profesional dhe shërbimit publik", text_style))

    # Build
    doc.build(elements)
    return output_path

if __name__ == "__main__":
    # Generate the CV
    pdf_path = generate_cv()
    print(f"CV generated successfully: {pdf_path}")
    print(f"File size: {os.path.getsize(pdf_path)} bytes")