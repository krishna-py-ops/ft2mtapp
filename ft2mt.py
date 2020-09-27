from tkinter import Tk,Button,Label,DoubleVar,Entry

#basic window
window = Tk()
window.title("Feet to Meter conversion App")
window.configure(background="black")
window.geometry("320x220")
window.resizable(width=False,height=False)

#creating function and testing

def convert():
    value = float(ft_entry.get())#converting the feet input to float
    meter = value*0.3048
    mt_value.set("%.4f" % meter)

def clear():
    ft_value.set("")
    mt_value.set("")


ft_lb1 = Label(window,text="Feet",bg="white",fg="black",width=15)
ft_lb1.grid(column=0,row=0,padx=15,pady=15)#postioning in 0,0 and padx and pady are used for spaces vertically and horizontally

ft_value = DoubleVar()
ft_entry = Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')

mt_lb1 = Label(window,text="Meter",bg="white",fg="black",width=15)
mt_lb1.grid(column=0,row=1)

mt_value = DoubleVar()
mt_entry = Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1,pady = 30)
mt_entry.delete(0,'end')

conbutton = Button(window,text='Convert',bg='white',width=14,command=convert)
conbutton.grid(column=0,row=3,padx=15)

clrbutton = Button(window,text='Clear',bg='white',width=14,command=clear)
clrbutton.grid(column=1,row=3,padx=15)


window.mainloop() #main loop runs the application

