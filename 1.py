from tkinter import *
import tkinter.messagebox as mesg
import mysql.connector as mysql
import matplotlib.pyplot as plt
from tkinter import ttk
#all funtion are defined here
def insert():
 id=e_id.get()
 name=e_name.get();
 marks=e_marks.get();
 graph=e_sex.get();
 if(id=="" or name=="" or marks=="" or graph==""):
 mesg.showinfo("insert status","All fields are required");
 else:
 con=
mysql.connect(host="localhost",user="root",password="tiger",database="tkinter")
 cursor=con.cursor()
 cursor.execute("insert into student values('"+id+"','"+
name+"','"+marks+"','"+graph+"')")
 cursor.execute("commit")
 show()
 mesg.showinfo("insert status","inserted sucessfully");
 con.close()
def delete():
 if(e_id.get()==""):
 mesg.showinfo("delte status","id is cumpolsary for delete")
 else:
 con=
mysql.connect(host="localhost",user="root",password="tiger",database="tkinter")
 cursor=con.cursor()
 cursor.execute("delete from student where id='"+ e_id.get()+"'")
 cursor.execute("commit")

 show()
 mesg.showinfo("delete status","deleted sucessfully");
 con.close()
def update():
 id=e_id.get()
 name=e_name.get();
 marks=e_marks.get();
 graph=e_sex.get();
 if(id=="" or name=="" or marks=="" or graph==""):
 mesg.showinfo("update status","All fields are required");
 else:
 con=
mysql.connect(host="localhost",user="root",password="tiger",database="tkinter")
 cursor=con.cursor()
 cursor.execute("update student set
name='"+name+"',marks='"+marks+"',gender='"+graph+"'where id ='"+id+"'" )
 cursor.execute("commit")
 show()
 mesg.showinfo("update status","updated sucessfully");
 con.close()
def get():
 if(e_id.get()==""):
 mesg.showinfo("fetch status","id is cumpolsary for delete")
 else:
 con=
mysql.connect(host="localhost",user="root",password="tiger",database="tkinter")
 cursor=con.cursor()
 cursor.execute("select*from student where id='"+e_id.get()+"'")
 rows=cursor.fetchall()
 for row in rows:
 e_name.insert(0,row[1])
 e_marks.insert(0,row[2])
 e_sex.insert(0,row[3])
 show()
 con.close()
def show():
 con=
mysql.connect(host="localhost",user="root",password="tiger",database="tkinter")
 cursor=con.cursor()
 cursor.execute("select*from student ")
 rows=cursor.fetchall()
 student_table.delete(*student_table.get_children())

 if len(rows)!=0:
 student_table.delete(*student_table.get_children())
 for row in rows:
 student_table.insert("",END,values=row)
 con.commit()
 con.close()
def clear():
 e_id.delete(0,END)
 e_name.delete(0,END)
 e_marks.delete(0,END)
 e_sex.delete(0,END)


def sexgraph():
 import pymysql
 import matplotlib.pyplot as plt

d1=pymysql.connect(host="localhost",user="root",password="tiger",database="tkinter")
 c1=d1.cursor()
 quer="select count(*) from student where gender='male';"
 c1.execute(quer)
 x=c1.fetchone()
 lst=list(x)
 quer="select count(*) from student where gender='female';"
 c1.execute(quer)
 y=c1.fetchone()
 lst1=list(y)
 lstt=lst+lst1
 y=["Male","Female"]
 plt.bar(y,lstt,color=["red","green"])
 plt.xlabel("Sex")
 plt.ylabel("no. of students")
 plt.show()

root=Tk()
root.geometry("880x505")
root.title("pytohn+tkinter")
title=Label(root,text="Student Mangement System",bd=9,relief=GROOVE,font=("times
new roman",50,"bold"),bg="blue",fg="black")
title.pack(side=TOP,fill=X)
#*********frame*********sa
Manage_Frame=Frame(root,bd=4,relief=RIDGE,bg="blue")
Manage_Frame.place(x=5,y=95,width=420,height=410)
#########label are here##############
id=Label(Manage_Frame,text="Enter ID",bg="blue",font=('italic',20,"bold"),fg="white")
id.place(x=20,y=10)
name=Label(Manage_Frame,text="Name",bg="blue",font=('italic',20,"bold"),fg="white")
name.place(x=20,y=40)
marks=Label(Manage_Frame,text="Marks",bg="blue",font=('italic',20,"bold"),fg="white")
marks.place(x=20,y=70)
graph=Label(Manage_Frame,text="Gender",bg="blue",font=('italic',20,"bold"),fg="white"
)
graph.place(x=20,y=100)
#entry fields are present here
e_id=Entry(Manage_Frame)
e_id.place(x=150,y=18)
e_name=Entry(Manage_Frame)
e_name.place(x=150,y=48)
e_marks=Entry(Manage_Frame)
e_marks.place(x=150,y=78)
e_sex=Entry(Manage_Frame)
e_sex.place(x=150,y=108)
insert=Button(Manage_Frame,text="Insert",font=("bold",10),bg="yellow",command=inse
rt)
insert.place(x=20,y=200,width=70,height=70)
update=Button(Manage_Frame,text="Update",font=("bold",10),bg="yellow",command=u
pdate)
update.place(x=150,y=200,width=70,height=70)
delete=Button(Manage_Frame,text="Delete",font=("bold",10),bg="yellow",command=del
ete)
delete.place(x=300,y=200,width=70,height=70)
get=Button(Manage_Frame,text="Get",font=("bold",10),bg="yellow",command=get)
get.place(x=20,y=300,width=70,height=70)
graph=Button(Manage_Frame,text="Graph plot",bg="lightgreen",command=sexgraph)
graph.place(x=150,y=300,width=70,height=70)
clear=Button(Manage_Frame,text="clear",width=20,height=6,command=clear,bg="yellow
")
clear.place(x=300,y=300,width=70,height=70)
# create listbox object
Table_frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
Table_frame.place(x=430,y=90,width=440,height=410)
scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
student_table=ttk.Treeview(Table_frame,column=("id","Name","Marks","Gender"),xscrol
lcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
student_table.heading("id",text="Roll no")
student_table.heading("Name",tex="Name")
student_table.heading("Marks",tex="Marks")
student_table.heading("Gender",tex="Gender")
student_table['show']='headings'
student_table.column("id",width=50)
student_table.column("Name",width=50)
student_table.column("Marks",width=50)
student_table.column("Gender",width=50)
student_table.pack(fill=BOTH,expand=1)
show()
root.mainloop()