import tkinter as tk
from VerticalScrolledFrame import VerticalScrolledFrame

class IncomeGUI:
    def createConstants(self):
        self.title = "Income GUI"
        self.titleFont = ["Times New Roman", 24, "bold underline"]
        self.mainfont = ["Arial CYR", 15]
        self.BG = "white"
        self.padX=10
        self.padY=5
    # End createConstants

    def __init__(self):
        self.createConstants()

        self.window = tk.Tk(className=self.title)
        self.window.geometry("500x500")

        self.createPageStructure()

        self.window.mainloop()
    # End __init__(self)

    # Clear the window for new page
    def destroyWidgets(self):
        # Gets rid of the mousewheel binding from VerticalScrollFrame
        self.window.unbind_all("<MouseWheel>")
        # Clears the window's widgets to add the new page's widgets
        for widget in self.window.winfo_children():
            widget.destroy()
    # End destroyWidgets

    # Creates all basic page Structures
    def createPageStructure(self):
        top = tk.Frame(self.window, bg=self.BG, height=1)
        self.middle = tk.Frame(self.window, bg=self.BG, height=1)
        bottom = tk.Frame(self.window, bg=self.BG, height=1)
        top.pack(fill=tk.X)
        self.middle.pack(fill=tk.BOTH, expand=True)
        bottom.pack(fill=tk.X)

        topLabel = tk.Label(
            text=self.title,
            height=1, bg = self.BG,
            font=self.titleFont
        )
        topLabel.pack(in_=top, fill=tk.X)

        # Creates the bottom label
        bottomLabel = tk.Label(
            text="Savings",
            height=1, bg=self.BG,
            font=self.mainfont
        )
        bottomLabel.pack(in_=bottom, fill=tk.X, expand=True)

        # This is where the middle goes
        self.createIncomeScroll()
        # End the middle part
    # End createPageStructure

    # Used to create the Equation page
    def createIncomeScroll(self):
        scframe = VerticalScrolledFrame(self.middle)
        scframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=self.padY)

        scframe.interior.grid_rowconfigure(0,weight=1)
        scframe.interior.grid_columnconfigure(0,weight=1)
        scframe.interior.grid_columnconfigure(1,weight=1)

        currRow = 0
        # Create physics and astronomy equation buttons in scrollframe
        currRow = self.addBasicEntries(scframe.interior, currRow)
    # End createEquation

    # Adds the equationType to scrollFrame starting at currRow
    # equationType can be "Physics Equations" or "Astronomy Equations"
    def addBasicEntries(self, scrollFrame, currRow):
        for i in range(0,50):
            equationName = tk.Label(
                scrollFrame, text="Text "+str(i),
                bg=self.BG, font=self.mainfont,
                height=1, width=1
            )
            equationName.grid(row=currRow, column=0,
                              padx=self.padX, pady=self.padY, sticky=tk.EW)

            equationButton = tk.Button(
                scrollFrame, text="Button Text And Stuff"+str(i),
                anchor="center", height=1, width=1,
                background="light blue", activebackground="purple",
                font=self.mainfont, cursor='hand2'
            )
            equationButton.grid(row=currRow, column=1, sticky=tk.EW)
            currRow+=10


        return currRow
    # End addEquationsToFrame
# End IncomeGUI

if (__name__ == "__main__"):
    incomeGui = IncomeGUI()
# End IF