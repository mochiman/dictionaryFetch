import codecs
import pyperclip
import pandas as pd

# returns somewhat formatted list of dictionary entries (very slow)

def main():

    # initialize dictionary
    # using rikaichamp dictionary
    thisFile = 'data/dict.dat'

    #thisString = ""
    
    kanjiDictionary = myDictionary(thisFile)

    # main program loop
    while 1:

        kanjiDictionary.newData = pyperclip.paste()
        # shove a stop character onto it
        kanjiDictionary.newData += 'F'

        # if the clipboard holds new data
        kanjiDictionary.dictionaryCheck()

    return 0


# dictionary class for fetching 
# calling the fetchentry function will load the lineBuffer property
# with list of found kanji 
class myDictionary:

    # initialize variables that need to be kept track of
    def __init__(self, thisFile):
        self.thisDictionary = codecs.open(thisFile, 'r', 'utf-8')
        self.newData = "NULL"
        self.oldData = "NULL"
        self.lineBuffer = {}


    def dictionaryCheck(self):
        if self.oldData != self.newData:
            print("Reading New Clipboard Data:\n")
            self.fetchEntry()
            self.oldData = self.newData
            #print(kanjiDictionary.lineBuffer)
            brics = pd.Series(data=self.lineBuffer, dtype=object)
            print(brics)

    # fetch kanji list from clipboard and save to linebuffer
    def fetchEntry(self):
        self.lineBuffer.clear()
        
        bufferIndex = 0

        #iterate over every element in clipboard
        #for element in newData:
        i = 0
        while i < (len(self.newData)):
        #for i in range ( len(newData) ):
            
            # check if the character is kanji
            if ord(self.newData[i]) in range(0x4E00,  0x9FAF): 

                # reset counter, get new value 
                counter = 0
                foundWord, counter = self.dictionarySearch(i)
                #print(foundWord)
                self.lineBuffer[bufferIndex] = foundWord
                bufferIndex += 1

                # skip re-using words
                i += counter - 1
                self.thisDictionary.seek(0)

            i += 1

    def dictionarySearch(self, i):
        prevLine = ""

        # keeps track of accuracy of character
        counter = 0
        
        #print(mainString)
        # we need to add a kanji checker in here
        # we don't really wanna check if it's in there; check first index of line
        for line in self.thisDictionary:
            if self.newData[i] == line[0]: 

                # we need to work on each invidual line to find ideal match
                newCount = 0
                j = 0
                while self.newData[i + j] != 'F':  
                    if self.newData[i + j] != line[j]:
                        break

                    j += 1
                    newCount += 1

                if newCount > counter:
                    counter = newCount
                    prevLine = line

            continue

                #if counter < 2:
                    #return newData[i]


        # if no line is found, return previous line
        return prevLine, counter

if __name__ == "__main__":
    main()

