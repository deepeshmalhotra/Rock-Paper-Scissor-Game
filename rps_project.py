from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from random import randint

win=tk.Tk()
win.title("Rock, Paper, Scissors")
win.config(bg='white')

score=0

#Images of rock ,paper and scissor
rock_img= ImageTk.PhotoImage(Image.open("rock.png"))
paper_img= ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img= ImageTk.PhotoImage(Image.open("scissor.png"))

#Randomly picks an image
image_list=[rock_img,paper_img,scissor_img]
pick_number=randint(0,2)

image_label=ttk.Label(win,image=image_list[pick_number])
image_label.pack(pady=20)

#Select your move label
choice_label=ttk.Label(win,text="Select your move : ")
choice_label.config(font=("Courier",18))
choice_label.pack()

#Combobox for choosing values
var=tk.StringVar()
box=ttk.Combobox(win, width=45, textvariable=var,state='readonly')
box['values']=['Rock','Paper','Scissor']
box.current(0)
box.pack()

#Spin Button
def spin():
    global score
    pick_number=randint(0,2)
    image_label.config(image=image_list[pick_number])

    if var.get()=='Rock':
        var_value=0
    elif var.get()=='Paper':
        var_value=1
    elif var.get()=='Scissor':
        var_value=2

    if var_value==0:
        if pick_number==0:
            win_lose_label.config(text=f"Tie..!!\nScore={score}\nSpin Again..!!")
        elif pick_number==1:
            score=score-1
            win_lose_label.config(text=f"You Lose..!!\nScore={score}\nSpin Again..!!")
        elif pick_number==2:
            score=score+1
            win_lose_label.config(text=f"You Win..!!\nScore={score}\nSpin Again..!!")

    if var_value==1:
        if pick_number==0:
            score=score+1
            win_lose_label.config(text=f"You Win..!!\nScore={score}\nSpin Again..!!")
        elif pick_number==1:
            win_lose_label.config(text=f"Tie..!!\nScore={score}\nSpin Again..!!")
        elif pick_number==2:
            score=score-1
            win_lose_label.config(text=f"You Lose..!!\nScore={score}\nSpin Again..!!")

    if var_value==2:
        if pick_number==0:
            win_lose_label.config(text=f"Tie..!!\nScore={score}\nSpin Again..!!")
        elif pick_number==1:
            score=score-1
            win_lose_label.config(text=f"You Lose..!!\nScore={score}\nSpin Again..!!")
        elif pick_number==2:
            score=score+1
            win_lose_label.config(text=f"You Win..!!\nScore={score}\nSpin Again..!!")


spin_btn=ttk.Button(win,text='Spin!!',command=spin)
spin_btn.pack(pady=50)

#spin button label
win_lose_label=ttk.Label(win,text='',font=("Helvetica",18))
win_lose_label.pack(pady=50)

win.mainloop()

#####################------------------###############################