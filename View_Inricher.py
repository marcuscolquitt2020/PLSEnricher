from tkinter import *
import tkinter as tk
from tkinter import Button, Text
from turtle import width

class PLSAutomateWindow:
    def __init__(self, master):
        self.master = master
        master.title('PLS Automator')
        master.geometry('500x600')
        master.resizable(False,False)

        self.frame_paths = Frame(master,padx=10,pady=10)
        self.frame_paths.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.frame_paths.pack()
        self.label_path = Label(self.frame_paths, text='Paste file paths to run enricher',width=500)
        self.label_path.pack()
        
        #frame 1 manual paste file paths
        self.frame1 = Frame(master,padx=10,pady=10)
        self.frame1.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.frame1.pack()

        self.label1 = Label(self.frame1, text='BAK MAIN FOLDER FILE PATH')
        self.label1.pack()
        self.text1 = Text(self.frame1,height=1)
        self.text1.pack()

        self.label2 = Label(self.frame1, text='PERMIT FOLDER')
        self.label2.pack()
        self.text2 = Text(self.frame1,height=1)
        self.text2.pack()

        self.label3 = Label(self.frame1, text='WIRE FILE PATH')
        self.label3.pack()
        self.text3 = Text(self.frame1,height=1)
        self.text3.pack()

        self.button = Button(self.frame1, text='Start PLS Enrichment')
        self.button.pack(side='bottom')

        self.frame_csv = Frame(master,padx=10,pady=10)
        self.frame_csv.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.frame_csv.pack()
        self.label_csv = Label(self.frame_csv, text='Paste csv path to run enricher', width=500)
        self.label_csv.pack()

        #frame 2 import csv file that contains the file paths
        self.frame2 = Frame(master,padx=10,pady=10,border=1)
        self.frame2.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.frame2.pack()

        self.label4 = Label(self.frame2, text='CSV FILE PATH')
        self.label4.pack()
        self.text4 = Text(self.frame2,height=1)
        self.text4.pack()

        self.button = Button(self.frame2, text='IMPORT CSV')
        self.button.pack()
        
        Lb1 = Listbox(self.frame2,width=100,height=4)
        Lb1.insert(0,'data')
        Lb1.pack()

        self.button = Button(self.frame2, text='Start PLS Enrichment')
        self.button.pack()



root = tk.Tk()
window = PLSAutomateWindow(root)
root.mainloop()