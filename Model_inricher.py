import csv
import os
from tkinter import filedialog as fd
import pandas as pd



class InrichCSV:
    data = pd.DataFrame
    def __init__(self,fpath):
        self.path = fpath
    def getCsvData(fpath):
        csvData = pd.read_csv(fpath)
        return csvData
    def selectFile():
        fileTypes = ('csv files', '*.csv'),
        fileName = fd.askopenfilename( 
            title = 'Select Inrich CSV',
            initialdir='/',
            filetypes=fileTypes)
        InrichCSV.data = InrichCSV.getCsvData(fileName)
