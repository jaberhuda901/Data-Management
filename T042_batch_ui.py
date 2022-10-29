from T042_image_filters import *
from Cimpl import * 
from simple_Cimpl_filters import grayscale

BLACK = create_color(0,0,0)
WHITE = create_color(255,255,255)
BLOOD = create_color(255,0,0)
GREEN = create_color(0,255,0)
BLUE = create_color(0,0,255)
LEMON = create_color(255,255,0)
CYAN = create_color(0,255,255)
MAGENTA = create_color(255,0,255)
GRAY = create_color(128,128,128) 

def _readScript(textFile: str):
    """opens and reads a text file then returns a copy of an image given, applies a series of given filters and saves the new image as the given name, closes the text file
    NAME: Jordan Geils
    # STUDENT ID: 101191770
    NAME: ARYAN MATHUR
    # STUDENT ID: 101211143
    """
    filterInfo = open(textFile, "r")
    
    arrayOfInfo = filterInfo.readlines()

    for x in range(len(arrayOfInfo)):
        lst = arrayOfInfo[x].split()
        i = 0
        for word in lst:
            if i == 0:
                image = Image(word)
            if i == 1:
                save_file = word
            if word == '3':
                image3 = three_tone(image, BLOOD, GRAY, LEMON)
                save_as(image3, save_file)
                image = image3
                
            elif word == 'S':
                imageS = sepia(grayscale(image))
                save_as(imageS, save_file)
                image = imageS    
                
            elif word == 'P':
                imageP = posterize(image)
                save_as(imageP, save_file)
                image = imageP
            
            elif word == 'X':
                imageX = extreme_contrast(image)
                save_as(imageX, save_file)
                image = imageX
            
            elif word == 'V':
                imageV = flip_verticle(image)
                save_as(imageV, save_file)
                image = imageV
        
            elif word == 'H':
                imageH = flip_horizontal(image)
                save_as(imageH, save_file)
                image = imageH
            
            elif word == 'E':
                imageE = detect_edges(image, 15)
                save_as(imageE, save_file)
                image = imageE 
            i += 1
        show(image) 
        print(lst)
    filterInfo.close()

_readScript("test.txt")

    

    



    
    
