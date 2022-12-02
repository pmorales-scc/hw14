    def getLastLine(self):
        filenames = self.findTTT()
        lineList = []
        for i in range(len(filenames)):
            filename = filenames[i]
            myF = open(filename, "r")
            lines = myF.readlines()
            lines = lines[-1:]
            lineList.append(lines)
            #print(lines)
            myF.close()
        return list(lineList)
    
    def xWinsFreq(self):
        lastLines = self.getLastLine()      
        for i in range(len(lastLines)):
            print(lastLines[i])