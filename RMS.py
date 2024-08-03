from tkinter import *
from tkinter import Tk
import random
from datetime import datetime
from tkinter import messagebox
import sys
def main():
    win=Tk()
    app=LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self, win):
        self.win=win
        self.win.geometry('1350x950+0+0')
        self.win.title('Restaurant Management System')
        self.win.configure(bg='#FFFBEB')
        self.title_label=Label(self.win, text='Restaurant Management System',fg='#914F1E',font=('Arial', 25, 'bold'), bd=20, bg='#FFE7CC')
        self.title_label.pack(side=TOP,fill=X)

        # Login 

        self.main_frame=Frame(self.win, bg='#FFFBEB')
        self.main_frame.place(x=265, y=210, width=800, height=470)
        self.login=Label(self.main_frame, text='Login', bd=15, anchor=CENTER, bg='#F8CBA6',fg='#FFFBEB', font=('sans-serif', 25, 'bold'))
        self.login.pack(side=TOP, fill=X)

        self.entry_frame=LabelFrame(self.main_frame, text='Enter Details',relief='solid',highlightbackground='#F8CBA6',bd=2,bg='#FFFBEB',fg='#F8CBA6',font=('sans-serif',15))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)

        username=StringVar()
        password=StringVar()

        # Quotes
        self.quote=Label(self.main_frame, text="username:'tahmeed', pass:'1234'", bd=2, bg='#FFFBEB', anchor=CENTER,fg='#F8CBA6', font=('sans-serif', 12, 'bold'))
        self.quote.place(x=255,y=390,width=300,height=15)

        # Inputs

        self.entry=Label(self.entry_frame, text='Enter Username',bd=15,fg='#914F1E',bg='#FFFBEB',anchor=CENTER, font=('sans-serif',16))
        self.entry.pack(side=TOP,fill=X)
        self.entry0=Entry(self.entry_frame, font=('sans-serif', 15), relief=SUNKEN, textvariable=username)
        self.entry0.pack(side=TOP)

        self.entry=Label(self.entry_frame, text='Password',bd=15,bg='#FFFBEB',anchor=CENTER, fg='#914F1E',font=('sans-serif',16))
        self.entry.pack(side=TOP,fill=X)
        self.entry0=Entry(self.entry_frame, font=('sans-serif', 15), relief=SUNKEN, textvariable=password, show='*')
        self.entry0.pack(side=TOP)

        # Function

        def check_login():
            if username.get()=='tahmeed' and password.get()=='1234':
                self.bill.config(state='normal')
            else:
                pass # Message box
        def reset():
            username.set('')
            password.set('')

        def billing():
            self.newWindow=Toplevel(self.win)
            self.app=Window2(self.newWindow)
            

        # Buttons

        self.button_frame=LabelFrame(self.entry_frame, text='Options',font=('Arial', 12),bg='#FFFBEB',fg='#F8CBA6',bd=2,relief='solid')
        self.button_frame.place(x=240,y=190,width=315,height=130)

        self.bill=Button(self.button_frame, text='Billing', bd=5, bg='#F8CBA6',fg='#FFFBEB', font=('sans-serif', 12, 'bold'), command=billing)
        self.bill.grid(row=0,column=0,padx=20,pady=10)
        self.bill.config(state='disabled') # disable it when necessary

        self.login_info=Button(self.button_frame, text='Login', bd=5, bg='#F8CBA6',fg='#FFFBEB', font=('sans-serif', 18, 'bold'), command=check_login)
        self.login_info.grid(row=0,column=1,padx=2,pady=10)

        self.reset=Button(self.button_frame, text='Reset', bd=5, bg='#F8CBA6',fg='#FFFBEB', font=('sans-serif', 12, 'bold'), command=reset)
        self.reset.grid(row=0,column=2,padx=20,pady=10)


