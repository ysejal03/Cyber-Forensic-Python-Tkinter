import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Text
from tkinter import filedialog


global casefiles
casefiles=['Heist.txt','Murder.txt','caseno3.txt','Hit&Runcase.txt']

def evidence():

    def save_inf():
        e22=entry22.get()
        e28=entry28.get()
        e24=entry24.get()
        e25=entry25.get()
        e29=entry29.get()
        
        with open(e3+'.txt',"a+") as file:
            file.writelines("\n\t\t\tEVIDENCE INFORMATION:")
            file.writelines("\nEVIDENCE NUMBER:\n")
            file.writelines(e22)
            file.writelines("\n\nFILE PATH:\n")
            file.writelines(e29)
            file.writelines("\n\nUNIQUE DESCRIPTION:\n")
            file.writelines(e28)
            file.writelines("\n\nEXAMINER:\n")
            file.writelines(e24)
            file.writelines("\n\nNOTES:\n")
            file.writelines(e25)
            file.close()
    root=Tk()
    root.geometry("1000x1000")

    root.title("Evidence")
    root.configure(background='black')

    label22=Label(root,text="EVIDENCE INFORMATION:",font=("Courier New",20,'bold')).place(x=270,y=60)

    
    label22=Label(root,text="Evidence number:",font=("Courier New",10,'bold')).place(x=270,y=130)
    entry22=Entry(root,width=40,font=("Courier New",10,'bold'))
    entry22.place(x=450,y=130)

    MyText=StringVar()

    label29=Label(root,text="Choose Evidence:",font=("Courier New",10,'bold')).place(x=270,y=180)
    entry29=Entry(root,width=40,textvariable= MyText,font=("Courier New",10,'bold'))
    entry29.place(x=450,y=180)

    def DisplayDir():
        feedback = filedialog.askopenfilename(initialdir=r'C:\Users\PC LAB\Desktop\cyber forensics',filetypes =(('Image Files', '*.gif'),('Image files','*.jpeg*')))
        entry29.delete(0,END)
        
        
        entry29.insert(END,feedback)
    browsebutton=Button(root,text="Browse",padx=3,pady=3,command=DisplayDir,font=("Courier New",10,'bold')).place(x=800,y=180) 

    label28=Label(root,text="Unique Description:",font=("Courier New",10,'bold')).place(x=270,y=230)
    entry28=Entry(root,width=40,font=("Courier New",10,'bold'))
    entry28.place(x=450,y=230)

    label24=Label(root,text="Examiner:",font=("Courier New",10,'bold')).place(x=270,y=280)
    entry24=Entry(root,width=40,font=("Courier New",10,'bold'))
    entry24.place(x=450,y=280)

    label25=Label(root,text="Notes:",font=("Courier New",10,'bold')).place(x=270,y=320)
    entry25=Entry(root,width=40,font=("Courier New",10,'bold'))
    entry25.place(x=450,y=320)

    def casemessage():
        messagebox.showinfo("Login info", "Added Case file Successfully",command=root.destroy())
        

    backbutton=Button(root,text="Back",padx=3,pady=3,font=("Courier New",8,'bold')).place(x=450,y=370)
    nextbutton=Button(root,text="Next",padx=3,pady=3,command=casemessage,font=("Courier New",8,'bold')).place(x=530,y=370)
    savebutton=Button(root,text="Save",padx=3,pady=3,command=save_inf,font=("Courier New",8,'bold')).place(x=610,y=370)
    cancelbutton=Button(root,text="Cancel",command=root.destroy,padx=3,pady=3,font=("Courier New",8,'bold')).place(x=690,y=370)

