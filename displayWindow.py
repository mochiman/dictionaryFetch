import tkinter as tk
import time
# tkinter window test
class app():
    def __init__(self, textFunction):
        self.textBuffer = {}
        self.dictionaryBuffer = {}
        self.textFunctionCallback = 0
        self.displayText = ""

        # initialize object with textFunction callback
        self.registerTextFunctionCallback(textFunction)
        self.initializeWindow()


    # initialize the frame/container information
    def initializeWindow(self):
        # works as container, arranging psoition of other widgets
        self.mainFrame = tk.Frame()
        self.mainFrame.pack()

        #window label
        self.top = tk.Label(self.mainFrame, text = "Translation List")
        self.top.pack()

        # configure label for displaying text
        self.readText = tk.Label(self.mainFrame, text=self.displayText, font=('times',12,'bold'), anchor="nw", justify='left')
        self.readText.pack()

        self.updateText() #first call it manually

    # will continuously check and update text on gui
    def updateText(self): 
        #self.textBuffer = self.searchCallback
        self.dictionaryBuffer = self.textFunctionCallback()
        self.printLineBuffer()
        #self.readText.configure(text=self.displayText, justify='left', anchor="nw")
        self.readText.configure(text=self.displayText)

        self.mainFrame.after(200, self.updateText) 

    # fetch the line buffer and save to string
    def printLineBuffer(self):
        self.displayText = ""
        for key in self.dictionaryBuffer:
            self.displayText += f"{key}: {self.dictionaryBuffer[key]}\n"

    # register the function callback for text
    def registerTextFunctionCallback(self, textFunction):
        self.textFunctionCallback = textFunction

