from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System", bd=5, relief=GROOVE, font=("times new roman",40,"bold"), bg="light grey", fg="black")
        title.pack(side=TOP, fill=X)

        # All Variables==========================

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        # Manage Frame===========================

        Manage_Frame=Frame(self.root, bd=4, relief=RIDGE)#, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=560)

        m_title=Label(Manage_Frame,text="Manage Student", font=("times new roman",30,"bold"), fg="black")
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No.", font=("times new roman",20,"bold"), fg="black")
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var, font=("times new roman",15,"bold"), bd=2, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name=Label(Manage_Frame,text="Name", font=("times new roman",20,"bold"), fg="black")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman",15,"bold"), bd=2, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email=Label(Manage_Frame,text="Email", font=("times new roman",20,"bold"), fg="black")
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var, font=("times new roman",15,"bold"), bd=2, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender=Label(Manage_Frame,text="Gender", font=("times new roman",20,"bold"), fg="black")
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var, font=("times new roman",13,"bold"), state="readonly")
        combo_gender['values']=("male", "female")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")


        lbl_contact=Label(Manage_Frame,text="Contact No.", font=("times new roman",20,"bold"), fg="black")
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman",15,"bold"), bd=2, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob=Label(Manage_Frame,text="D.O.B", font=("times new roman",20,"bold"), fg="black")
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var, font=("times new roman",15,"bold"), bd=2, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # Button Frame=================================================

        btn_Frame=Frame(Manage_Frame, relief=RIDGE)#, bg="crimson")
        btn_Frame.place(x=10, y=475, width=430)

        Addbtn=Button(btn_Frame, text="Add", command=self.add_students, width=10).grid(row=0, column=0, padx=10, pady=10)
        #Addbtn.pack()
        Updatebtn=Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn=Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn=Button(btn_Frame, text="Clear", width=10, command=self.Clear).grid(row=0, column=3, padx=10, pady=10)

        # Details Frame===============================================

        Details_Frame=Frame(self.root, bd=4, relief=RIDGE)#, bg="crimson")
        Details_Frame.place(x=500, y=100, width=825, height=560)

        lbl_search=Label(Details_Frame,text="Search By:", font=("times new roman",20,"bold"), fg="black")
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search=ttk.Combobox(Details_Frame, width=10,textvariable=self.search_by, font=("times new roman",13,"bold"), state="readonly")
        combo_search['values']=("Roll_no", "Name")
        combo_search.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        txt_search=Entry(Details_Frame, font=("times new roman",15,"bold"),textvariable=self.search_txt, bd=2, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn=Button(Details_Frame, text="Search", width=10,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        Showallbtn=Button(Details_Frame, text="Show All", width=10, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        # Table Frame=========================================

        Table_Frame=Frame(Details_Frame, bd=3, relief=RIDGE)#, bg="crimson")
        Table_Frame.place(x=20, y=70, width=775, height=460)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="DOB")
        self.Student_table['show']='headings'                #to avoid first blank column
        self.Student_table.column("roll",width=150)
        self.Student_table.column("gender",width=150)
        self.Student_table.column("dob",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","All fields are required.")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stms",port=3307)
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get()
                                                                            ))
            con.commit()
            self.fetch_data()
            self.Clear()
            con.close()
            messagebox.showinfo("Success","Record has been Created.")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stms",port=3307)
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def Clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")

    def get_cursor(self, event):
        cursour_row=self.Student_table.focus()
        contents=self.Student_table.item(cursour_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])

    def update_data(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","All fields are required to Update.")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stms",port=3307)
            cur=con.cursor()
            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s where roll_no=%s",(self.name_var.get(),
                                                                                                                        self.email_var.get(),
                                                                                                                        self.gender_var.get(),
                                                                                                                        self.contact_var.get(),
                                                                                                                        self.dob_var.get(),
                                                                                                                        self.Roll_No_var.get()
                                                                                                                        ))
            con.commit()
            self.fetch_data()
            self.Clear()
            con.close()
            messagebox.showinfo("Success","Record has been Updated.")

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stms",port=3307)
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.Clear()
        messagebox.showinfo("Success","Record has been Deleted.")

    def search_data(self):
        if self.search_by.get()=="" or self.search_txt.get()=="":
            messagebox.showerror("Error","Select or insert values properly")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stms",port=3307)
            cur=con.cursor()
            cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
            else:
                messagebox.showinfo("Search","No data in Database for searched values.")
            con.close()



        

root=Tk()
ob=Student(root)
root.mainloop()