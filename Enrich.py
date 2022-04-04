import pandas as pd
import os
import time
import pyautogui
import pyperclip

class GenAll:

    def __init__(self,permitNum,bakPath,modelpath,enrichPath,wirepath):
        self.permitNum = permitNum
        self.bakPath = bakPath
        self.modelpath = modelpath
        self.enrichPath = enrichPath
        self.wirepath = wirepath 

    def genBak():
        gA = GenAll
        #list that contains the file paths that are to be pasted into .bak restore paths
        pasteBak = [gA.modelpath,f"{gA.enrichPath}\\structures",gA.wirepath,gA.modelpath]

        #open .bak file per the instance of permit # 
        os.startfile(f"{gA.bakPath}\\Perm_{gA.permitNum}.bak")

        #timer to give pls a chnace to open
        time.sleep(3)

        #copy pasteBak list and paste into .bak restore paths and submit
        pyautogui.click(500,100)
        pyautogui.hotkey('ctrl','home')
        pyautogui.hotkey('tab')
        pyperclip.copy('\n'.join(pasteBak))
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('return')

        #timer to give pls a chance to restore
        time.sleep(3)

    def insertStkTable():
        gA = GenAll

        #temp path
        stkData = pd.read_csv(f"{gA.enrichPath}\\StakingTable.csv")

        #use case path
        #stkData = pd.read_csv(f"{gA.enrichPath}\\Permit_{gA.permitNum}\\PLS\\ModelEnrichment\\StakingTable.csv",skiprows=[0])
        stkData.to_clipboard(index=False)

        #opens staking table
        pyautogui.hotkey('ctrl','k')#todo: set scema for model to be able to run from here
        time.sleep(2)
        pyautogui.click(500,300)
        pyautogui.hotkey('ctrl','home')
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        time.sleep(3)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        time.sleep(3)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
    
    def insertSctTable():
        gA = GenAll
        #temp path
        stkData = pd.read_csv(f"{gA.enrichPath}\\SectionTable.csv")

        #use case path
        #stkData = pd.read_csv(f"{gA.enrichPath}\\Permit_{gA.permitNum}\\PLS\\ModelEnrichment\\SectionTable.csv",skiprows=[0])
        stkData.to_clipboard(index=False)

        #opens section table
        pyautogui.hotkey('ctrl','l')#todo: set scema for model to be able to run from here
        time.sleep(2)
        pyautogui.click(500,500)
        pyautogui.hotkey('ctrl','home')
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        time.sleep(3)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')

    def savePLS():
        #save pls model
        pyautogui.hotkey('ctrl','s', interval = 0.15)
        time.sleep(3)
        #save new .don file select no 
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        time.sleep(3)


def bakGenFromCSV():
    #the csv data that is imported is to be generated when the permit folder generator runs
    headers = ['permitnum','bakpath','modelpath','wirepath','enrichpath']
    csvPath = input('Input file path for Inrich csv')
    csvData = pd.read_csv(f"{csvPath}\\ModelEnricher.csv",names=headers,skiprows=[0])
    for ind in csvData.index:
        GenAll.permitNum = csvData['permitnum'][ind]
        GenAll.bakPath = csvData['bakpath'][ind]
        GenAll.modelpath = csvData['modelpath'][ind]
        GenAll.wirepath = csvData['wirepath'][ind]
        GenAll.enrichPath = csvData['enrichpath'][ind]
        GenAll.genBak()
        GenAll.insertStkTable()
        GenAll.insertSctTable()
        GenAll.savePLS()

bakGenFromCSV()