def evidence02():


    def save_inf():
        e22=entry22.get()
        e23=entry28.get()
        e24=entry24.get()
        e25=entry25.get()
        e26=entry30.get()
        e29=entry29.get()
        
        with open(e26+'.txt',"a+") as file:
            file.writelines("\n\t\t\tEVIDENCE INFORMATION:")
            file.writelines("\nEVIDENCE NUMBER:\n")
            file.writelines(e22)
            file.writelines("\n\nFILE PATH:\n")
            file.writelines(e29)
            file.writelines("\n\nUNIQUE DESCRIPTION:\n")
            file.writelines(e23)
            file.writelines("\n\nEXAMINER:\n")
            file.writelines(e24)
            file.writelines("\n\nNOTES:\n")
            file.writelines(e25)
            file.close()
    root=Tk()
    root.geometry("1000x1000")

    root.title("Evidence")
    root.configure(background='black')
    label22=Label(root,text="EVIDENCE INFORMATION:",font=("Courier New",20,'bold')).place(x=320,y=60)

    label30=Label(root,text="Case name",font=("Courier New",10,'bold')).place(x=270,y=130)
    entry30=Entry(root,width=40,font=("Courier New",10,'bold'))
    entry30.place(x=450,y=130)

    
    label22=Label(root,text="Evidence number:",font=("Courier New",10,'bold')).place(x=270,y=180)
    entry22=Entry(root,width=40,font=("Courier New",10,'bold'))
    entry22.place(x=450,y=180)

    MyText=StringVar()

    label29=Label(root,text="Choose Evidence:",font=("Courier New",10,'bold')).place(x=270,y=230)
    entry29=Entry(root,width=40,textvariable= MyText,font=("Courier New",10,'bold'))
    entry29.place(x=450,y=230)    

    def DisplayDir():
        feedback = filedialog.askopenfilename(initialdir=r'C:\Users\PC LAB\Desktop\cyber forensics',filetypes =(('Image Files', '*.png'),('Image Files', '*.gif'),('Image files','*.jpeg*')))
        entry29.delete(0,END)

        entry29.insert(END,feedback)
    browsebutton=Button(root,text="Browse",padx=3,pady=3,command=DisplayDir,font=("Courier New",10,'bold')).place(x=800,y=230) 

    label28=Label(root,text="Unique Description:",font=("Courier New",10,'bold')).place(x=270,y=280)
    entry28=Entry(root,width=40,font=("Courier New",10,'bold'))
    entry28.place(x=450,y=280)

    label24=Label(root,text="Examiner:",font=("Courier New",10,'bold')).place(x=270,y=320)
    entry24=Entry(root,width=40,font=("Courier New",10,'bold'))
    entry24.place(x=450,y=320)

    label25=Label(root,text="Notes:",font=("Courier New",10,'bold')).place(x=270,y=370)
    entry25=Entry(root,width=40,font=("Courier New",10,'bold'))
    entry25.place(x=450,y=370)
        
        

        
    def casemessage():
        messagebox.showinfo("Login info", "Added Evidence file Successfully",command=root.destroy())
        

    backbutton=Button(root,text="Back",padx=3,pady=3,font=("Courier New",8,'bold')).place(x=480,y=420)
    nextbutton=Button(root,text="Next",padx=3,pady=3,command=casemessage,font=("Courier New",8,'bold')).place(x=560,y=420)
    savebutton=Button(root,text="Save",padx=3,pady=3,command=save_inf,font=("Courier New",8,'bold')).place(x=640,y=420)
    cancelbutton=Button(root,text="Cancel",command=root.destroy,padx=3,pady=3,font=("Courier New",8,'bold')).place(x=720,y=420)
