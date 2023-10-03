import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, NE, NW
from datetime import datetime
import os


os.chdir(os.path.dirname(__file__))
file_path = os.getcwd() + "\saved_list"


file = open(file_path, "r")
current_text = []
current_text.append(file.read())
file.close()


root = tk.Tk()
root.title('Homework Database')
root.geometry('400x750')
root.config(bg = 'Gray81')


time_val = datetime.now()
time_str = time_val.strftime("%D")
time_var = tk.StringVar()
time_var.set(time_str)


def clear():
    editor1.configure(state='normal')
    editor1.delete('1.0', 'end-1c')
def edit():
    editor1.configure(state="normal")
def save():
    global current_text
    current_text = [editor1.get('1.0', 'end-1c')]
    editor1.configure(state='disabled')
    file = open(file_path, 'w')
    file.write(current_text[0])
    file.close()
def period_update():
    if period1_check.get() == 0:
        F_period_2.set(first_half[1])
        F_period_3.set(first_half[2])
        period_lunch.set(lunch[1])
        S_period_1.set(second_half[0])
        S_period_2.set(second_half[1])
        S_period_3.set(second_half[2])
    elif period1_check.get() == 1:
        F_period_2.set(first_half[2])
        F_period_3.set(first_half[3])
        period_lunch.set(lunch[0])
        S_period_1.set(second_half[1])
        S_period_2.set(second_half[2])
        S_period_3.set(second_half[3])
    elif period1_check.get() == 2:
        F_period_2.set(first_half[3])
        F_period_3.set(first_half[0])
        period_lunch.set(lunch[0])
        S_period_1.set(second_half[2])
        S_period_2.set(second_half[3])
        S_period_3.set(second_half[0])
    elif period1_check.get() == 3:
        F_period_2.set(first_half[0])
        F_period_3.set(first_half[1])
        period_lunch.set(lunch[0])
        S_period_1.set(second_half[3])
        S_period_2.set(second_half[0])
        S_period_3.set(second_half[1])


font_config = 'Arial'
size_config = 10

time = tk.Label(textvariable = time_var)
time.place(x=199, y=30, anchor= CENTER)
time.configure(font=(font_config, size_config))


new_hw = tk.Button(text = 'New Entry', command = clear)
new_hw.place(x=128, y=67, anchor= NE)
new_hw.configure(font=(font_config, size_config))

edit_hw = tk.Button(text = 'Edit Entry', command = edit)
edit_hw.place(x=200, y=82, anchor= CENTER)
edit_hw.configure(font=(font_config, size_config))

save_hw = tk.Button(text = 'Save Entry', command = save)
save_hw.place(x=272, y=67, anchor= NW)
save_hw.configure(font=(font_config, size_config))


editor1 = tk.Text()
editor1.place(x=27, y=130, width=350, height=300)
editor1.configure(font=(font_config, 10))

editor1.insert(tk.END, current_text[0][0:len(current_text[0])])
editor1.configure(state='disabled')



first_half = ['Government', 'English', 'Physics', 'French']
lunch = ['Lunch', 'Lunch / Lab']
second_half = ['Gym', 'Photo', 'Precalculus', 'AP Computer Science']
    


F_period_2 = tk.StringVar()
F_period_2.set(first_half[1])
F_period_3 = tk.StringVar()
F_period_3.set(first_half[2])

period_lunch = tk.StringVar()
period_lunch.set(lunch[1])

S_period_1 = tk.StringVar()
S_period_1.set(second_half[0])
S_period_2 = tk.StringVar()
S_period_2.set(second_half[1])
S_period_3 = tk.StringVar()
S_period_3.set(second_half[2])



period1_check = tk.IntVar()
period_option1 = tk.Radiobutton(root, text = "Gov.", variable = period1_check, value = 0, command = period_update)
period_option2 = tk.Radiobutton(root, text = "Eng.", variable = period1_check, value = 1, command = period_update)
period_option3 = tk.Radiobutton(root, text = "Phys.", variable = period1_check, value = 2, command = period_update)
period_option4 = tk.Radiobutton(root, text = "Fr.", variable = period1_check, value = 3, command = period_update)
period_option1.place(x= 120, y = 453)
period_option2.place(x= 190, y = 453)
period_option3.place(x= 260, y = 453)
period_option4.place(x= 330, y = 453)



period_2_label = tk.Label(textvariable= F_period_2)
period_2_label.place(x= 210, y= 495)
period_2_label.configure(font=(font_config, size_config))

period_3_label = tk.Label(textvariable= F_period_3)
period_3_label.place(x= 210, y= 535)
period_3_label.configure(font=(font_config, size_config))

period_4_label = tk.Label(textvariable= period_lunch)
period_4_label.place(x= 210, y= 575)
period_4_label.configure(font=(font_config, size_config))

period_5_label = tk.Label(textvariable= S_period_1)
period_5_label.place(x= 210, y= 615)
period_5_label.configure(font=(font_config, size_config))

period_6_label = tk.Label(textvariable= S_period_2)
period_6_label.place(x= 210, y= 655)
period_6_label.configure(font=(font_config, size_config))

period_7_label = tk.Label(textvariable= S_period_3)
period_7_label.place(x= 210, y= 695)
period_7_label.configure(font=(font_config, size_config))


period_1 = tk.Label(text = 'Period 1:')
period_1.place(x= 40, y= 455)
period_1.configure(font=(font_config, size_config))

period_2 = tk.Label(text = 'Period 2:')
period_2.place(x= 40, y= 495)
period_2.configure(font=(font_config, size_config))

period_3 = tk.Label(text = 'Period 3:')
period_3.place(x= 40, y= 535)
period_3.configure(font=(font_config, size_config))

period_4 = tk.Label(text = 'Period 4:')
period_4.place(x= 40, y= 575)
period_4.configure(font=(font_config, size_config))

period_5 = tk.Label(text = 'Period 5:')
period_5.place(x= 40, y= 615)
period_5.configure(font=(font_config, size_config))

period_6 = tk.Label(text = 'Period 6:')
period_6.place(x= 40, y= 655)
period_6.configure(font=(font_config, size_config))

period_7 = tk.Label(text = 'Period 7:')
period_7.place(x= 40, y= 695)
period_7.configure(font=(font_config, size_config))


tk.mainloop()