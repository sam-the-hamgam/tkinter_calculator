#Important : since i made this on a phone, the sizes are made to fit on a phone so it may look weird on pc

#a tkinter calculator i made :3

import tkinter as tk
import traceback
from tkinter import messagebox as mb
import math
#2 lists, one for the user and the other for eval
text=[]
math_list=[]
def flawless_factorial(n):
    if type(n)==float:
        n=round(n)
        return math.factorial(n)
    else:
        return math.factorial(n)
def back_space():
    if text:
        text.pop()
        math_list.pop()
        update_text()
    else:
        mb.showwarning("nope","there is nothing to delete!")
def button_pressed(symbol):
    #implicit multiplication!
    #this causes issues with backspace, i tried to fix this easily by adding a space bar to the text list
    if math_list and math_list[-1][-1] in ["0","1","2","3","4","5","6","7","8","9",")"] and symbol in ["math.pi","(","math.sqrt(","math.factorial("]:
        math_list.append("*")
        text.append(" ")
    match symbol:
        case "math.sqrt(":
            text.append("√(")
        case "math.pi":
            text.append("π")
        case "math.factorial(":
            text.append("!(")
            symbol="flawless_factorial("
        case "**(":
            text.append("^(")
        case _:
            text.append(symbol)
    math_list.append(symbol)
    update_text()

def update_text():
    op_string="".join(text)
    label.config(text=op_string)
def clear():
    text.clear()
    math_list.clear()
    update_text()
def do_math():
    global math_list, text
    try:
        math_string="".join(math_list)
        #the inputs for the eval are restricted so eval use here is ok
        result=str(eval(math_string))
        #making sure the text stays inside the label and not outside the screen
        if float(result)>(10**10):
            if len(result)>15:
                result = "{:.6e}".format(float(result))
                #no idea what this means, but i do know it makes the result shorter
        label.config(text=result)
        text=[result]
        math_list=[result]
    #errors are pop-ups to direct the users attention, and teach the user
    
    except SyntaxError:
        #most problable cause is forgetting ")" so i fixed it alongside a warning
        missing_1=math_string.count("(")
        missing_2=math_string.count(")")
        missing_total=missing_1-missing_2
        if missing_total !=0:
            if missing_total>0:
                for _ in range (missing_total):
                    math_list.append(")")
            else:
                mb.showwarning("uh oh","please do not try to close something \nthat isnt open")
                return
            mb.showinfo("uh oh","hey there looks like you forgot \nto end the pharantheses! \n we fixed it but dont let it happen again")
            do_math()
        #multiple dots near each other
        if ".." in math_string:
            i=0
            for letter in math_string:
                if i==1:
                    if letter==".":
                        math_list.remove(letter)
                        mb.showinfo("oopsie woopsie","no multiple dots!")
                        do_math()
                        return
                elif letter==".":
                    i+=1
                else:
                    i=0
        else:
            mb.showwarning("ugh!","okay this time its getting ridicilus \nyou litteraly did the math wrong")
            clear()
    except ZeroDivisionError:
        #most problable cause is obvious
        mb.showwarning("uh oh!","dividing by 0 is not possible")
        clear()
    except ValueError:
        #root of a negative number
        mb.showwarning("uh oh","please do not root the negative numbers")
        clear()
    except OverflowError:
        mb.showwarning("uh oh","please lay down on the math")
    except TypeError:
        mb.showerror("oh come on"," you wanted it to crash \nsince crashing this way isnt ez")
