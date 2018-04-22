from tkinter import Tk, Label, Button
from converter import Converter

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)
        self.wm_title('Converts KM to Miles')
        self.geometry('147x75')
        self.button1 = Button(text='Display Conversion',
                              command=self.display_labels)
        self.button1.grid(row=0, column=0)
        self.button2 = Button(text='Quit',
                              command=self.quit)
        self.button2.grid(row=0, column=1)
        self.mainloop()
    def display_labels(self):
        self.label = Label(self, text='KM : 100' )
        self.label.grid(row=1, column=0)
        miles = str(Converter.get_miles_from_km(100))
        self.label2 = Label(self, text='Miles : ' + miles)
        self.label2.grid(row=2, column=0)
        self.mainloop()
    def quit(self):
        self.destroy()
