'''
Created on May 3, 2016

@author: jwb33
'''

from tkinter import *
from soil import *
from veg_list import *
from profit_calc import *



class Garden:

    def __init__(self, window):
        
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        
        self.terminated = False 
        
        self._current = True
        self._row_count = 1
        
        self._planted_list = []
        
        self.layout = Soil(window)
        
        #All the calculator class here
        self.calculator = Calculator(window, self._planted_list)
        
        
        vis_label = Label(window,text='Visualization',font=('Arial',20,'bold'))
        vis_label.grid(row=0,column=3, sticky=S)
        
        #welcome title text
        welcome = Label(window,text='Welcome!',font=('Arial',20,'bold'), fg='green')
        welcome.grid(row=0,column=0, sticky=N, columnspan=3, padx=150)
        
        #Veggie list frame
        self.veggie_frame= Frame(window)
        self.veggie_frame.grid(row=1, column=0, sticky=N)
        
        #Frame for planted crop list
        self.crop_list_frame=Frame(self.veggie_frame)
        self.crop_list_frame.grid(row=11, column=1, sticky=NW, rowspan=10)
        
        #select your preferred vegetable
        select_write= Label(self.veggie_frame, text='Select your desired vegetable to plant and click \nthe desired location to plant on the grid', font='bold')
        select_write.grid(row=0, column=0, columnspan=2, sticky=N,pady=5)
        
        #rules and assumption text
        #http://www.harvesttotable.com/2011/05/vegetable_seeds_per_ounce_per/
        #http://www.edenbrothers.com/store/corn_seeds.html
        rules= Label(self.veggie_frame, text='Rules and assumptions:\n\
        -Type the crop you desire exactly as written on the list\n\
        -Seed Price is based on edenbrothers.com\n-Revenue is from rough assumption that every seed is\n\
        successful with number of seed per ounce based \non harvesttotable.com\n\
        -Tall-grass prairie is required as crop rotation for healthy soil\n\
        -Always click "Plant!" before planting them on the grid ')
        rules.grid(row=1, column=0, columnspan=2, sticky=N)
        
        #Label for warm-climate crops
        Label(self.veggie_frame, text='Warm-climate crops', font='bold').grid(row=2, column=0, columnspan=2, sticky=N)
        
        #List of warm vegetables down the list
        Label(self.veggie_frame, text=warmvegs_type).grid(row=3, column=0, sticky=N)
        #warm veggies price
        Label(self.veggie_frame, text=warmvegs_price).grid(row=3, column=1, sticky=N)
        
         #Label for cool-climate crops
        Label(self.veggie_frame, text='Cool-climate crops', font='bold').grid(row=4, column=0, columnspan=2, sticky=N )
        
        #List of cool vegetables down the list
        Label(self.veggie_frame, text=coolvegs_type).grid(row=5, column=0, sticky=N)
        #cool climate price
        Label(self.veggie_frame, text=coolvegs_price).grid(row=5, column=1, sticky=N)
        
        #'type your veggie' command label and entry box
        type_crop = Label(self.veggie_frame, text='Type the desired crop to grow:')
        type_crop.grid(row=6, column=0, sticky=NE)
        
        
        #Entry box
        self._cropType = StringVar()
        type_crop_entry = Entry(self.veggie_frame, textvariable= self._cropType)
        type_crop_entry.grid(row=7, column=0, sticky=E)
        
        #Plant! Button
        plant_button = Button(self.veggie_frame, text='Plant!', command=self.get_crop)
        plant_button.grid(row=7,column=1, sticky=W)
        
        #grass prairie buton
        grass_button = Button(self.veggie_frame, text='Tall-grass prairie', command=self.prairie_grass)
        grass_button.grid(row=8, column=1, sticky=W)
        
        #Label for currently selected crop
        selected_picture = Label(self.veggie_frame, text='Currently selected:')
        selected_picture.grid(row=10, column=0)
        
        #prairie picture and caption is on default       
        self._prairie = PhotoImage(file= './'+ 'images/prairie.gif')
        picture_prairie = Label(self.veggie_frame, image= self._prairie )
        picture_prairie.grid(row=11, column=0)
        
        #Caption for picture
        self.crop_now = StringVar()
        self.crop_now.set('Tall-grass prairie')
        self.caption(self.crop_now)
       
        
        #Crops you have planted list label
        planted_crop = Label(self.veggie_frame, text='Crops you have planted:')
        planted_crop.grid(row=10, column=1)
        
        #error label
        self.error_text = StringVar()
        self.error_text.set('')
    
    def error_message (self, error_a):
        Label(self.veggie_frame, textvariable = error_a, fg='red').grid(row=9, column=0, columnspan=3, sticky=N)
    
    def caption(self, capt):
        Label(self.veggie_frame, textvariable = capt).grid(row=12, column=0)  
        
     #access selected crop type    
    def get_crop(self):
        
            
        if self._cropType.get() in all_vegs:
            self.layout.change_crop(self._cropType.get())
            
            #picture sample
            self._photo = PhotoImage(file= './'+ self.layout._veg_dict[self._cropType.get()])
            picture = Label(self.veggie_frame, image= self._photo )
            picture.grid(row=11, column=0)
            
            #to help counting up for the list of crops planted
            self._current = False
            
            if self._current == False:
                self._row_count += 1
                self._current == True
                self._planted_list.append(self._cropType.get())
            
            if self._row_count == 21:
                Label(self.window, text='Exceeded maximum amount of planting!', fg='red').grid(row=1, column=3)
                plant_button = Button(self.veggie_frame, text='Plant!', command=self.get_crop, state=DISABLED)
                plant_button.grid(row=7,column=1, sticky=W)
            
            #caption for picture
            self.crop_now.set(self._cropType.get())
            self.caption(self.crop_now)
            
            #list of planted crops
            planted = Label(self.crop_list_frame, text= self._cropType.get())
            planted.grid(row=self._row_count,column=0, sticky=W)
            
            #error text
            self.error_text.set('')
            self.error_message(self.error_text)    
            
        else:
            self.error_text.set('Type your crop of choice exactly as listed above')
            self.error_message(self.error_text)            


    #button to return to default prairie grass   
    def prairie_grass(self):
        self.layout.change_crop('Tall-grass prairie')
       
        #picture
        self._photo = PhotoImage(file= './'+ 'images/prairie.gif')
        picture = Label(self.veggie_frame, image= self._photo )
        picture.grid(row=11, column=0)
        
        #caption for pic
        self.crop_now.set(self.layout.get_croptype())
        self.caption(self.crop_now)
        
        print(self.crop_now.get())

    #Turn off the event loop before closing the GUI
    def safe_exit(self):
        self.terminated = True
        self.window.destroy()
        
if __name__ == '__main__':
    root = Tk()
    root.title('Budi\'s Garden manager') 
    root.geometry('1200x900')  
    app = Garden(root)
    
    root.mainloop()