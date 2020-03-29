'''
Created on May 16, 2016
Profit Calculator for Garden Manager Program
@author: jwb33
'''


from tkinter import *
from gui import *
from veg_list import *


class Calculator:
    
    def __init__(self, window, plist=[]):
        self.window = window
        
        self._planted_list = plist

        
        self.frame_calc = Frame(window, width=450, height=200)
        self.frame_calc.grid(row=1,column=4, sticky=NW)
        
        title = Label(self.frame_calc, text='Profit Calculator\n', font='bold')
        title.grid(row=0, column=0, sticky=NW)
        
        #spending text
        Label(self.frame_calc, text='Your total spending from seed: $').grid(row=1, column=0, sticky=W)
        #revenue text
        Label(self.frame_calc, text='Your total revenue:                   $\n').grid(row=2, column=0, sticky = W)
        #profit text
        Label(self.frame_calc, text='Your total profit:                       $').grid(row=3, column=0, sticky = W)
        
        
        Button(self.frame_calc, text='Calculate!', command=self.calculate).grid(row=4, column=1)
        
        #Labels and variable for spending,revenue, and profit
        self._spending = DoubleVar()
        self._spending.set(0)
        Label(self.frame_calc, textvariable=self._spending).grid(row=1, column=1, sticky=W)
        
        self._revenue = IntVar()
        self._revenue.set(0)
        Label(self.frame_calc, textvariable=self._revenue).grid(row=2, column=1, sticky=NW)

        self._profit = DoubleVar()
        self._profit.set(0)
        Label(self.frame_calc, textvariable=self._spending).grid(row=3, column=1, sticky=W)
        
    #calculate spending, revenue and spending and create labels for it    
    def calculate(self):
        self._spending = 0
        self._revenue = 0
        self._profit = 0
        print(self._planted_list)
        
        #to find total spending and total revenue, using for-loop
        for planted in self._planted_list:
            for veg in all_vegs:
                if planted == veg:
                    veg_index = all_vegs.index(veg)
                    
                    self._spending += float(all_vegs_price[veg_index])
                    self._revenue += int(all_vegs_revenue[veg_index])
        
        self._profit = self._revenue - self._spending - 6000
                  
        Label(self.frame_calc, text=self._spending).grid(row=1, column=1, sticky=W)  
        Label(self.frame_calc, text=self._revenue).grid(row=2, column=1, sticky=NW)  
        Label(self.frame_calc, text=self._profit).grid(row=3, column=1, sticky=NW)  
        Label(self.frame_calc, text='Profit takes into account $6000 \ncost of labor and maintenance').grid(row=5, column=0, columnspan=10)
        

        
if __name__ == '__main__':
    root = Tk()
    app = Calculator(root)
    root.title('Calculator')
    root.mainloop()
    
   
