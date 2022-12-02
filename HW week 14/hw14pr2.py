
# CSCI1550
# homework 14 problem 2
# hw14pr2.py
# Name: Peter Morales

from csci1550png import *
import copy


def change( p ):
    """ change takes in a pixel (an [R,G,B] list)
        and returns a new pixel to take its place!
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    return [ 255-red, 255-green, 255-blue ]


def invert(fname = 'in.png'):
    """Run this function to read the in.png image,
       change it, and write the result to out.png.
    """
    Im_pix = getRGB(fname)  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])
    #
    # Remember that Im_pix is a list (the image)
    # of lists (each row) of lists (each pixel is [R,G,B])
    #
    New_pix = copy.deepcopy(Im_pix)
    [numCols, numRows] = getWH(New_pix)
    for rowInd in range(numRows):
        for colInd in range(numCols):
            New_pix[rowInd][colInd] = change(New_pix[rowInd][colInd])
    # now, save to the file 'out.png'
    saveRGB(New_pix, 'out.png')
    
# test it out!
#invert('olin.png')


def testBinaryImage():
    """ run this function to create an 8x8 alien image
        named binary.png
    """
    ALIEN = "0"*8 + "11011011"*2 + "0"*8 + "00001000" + \
            "01000010" + "01111110" + "0"*8
    # this function is imported from cs1550png.py
    NUM_ROWS = 8
    NUM_COLS = 8
    binaryIm( ALIEN, NUM_COLS, NUM_ROWS )
    # that should create a file, binary.png, in this
    # directory with the 8x8 image...




def newChange( p ):
    """ change takes in a pixel (an [R,G,B] list)
        and returns a new pixel to take its place!
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    lum = int((red*.21) + (green*.71) + (blue*.07))
    return [ lum, lum, lum ]

def greyscale(fname):
    Im_pix = getRGB(fname)  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])
    New_pix = copy.deepcopy(Im_pix)
    [numCols, numRows] = getWH(New_pix)
    for rowInd in range(numRows):
        for colInd in range(numCols):
            New_pix[rowInd][colInd] = newChange(New_pix[rowInd][colInd])
    # now, save to the file 'out.png'
    saveRGB(New_pix, 'out.png')

#greyscale('spam.png')




def threshChangeBlack():
    red = 0
    green = 0
    blue = 0
    return [ red, green, blue ]

def threshChangeWhite():
    red = 255
    green = 255
    blue = 255
    return [ red, green, blue ]

def threshCompare( p ):
    red = p[0]
    green = p[1]
    blue = p[2]
    return [ red, green, blue ]

def binarize(fname, thresh):
    greyscale(fname)
    Im_pix = getRGB('out.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])
    New_pix = copy.deepcopy(Im_pix)
    [numCols, numRows] = getWH(New_pix)
    for rowInd in range(numRows):
        for colInd in range(numCols):
            if thresh <= threshCompare(New_pix[rowInd][colInd])[0]:
                New_pix[rowInd][colInd] = threshChangeWhite()
            if thresh >= threshCompare(New_pix[rowInd][colInd])[0]:
                New_pix[rowInd][colInd] = threshChangeBlack()

            if thresh <= threshCompare(New_pix[rowInd][colInd])[1]:
                New_pix[rowInd][colInd] = threshChangeWhite()
            if thresh >= threshCompare(New_pix[rowInd][colInd])[1]:
                New_pix[rowInd][colInd] = threshChangeBlack()

            if thresh <= threshCompare(New_pix[rowInd][colInd])[2]:
                New_pix[rowInd][colInd] = threshChangeWhite()
            if thresh >= threshCompare(New_pix[rowInd][colInd])[2]:
                New_pix[rowInd][colInd] = threshChangeBlack()

    # now, save to the file 'out.png'
    saveRGB(New_pix, 'out.png')

#binarize('spam.png', 100)

def scaleBy2(fname):
    Im_pix = getRGB(fname)  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])
    New_pix = copy.deepcopy(Im_pix)
    [numCols, numRows] = getWH(New_pix)
    for rowInd in range(numRows):
        for colInd in range(numCols):
            if rowInd%2 != 0:
                New_pix[rowInd][colInd] = New_pix[rowInd-1][colInd]
            if colInd%2 != 0:
                New_pix[rowInd][colInd] = New_pix[rowInd][colInd-1]
    # now, save to the file 'out.png'
    saveRGB(New_pix, 'out.png')

#scaleBy2('spam.png')

def is1or0(p):
    red = p[0]
    green = p[1]
    blue = p[2]
    if red and green and blue == 255:
        return True
    if red and green and blue == 0:
        return False


def pngToBinaryString(fname, thresh):
    binarize(fname, thresh)
    Im_pix = getRGB('out.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])
    New_pix = copy.deepcopy(Im_pix)
    [numCols, numRows] = getWH(New_pix)
    binList = []
    for rowInd in range(numRows):
        for colInd in range(numCols):
            if is1or0(New_pix[rowInd][colInd]) == True:
                binList.append('1')
            else:
                binList.append('0')

    return ''.join(binList), numCols, numRows
    

def compress(S):
    binStr = []
    counterList = []   
    starterList = []
    while S != '':
        counter = 0
        starter = S[0]
        starterList.append(starter)
        for j in S:
            if counter == 127:
                break
            if starter == j:
                counter += 1
                S = S[1:]
            else:
                break
        counterList.append(counter)
    
    while counterList != []:
        counter2 = 0 
        bTen = counterList[0]
        binList = []
        while counter2 != 7:
            counter2 += 1
            if bTen%2 == 0:
                binList.insert(0,'0')
                bTen = bTen//2
            else:
                binList.insert(0,'1')
                bTen = bTen//2
        
        binList.insert(0,starterList[0])
        starterList = starterList[1:]
        binStr.append(''.join(binList))
        counterList = counterList[1:]
    
    return ''.join(binStr)


def uncompress(S):
    totalList = []
    total = 0
    counter = 0
    outputStr = []
    while S != '':
        oneOrZero = S[0]
        counter = 0
        while counter != 8:
            totalList.append(S[0])
            S = S[1:]
            counter += 1
        totalList = totalList[1:]
        
        counter2 = 0
        total = 0
        for i in range(len(totalList)):
            if totalList == []:
                break
            if totalList[-1] == '1':
                total += (2**i)
                counter2 += 1
            totalList = totalList[:-1]
        
        outputStr.append(str(oneOrZero*total))
    
    return ''.join(outputStr)

def compressedBinaryIm(s, cols, rows):
    S = uncompress(s)
    PX = []
    for row in range(rows):
        ROW = []
        for col in range(cols):
            c = int(S[row*cols + col])*255
            px = [ c, c, c ]
            ROW.append( px )
        PX.append( ROW )
    saveRGB( PX, 'binary.png' )
