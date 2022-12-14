import os
from PIL import Image
import time
"""
takes in two arguments, one being a file
prints out filename
assigns W and H with the helper function "getWH"
assigns im to a new image with values from W and H
assings px the values of im
loops through the range of H
nested loop through range of W
assigns variable bp the values of boxed_pixels[r][c]
assigns variable t tuple(bp)
assigns px[c,r] to the values of t
saves im file to filename
waits half a second
prints out saved.
"""
def saveRGB( boxed_pixels, filename="out.png" ):
    """ need docstrings! """
    print( 'Starting to save', filename, '...' )
    W, H = getWH( boxed_pixels )
    im = Image.new("RGB", (W, H), "black")
    px = im.load()
    for r in range(H):
        #print( ".", end="" )
        for c in range(W):
            bp = boxed_pixels[r][c]
            t = tuple(bp)
            px[c,r] = t
    im.save( filename )
    time.sleep(0.5)
    print( filename, "saved." )


"""
reads in a png file.
assigns the image to a variable. 
prints file format, size, and mode.
assigns width and height (318,293)
assigns px to original.load()
assigns an empty list called PIXEL_LIST
loops through the range of height
assings row as an empty list
loops throught the range of width
appends row to the value of px[c,r][:3] (slices from beginning to 2)
PIXEL_LIST is appended to the value of row.
returns PIXEL_LIST
"""
def getRGB( filename="in.png" ):
    """ reads a png file """
    original = Image.open(filename)
    print( "The size of the Image is: " )
    print(original.format, original.size, original.mode)
    WIDTH, HEIGHT = original.size
    px = original.load()
    PIXEL_LIST = []
    for r in range(HEIGHT):
        row = []
        for c in range(WIDTH):
            row.append( px[c,r][:3] )
        PIXEL_LIST.append( row )
    return PIXEL_LIST

def getWH( PX ):
    """ need docstrings! """
    H = len(PX)
    W = len(PX[0])
    return W, H


"""
finction takes in 3 arguments
assigns variable PX as an empty list
loops through the range of rows
assigns ROW as an empty list
nested loops through the range of cols
c = value calculated
px is assigned the values of c
ROW is appended with px
PX is appeneded with ROW
calls helper function saveRGB

"""
def binaryIm( s, cols, rows ):
    """ need docstrings! """
    PX = []
    for row in range(rows):
        ROW = []
        for col in range(cols):
            c = int(s[row*cols + col])*255
            px = [ c, c, c ]
            ROW.append( px )
        PX.append( ROW )
    saveRGB( PX, 'binary.png' )
    #return PX

class PNGImage:

    def __init__(self, width, height):
        """ constructor for PNGImage """
        self.width = width
        self.height = height
        default = (255,255,255)
        self.image_data = \
            [ [ default for col in range(width) ] \
                        for row in range(height)]

    def plotPoint(self, col, row, rgb=(0,0,0)):
        """ plot a single point to a PNGImage """
        # check if rgb is a three-tuple
        if type(rgb) == type( (0,0,0) ) and \
           len(rgb) == 3:
            pass # ok
        elif type(rgb) == type( [0,0,0] ) and \
           len(rgb) == 3:
            rgb = tuple(rgb)
        else:
            print( "in plotPoint, the color", rgb )
            print( "was not in a recognized format." )
            
        # check if we're in bounds
        if 0 <= col < self.width and \
           0 <= row < self.height:
            self.image_data[ row ][ col ] = rgb

        else:
            print( "in plotPoint, the col,row:", col, row, )
            print( "was not in bounds." )
            return

        return

    def saveFile( self, filename = "test.png" ):
        """ save the object's data to a file """
        # we reverse the rows so that the y direction
        # increases upwards...
        saveRGB( self.image_data[::-1], filename )




    