def info():

    def save():
        e12=entry2.get()
        e13=entry3.get()
        e14=entry4.get()
        e15=entry5.get()
        e16=entry6.get()
        e17=entry7.get()
        e18=entry8.get()

        with open(e3+'.txt',"a+") as file:
            file.writelines("\n\t\t\tCASE INFORMATION FORENSIC EXAMINER INFORMATION\n")
            file.writelines("\nAgencies/companies:\n")
            file.writelines(e12)
            file.writelines("\n\nExaminer's name:\n")
            file.writelines(e13)
            file.writelines("\n\nAddress:\n")
            file.writelines(e14)
            file.writelines("\n\nPhone:\n")
            file.writelines(e15)
            file.writelines("\n\nFax:\n")
            file.writelines(e16)
            file.writelines("\n\nEmail:\n")
            file.writelines(e17)
            file.writelines("\n\nComments:\n")
            file.writelines(e18)
            file.close()
        
    root=Tk()
    root.geometry("1000x1000")
    root.title("case information")
    root.configure(background='black')
    
    
    label1=Label(root,text="Forensic examiner information",font=("Courier New",20,'bold')).place(x=250,y=80)
    label1=Label(root,text="Enter the following case information",font=("Courier New",13,'bold')).place(x=210,y=140)

    label2=Label(root,text="Agencies/companies",font=("Courier New",13,'bold')).place(x=210,y=180)
    entry2=Entry(root,width=35,font=("Courier New",13,'bold'))
    entry2.place(x=420,y=180)

    label3=Label(root,text="Examiner's name",font=("Courier New",13,'bold')).place(x=210,y=220)
    entry3=Entry(root,width=35,font=("Courier New",13,'bold'))
    entry3.place(x=420,y=220)
    label4=Label(root,text="Address",font=("Courier New",13,'bold')).place(x=210,y=260)
    entry4=Entry(root,width=35,font=("Courier New",13,'bold'))
    entry4.place(x=420,y=260)

    label5=Label(root,text="Phone",font=("Courier New",13,'bold')).place(x=210,y=300)
    entry5=Entry(root,width=17,font=("Courier New",13,'bold'))
    entry5.place(x=420,y=300)

    label6=Label(root,text="Fax",font=("Courier New",13,'bold')).place(x=600,y=300)
    entry6=Entry(root,width=12,font=("Courier New",13,'bold'))
    entry6.place(x=650,y=300)

    label7=Label(root,text="Email",font=("Courier New",13,'bold')).place(x=210,y=340)
    entry7=Entry(root,width=35,font=("Courier New",13,'bold'))
    entry7.place(x=420,y=340)

    label8=Label(root,text="Comments:",font=("Courier New",13,'bold')).place(x=210,y=380)
    entry8=Entry(root,width=35,font=("Courier New",13,'bold'))
    entry8.place(x=420,y=380)

    savebutton=Button(root,text="Save",padx=3,pady=3,command=save,font=("Courier New",10,'bold')).place(x=420,y=420)
    nextbutton=Button(root,text="Add Evidence",padx=3,pady=3,command=evidence,font=("Courier New",10,'bold')).place(x=490,y=420)
    cancelbutton=Button(root,text="Cancel",command=root.destroy,padx=3,pady=3,font=("Courier New",10,'bold')).place(x=620,y=420)
    backbutton=Button(root,text="Back",padx=3,pady=3,command=data,font=("Courier New",10,'bold')).place(x=700,y=420)

