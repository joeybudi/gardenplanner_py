'''
Created on May 3, 2016

@author: jwb33
'''

from tkinter import *
from gui import *


                
class Soil:
    
    
    def __init__(self, window):
        
        self.window = window
        
        self.plot = Frame(window)
        self.plot.grid(row=1,column=3, sticky=N)
        
        self._veg_dict = {'Corn': 'images/corn.gif', 'Cucumber':'images/cucumber.gif', 'Eggplant':'images/eggplant.gif',
                          'Pepper': 'images/pepper.gif','Tomato':'images/tomato.gif',  'Beet':'images/beet.gif', 'Broccoli':'images/broccoli.gif', 'Cabbage':'images/cabbage.gif', 'Carrot':'images/carrot.gif',
                          'Kale':'images/kale.gif', 'Bokchoy':'images/bokchoy.gif', 'Tall-grass prairie':'images/prairie.gif' }
        self._cropType = 'Tall-grass prairie'
        
        self._photos = []
        
        
        #@smn4 from telephone dialer example
        for i in range (0,20):
            self.b1=Button(self.plot, width=10, height=7, command=lambda x=i: self.planting(x//4, x%4))
            self.b1.grid(row=i//4, column=i%4)

    
    def planting(self, r, c):
        if self._cropType in self._veg_dict:
            print(self._cropType)
            canvas = Canvas(self.plot, bg='green', width=100, height=100)
            
            #canvas.create_text(50,50,text=self._veg_dict.get(self._cropType,'N/A'), fill='white')
            
            #with @smn4
            self._photos.append(PhotoImage(file='./'+ self._veg_dict.get(self._cropType)))
            canvas.create_image(50,50,image=self._photos[len(self._photos)-1])
            
            canvas.grid(row=r,column=c)
            
            
            #with open('list_planted', 'a') as planted:
                #planted.write(self._cropType + '\n') 
    
    #mutator to change crop      
    def change_crop(self,newcrop):
        self._cropType= newcrop
        
    def get_croptype(self):
        return self._cropType
            
if __name__ == '__main__':
    root = Tk()
    app = Soil(root)
    root.title('Soil')
    root.mainloop()