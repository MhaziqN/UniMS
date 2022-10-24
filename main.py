from tkinter import *
from PIL import ImageTk,Image
import pypyodbc as odbc

#Sql Connnection
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME ='HAZIQ-PC\SQLEXPRESS01'
DATABASE_NAME = 'UniMs'

connection_string = f"""
  DRIVER={{{DRIVER_NAME}}};
  SERVER={SERVER_NAME};
  DATABASE={DATABASE_NAME};
  Trust_connection=yes;

"""
conn=odbc.connect(connection_string)
print(conn)
cursor=conn.cursor()

#def logginB():



#AddFunction
def addEmployee():

    def Ok_button():

        id = EmpID_Ent.get()
        name = EmpN_Ent.get()
        address = EmpA_Ent.get()
        Email = EmpE_Ent.get()
        NPhone = EmpPN_Ent.get()
        Age = EmpAGE_Ent.get()
        Position = EmpPOS_Ent.get()

        # nnti tambah add func for pic

        cursor.execute("""INSERT INTO dbo.EmployeeP_ VALUES (?, ?, ?, ?, ?, ?, ?,) """,
                       (id, name, Email, NPhone, Position, address, Age))
        conn.commit()
        print('Employee information successfully added\n')  # Nnti buat Notification # Twitter

    root.title("UniMS")
    root.iconbitmap('UCSI.ico')
    root.geometry("1920x1080")
    root.configure(background="#F0F8FF")

    text_Label = Label(root, text="EMPLOYEE INFORMATION \n (UniMS),", bg="#F0F8FF")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 20))

    text_Label = Label(root, text="Employee ID : " , bg = "#F0F8FF", fg = "Black")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 15))

    EmpID_Ent = Entry(root,width=30)
    EmpID_Ent.pack (ipady=6,pady=(1,15))

    text_Label = Label(root, text="Employee Name : " , bg = "#F0F8FF", fg = "Black")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 15))

    EmpN_Ent = Entry(root, width=30)
    EmpN_Ent.pack(ipady=6, pady=(1, 15))

    text_Label = Label(root, text="Address : ", bg="#F0F8FF", fg="Black")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 15))

    EmpA_Ent = Entry(root, width=30)
    EmpA_Ent.pack(ipady=6, pady=(1, 15))

    text_Label = Label(root, text="Email : ", bg="#F0F8FF", fg="Black")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 15))

    EmpE_Ent = Entry(root, width=30)
    EmpE_Ent.pack(ipady=6, pady=(1, 15))

    text_Label = Label(root, text="Phone Number : ", bg="#F0F8FF", fg="Black")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 15))

    EmpPN_Ent = Entry(root, width=30)
    EmpPN_Ent.pack(ipady=6, pady=(1, 15))

    text_Label = Label(root, text="Date Of Birth : ", bg="#F0F8FF", fg="Black")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 15))

    EmpDB_Ent = Entry(root, width=30)
    EmpDB_Ent.pack(ipady=6, pady=(1, 15))

    text_Label = Label(root, text="Age : ", bg="#F0F8FF", fg="Black")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 15))

    EmpAGE_Ent = Entry(root, width=30)
    EmpAGE_Ent.pack(ipady=6, pady=(1, 15))

    text_Label = Label(root, text="Department ", bg="#F0F8FF", fg="Black")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 15))

    EmpDep_Ent = Entry(root, width=30)
    EmpDep_Ent.pack(ipady=6, pady=(1, 15))

    text_Label = Label(root, text="Position ", bg="#F0F8FF", fg="Black")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 15))

    EmpPOS_Ent = Entry(root, width=30)
    EmpPOS_Ent.pack(ipady=6, pady=(1, 15))

    Ok_butt = Button(root, text='OK', fg='black', bg='azure1', width=30, height=1, command=ok_btn)
    Ok_butt.pack(pady=(2, 40))
    Ok_butt.config(font=('Amasis MT Pro Medium', 10))





