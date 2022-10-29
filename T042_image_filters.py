from Cimpl import * 
from unit_testing import check_equal
import numpy

#FILTER THREE TONE
BLACK = create_color(0,0,0)
WHITE = create_color(255,255,255)
BLOOD = create_color(255,0,0)
GREEN = create_color(0,255,0)
BLUE = create_color(0,0,255)
LEMON = create_color(255,255,0)
CYAN = create_color(0,255,255)
MAGENTA = create_color(255,0,255)
GRAY = create_color(128,128,128) 

def three_tone(image,colour_1,colour_2,colour_3):
    """
    NAME: JABER-UL HUDA
    STUDENT ID: 101137524
    
    
    Returns a copy of an image which has three colors set by the user.
    The user has to choose any three among black, white, blood, green, blue,
    lemon, cyan, magenta and gray
    
    >>> image = load_image(choose_file())
    >>> three_tone_image = three_tone(image,black,lime,white)
    >>> show(three_tone_image)
    """  
    copy_image=copy(image)
    
    for x, y, (r, g, b) in copy_image:
         
        
        pixel_brightness = (r + g + b) // 3
        
        if 0 <= pixel_brightness <= 84:
            new_colour = colour_1
            set_color(copy_image, x, y, new_colour)
        
        elif 85 <= pixel_brightness <= 170:
            new_colour = colour_2
            set_color(copy_image, x, y, new_colour)
        
        else:
            new_colour = colour_3
            set_color(copy_image, x, y, new_colour)

    return copy_image



#FILTER SEPIA
def sepia_tint(image: Image) ->Image:
    """returns a copy of a grayscaled that has sepia tinting
    
    >>>image=load_image(choose_file())
    >>>blue_image=blue_channel(image)
    >>>show(blue_image)
    Jordan Geils
    """
    sepia_image = copy(image)
    for x, y, (r,g,b) in image:
        if r < 63:
            sepia_dark = create_color(r*1.1, g, b*0.9)
            set_color(sepia_image, x, y, sepia_dark)
        elif 63 <= r <= 191:
            sepia_med = create_color(r*1.15, g, b*0.85)
            set_color(sepia_image, x, y, sepia_med)
        else:
            sepia_light = create_color(r*1.08, g, b*0.93)
            set_color(sepia_image, x, y, sepia_light)
    return sepia_image


#FILTER POSTERIZE
def _adjust_component(value: int) -> int:
    
    '''
    NAME: ARYAN MATHUR
    # STUDENT ID: 101211143
    
    This function applies returns the adjusted interger value requried for
    the poseterize function
    
    '''
    
    if ((value >= 0) and (value <= 63)):
        return 31
    elif ((value>=64) and (value <= 127)):
        return 95
    elif ((value >=128) and (value <= 191)):
        return 159
    else:
        return 223
    
def posterize (image: Image) -> Image:
    
    '''
     NAME: ARYAN MATHUR
     # STUDENT ID: 101211143
     
     This function applies the posterize filter to a given image
     
    >>>newPhoto = copy(originalPhoto)
    >>>set_color(newPhoto, x, y, finalColor)
    >>>return newPhoto
    '''
    newPhoto = copy(image)
    
    for x, y, (r,g,b) in newPhoto:
        imageColor = get_color(newPhoto, x, y)
        redVal = _adjust_component(imageColor[0])
        greenVal = _adjust_component(imageColor[1])
        blueVal = _adjust_component(imageColor[2])
        finalColor = create_color(redVal, greenVal, blueVal)
        set_color(newPhoto, x, y, finalColor)
    return newPhoto


#FILTER EXTREME
def colorChanger(value: int) -> int:
    if ((value >= 0) and (value <= 127)):
        return 0
    elif ((value>=128) and (value <= 255)):
        return 255
       

def extreme_contrast(image: Image) -> Image:
    '''
     NAME: ARYAN MATHUR
     # STUDENT ID: 101211143
    
    This function applies the extreme_contrast filter to any image passed into it
    by manipulating each rgb value to their extremes
    
    >>>newPhoto = copy(originalPhoto)
    >>>set_color(newPhoto, x, y, finalColor)
    >>>return newPhoto
    '''
    
    newPhoto = copy(image)
    
    for x, y, (r,g,b) in newPhoto:
        imageColor = get_color(newPhoto, x, y)
        redVal = colorChanger(imageColor[0])
        greenVal = colorChanger(imageColor[1])
        blueVal = colorChanger(imageColor[2])
        finalColor = create_color(redVal, greenVal, blueVal)
        set_color(newPhoto, x, y, finalColor)
    return newPhoto



#-----------------------------------------------------------------------------------------


