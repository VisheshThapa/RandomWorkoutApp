import tkinter as tk
from tkinter import font
from tkinter import IntVar
import csv
import random
from tkinter import ttk

root = tk.Tk()
root.title("Workout Generator")

# create canvas
canvas = tk.Canvas(root, height = 700, width = 600)
canvas.pack()

main_result_array = []

#background
topframe_color = '#ADA3CC'
background_image = tk.PhotoImage(file = 'dog.png')
background_label = tk.Label(root, image = background_image)
background_label.place(x=0,y=0, relwidth = 1, relheight =1)

# create a frame
frame = tk.Frame(root, bg= topframe_color, bd = 5)
frame.place(relx = 0.5, rely = 0.009, relwidth = 0.74, relheight = 0.35, anchor = 'n')
top_display = frame

# Label for body part workout
label = tk.Label(top_display, text = "What body part would you like to workout? ", bg = topframe_color, font = ('arial', 10) )
label.place(relx = 0.525, rely = 0 , relwidth = 0.7, relheight = 0.125, anchor = 'n')

# What body part workout
rely_bodypart = 0.17
relheight_bodypart = 0.05

bodypart_var_chest= IntVar()
bodypart_var_arms= IntVar()
bodypart_var_back= IntVar()
bodypart_var_legs= IntVar()
bodypart_var_abs= IntVar()

def bodypart_fuc(x):
    bodypart_array[x] = 1
    return

bodypartpicker_chest = tk.Checkbutton(top_display, text = "Chest", bg = topframe_color, activebackground = topframe_color, variable = bodypart_var_chest)
bodypartpicker_chest.place(relx = 0.05, rely = rely_bodypart , relwidth = 0.15, relheight = relheight_bodypart)

bodypartpicker_arms = tk.Checkbutton(top_display, text = "Arms", bg = topframe_color, activebackground = topframe_color, variable = bodypart_var_arms)
bodypartpicker_arms.place(relx = 0.25, rely = rely_bodypart , relwidth = 0.15, relheight = relheight_bodypart)

bodypartpicker_back = tk.Checkbutton(top_display, text = "Back", bg = topframe_color, activebackground = topframe_color, variable = bodypart_var_back)
bodypartpicker_back.place(relx = 0.45, rely = rely_bodypart , relwidth = 0.15, relheight = relheight_bodypart)

bodypartpicker_legs = tk.Checkbutton(top_display, text = "Legs", bg = topframe_color, activebackground = topframe_color, variable = bodypart_var_legs)
bodypartpicker_legs.place(relx = 0.65, rely = rely_bodypart , relwidth = 0.15, relheight = relheight_bodypart)

bodypartpicker_abs = tk.Checkbutton(top_display, text = "Abs", bg = topframe_color, activebackground = topframe_color, variable = bodypart_var_abs)
bodypartpicker_abs.place(relx = 0.85, rely = rely_bodypart , relwidth = 0.15, relheight = relheight_bodypart)

# Label for sets


label_set = tk.Label(top_display, text = "How many sets per workout? ", bg = topframe_color, font = ('arial', 10))
label_set.place(relx = 0.3, rely = 0.3 , relwidth = 0.45, relheight = 0.125)

# Radio Button for sets
sets = IntVar()

rely_sets = 0.48

set_button1 = tk.Radiobutton(top_display, text = "1", bg = topframe_color, activebackground = topframe_color, variable = sets, value = 1)
set_button1.place(relx = 0, rely = rely_sets, relwidth = 0.25, relheight = relheight_bodypart)

set_button2 = tk.Radiobutton(top_display, text = "2", bg = topframe_color, activebackground = topframe_color, variable = sets, value = 2)
set_button2.place(relx = 0.2, rely = rely_sets, relwidth = 0.25, relheight = relheight_bodypart)

set_button3 = tk.Radiobutton(top_display, text = "3", bg = topframe_color, activebackground = topframe_color, variable = sets, value = 3)
set_button3.place(relx = 0.4, rely = rely_sets, relwidth = 0.25, relheight = relheight_bodypart)

set_button4 = tk.Radiobutton(top_display, text = "4", bg = topframe_color, activebackground = topframe_color, variable = sets, value = 4)
set_button4.place(relx = 0.6, rely = rely_sets, relwidth = 0.25, relheight = relheight_bodypart)

