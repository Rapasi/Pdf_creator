# Importing necessary libraries 

from fpdf import FPDF
from matplotlib import colors
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime
import matplotlib as mp
import matplotlib.pyplot as plt
from os import path
import numpy as np

# Setting start date and end date for graphs  

start=datetime(2019,1,1)
end=datetime.today()
# Dimensions of document (not accurate currently)

WIDTH=210
HEIGHT=590

# List of stocks to plot

osakkeet=['ORTHEX.HE','WRT1V.HE','TYRES.HE','UPM.HE','METSB.HE','SHOT.ST','ZIGN.ST','OUT1V.HE','FIA1S.HE']


label_list = [
    pd.to_datetime("2021-07-21"), 
    pd.to_datetime("2019-11-29"), 
    pd.to_datetime("2019-01-09"),
    pd.to_datetime("2020-03-31"), 
    pd.to_datetime("2019-06-03"), 
    pd.to_datetime("2020-10-16"),
    pd.to_datetime("2021-01-04"), 
    pd.to_datetime("2021-05-08"), 
    pd.to_datetime("2020-06-11") ]


# Functions to download stock prices and plot graphs


def open_stock(Osake):
    osake=pdr.DataReader(Osake,'yahoo',start,end)
    hinta=osake['Adj Close']
    return(hinta)

def kuvaaja(Osake):
    colours=['r','g','b','k','c','y','m','teal','sienna']
    ax=plt.gca()
    for i in range(len(osakkeet)):
        plt.figure(figsize=(10,6))
        plt.plot(open_stock(osakkeet[i]),colours[i])
        plt.axvline(label_list[i],c=colours[i])
        plt.title(osakkeet[i])
        plt.xlabel('Aika')
        plt.xticks(rotation=20)
        plt.ylabel('Hinta')
        plt.savefig(r'C:\Users\ramie\Projects\Kuvaaja_{0}.png'.format(i))

if __name__=='__main__':
    kuva=kuvaaja(open_stock(osakkeet))   
 
# Creating pdf using fpdf

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial','B',16)
    pdf.cell(0,30,f'Osakekurssit {start.strftime("%m/%d/%y").replace("/0","/").lstrip("0")}-{end.strftime("%m/%d/%y").replace("/0","/").lstrip("0")}')
    pdf.image('Kuvaaja_0.png',5,30,WIDTH/2-5)
    pdf.image('Kuvaaja_1.png',WIDTH/2+5,30,WIDTH/2-5)
    pdf.image('kuvaaja_2.png',5,115,WIDTH/2-5)
    pdf.image('kuvaaja_3.png',WIDTH/2+5,115,WIDTH/2-5)
 
    pdf.add_page()
    pdf.image('kuvaaja_4.png',5,30,WIDTH/2-5)
    pdf.image('kuvaaja_5.png',WIDTH/2+5,30,WIDTH/2-5)
    pdf.image('kuvaaja_6.png',5,110,WIDTH/2-5)
    pdf.image('kuvaaja_7.png',WIDTH/2+5,110,WIDTH/2-5)
    pdf.image('kuvaaja_8.png',5,190,WIDTH/2-5)
    pdf.output(r'C:\Users\ramie\Projects\report_pdf','F')