#EDGE DETECTION
def detect_edges(image: Image,threshold: int) -> Image :
    
       
    """
    
    NAME: JABER-UL HUDA
    STUDENT ID: 101137524
    
    Returns a copy  of the image  that looks like a pencil sketch, by changing 
    the pixels to black or white
    
    >>> image=load_image(choose_file())
    >>> edge_image = detect_edges(image, 50 )
    >>> show(edge_image)
    
    """
    BLACK = create_color(0,0,0)
    WHITE = create_color(255,255,255)
    copy_image = copy(image)
    
    
    
    for x in range(0,get_width(image)):
        set_color(copy_image,x,get_height(image)-1,WHITE)
    
    for y in range(0,get_height(image)-1):
        for x in range(0,get_width(image)):
            
            
            
            top_r,top_g,top_b = get_color(image,x,y)
            bottom_r,bottom_g,bottom_b = get_color(image,x,y+1)
            
            top_brightness = (top_r+ top_g + top_b) // 3
            bottom_brightness = (bottom_r + bottom_g + bottom_b) // 3 
            
            contrast= abs(top_brightness - bottom_brightness)
            
            if contrast>threshold:
                set_color(copy_image,x,y,BLACK)
            else:
                set_color(copy_image,x,y,WHITE)
    
    return copy_image

#FLIP VERTICAL
def flip_verticle(image: Image) ->Image:
    """ 
    
    NAME: Jordan Geils
    STUDENT ID: 101191770
    
    Returns a copy if an image that is flipped over a horizontal axis
    
    >>>image = load_image(choose_file())
    >>>flip_image = flip_verticle(image)
    >>>show(flip_image)
    
    101191770
    """    
    flip_v_image = copy(image)
    
    width = image.get_width()
    height = image.get_height()    
    z = 0
    for x in range(0, width):
        for y in range(0, height):
            if z == height:
                z = 0
            Y = height - z - 1
            set_color(flip_v_image, x, Y, get_color(image, x, y))
            z += 1
    return flip_v_image



#FLIP HORIZONTAL
def flip_horizontal(image: Image) ->Image:
    """ 
    
    NAME: Jordan Geils
    STUDENT ID: 101191770
    
    Returns a copy if an image that is flipped over a verticle axis
    
    >>>image = load_image(choose_file())
    >>>flip_image = flip_horizontal(image)
    >>>show(flip_image)
    
    """
    flip_h_image = copy(image)
    
    width = image.get_width()
    height = image.get_height()    
    z = 0
    for y in range(0, height):
        for x in range(0, width):
            if z == width:
                z = 0
            X = width - z - 1
            set_color(flip_h_image, X, y, get_color(image, x, y))
            z += 1
    return flip_h_image

#DRAW CURVE
def draw_curve (image: Image, color: str, pointlist: list) -> (Image, list):
    """
    NAME: ARYAN MATHUR
    STUDENT ID: 101211143
    
    Takes an image, color string, and list of coordinates. Returns an image with a curve going through the coordinates
    
    >>> for x in range(numPoints): --> gets coordinates if none are given
    >>> _interpolation: --> returns a coeffecient list with the given coordinates
    >>> _image_border_finding --> returns which points are in the picture.
    >>> draws all points in given color on the newImage
    
    """
    newImage = copy(image)
    
    #assigns all color values
    if (color == "black"):
        colorVal = create_color(0,0,0)
    elif (color == "white"):
        colorVal = create_color(255,255,255)
    elif (color == "blood"):
        colorVal = create_color(255,0,0)
    elif (color == "green"):
        colorVal = create_color(0,255,0)
    elif (color == "CYAN"):
        colorVal = create_color(0,255,255)    
    else:
        colorVal = create_color(0,0,255)     
    
    #checks if a list is empty, is so, asks for coordinate values
    if not pointlist:
        print("The size of your image is",image.get_width(), "x", image.get_height()) 
    
        pointlist = []
        numPoints = int(input("Number of Points: \n"))
        
        for x in range(numPoints):
            #input x and y values
            coordinateX = int(input("Enter the x-component of coordinate #" + str(x+1) + "\n"))
            coordinateY = int(input("Enter the y-component of coordinate #" + str(x+1) + "\n"))
            pointlist.append((coordinateX,coordinateY))
            pointlist.sort()
    #if passed list is full, sort it   
    else:
        numPoints = len(pointlist)
        pointlist.sort()
    
    
    def _interpolation(list):
        xCoordinateList = []
        for item in list:
            #split all x componnents into one list
            xCoordinateList.append(item[0])
        
        yCoordinateList = []
        for item in list:
            #split all y components into one list
            yCoordinateList.append(item[1])  
       
        #do math to get coeffecients
        coeffecientArray = numpy.poly1d(numpy.polyfit(xCoordinateList, yCoordinateList, numPoints-1))
        return coeffecientArray
                               
    def _image_border_finding(xMax: int, coeffecient:list, yMax: int) -> list:
        xWithin = [] # all x values that are within image bounds
        for x in range(xMax):
            value = numpy.polyval(coeffecient, x)
            if (value >= 0) and (value <= yMax):
                xWithin.append(x) 
            else:
                continue
        return xWithin
    
    def lineClip(xMax: int, coeffecient:list, yMax: int) -> list:
        #all coordinates that are on the border of the image
        coordinateClip = []
        for x in range(xMax):
            value = numpy.polyval(coeffecient, x)
            if (x == 0) or (x == xMax) or (value == 0) or (value == yMax):
                coordinateClip.append((x, value)) 
            else:
                continue
        return coordinateClip  
    
    listClip = lineClip(image.get_width(), _interpolation(pointlist), image.get_height())
    
    allowedX = _image_border_finding(image.get_width(), _interpolation(pointlist), image.get_height())
    
    for x in range(len(allowedX)):
        
        if ((int(numpy.polyval(_interpolation(pointlist), x))-2) >= 0):
            set_color(newImage, allowedX[x], int(numpy.polyval(_interpolation(pointlist), x))-2, colorVal)
            
        if ((int(numpy.polyval(_interpolation(pointlist), x))-1) >= 0):
            set_color(newImage, allowedX[x], int(numpy.polyval(_interpolation(pointlist), x))-1, colorVal)
            
        set_color(newImage, allowedX[x], int(numpy.polyval(_interpolation(pointlist), x)), colorVal)
        
        if ((int(numpy.polyval(_interpolation(pointlist), x))+1) <= image.get_width()-1):
            set_color(newImage, allowedX[x], int(numpy.polyval(_interpolation(pointlist), x))+1, colorVal)
            
        if ((int(numpy.polyval(_interpolation(pointlist), x))+2) <= image.get_width()-1):
            set_color(newImage, allowedX[x], int(numpy.polyval(_interpolation(pointlist), x))+2, colorVal)
    
    return newImage, listClip