def data():
    root=Tk()
    root.geometry("1000x1000")
    root.title("new case")
    root.configure(background='black')



    def save_info():
        e1=entry1.get()
        e2=spin1.get()
        global e3
        e3=entry5.get()
        e4=entry6.get()
        text_repo=text1.get('1.0','end-1c')

        casefiles.append(e3)
        
        print("Investigator's name:",e1,"\nCase Number:",e2,"\nCase name:",e3,"\nCase path:",e4)

        with open(e3+'.txt',"w") as file:
            file.writelines("\t\t\t\tCASE INFORMATION:\n")
            file.writelines("\n\nInvestigator's name:\n")
            file.writelines(e1)
            file.writelines("\n\nCase Number:\n")
            file.writelines(e2)
            file.writelines("\n\nCase Name:\n")
            file.writelines(e3)
            file.writelines("\n\nCase path:\n")
            file.writelines(e4)
            file.writelines("\n\nCase Description:\n")
            file.writelines(text_repo)
            file.close()

        
    global invname
    invname=StringVar()
    global casename
    casename=StringVar()
    global casepath
    casepath=StringVar()
    global casedes
    casedes=StringVar()
    global casenumber
    casenumber=IntVar()
    
    label1=Label(root,text="ACCESS DATA'S CYBER FORENSIC",font=("Courier New",20,'bold')).place(x=250,y=80)

    label2=Label(root,text="Investigator's name:",font=("Courier New",13,'bold')).place(x=200,y=160)
    entry1=Entry(root,textvariable=invname,width=22,font=("Courier New",13,'bold'))
    entry1.place(x=440,y=160)

    label3=Label(root,text="Case information:",font=("Courier New",13,'bold')).place(x=200,y=200)

    label4=Label(root,text="Case number:",font=("Courier New",13,'bold')).place(x=350,y=240)
    spin1=Spinbox(root,textvariable=casenumber,width=20,font=("Courier New",13,'bold'),from_=0,to=100)
    spin1.place(x=500,y=240)
    
    label5=Label(root,text="Case name:",font=("Courier New",13,'bold')).place(x=350,y=280)
    entry5=Entry(root,textvariable=casename,width=22,font=("Courier New",13,'bold'))
    entry5.place(x=500,y=280)

    MyText=StringVar()

    label6=Label(root,text="Case path:",font=("Courier New",13,'bold')).place(x=350,y=320)
    entry6=Entry(root,textvariable= MyText,width=22,font=("Courier New",13,'bold'))
    entry6.place(x=500,y=320)
    
        

    def DisplayDir():
        feedback = filedialog.askdirectory()
        entry6.delete(0,END)
        
        
        entry6.insert(END,feedback)
    browsebutton=Button(root,text="Browse",padx=3,pady=3,command=DisplayDir,font=("Courier New",10,'bold')).place(x=750,y=320) 

    label7=Label(root,text="Case description:",font=("Courier New",13,'bold')).place(x=200,y=360)
    text1=Text(root,font=("Courier New",9,'bold'),width=55,height=10)
    text1.place(x=200,y=400)
    
    

    savebutton=Button(root,text="Save",padx=3,pady=3,command=save_info,font=("Courier New",10,'bold')).place(x=650,y=400)
    nextbutton=Button(root,text="Next",padx=3,pady=3,command=info,font=("Courier New",10,'bold')).place(x=730,y=400)
    cancelbutton=Button(root,text="Cancel",padx=3,pady=3,command=root.destroy,font=("Courier New",10,'bold')).place(x=685,y=450) 

def research():
    root=Tk()
    root.geometry("1000x1000")
    root.title("Search")
    root.configure(background='black')

        
    entrysearch=ttk.Combobox(root)

    var=StringVar()

    labeltext=Label(root,text="Enter a regular expression to search through files",background="black",fg="white",font=("Courier New",15,'bold')).place(x=210,y=100)
    
    labelsearch=Label(root,text="Search",background="black",fg="white",font=("Courier New",15,'bold')).place(x=340,y=150)
    entrysearch['values']= ('[0-9*]', '[A-Z*]','[@]', "Text")
    entrysearch.place(x=430,y=150)

    
    def search():
        expression=entrysearch.get()
        string=[]
        in_list=[]
        
        for i in casefiles:
            hand=open(i)
            for line in hand:
                line=line.rstrip()
                if re.search(expression,line):
                    string.append('Found in file:')
                    string.append(i)
                    string.append(':')
                    string.append(line)
                    string.append('\n\n')
                    in_list.append(string)
                    string=[]
                    def msg():
                        root = Tk()
                        #scrollbar = Scrollbar(root)
                        root.configure(background="white")
                        root.geometry('500x500')
                        label1=Label(root, text="Result:",font=("Courier New",5,'bold')).place(x=30,y=20)
                        label = Message(root, text=in_list,font=("Times",8),width=950).place(x=30,y=40)
                        root.mainloop()
        
                
     
                        
        msg()

    searchbutton=Button(root,text="Search",padx=3,pady=3,command=search,font=("Courier New",10,'bold')).place(x=400,y=280)
    cancelbutton=Button(root,text="Cancel",padx=3,pady=3,command=root.destroy,font=("Courier New",10,'bold')).place(x=480,y=280)
    root.mainloop()


def openfile():
  
  
    # This function will be used to open
    # file in read mode and only Python files 
    # will be opened 
    def open_file(): 
        file = filedialog.askopenfilename(initialdir=r'C:\Users\PC LAB\Desktop\cyber forensics',filetypes =(('Text Files', '*.txt'),('all files','*.*')))
        string=[]
        file_name=file[40:]
        real_file=open(file_name,'r')
        if real_file is not None: 
            content = real_file.read()
            string.append(content)
        def msgb():
            root = Tk()
            root.geometry('1000x1000')
           
            label = Message(root, text=string,font=("Courier New",8,'bold')).place(x=50,y=60)
            root.mainloop()
        msgb()
    

    open_file()


