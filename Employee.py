from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pypyodbc as odbc
import time
from plyer import notification

# Sql Connnection
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'HAZIQ-PC\SQLEXPRESS01'
DATABASE_NAME = 'UniMs'

connection_string = f"""
  DRIVER={{{DRIVER_NAME}}};
  SERVER={SERVER_NAME};
  DATABASE={DATABASE_NAME};
  Trust_connection=yes;

"""
conn = odbc.connect(connection_string)
print(conn)
cursor = conn.cursor()

root = Tk()


def addEmployee():
    def open():
        global My_EmpI
        root.filename = filedialog.askopenfilename(initialdir='d:/', title='Select Image', filetypes=(
        ("png files", ".png"), ("all files", "*.*")))  # declare type of file
        My_lable = Label(root, text=root.filename)
        My_lable.pack(pady=(1, 1))
        My_EmpI = ImageTk.PhotoImage(Image.open(root.filename))
        EmpI_Label_P = Label(image=My_EmpI)
        EmpI_Label_P.pack()


    def Ok_button():
        id = EmpID_Ent.get()
        name = EmpN_Ent.get()
        address = EmpA_Ent.get()
        Email = EmpE_Ent.get()
        NPhone = EmpPN_Ent.get()
        Age = EmpAGE_Ent.get()
        Position = EmpPos_Ent.get()

        # nnti tambah add func for pic

        cursor.execute("""INSERT INTO dbo.EmployeeP_ VALUES (?, ?, ?, ?, ?, ?, ?) """,
                       (id, name, Email, NPhone, Position, address, Age, ))
        conn.commit()

#        if conn.commit()=='success':
#            while True:
#                notification.notify(
#                    title = "NOTE",
#                    MESSAGE = "Employee information successfully added",
#                    TIMEOUT = 6
#                )




    root.title("UniMS")
    root.iconbitmap('UCSI.ico')
    root.geometry("1920x1080")
    root.configure(background="#F0F8FF")

    text_Label = Label(root, text="EMPLOYEE INFORMATION \n (UniMS),", bg="#F0F8FF")
    text_Label.pack()
    text_Label.config(font=("Helvetica", 20))

    text_Label1 = Label(root, text="Employee ID : ", bg="#F0F8FF", fg="Black")
    text_Label1.pack(pady=(40, 1))
    text_Label1.config(font=("Helvetica", 15))

    EmpID_Ent = Entry(root, width=30)
    EmpID_Ent.pack(ipady=6, pady=(1, 15))

    text_Label2 = Label(root, text="Employee Name : ", bg="#F0F8FF", fg="Black")
    text_Label2.pack()
    text_Label2.config(font=("Helvetica", 15))

    EmpN_Ent = Entry(root, width=30)
    EmpN_Ent.pack(ipady=6, pady=(1, 15))

    text_Label3 = Label(root, text="Address : ", bg="#F0F8FF", fg="Black")
    text_Label3.pack()
    text_Label3.config(font=("Helvetica", 15))

    EmpA_Ent = Entry(root, width=30)
    EmpA_Ent.pack(ipady=6, pady=(1, 15))

    text_Label4 = Label(root, text="Email : ", bg="#F0F8FF", fg="Black")
    text_Label4.pack()
    text_Label4.config(font=("Helvetica", 15))

    EmpE_Ent = Entry(root, width=30)
    EmpE_Ent.pack(ipady=6, pady=(1, 15))

    text_Label5 = Label(root, text="Phone Number : ", bg="#F0F8FF", fg="Black")
    text_Label5.pack()
    text_Label5.config(font=("Helvetica", 15))

    EmpPN_Ent = Entry(root, width=30)
    EmpPN_Ent.pack(ipady=6, pady=(1, 15))

    text_Label7 = Label(root, text="Age : ", bg="#F0F8FF", fg="Black")
    text_Label7.pack()
    text_Label7.config(font=("Helvetica", 15))

    EmpAGE_Ent = Entry(root, width=30)
    EmpAGE_Ent.pack(ipady=6, pady=(1, 15))

    text_Label9 = Label(root, text="Position : ", bg="#F0F8FF", fg="Black")
    text_Label9.pack()
    text_Label9.config(font=("Helvetica", 15))

    EmpPos_Ent = Entry(root, width=30)
    EmpPos_Ent.pack(ipady=6, pady=(1, 15))

    text_Label10 = Label(root, text="Picture : ", bg="#F0F8FF", fg="Black")
    text_Label10.pack()
    text_Label10.config(font=("Helvetica", 15))

    SearchP = Button(root, text='Open File ', fg='black', bg='azure1', width=10, height=1, command=open)
    SearchP.pack(pady=(2, 2))
    SearchP.config(font=('Amasis MT Pro Medium', 10))

    Ok_butt = Button(root, text='OK', fg='black', bg='azure1', width=20, height=1, command=Ok_button)
    Ok_butt.pack(pady=(2, 2))
    Ok_butt.config(font=('Amasis MT Pro Medium', 10))

    root.mainloop()

while True:
    addEmployee()