set_button5 = tk.Radiobutton(top_display, text = "5", bg = topframe_color, activebackground = topframe_color, variable = sets, value = 5)
set_button5.place(relx = 0.8, rely = rely_sets, relwidth = 0.25, relheight = relheight_bodypart)

# Label for amount of exercises


label_exer = tk.Label(top_display, text = "How many exercies per group? ", bg = topframe_color, font = ('arial', 10))
label_exer.place(relx = 0.3, rely = 0.6 , relwidth = 0.45, relheight = 0.125)

# Radio Button for amount of exercises
amtexe = IntVar()

rely_amtexe = 0.8

set_button1 = tk.Radiobutton(top_display, text = "1", bg = topframe_color, activebackground = topframe_color, variable = amtexe, value = 1)
set_button1.place(relx = 0, rely = rely_amtexe, relwidth = 0.25, relheight = relheight_bodypart)

set_button2 = tk.Radiobutton(top_display, text = "2", bg = topframe_color, activebackground = topframe_color, variable = amtexe, value = 2)
set_button2.place(relx = 0.2, rely = rely_amtexe, relwidth = 0.25, relheight = relheight_bodypart)

set_button3 = tk.Radiobutton(top_display, text = "3", bg = topframe_color, activebackground = topframe_color, variable = amtexe, value = 3)
set_button3.place(relx = 0.4, rely = rely_amtexe, relwidth = 0.25, relheight = relheight_bodypart)

set_button4 = tk.Radiobutton(top_display, text = "4", bg = topframe_color, activebackground = topframe_color, variable = amtexe, value = 4)
set_button4.place(relx = 0.6, rely = rely_amtexe, relwidth = 0.25, relheight = relheight_bodypart)

set_button5 = tk.Radiobutton(top_display, text = "5", bg = topframe_color, activebackground = topframe_color, variable = amtexe, value = 5)
set_button5.place(relx = 0.8, rely = rely_amtexe, relwidth = 0.25, relheight = relheight_bodypart)

# Generate Workout Button

generate_workoutbutton = tk.Button(top_display, text = "Generate Workout", command =lambda: generate_workout0() )
generate_workoutbutton.place(relx = 0.37, rely = 0.9 , relwidth = 0.3, relheight = 0.10)

#try

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, bg = color2)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


#create the display board

color2  = '#F2D1C9'

displayboard = ScrollableFrame(root)

display = tk.Label(displayboard.scrollable_frame, font = ('arial', 12), anchor = 'nw', justify = 'left', bd = 2, bg = color2)
display.pack()

displayboard.place(relx = 0.5, rely = 0.375, relwidth = 0.75, relheight = 0.6, anchor = 'n')





# Get the workout into the file


def generate_workout0():
    main_result_array = []
    main_result_array.append(str(sets.get()) + " Sets of Each Workout: ")
    if(bodypart_var_chest.get()):
        main_result_array.append("\nChest: ")
        main_result_array = main_result_array + generate_workout('Chest', amtexe.get())
    if (bodypart_var_arms.get()):
        main_result_array.append("\nArms: ")
        main_result_array = main_result_array + generate_workout('Arms', amtexe.get())
    if (bodypart_var_back.get()):
        main_result_array.append("\nBack: ")
        main_result_array = main_result_array + generate_workout('Back', amtexe.get())
    if (bodypart_var_legs.get()):
        main_result_array.append("\nLeg: ")
        main_result_array = main_result_array + generate_workout('Legs', amtexe.get())
    if (bodypart_var_abs.get()):
        main_result_array.append("\nAbs: ")
        main_result_array = main_result_array + generate_workout('Abs', amtexe.get())
    display['text'] = format_response(main_result_array)
    return

def generate_workout(bodygroup_name, numexe):
    with open('exercises.csv', 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        exercisearray = []
        result_array= []
        for row in csv_reader:

            bodygroup = row['bodygroup']
            workout = row['workout']
            if (bodygroup_name == bodygroup):
                exercisearray.append(workout)
        if(numexe > len(exercisearray)):
            return print("Invaid Num of Exercises")
        for exercise_range in range (numexe) :
            exe_add =exercisearray[random.randint(0, len(exercisearray) - 1)]
            result_array.append(exe_add)
            exercisearray.remove(exe_add)

    return result_array

def format_response(arr):
    response = ""
    for i in range(len(arr)):
        response += arr[i] + "\n"
    return response

root.mainloop()