class Window2:
    def __init__(self, win):
        self.win=win
        self.win.geometry('1350x950+0+0')
        self.win.title('Restaurant Management System')
        self.win.configure(bg='#FFFBEB')
        self.title_label=Label(self.win, text='Restaurant Management System',fg='#914F1E',font=('Arial', 25, 'bold'), bd=20, bg='#FFE7CC')
        self.title_label.pack(side=TOP,fill=X)

        self.win.resizable(0,0)

        # Bill Variables

        bill_no=random.randint(100,99999)
        bill_no_tk=IntVar()
        bill_no_tk.set(bill_no)

        cal_var=StringVar()
        cus_num=StringVar()
        cus_con=StringVar()
        date=StringVar()
        item_pur=StringVar()
        item_quan=StringVar()
        cost=StringVar()

        date.set(datetime.now())


        # Entry

        self.entry_frame=Frame(self.win, bg='#FFE7CC')
        self.entry_frame.place(x=60,y=110,width=440,height=680)

        self.bill_no=Label(self.entry_frame, text='Enter Details', font=('Arial', 15, 'bold'), bg='#FFE7CC')
        self.bill_no.grid(row=0, column=0,padx=4,pady=7)

        self.bill_no=Label(self.entry_frame, text='Bill Number', font=('Arial', 15), bg='#FFE7CC')
        self.bill_no.grid(row=1, column=0,padx=4,pady=5)

        self.bill_no_ent=Entry(self.entry_frame, bd=3, font=('Arial', 15), textvariable=bill_no_tk, fg='lightgray')
        self.bill_no_ent.grid(row=1, column=1,padx=4,pady=5)


        self.cus_num=Label(self.entry_frame, text='Customer Name', font=('Arial', 15), bg='#FFE7CC')
        self.cus_num.grid(row=2, column=0,padx=4,pady=5)

        self.cus_num_ent=Entry(self.entry_frame, bd=3,textvariable=cus_num, font=('Arial', 15))
        self.cus_num_ent.grid(row=2, column=1,padx=4,pady=5)


        self.cus_con=Label(self.entry_frame, text='Customer Contact', font=('Arial', 15), bg='#FFE7CC')
        self.cus_con.grid(row=4, column=0,padx=4,pady=5)

        self.cus_con_ent=Entry(self.entry_frame, bd=3,textvariable=cus_con, font=('Arial', 15))
        self.cus_con_ent.grid(row=4, column=1,padx=4,pady=5)


        self.date=Label(self.entry_frame, text='Date', font=('Arial', 15), bg='#FFE7CC')
        self.date.grid(row=5, column=0,padx=4,pady=5)

        self.date_ent=Entry(self.entry_frame, bd=3,textvariable=date, font=('Arial', 15), fg='lightgray')
        self.date_ent.grid(row=5, column=1,padx=4,pady=5)


        self.item_pur=Label(self.entry_frame, text='Item Purchased', font=('Arial', 15), bg='#FFE7CC')
        self.item_pur.grid(row=6, column=0,padx=4,pady=5)

        self.item_pur_ent=Entry(self.entry_frame, bd=3,textvariable=item_pur, font=('Arial', 15))
        self.item_pur_ent.grid(row=6, column=1,padx=4,pady=5)


        self.item_quan=Label(self.entry_frame, text='Item quantity', font=('Arial', 15), bg='#FFE7CC')
        self.item_quan.grid(row=7, column=0,padx=4,pady=5)

        self.item_quan_ent=Entry(self.entry_frame, bd=3,textvariable=item_quan, font=('Arial', 15))
        self.item_quan_ent.grid(row=7, column=1,padx=4,pady=5)


        self.cost=Label(self.entry_frame, text='cost of one', font=('Arial', 15), bg='#FFE7CC')
        self.cost.grid(row=8, column=0,padx=4,pady=5)

        self.cost_ent=Entry(self.entry_frame, bd=3,textvariable=cost, font=('Arial', 15))
        self.cost_ent.grid(row=8, column=1,padx=4,pady=5)

        # Functions of entries

        total_list=[]
        self.grand_total=0

        def default_bill():
            self.bill_text.insert(END, '\t\t\t\t    Street Restaurant')
            self.bill_text.insert(END, '\n\t\t\t    H#3-3 R#7/A Kaderabad Mohammadpur')
            self.bill_text.insert(END, '\n\t\t\t    Contact no.: +880 -163 -151 -1325')
            self.bill_text.insert(END, '\n==========================================================================================')
            self.bill_text.insert(END,f'\nBill Number {bill_no_tk.get()}')

        def genbill():
            if cus_num=='' and cus_con=='':
                messagebox.showerror('Error! Please enter all the fields')
            else:
                self.bill_text.insert(END, f'\nCustomer Name: {cus_num.get()}')
                self.bill_text.insert(END, f'\nCustomer Name: {cus_con.get()}')
                self.bill_text.insert(END, f'\nCustomer Name: {date.get()}')
                self.bill_text.insert(END, '\n==========================================================================================')
                self.bill_text.insert(END,'\nProduct\t\t          Quantity          \t\tCost\t\t             Total')
                self.bill_text.insert(END, '\n==========================================================================================')
    
                self.but_add.config(state='normal')
                self.total.config(state='normal')

        def addfunc():
            if item_pur.get()=='' and item_quan.get()=='':
                messagebox.showerror('Error! Please fill all the fields')
            else:
                tot=int(item_quan.get())*int(cost.get())
                total_list.append(tot)
                self.bill_text.insert(END,f'\n{item_pur.get()}:\t\t          {item_quan.get()}                 \t\t{cost.get()} Tk\t\t            {tot} Tk')
            

        def grandtotal():
            for item in total_list:
                self.grand_total=self.grand_total+item
            self.bill_text.insert(END, '\n==========================================================================================')
            self.bill_text.insert(END,f'\n\t\t\t\tGrand Total: {self.grand_total} Tk')
            self.bill_text.insert(END, '\n==========================================================================================')
            self.sav.config(state='normal')
    

        def clearfunc():
            cus_con.set('')
            cus_num.set('')
            item_pur.set('')
            item_quan.set('')
            cost.set('')

        def resetfunc():
            self.grand_total=0
            total_list.clear()
            self.bill_text.delete('1.0', END)
            self.sav.config(state='disabled')
            self.total.config(state='disabled')
            self.but_add.config(state='disabled')

        def savefunc():
            user_choice=messagebox.askyesno("Confirm?",f"Do you want to save the bill{bill_no_tk.get()}?")
            if user_choice>0:
                self.bill_content=self.bill_text.get('1.0',END)
                try:
                    with open(f"{sys.path[0]}/bills/{bill_no_tk.get()}.txt", 'w') as con:
                        con.write(self.bill_content)
                    messagebox.showinfo('Success!', f'Bill {bill_no_tk.get()} has been saved successfully!')
                    con.close()
                except Exception as e:
                    messagebox.showerror("Error 404")
            else:
                return
            

        # Button

        self.button_frame=LabelFrame(self.entry_frame,bd=3,text='Options',bg='#F8CBA6',font=('Arial',15))
        self.button_frame.place(x=20,y=360,width=390,height=300)

        self.but_add=Button(self.button_frame, bd=2,bg='#FFFBEB', text='Add',font=('Arial',12), width=12,height=3, command=addfunc)
        self.but_add.grid(row=0,column=1,padx=4,pady=2)

        self.generate=Button(self.button_frame, bd=2,bg='#FFFBEB', text='Generate',font=('Arial',12), width=12,height=3, command=genbill)
        self.generate.grid(row=0,column=0,padx=4,pady=2)

        self.total=Button(self.button_frame, bd=2,bg='#FFFBEB', text='Total',font=('Arial',12), width=12,height=3, command=grandtotal)
        self.total.grid(row=0,column=2,padx=4,pady=2)

        self.reset=Button(self.button_frame, bd=2,bg='#FFFBEB', text='Reset',font=('Arial',12), width=12,height=3, command=resetfunc)
        self.reset.grid(row=1,column=0,padx=4,pady=2)

        self.clear=Button(self.button_frame, bd=2,bg='#FFFBEB', text='Clear',font=('Arial',12), width=12,height=3, command=clearfunc)
        self.clear.grid(row=1,column=2,padx=4,pady=2)

        self.play=Button(self.button_frame, bd=2,bg='#FFFBEB', text='Play Game',font=('Arial',15))
        self.play.grid(row=2,column=1,padx=5,pady=10)
        self.play.place(x=10,y=155,width=360,height=100)

        self.sav=Button(self.button_frame, bd=2,bg='#FFFBEB', text='Save',font=('Arial',12), width=12,height=3, command=savefunc)
        self.sav.grid(row=1,column=1,padx=4,pady=2)

        self.sav.config(state='disabled')
        self.total.config(state='disabled')
        self.but_add.config(state='disabled')

        # Calculator

        self.cal_frame=Frame(self.win, bd=1,bg='#F8CBA6')
        self.cal_frame.place(x=530,y=110,width=760,height=295)

        self.num_ent=Entry(self.cal_frame, bd=15, bg='#FFFBEB',textvariable=cal_var, font=('Arial',12), width=81,justify='right')
        self.num_ent.grid(row=0,column=0, columnspan=5) # even tho row one has a bigger len still lets the other rows arrange below

        def press_btn(event):
            text=event.widget.cget('text')
            if text=='=':
                if cal_var.get().isdigit():
                    value=int(cal_var.get())
                else:
                    try:
                        value=eval(self.num_ent.get())
                    except:
                        print('Error')
                cal_var.set(value)
                self.num_ent.update()
            elif text=='Clear':
                cal_var.set('')
            else:
                cal_var.set(cal_var.get()+text)
                self.num_ent.update()

        self.btn7=Button(self.cal_frame, bg='#FFE7CC',text='7', bd=8, width=14,height=1, font=('Arial',15))
        self.btn7.grid(row=1,column=0,padx=1,pady=4)
        self.btn7.bind('<Button-1>',press_btn)
        self.btn8=Button(self.cal_frame, bg='#FFE7CC',text='8', bd=8, width=14,height=1, font=('Arial',15))
        self.btn8.grid(row=1,column=1,padx=1,pady=4)
        self.btn8.bind('<Button-1>',press_btn)
        self.btn9=Button(self.cal_frame, bg='#FFE7CC',text='9', bd=8, width=14,height=1, font=('Arial',15))
        self.btn9.grid(row=1,column=2,padx=1,pady=4)
        self.btn9.bind('<Button-1>',press_btn)
        self.btnadd=Button(self.cal_frame, bg='#FFE7CC',text='+', bd=8, width=14,height=1, font=('Arial',15))
        self.btnadd.grid(row=1,column=3,padx=1,pady=4)
        self.btnadd.bind('<Button-1>',press_btn)

        self.btn4=Button(self.cal_frame, bg='#FFE7CC',text='4', bd=8, width=14,height=1, font=('Arial',15))
        self.btn4.grid(row=2,column=0,padx=1,pady=4)
        self.btn4.bind('<Button-1>',press_btn)
        self.btn5=Button(self.cal_frame, bg='#FFE7CC',text='5', bd=8, width=14,height=1, font=('Arial',15))
        self.btn5.grid(row=2,column=1,padx=1,pady=4)
        self.btn5.bind('<Button-1>',press_btn)
        self.btn6=Button(self.cal_frame, bg='#FFE7CC',text='6', bd=8, width=14,height=1, font=('Arial',15))
        self.btn6.grid(row=2,column=2,padx=1,pady=4)
        self.btn6.bind('<Button-1>',press_btn)
        self.btnsub=Button(self.cal_frame, bg='#FFE7CC',text='-', bd=8, width=14,height=1, font=('Arial',15))
        self.btnsub.grid(row=2,column=3,padx=1,pady=4)
        self.btnsub.bind('<Button-1>',press_btn)

        self.btn1=Button(self.cal_frame, bg='#FFE7CC',text='1', bd=8, width=14,height=1, font=('Arial',15))
        self.btn1.grid(row=3,column=0,padx=1,pady=4)
        self.btn1.bind('<Button-1>',press_btn)
        self.btn2=Button(self.cal_frame, bg='#FFE7CC',text='2', bd=8, width=14,height=1, font=('Arial',15))
        self.btn2.grid(row=3,column=1,padx=1,pady=4)
        self.btn2.bind('<Button-1>',press_btn)
        self.btn3=Button(self.cal_frame, bg='#FFE7CC',text='3', bd=8, width=14,height=1, font=('Arial',15))
        self.btn3.grid(row=3,column=2,padx=1,pady=4)
        self.btn3.bind('<Button-1>',press_btn)
        self.btnmul=Button(self.cal_frame, bg='#FFE7CC',text='*', bd=8, width=14,height=1, font=('Arial',15))
        self.btnmul.grid(row=3,column=3,padx=1,pady=4)
        self.btnmul.bind('<Button-1>',press_btn)

        self.btndot=Button(self.cal_frame, bg='#FFE7CC',text='Clear', bd=8, width=14,height=1, font=('Arial',15))
        self.btndot.grid(row=4,column=0,padx=1,pady=4)
        self.btndot.bind('<Button-1>',press_btn)
        self.btn0=Button(self.cal_frame, bg='#FFE7CC',text='0', bd=8, width=14,height=1, font=('Arial',15))
        self.btn0.grid(row=4,column=1,padx=1,pady=4)
        self.btn0.bind('<Button-1>',press_btn)
        self.btneq=Button(self.cal_frame, bg='#FFE7CC',text='=', bd=8, width=14,height=1, font=('Arial',15))
        self.btneq.grid(row=4,column=2,padx=1,pady=4)
        self.btneq.bind('<Button-1>',press_btn)
        self.btndiv=Button(self.cal_frame, bg='#FFE7CC',text='/', bd=8, width=14,height=1, font=('Arial',15))
        self.btndiv.grid(row=4,column=3,padx=1,pady=4)
        self.btndiv.bind('<Button-1>',press_btn)

        # Bill

        self.bill_frame=LabelFrame(self.win,text='Bill Info', font=('Arial',15), bg='#FFE7CC', bd=1, relief=SOLID)
        self.bill_frame.place(x=540,y=420,width=745,height=370)

        self.y_scroll=Scrollbar(self.bill_frame, orient='vertical')
        self.bill_text=Text(self.bill_frame,bg='white')
    
        self.y_scroll.config(command=self.bill_text.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_text.pack(fill=BOTH, expand=TRUE)

        default_bill()
        









if __name__=='__main__':
    main()