# Importing necessary libraries 

import yfinance as yf
from fpdf import FPDF
from matplotlib import colors
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib as mp
import matplotlib.pyplot as plt
from os import path
import numpy as np

# Setting start date and end date for graphs  

start=datetime(2018,1,1)
end=datetime.today()
# Dimensions of document (not accurate currently)

WIDTH=210
HEIGHT=590

# List of stocks to plot

def get_name(osake_list):
    company_names=[]
    for name in osake_list:
        osake=yf.Ticker(name)
        company_name=osake.info['longName']
        company_names.append(company_name)
    return(company_names)

colours=['r','g','b','k','c','y','m','teal','sienna']
osakkeet=['ORTHEX.HE','WRT1V.HE','TYRES.HE','UPM.HE','METSB.HE','SHOT.ST','ZIGN.ST','OUT1V.HE','FIA1S.HE']
stock_names=get_name(osakkeet)

label_list = [
    pd.to_datetime("2021-07-21"),
    pd.to_datetime("2019-11-29"), 
    pd.to_datetime("2019-01-09"),
    (pd.to_datetime("2020-03-31"), pd.to_datetime("2019-06-27")),
    pd.to_datetime("2019-06-03"), 
    pd.to_datetime("2020-10-16"), 
    (pd.to_datetime("2021-01-04"), pd.to_datetime("2021-08-11")),
    (pd.to_datetime("2021-05-08"), pd.to_datetime("2019-02-13")),
    (pd.to_datetime("2020-06-11"), pd.to_datetime("2019-07-25"),pd.to_datetime("2018-11-27"))]

# Functions to download stock prices and plot graphs

def open_stock(Osake):
    osake=pdr.DataReader(Osake,'yahoo',start,end)
    hinta=osake['Adj Close']
    return(hinta)

my_stocks=open_stock(osakkeet)

def purchase(labels):
    for date in labels: 
        if labels[date] in open_stock(osakkeet):
           plt.axvline(label_list[date], linewidth=1,ls=':')
        else: continue

def kuvaaja(Osake):
    ax=plt.gca()
    for i in range(len(osakkeet)):
        plt.close()
        plt.figure(figsize=(10,6))
        plt.plot(open_stock(osakkeet[i]),color=colours[i])
        plt.xlabel('Aika')
        plt.xticks(rotation=20)
        plt.title(stock_names[i])
        plt.ylabel('Hinta')
        plt.vlines(label_list[i],0,open_stock(osakkeet[i]).max(),color=colours[i],ls=':')
        plt.savefig(r'C:\Users\ramie\Projects\Kuvaaja_{0}.png'.format(i),'r')

        
if __name__=='__main__':
    kuva=kuvaaja(open_stock(osakkeet))   
 