# ================================================================================

    # ----------- COMBINE FILTER ------------
    
    # NAME: ARYAN MATHUR     
    # STUDENT ID: 101211143
def combine(red_photo: Image, green_photo: Image, blue_photo: Image) -> Image:
        
        '''
        This function is used to combine the red, green, and blue components of 
        one picture. The function will iterate through each pixel of all three images
        and store their RGB values, before creating a new color for each pixel in a new
        image and returning it
        
    
        >>> combine(red_photo, green_photo, blue_photo)
        >>> return combined photo 
        
        '''
        
    comb_image = copy(red_photo)
        
    for x, y, (r, g, b) in comb_image:
        #get all colors from respective images
        imageColor_r = get_color(red_photo, x, y)
        #print(imageColor_r)
        imageColor_g = get_color(green_photo, x, y)
        imageColor_b = get_color(blue_photo, x, y)
            
        #add all color values up
        red_final = imageColor_r[0] + imageColor_g[0] + imageColor_b[0]
        green_final = imageColor_r[1] + imageColor_g[1] + imageColor_b[1]
        blue_final = imageColor_r[2] + imageColor_g[2] + imageColor_b[2]
            
        #create the final color and set it to the new created image, then return
        finalColor = create_color(red_final, green_final, blue_final)
        set_color(comb_image, x, y, finalColor)
    return comb_image

# ----------- RED FILTER ------------

# NAME: JABER-UL HUDA
# STUDENT ID: 101137524

def red_channel(image: Image) -> Image :
    
    """Return the red channel of an coloured png image file. Thus only the red value 
    of the RGB is shown and others filtered out.
    
    >>> image = load_image(choose_file()) 
    >>> red_image = red_channel(image)
    >>> show(red_image)     
    """    
    
    copy_image = copy(image)
    
    for x, y, (r, g, b) in copy_image:
        red = create_color(r, g - 255, b - 255)
        set_color(copy_image, x, y, red)
    return copy_image

# ----------- BLUE FILTER ------------

#Student ID: 101191770
#Name: Jordan Geils 


def blue_channel(image: Image) ->Image:
    """ Returns a new image that is bue. Only the blue components of the pixels are shown
    
    >>>image=load_image(choose_file())
    >>>blue_image=blue_channel(image)
    >>>show(blue_image)
    """
    new_b_image = copy(image)
    
    for x, y, (r,g,b) in new_b_image:
        blue = create_color(r-255, g-255, b)
        set_color(new_b_image, x, y, blue)
    return new_b_image

# ----------- GREEN FILTER ------------


# NAME: Abdullah Fayad
# STUDENT ID:  101135979

def green_channel(image: Image) -> Image :
    
    """Return the green channel image copy in png format. takes a monocromed coloured imge
       in png format. then shows the green channel of the image only.
    
    >>> image = load_image(choose_file()) 
    >>> green_image = green_channel(image)
    >>> show(green_image)     
    """    
    
    copy_image = copy(image)
    
    for x, y, (r, g, b) in copy_image:
        green = create_color(r- 255, g , b - 255)
        set_color(copy_image, x, y, green)
    return copy_image