try:
    calc=tk.Tk()
    calc.config(bg="#112233")
    label=tk.Label(calc,text="your operations appear here",height=13,width=35,font=("Arial",10), bg="#000000",fg="#FFFFFF")
    label.pack(pady=30, side=tk.TOP)
    buttons=tk.Frame(calc,width=100,height=100,bg="#332211")
    buttons.pack(side=tk.BOTTOM,expand=True,fill=tk.BOTH)
    #this is an inefficitent to make the buttons
    b1=tk.Button(buttons, text="1", command= lambda: button_pressed("1"))
    b2=tk.Button(buttons, text="2", command= lambda: button_pressed("2"))
    b3=tk.Button(buttons, text="3", command= lambda: button_pressed("3"))
    b4=tk.Button(buttons, text="4", command= lambda: button_pressed("4"))
    b5=tk.Button(buttons, text="5", command= lambda: button_pressed("5"))
    b6=tk.Button(buttons, text="6", command= lambda: button_pressed("6"))
    b7=tk.Button(buttons, text="7", command= lambda: button_pressed("7"))
    b8=tk.Button(buttons, text="8", command= lambda: button_pressed("8"))
    b9=tk.Button(buttons, text="9", command= lambda: button_pressed("9"))
    b0=tk.Button(buttons, text="0", command= lambda: button_pressed("0"))
    b_plus=tk.Button(buttons, text="+", command= lambda: button_pressed("+"))
    b_minus=tk.Button(buttons, text="-", command= lambda: button_pressed("-"))
    b_multiply=tk.Button(buttons, text="*", command= lambda: button_pressed("*"))
    b_divide=tk.Button(buttons, text="/", command= lambda: button_pressed("/"))
    b_sprt=tk.Button(buttons, text="√", command= lambda: button_pressed("math.sqrt("))
    b_exponent=tk.Button(buttons, text="^", command= lambda: button_pressed("**("))
    b_idk=tk.Button(buttons, text="(", command= lambda: button_pressed("("))
    b_idk_2=tk.Button(buttons, text=")", command= lambda: button_pressed(")"))
    b_equal=tk.Button(buttons, text="=", command=do_math, bg="#00AA00")
    b_clear=tk.Button(buttons, text="C", command=clear,bg="#AA0000")
    b_pi=tk.Button(buttons, text="π", command= lambda: button_pressed("math.pi"))
    b_decimal=tk.Button(buttons, text="•", command= lambda: button_pressed("."))
    b_back_space=tk.Button(buttons, text="​​⌫", command=back_space, bg="#AA0000")
    #if an error happens because, its because of the text of backspace btn, it works for me but change it if it doesnt work for you
    b_fact=tk.Button(buttons, text="!", command= lambda: button_pressed("math.factorial("))
    #i did now know you could do multiple collumns or rows in once
    buttons.columnconfigure(0, weight=1)
    buttons.columnconfigure(1, weight=1)
    buttons.columnconfigure(2, weight=1)
    buttons.columnconfigure(3, weight=1)
    buttons.rowconfigure(0, weight=1)
    buttons.rowconfigure(1, weight=1)
    buttons.rowconfigure(2, weight=1)
    buttons.rowconfigure(3, weight=1)
    buttons.rowconfigure(4, weight=1)
    buttons.rowconfigure(5, weight=1)
    b1.grid(row=0, column=0, sticky="nsew")
    b2.grid(row=0, column=1, sticky="nsew")
    b3.grid(row=0, column=2, sticky="nsew")
    b_plus.grid(row=0, column=3, sticky="nsew")
    b4.grid(row=1, column=0, sticky="nsew")
    b5.grid(row=1, column=1, sticky="nsew")
    b6.grid(row=1, column=2, sticky="nsew")
    b_minus.grid(row=1, column=3, sticky="nsew")
    b7.grid(row=2, column=0, sticky="nsew")
    b8.grid(row=2, column=1, sticky="nsew")
    b9.grid(row=2, column=2, sticky="nsew")
    b_multiply.grid(row=2, column=3, sticky="nsew")
    b_idk.grid(row=3, column=0, sticky="nsew")
    b0.grid(row=3, column=1, sticky="nsew")
    b_idk_2.grid(row=3, column=2, sticky="nsew")
    b_divide.grid(row=3, column=3, sticky="nsew")
    b_exponent.grid(row=4, column=0, sticky="nsew")
    b_sprt.grid(row=4, column=1, sticky="nsew")
    b_clear.grid(row=5, column=2, sticky="nsew")
    b_equal.grid(row=5, column=3, sticky="nsew")
    b_pi.grid(row=5, column=0, sticky="nsew")
    b_back_space.grid(row=5, column=1, sticky="nsew")
    b_fact.grid(row=4, column=2, sticky="nsew")
    b_decimal.grid(row=4, column=3, sticky="nsew")
    
    
    calc.mainloop()
#to catch any error happening in the code (made mostly for me, the develeper)
except Exception as e:
    error_window=tk.Tk()
    error_window.withdraw()
    error=traceback.format_exc()
    mb.showerror("uh oh",error)
