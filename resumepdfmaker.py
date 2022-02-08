# Assignment 9

# PDF Resume Creator
#	- Create a python program that will create your personal resume in PDF format
#	- All personal details are stored in a JSON file
#	- Your program should read the JSON file and write the details in the PDF
#	- The output file should be: LASTNAME_FIRSTNAME.pdf

# Steps:
# 1. Install necessary extensions.
# 2. Set-up both .json and .py files.
# 3. Set-up the code that will convert the .json file into a .pdf file
# 4. Format the final output.

from fpdf import FPDF
import json
from ctypes import alignment

#header
class PDF(FPDF):
    def header(self):
        self.image('demopic.jpg', 10, 8, 40)
        self.set_font('helvetica', 'B', 28.5)
        self.cell(0, 30, 'GIAN CARLO BIRON ESTRELLA', align = 'R', ln=1)
        self.ln(3)

#PDF Format
pdf = PDF('P', 'mm', "Letter")
pdf.set_auto_page_break(auto=1, margin=30)
pdf.add_page() 

#Read Information
Resume_Info = open('sampleresume.json', 'r')
PDFCreator = Resume_Info.read()
Raw_Info = json.loads(PDFCreator)

#Information
for information in Raw_Info:
    pdf.ln(5)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header1']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(0, 5, f"Name: {information['Name']}", align='L', ln=1)
    pdf.cell(0, 5, f"Address: {information['Address']}", align='L', ln=1)
    pdf.cell(0, 5, f"Contact No.: {information['Contact No.']}", align='L', ln=1)
    pdf.cell(0, 5, f"Email: {information['Email']}", align='L', ln=1)
    pdf.ln(8)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header2']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', '', 12)
    pdf.multi_cell(0, 5, f"{information['OBJECTIVES']}", align='L', ln=1)
    pdf.ln(8)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header3']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'BIU', 12)
    pdf.cell(0, 5, "Tertiary:", align='L', ln=1)
    pdf.set_font('helvetica', 'BI', 12)
    pdf.cell(0, 5, f"{information['Tertiary']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{information['Tadd']}", align='L', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'BIU', 12)
    pdf.cell(0, 5, "Secondary:", align='L', ln=1)
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 5, f"{information['Secondary']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{information['Sadd']}", align='L', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'BIU', 12)
    pdf.cell(0, 5, "Primary:", align='L', ln=1)
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 5, f"{information['Primary']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{information['Padd']}", align='L', ln=1)
    pdf.ln(8)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header4']}", 'BI', ln=1)
    pdf.ln(5)
    pdf.set_font('helvetica', 'BIU', 12)
    pdf.cell(0, 5, f"{information['Work1']}", align='L', ln=1)
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 5, f"{information['Company1']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{information['Wyear1']}", align='L', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'BIU', 12)
    pdf.cell(0, 5, f"{information['Work2']}", align='L', ln=1)
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 5, f"{information['Company2']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{information['Wyear2']}", align='L', ln=1)
    pdf.ln(8)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header5']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', '', 12)
    pdf.cell(0, 5, f"- {information['Skill1']}", align='L', ln=1)
    pdf.cell(0, 5, f"- {information['Skill2']}", align='L', ln=1)
    pdf.set_font('helvetica', 'BI', 12)
    pdf.cell(0, 5, f"- Has knowledge in {information['Skill3']} and {information['Skill4']}", align='L', ln=1)
    pdf.ln(8)
    pdf.set_font('helvetica', 'BI', 18)
    pdf.cell(0, 10, f"{information['header6']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('helvetica', 'BIU', 12)
    pdf.cell(0, 5, f"{information['REFERENCE']}", align='L', ln=1)
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 5, f"{information['Occupation']}", align='L', ln=1)
    pdf.set_font('helvetica', 'I', 12)
    pdf.cell(0, 5, f"{information['RContact']}", align='L', ln=1)

pdf.output('ESTRELLA_GIAN_CARLO.pdf')