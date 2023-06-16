#!/usr/bin/python3

"""
chnhash provides you with the functionalities of generating and comparing hash values.
Copyright (C) 2022-2023 Himashana Suraweera (Email : Himashana@chnsoftwaredevelopers.com)

This file is part of chnhash.

chnhash is free software: you can redistribute it and/or modify it under the terms of the GNU General
Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

chnhash is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with chnhash. If not, see
<https://www.gnu.org/licenses/>.

"""

import tkinter, tkinter.messagebox
from tkinter import ttk
import compareHash
import generateHash
import appUpdater

class LoadingScreen:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('chnhash - GUI'), self.main.resizable(width=False, height=False)
        self.main.geometry("400x140")
        self.main.eval('tk::PlaceWindow . center')
        self.main.wm_attributes('-toolwindow', 'True')
        self.timer = tkinter.IntVar()
        self.timer.set(1)
        
        self.row1 = tkinter.Frame(self.main)
        self.row2 = tkinter.Frame(self.main)

        self.appTitle = tkinter.Label(self.row1, text='chnhash',fg='blue', font=("Arial", 24), justify="right")
        self.copyrightInfo = tkinter.Label(self.row2, text='Copyright (C) 2022-2023 Himashana Suraweera\nLicensed under the terms of the GNU GPLv3\nhttps://chnsoftwaredevelopers.com', font=("Arial", 10), justify="right")

        self.appTitle.pack()
        self.copyrightInfo.pack(side='right')

        self.row1.pack(pady=5)
        self.row2.pack(side='right', padx=10)

        self.appTitle.config(text=" " * 28 + "chnhash")

        self.updateTimer()

        tkinter.mainloop()

    def updateTimer(self):
        if self.timer.get() < 1:
            self.main.destroy()
        else:  
            self.timer.set(self.timer.get() - 1)
            self.main.after(1000, self.updateTimer)


class ProgramGUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('chnhash - GUI'), self.main.resizable(width=False, height=False)
        self.main.eval('tk::PlaceWindow . center')

        self.appVersion = "v1.0.0"
        self.results = ""

        self.header = tkinter.Frame(self.main, pady=10, padx=60)
        self.resultsSection = tkinter.Frame(self.main, pady=10, padx=0)

        self.appTitle = tkinter.Label(self.header, text='chnhash',fg='blue', font=("Arial", 14))

        self.algorithmSection = tkinter.Frame(self.main, pady=10, padx=0)
        self.algorithmCtrlLabel = tkinter.Label(self.algorithmSection, text="Algorithm: " + (" " * 15))
        self.algorithmCtrl = ttk.Combobox(self.algorithmSection, width=27, values=["sha1", "sha256", "sha512"])
        self.algorithmCtrl.current(0)

        self.fileCtrlSection = tkinter.Frame(self.main, pady=10, padx=0)
        self.fileCtrlLabel = tkinter.Label(self.fileCtrlSection, text="File (with location): ")
        self.fileCtrl = tkinter.Entry(self.fileCtrlSection, width=30)
        
        self.generateHashBtn = tkinter.Button(self.resultsSection, text="Generate", command=lambda: self.generateHashBtn_onClick())
        self.resultsText = tkinter.Text(self.resultsSection, width=45, height=8, state='disabled')

        self.appTitle.pack(side='left', padx=5)

        self.algorithmCtrlLabel.pack(side='left')
        self.algorithmCtrl.pack()

        self.fileCtrlLabel.pack(side='left')
        self.fileCtrl.pack()

        self.generateHashBtn.pack()
        self.resultsText.pack()

        self.header.pack()
        self.algorithmSection.pack()
        self.fileCtrlSection.pack()
        self.resultsSection.pack()

        self.appTitle.config(text = "chnhash - " + self.appVersion)

        tkinter.mainloop()

    def generateHashBtn_onClick(self):
        self.resultsText.config(state='normal')
        self.resultsText.delete('1.0', tkinter.END)

        try:
            # Calling the generateHash() function to generate a hash value.
            self.results = generateHash.generateHash(self.algorithmCtrl.get(), self.fileCtrl.get())

            if self.results[0] != "":
                self.resultsText.insert(tkinter.END, "Using: " + self.results[0] + "\n")
                self.resultsText.insert(tkinter.END, self.results[0] + ": " + self.results[1] + " " + self.fileCtrl.get())
            else:
                self.resultsText.insert(tkinter.END, "Sorry, an error occurred, or the algorithm is not supported with this tool. Please try to use a supported algorithm.")
        except:
            self.resultsText.insert(tkinter.END, "An error occured. please try again!")

        self.resultsText.config(state='disabled')

loadingScreen = LoadingScreen()

if loadingScreen.timer.get() < 1:
    app = ProgramGUI()
else:
    print("An error occured. Please try again!")
