import pyperclip
import tkinter as tk
from myDictionary import myDictionary
from displayWindow import app

# let's find a way to add one character to the string at a time:
# iterate through every element of string

def main():
    # main loop that prints line
    version = "v0.2"
    print(version)
    
    thisFile = 'data/dict.dat'
    # initialize the myDictionary kanji dictionary
    kanjiDictionary = myDictionary(thisFile)

    # Tkinter class root window
    root = tk.Tk()

    # pass dictionaryCheck as callback function
    appWindow = app(kanjiDictionary.dictionaryCheck)

    root.title('Kanji Dictionary Parser')
    root.geometry("500x100") #Width x Height
    #root.pack_propagate(0)
    root.mainloop()
    return 0


if __name__ == "__main__":
    main()

