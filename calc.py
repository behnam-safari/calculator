from tkinter import *
from tkinter import ttk
win = Tk()
def click(number):
    ent.insert(END,number)
def clear():
    ent.delete(0,END)


#--------------------***back_end of add***-------------------------------       
def addition():
    global first_num
    global sign
    sign = 'additional' 
    first_num = float(ent.get())
    ent.delete(0,END)


#---------------------***back_end of subtract***-------------------------
def submission():
    global first_num
    global sign
    sign = 'submission'
    first_num = float(ent.get())
    ent.delete(0,END)

#---------------------***back_end of divide***----------------------------
def divide():
    global first_num
    global sign
    sign = 'divid'
    first_num = float(ent.get())
    ent.delete(0,END) 

#---------------------***back_end of multiple***---------------------------
def multiple():
    global first_num
    global sign
    sign = 'multi'
    first_num = float(ent.get())
    ent.delete(0,END)


#---------------------***back_end of equal***------------------------------
def equal():
    global second_num
    second_num = float(ent.get())
    ent.delete(0,END)
    if sign == 'additional':
        ent.insert(0,first_num + second_num)
    elif sign == 'submission':
        ent.insert(0,first_num - second_num) 
    elif sign == 'divid': 
        ent.insert(0,first_num / second_num)
    elif sign == 'multi':
        ent.insert(0,first_num * second_num)        


#--------------------------***(THIS IS FRONT OF MY PROJECT)***---------------------------------------------------------------------
win.geometry('328x450')
fram_top = Frame(win,bg ='#180b26').place(x=0,y=0,width=335,height=100)
ent = Entry(win,bg = '#010128', fg = '#fffdc2',highlightbackground = '#c8c20c',font= 'Tahoma 18 bold')
ent.place(x = 10,y = 10,width =310,height =80)
fram_mid = Frame(win,bg = '#000116',highlightbackground='#c8c20c').place(x=0,y=102,width = 335,height =370)


#--------------------------***(photo of number input from pc)***-----------------------------------------------------------------------------
img0 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/00.png') 
img1 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/1.png') 
img2 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/2.png') 
img3 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/3.png')
img4 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/4.png')
img5 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/5.png')
img6 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/6.png')
img7 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/7.png')
img8 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/8.png')
img9 =PhotoImage(file = r'/home/reza/Desktop/calc_pic/9.png')


#----------------------------***(photo of 4 action)***---------------------------------------------------------------------------------
img_plus =PhotoImage(file = r'/home/reza/Desktop/calc_pic/plus.png')
img_mines =PhotoImage(file = r'/home/reza/Desktop/calc_pic/mines.png')
img_multi =PhotoImage(file = r'/home/reza/Desktop/calc_pic/multiple.png')
img_div = PhotoImage(file = r'/home/reza/Desktop/calc_pic/divison.png')
reset_img = PhotoImage(file = r'/home/reza/Desktop/calc_pic/reset.png')
img_dot = PhotoImage(file = r'/home/reza/Desktop/calc_pic/dot1.png')
img_eq= PhotoImage(file = r'/home/reza/Desktop/calc_pic/eq1.png')


#------------------------------***(number button)***--------------------------------------------------------------------------------- 
btn1 =Button(fram_mid,image =img7,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command =lambda : click(7))
btn1.place(x=5,y=170)
btn2 = Button(fram_mid,image =img8,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command =lambda : click(8))
btn2.place(x=85,y=170)
btn3 = Button(fram_mid,image =img9,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command =lambda: click(9))
btn3.place(x=165,y=170)
btn4 = Button(fram_mid,image =img4,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command =lambda: click(4))
btn4.place(x=5,y=240)
btn5 = Button(fram_mid,image =img5,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = lambda:click(5))
btn5.place(x=85,y=240)
btn6 = Button(fram_mid,image =img6,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = lambda:click(6))
btn6.place(x=165,y=240)
btn7 = Button(fram_mid,image =img1,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = lambda:click(1))
btn7.place(x=5,y=310)
btn8 = Button(fram_mid,image =img2,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = lambda:click(2))
btn8.place(x=85,y=310)
btn9 = Button(fram_mid,image =img3,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = lambda:click(3))
btn9.place(x=165,y=310)
btn0 = Button(fram_mid,image =img0,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = lambda:click(0))
btn0.place(x=5,y=380)


#---------------------------***(Button 4 action in calculator)***-----------------------------------------------------------------------
btn_plus =Button(fram_mid,image =img_plus,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = addition)
btn_plus.place(x=240,y=170)
btn_mines = Button(fram_mid,image =img_mines,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command=submission)
btn_mines.place(x=240,y=240)
btn_multi = Button(fram_mid,image =img_multi,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = multiple)
btn_multi.place(x=240,y=310)
btn_div = Button(fram_mid,image =img_div,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command=divide)
btn_div.place(x=240,y=380)
btn_reset = Button(fram_mid,image =reset_img,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = clear)
btn_reset.place(x=5,y=103)
btn_dot = Button(fram_mid,image =img_dot,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116')
btn_dot.place(x=85,y=381)
btn_eq = Button(fram_mid,image =img_eq,bg='#000116',borderwidth = 0,highlightbackground='#000116',activebackground='#000116',command = equal)
btn_eq.place(x=165,y=381)
win.mainloop()
