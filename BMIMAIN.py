import tkinter
from tkinter import *

window = tkinter.Tk()

heightvariable = tkinter.IntVar()
weightvariable = tkinter.IntVar()
height = heightvariable
weight = weightvariable


def calculatebmi():
    global BodyMassIndex
    BodyMassIndex = ((weight.get() / ((height.get() / 10) ** 2)))
    if BodyMassIndex < 0.18:
        label5.config(text="Invalid Input")
    if BodyMassIndex < 0:
        label5.config(text="Invalid Input")
    if BodyMassIndex == 0:
        label5.config(text="Invalid Input")
    if BodyMassIndex > 0:
        if BodyMassIndex < 0.18:
            label5.config(text="Severely Underweight")
        elif BodyMassIndex < 0.25:
            label5.config(text="Underweight")
        elif BodyMassIndex < 0.30:
            label5.config(text="Normal")
        elif BodyMassIndex < 0.35:
            label5.config(text="Overweight")
        elif BodyMassIndex < 0.40:
            label5.config(text="Obese")
        elif BodyMassIndex < 0.45:
            label5.config(text="Severely Obese")
        elif BodyMassIndex < 0.50:
            label5.config(text="Morbidly Obese")
        elif BodyMassIndex < 0.60:
            label5.config(text="Super Obese")
        elif BodyMassIndex < 0.70:
            label5.config(text="Hyper Obese")
label2 = tkinter.Label(
    window,
    text="Enter your height in centimeters:",
    font=("Arial Bold", 15)
)
EntryHeight = Entry(
    window,
    textvariable=height
)

label3 = tkinter.Label(
    window,
    text="Enter your weight in kilograms:",
    font=("Arial Bold", 15)
)

EntryWeight = Entry(
    window,
    textvariable=weight
)

Button1 = Button(
    text="Calculate BMI",
    justify="center",
    activebackground="#FF0000",
    command=calculatebmi,
)
label4 = tkinter.Label(
    window,
    text="Your Body Mass Index Is:",
)
label5 = tkinter.Label(
    window,
    text="Waiting For Input"
)
label6 = tkinter.Label(
    window,
    text=""
)
window.title("BMI Calculator")
window.geometry("400x400")

label2.pack()
EntryHeight.pack()
label3.pack()
EntryWeight.pack()
Button1.pack(padx=50, pady=50)
label4.pack()
label5.pack()
label6.pack()
window.mainloop()