def firstpage():
    root=Tk()
    root.geometry("1000x1000")
    root.title("Cyber Forensic Data")
    root.configure(background="black")
   
    def search_1():
        if v.get()==1:
            data()
        if v.get()==3:
            research()
        if v.get()==2:
            openfile()
        if v.get()==4:
            evidence02()

    def destroy():
        root.destroy()

    canvas = Canvas(root, width = 600, height =400)
    canvas.place(x=200,y=150)
    my_image = PhotoImage(file='C:\\Users\\PC LAB\\Documents\\firstpage.gif')
    canvas.create_image(0,0, anchor = NW, image=my_image)

    label1=Label(root,text="CYBER FORENSICS",background="black",fg="white",font=("Times",30,'bold')).place(x=310,y=190)
    
    okbutton=Button(root,text="OK",padx=3,pady=3,font=("Courier New",10,'bold'),background="black",fg='white',command=search_1)
    okbutton.place(x=620,y=320)
    cancelbutton=Button(root,text="Cancel",padx=5,pady=5,font=("Courier New",10,'bold'),background="black",fg='white',command=root.destroy)
    cancelbutton.place(x=600,y=380)
    v = IntVar()
    r1=Radiobutton(root, text ="Start a new case",font=("Times",15,'bold'),background='black',fg='white',  variable = v, value = 1)
    r1.place(x=350,y=300)
    r2=Radiobutton(root, text ="Open an existing case",font=("Times",15,'bold'),background='black',fg='white',   variable = v, value = 2)
    r2.place(x=350,y=340)
    r3=Radiobutton(root, text ="Search",font=("Times",15,'bold'),background='black',fg='white',   variable = v, value = 3)
    r3.place(x=350,y=380)
    r3=Radiobutton(root, text ="Add Evidence",font=("Times",15,'bold'),background='black',fg='white',   variable = v, value = 4)
    r3.place(x=350,y=420)

    root.mainloop()

def login():
      
    class LoginFrame(Frame):
        def __init__(self, root):
            super().__init__(root)

            self.label_username = Label(self, text="Username",font=("Times",15,'bold'))
            self.label_password = Label(self, text="Password",font=("Times",15,'bold'))

            self.entry_username = Entry(self)
            self.entry_password = Entry(self, show="*")

            self.label_username.grid(row=1, sticky=E)
            self.label_password.grid(row=2, sticky=E)
            self.entry_username.grid(row=1, column=1)
            self.entry_password.grid(row=2, column=1)
    
            self.checkbox = Checkbutton(self, text="Keep me logged in",font=("Times",10,'bold'))
            self.checkbox.grid(columnspan=2)

            self.logbtn = Button(self, text="Login", command=self._login_btn_clicked,font=("Times",10,'bold'))
            self.logbtn.grid(columnspan=2)

            self.pack()

        def _login_btn_clicked(self):
            # print("Clicked")
            username = self.entry_username.get()
            password = self.entry_password.get()

            # print(username, password)

            if username == "Admin" and password == "password":
                messagebox.showinfo("Login info", "Welcome")
                root.destroy()
                firstpage()
            
            else:
                messagebox.showerror("Login error", "Incorrect username")


    root = Tk()
    root.title('cyber forensics')
    root.configure(bg='black')
    root.geometry('1000x1000')
    canvas = Canvas(root,bg="black", width = 300, height =320)
    canvas.pack()
    my_image = PhotoImage(file='C:\\Users\\PC LAB\\Documents\\Hacker.gif')
    canvas.create_image(0,0, anchor = NW, image=my_image)


    label1=Label(root,text="CYBER FORENSICS",background="black",fg="white",font=("Times",60,'bold')).place(x=130,y=500)

    
    lf = LoginFrame(root)
    root.mainloop()
login()



