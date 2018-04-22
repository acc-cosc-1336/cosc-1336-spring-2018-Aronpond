from tkinter import Tk, Label, Button
from converter import Converter

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)
        self.wm_title('Converts KM to Miles')
        self.geometry('640x480')
        self.button1 = Button(text='Display Conversion',
                              command=self.display)
        self.button1.pack()
        self.button2 = Button(text='Quit',
                              command=self.quit)
        self.button2.pack()
        self.mainloop()
    def display(self):
        self.label = Label(self, text='KM : 100' )
        self.label.pack()
        miles = str(Converter.get_miles_from_km(100))
        self.label2 = Label(self, text='Miles : ' + miles)
        self.label2.pack()
        self.mainloop()
    def quit(self):
        self.destroy()
