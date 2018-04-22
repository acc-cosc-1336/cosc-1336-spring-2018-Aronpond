from tkinter import Tk, Label
class Converter:
    def get_miles_from_km(km):
        answer = float(round(km * .621371, 2))
        return answer