def addStudent ():
    id = input('Student ID: ')
    name = input('Student Name : ')
    address = input('Address : ')
    Email = input('Email : ')
    NPhone = input('Phone Number : ')
    Sem = input ('Semester : ')
    DOB = input("Date of Birth : ")
    Age = input('Age : ')

    cursor.execute("""INSERT INTO dbo.StudentP_ VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",(id,name,address,Email,NPhone,Sem,DOB,Age ))
    conn.commit()
    print('Student information successfully added\n') #Nnti buat Notification # Twitter

def addSubject():  #for lecturer
    Sem = input('Semester : ')
    Subj1 = input ('Subject 1 : ')
    Subj2 = input ('Subject 2 : ')
    Subj3 = input ('Subject 3 : ')
    Subj4 = input ('Subject 4 : ')
    Subj5 = input ('Subject 5 : ')

    cursor.execute("""INSERT INTO dbo.SubjectL_ VALUES (?, ?, ?, ?, ?, ?)""",(Sem,Subj1,Subj2,Subj3,Subj4,Subj5))
    conn.commit()
    print('Subject information successfully added\n') #Nnti buat Notification # Twitter


def addFinance():
    id = input('Student ID : ')
    Cfee = input('Current Fee : ')
    Tfee = input('Total Fee : ')

    cursor.execute("""INSERT INTO dbo.Finance_ VALUES (?, ?, ?)""",(id,Cfee,Tfee))
    conn.commit
    print('Finance information successfully added\n')#Nnti buat Notification # Twitter


def AddMark():
    id = input('Student ID : ')
    Malay = int(input('Malay Mark: '))
    English = int(input('English Mark: '))
    Maths = int(input('Math Mark: '))
    Science = int(input('Science Mark: '))
    Geometry = int(input('Geography Mark:'))
    Arts = int(input('Art Mark: '))
    History = int(input('History Mark: '))

    total = Malay + English + Maths + Science + Geometry + Arts + History
    Average =total/7

    if Average >= 90:
        Result =('PASS')
        Grade = 'A+'
    elif Average >= 80:
        Result ='PASS'
        Grade ='A'
    elif Average >= 70:
        Result ='PASS'
        Grade ='B+'
    elif Average >= 60:
        Result ='PASS'
        Grade = 'B'
    elif Average >= 40:
        Result = 'PASS'
        Grade = 'C'
    elif Average <= 39:
        Result = 'FAIL'
        Grade = 'G'

    cursor.execute("""INSERT INTO dbo.ResultS_ VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (id,Malay,English,Maths,Science,Geometry,Arts,History,Result,Grade))
    conn.commit()
    print('Mark information successfully added\n')  # Nnti buat Notification # Twitter

#update func

def exitB_ ():
    root.destroy()

root = Tk()

root.title("UniMS")
root.iconbitmap('UCSI.ico')
root.geometry("1920x1080")
root.configure(background="#F0F8FF")

img=Image.open("UCSI.png")
resize_img=img.resize((200,200))
img=ImageTk.PhotoImage(resize_img)

image_Label=Label(root,image=img)
image_Label.pack(pady=(15,15))

text_Label =Label(root,text="UNIVERSITY MANAGEMENT SYSTEM \n (UniMS),",bg="#F0F8FF")
text_Label.pack()
text_Label.config(font=("Helvetica", 20 ))

emp_btn =Button(root,text="Employee",fg="Black",bg='white',width=30,height=1)
emp_btn.pack(pady=(40,20))
emp_btn.config(font=("Helvetica",15))

std_btn =Button(root,text="Student",fg="Black",bg='white',width=30,height=1)
std_btn.pack(pady=(20,20))
std_btn.config(font=("Helvetica",15))

Fin_btn =Button(root,text="Finance",fg="Black",bg='white',width=30,height=1)
Fin_btn.pack(pady=(20,20))
Fin_btn.config(font=("Helvetica",15))

std_btn =Button(root,text="Subject",fg="Black",bg='white',width=30,height=1)
std_btn.pack(pady=(20,20))
std_btn.config(font=("Helvetica",15))

att_btn =Button(root,text="Attendance",fg="Black",bg='white',width=30,height=1)
att_btn.pack(pady=(20,20))
att_btn.config(font=("Helvetica",15))

ex_btn =Button(root,text="Exit",fg="Black",bg='white',width=30,height=1,command=exitB_)
ex_btn.pack(pady=(20,20))
ex_btn.config(font=("Helvetica",15))


root.mainloop()

#while True :
#    addEmployee()









