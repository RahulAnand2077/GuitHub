from tkinter import *
from Functionalities import *

root = Tk()
root.configure(bg='#1a1d1e')
root.title('GuitHub')
root.geometry('700x700')

back_ground = Canvas(root, width=700, height=700)
back_ground.place(x=0, y=0)
try:
    filename = PhotoImage(file='E:/Coding Folder/GuitHub/B_G12.png')
    image = back_ground.create_image(0, 200, anchor=W, image=filename)
except TclError as e:
    print(f"Error loading image: {e}")

back_ground_text = Label(root, text='GuitHub', font=('Helvetica', 36), fg='#ffffff', bg=root.cget('bg'), highlightthickness=0)
back_ground_text.place(x=250, y=100)

b1 = Button(root,text='Search',command=Search,bg='#444442',fg='#ffffff',activebackground='#75818d',border=5,height=1,width=17).place(x=275,y=300)
b2 = Button(root,text='Introduction',command=Introduction,bg='#444442',fg='#ffffff',border=5,height=1,width=17).place(x=275,y=335)
b3 = Button(root,text='Interval Theory',command=IT,bg='#444442',fg='#ffffff',border=5,height=1,width=17).place(x=275,y=370)
b4 = Button(root,text='Chord Classifications',command=CC,bg='#444442',fg='#ffffff',border=5,height=1,width=17).place(x=275,y=405)
b5 = Button(root,text='7th Classification',command=CC_7,bg='#444442',fg='#ffffff',border=5,height=1,width=17).place(x=275,y=440)
b6 = Button(root,text='9th Classification',command=CC_9,bg='#444442',fg='#ffffff',border=5,height=1,width=17).place(x=275,y=475)
b7 = Button(root,text='11th Classification',command=CC_11,bg='#444442',fg='#ffffff',border=5,height=1,width=17).place(x=275,y=510)
b8 = Button(root,text='Chord Library',command=CL,bg='#444442',fg='#ffffff',border=5,height=1,width=17).place(x=275,y=545)
b9 = Button(root,text='Scales Library',command=SL,bg='#444442',fg='#ffffff',border=5,height=1,width=17).place(x=275,y=580)
b10= Button(root,text='Exit',command=exit,bg='#444442',fg='#ffffff',border=5,height=1,width=17).place(x=275,y=615)

root.mainloop() 
