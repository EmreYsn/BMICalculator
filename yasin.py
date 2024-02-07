from tkinter import *

window = Tk()
window.config(padx=75 , pady=75)
window.title("BMI Calculator")

def bmi_calculation():
    weight = my_entry.get()
    height = my_entry_2.get()

    if weight == "" and height == "":
        answer_label.config(text="Enter both!!!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = answer_calculation(bmi)
            answer_label.config(text=result_string)
        except:
            answer_label.config(text="Enter a valid number")

my_label = Label()
my_label.config(width=20,text="Enter your weight (kg)")
my_label.pack()

my_entry = Entry()
my_entry.config(width=20)
my_entry.pack()

my_label_2 = Label()
my_label_2.config(width=20,text="Enter your height (cm)")
my_label_2.pack()

my_entry_2 = Entry()
my_entry_2.config(width=20)
my_entry_2.pack()

my_button = Button(width=20,text="Calculate",command=bmi_calculation)
my_button.pack()

answer_label = Label()
answer_label.pack()

def answer_calculation(bmi):
    result_string = f"Your BMI is {round(bmi,2)}. You are  "
    if bmi <16:
        result_string += "severe thin"
    elif 16 < bmi <= 17:
        result_string += "moderate thin"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin"
    elif 18.5 < bmi <= 25:
        result_string += "normal"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class I"
    elif 35 < bmi <= 40:
        result_string += "obese class II"
    else:
        result_string += "obese class III"
    return result_string

window.mainloop()