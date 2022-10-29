
from Cimpl import *
from T042_image_filters import *  
from simple_Cimpl_filters import grayscale

#name: JABER-UL HUDA
#STUDENT ID: 101137524

def main_logic(copy_image) -> str :
    
    '''
    this function contains main logic as it contains all the filter function calls. 
    this function returns a string to be used in conjunction with main_program
    
    
    
    '''
    
    load_run = True
    
    while load_run == True :
        
        command_prompt()  # displayes command prompt
        
        proper_comand_1 = ("3","X","T","P","E","D","V","H",'Q','S')
        user_input_2 = str(input(": "))            
        
        valid_input = True 
        
        i = 0
        
                    
        
        
        if user_input_2 == "V" :
            copy_image = flip_verticle(copy_image)
            show(copy_image)
        
        if user_input_2 == "H" :
            copy_image = flip_horizontal(copy_image)
            show(copy_image)               
        
        if user_input_2 == "T" :    # there is a problem with this 
            copy_image = sepia_tint(copy_image)
            show(copy_image)            
        
        if user_input_2 == "X" :
            
            #print('please enter an int value: ')
            #value_1 = int(input())
            
            #colorChanger(value_1)
            
            copy_image = extreme_contrast(copy_image)
            show(copy_image)            
        
        if user_input_2 == "P" :              
                
            
                
            copy_image = posterize(copy_image)
            show(copy_image)            
        
        if user_input_2 == "D" :
            
            CYAN = create_color(0,255,255)
                    
            lst = [] 
                    
            copy_image, func_list = draw_curve(copy_image,"CYAN",lst)
            show(copy_image) 
            print(func_list)
        
        if user_input_2 == "3" :
                    
            
            BLOOD = create_color(255,0,0)
            LEMON = create_color(255,255,0)
            GRAY = create_color(128,128,128)
                    
            copy_image = three_tone(copy_image,BLOOD,LEMON,GRAY)
            show(copy_image)    
            
        
        if user_input_2 == "E" :
                    
            value_3 = int(input('\n' +'threshold?: '))
                    
                   
            copy_image = detect_edges(copy_image,value_3)
            show(copy_image)            
            
        if user_input_2 == "T" :
            
            copy_image = sepia_tint(grayscale(copy_image))
            show(copy_image)            
        
        if user_input_2 == "S" :  
            save_as(copy_image)           
            load_run = False              
            run = False 
            print('\n' + 'the image has been saved and \n')
            #user_input = '3'       
            user_input = 'Q'
            return user_input            
            
        if user_input_2 == "Q" :
            load_run = False
            run = False 
            user_input = 'Q'
            return user_input
                   
            
        
        if not(user_input_2 in proper_comand_1) : 
            print('\n' +'please enter a valid command \n')


def command_prompt():
    print('L)oad image   S)ave-as')
    print('3)-tone  X)treme contrast T)int sepia P)osterize')
    print('E)dge detect D)raw curve V)ertical flip H)orizontal flip')
    print('Q)uit')
    print('')    


# MAIN SCRIPT 

run = True

loop_over = 0

while run == True : 
    
    command_prompt()     # displayes command prompt 
    
    proper_comand_first = ("3","X","T","P","E","D","V","H")
    
    proper_comand_1 = ("3","X","T","P","E","D","V","H",'Q','S')
    proper_comand_2 = ("3","X","T","P","E","D","V","H",'Q',)
    
    user_input = str(input(": "))  
    
    
    
    if user_input == "l" :
        user_input = "L"    
    
    if user_input == "L" :
        copy_image = load_image(choose_file())
        show(copy_image) 
        
                    
            
        main_logic(copy_image)
                
                
                    
                    
    if user_input == "Q":
        print('\n' +'the program has terminated \n ') 
        run = False        
        
    
    for i in proper_comand_first :
        if i == user_input :
            print(' \n No image loaded \n ') 
            
    if not(user_input in proper_comand_2) : 
        print('\n' +'please enter a valid command')    
    print('')
          
    loop_over += 1
    if loop_over == 2 :
        run = False   
    
