#Creating pdf using fpdf

from fpdf import FPDF
from datetime import datetime

# Setting start date and end date for graphs  

start=datetime(2018,1,1)
end=datetime.today()
# Dimensions of document (not accurate currently)

WIDTH=210
HEIGHT=590

pdf=FPDF()
pdf.add_page()
pdf.set_font('Arial','B',16)
pdf.set_fill_color(155,50,80)
pdf.cell(80,10,f'Osakekurssit {start.strftime("%m/%d/%y").replace("/0","/").lstrip("0")}-{end.strftime("%m/%d/%y").replace("/0","/").lstrip("0")}',fill=True)
pdf.image('Kuvaaja_0.png',5,30,WIDTH/2-5)
pdf.image('Kuvaaja_1.png',WIDTH/2+5,30,WIDTH/2-5)
pdf.image('kuvaaja_2.png',5,115,WIDTH/2-5)
pdf.image('kuvaaja_3.png',WIDTH/2+5,115,WIDTH/2-5)
pdf.image('kuvaaja_4.png',5,190,WIDTH/2-5)
pdf.image('kuvaaja_5.png',WIDTH/2+5,190,WIDTH/2-5)

pdf.add_page()
pdf.image('kuvaaja_6.png',5,20,WIDTH/2-5)
pdf.image('kuvaaja_7.png',WIDTH/2+5,20,WIDTH/2-5)
pdf.image('kuvaaja_8.png',5,100,WIDTH/2-5)
pdf.image('kuvaaja_all.png',WIDTH/2+5,100,WIDTH/2-5)
pdf.output(r'C:\Users\ramie\Projects\report_pdf','F')