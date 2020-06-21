import pyperclip 

# dictionary class for fetching 
# calling the fetchentry function will load the lineBuffer property
# with list of found kanji 
class myDictionary:

    # initialize variables that need to be kept track of
    def __init__(self, thisFile):
        self.thisDictionary = {}
        self.dictionaryInit(thisFile)
        self.newData = "NULL"
        self.oldData = "NULL"
        self.lineBuffer = {}


    # initialize dictionary object from file and 
    # load all entires into thisDictionary hashmap 
    # longest initial startup
    def dictionaryInit(self, thisFile):
        with open(thisFile, encoding="utf-8") as f:
            for line in f:
                key, value = line.strip().split(" ", maxsplit=1)
                self.thisDictionary[key] = value


    # check the dictionary for new data. if new data is found,
    # search thisDictionary for the corresponding line entry.
    # new data is stored to line buffer
    def dictionaryCheck(self):
        self.newData = pyperclip.paste()
        if self.oldData != self.newData:
            print("Reading New Clipboard Data:\n")
            # clear the current kanji list and make new one
            self.lineBuffer.clear()
            self.fetchEntry()
            self.oldData = self.newData
            #self.printLineBuffer(self.lineBuffer)
            #return "something new"
            return self.lineBuffer
        
        #return "nothing new"
        return self.lineBuffer

    # print the key value pair of the found entries
    def printLineBuffer(self, lineBuffer):
        for key in lineBuffer:
            print(f"{key}: {lineBuffer[key]}\n")

    # fetch kanji list from clipboard and save to linebuffer
    def fetchEntry(self):    
        bufferIndex = 0

        #iterate over every element in clipboard
        i = 0
        while i < (len(self.newData)):
            
            # check if the character is kanji
            if ord(self.newData[i]) in range(0x4E00,  0x9FAF): 
                
                # get the entry and translation
                # i updates so that it skips already translated words
                entry, translation, i = self.dictionarySearch(i)

                self.lineBuffer[bufferIndex] = f"{entry} - {translation}"
                
                bufferIndex += 1

            else: 
                i += 1

    # find the longest matching entry starting from i
    def dictionarySearch(self, i):
        entry, translation = self.newData[i], "NO TRANSLATION"

        # keeps track of accuracy of character
        j = i + 1
        counter = j

        # keep track of end of string
        maxIndex = len(self.newData) + 1

        while j < maxIndex:
           
            # use string slicing to select substring
            # safe for j to be greater than the length of the string
            k = self.newData[i:j]
            #print(self.newData[i:j])

            # use dict.get(key) instead of dict[key]
            # .get returns default value of none instead of error
            # can set the default value with dict.get(key, default)
            t = self.thisDictionary.get(k)
            #print(t)

            # currently iterates through entirety of untranslated string,
            # is this neccessary?
            if t is not None:
                entry, translation = k, t
                counter = j

            j +=1

        return entry, translation, counter