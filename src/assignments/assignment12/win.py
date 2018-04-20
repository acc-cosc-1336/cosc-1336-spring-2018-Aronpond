from tkinter import Tk, Label
from converter import Converter

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)
        self.wm_title('Converts KM to Miles')
        self.geometry('640x480')
        self.label = Label(self, text='KM : 100' )
        self.label.pack()
        kilo = str(Converter.get_miles_from_km(100))
        self.label2 = Label(self, text='Miles : ' + kilo)

        



        self.label2.pack()
    
        self.mainloop()
