from tkinter import *
pro=Tk()
pro.geometry('400x400')
pro.title('ibrahim')
def us():
    name=Label(pro,text='your name is : '+inp1.get())
    name.place(x=130,y=240)
    age=Label(pro,text='your age is : '+inp2.get())
    age.place(x=130,y=260)
    
tite=Label(pro,text='peogram',bg='blue',fg='white',font=('tajawal',17,'bold'))
tite.pack(fill=X)
l1=Label(pro,text='Enter your Name :',font=('tajawal',14,))
l1.pack()
inp1=Entry(pro,width=35,font=('tajawal',13),justify='center')
inp1.pack()
l2=Label(pro,text='Enter your Age :',font=('tajawal',14,))
l2.pack()
inp2=Entry(pro,width=35,font=('tajawal',13),justify='center')
inp2.pack()
btn=Button(pro,text='Add user',font=('tajawal',14,),width=20,command=us)
btn.place(x=100,y=170)
pro.mainloop()

