import sqlite3
import matplotlib.pyplot as plt
connection=sqlite3.connect("student_detail.db")
cursor=connection.cursor()
print("\n----------------VISUALIZE AND COMPARE YOUR MARKS----------------\n")

def home():
    print("\n----------------HOME----------------\n")
    a=int(input("""1.Login
2.Sign up
3.Exit\n\n"""))
    if a==1:
        login()
    elif a==2:
        signup()
    else:
        connection.commit()
        connection.close()

def signup():
    print("\n----------------SIGNUP PORTAL----------------\n")
    user=input("Enter your name for userid: ")
    command1="""
    CREATE TABLE {userid}
    (password CHAR(20),Exam CHAR(10),Physics INTEGER,Maths INTEGER,
    DS INTEGER,BEEE INTEGER,EG INTEGER,Total INTEGER)
    """
    command2=command1.format(userid=user)
    cursor.execute(command2)
    command1="""INSERT INTO {userid} (password)VALUES("{password}")"""
    command2=command1.format(userid=user,password=input("Enter password: "))
    cursor.execute(command2)
    connection.commit()
    print("\nSIGN UP SUCCESSFULL !!!\n")
    print("now login to visualize your marks\n")
    home()

def login():
    print("\n----------------LOGIN PORTAL----------------\n")
    user=input("Enter userid: ")
    pw=input("Enter password: ")
    command1="SELECT password FROM {userid}"
    command2=command1.format(userid=user)
    cursor.execute(command2)
    result=cursor.fetchone()
    if(result[0]==pw):
        print("\nLOGIN SUCCESSFULL !!!")
        menu(user)
    else:
        print("\nLOGIN FAILED !!!")
        home()

def menu(user):
    print("\n----------------MAIN MENU----------------\n")
    a=int(input("""\n1.Enter marks
2.Visualize marks
3.Compare CAT vs SEMESTER
0 to log out\n   
"""))
    if a==1:
        enter(user)
    elif a==2:
        visualize(user)
    elif a==3:
        compare(user)
    else:
        home()

def enter(user):
    print("\n----------------MARK ENTERING MENU----------------\n")
    ch=int(input("""\nENTER MARKS out of 100\n
1.CAT1
2.CAT2
3.CAT3
4.Semester
5 for menu\n"""))
    if ch==6:
        connection.commit()
    elif ch==1 or ch==2 or ch==3 or ch==4:
        phy=int(input("Enter physics marks: "))
        ds=int(input("Enter DS marks: "))
        beee=int(input("Enter BEEE marks: "))
        maths=int(input("Enter maths marks: "))
        eg=int(input("Enter EG marks: "))
        tot=phy+ds+beee+maths+eg
        if ch==1:
            ex="CAT1"
        elif ch==2:
            ex="CAT2"
        elif ch==3:
            ex="CAT3"
        elif ch==4:
            ex="Semester"
        command1="""INSERT INTO {userid}(Exam,Physics,Maths,DS,BEEE,EG,Total) 
        VALUES("{Exam}",{Physics},{Maths},{DS},{BEEE},{EG},{total})"""
        command2=command1.format(userid=user,Exam=ex,Physics=phy,Maths=maths,DS=ds,BEEE=beee,EG=eg,total=tot)
        cursor.execute(command2)
        print("\nMARKS ENTERED SUCCESSFULLY !!!")
        connection.commit()
        menu(user)
    else:
        menu(user)

def visualize(user):
    print("\n----------------VISUALIZE----------------\n")
    ch=int(input("""\nEnter choice visualizing\n
1.CAT1
2.CAT2
3.CAT3
4.Semester
5 for menu\n\n"""))
    if ch==1 or ch==2 or ch==3 or ch==4:
        if ch==1:
            ex="CAT1"
        elif ch==2:
            ex="CAT2"
        elif ch==3:
            ex="CAT3"
        elif ch==4:
            ex="Semester"
        command1="""SELECT Physics,Maths,BEEE,EG,DS FROM {userid} WHERE (Exam="{exam}")"""
        command2=command1.format(userid=user,exam=ex)
        cursor.execute(command2)
        result=cursor.fetchall()
        labels=["PHYSICS","MATHS","BEEE","EG","DS"]
        marks=[result[0][0],result[0][1],result[0][2],result[0][3],result[0][4]]
        y_positions=range(len(labels))
        plt.bar(y_positions,marks,color=["blue","orange","red","cyan","green"])
        plt.xticks(y_positions,labels)
        plt.ylabel("TOTAL MARKS: 500")
        plt.xlabel("SUBJECT")
        plt.title(ex)
        plt.show()
        visualize(user)
    else:
        menu(user)

def compare(user):
    command1="""SELECT Exam FROM {userid}"""
    command2=command1.format(userid=user)
    cursor.execute(command2)
    result=cursor.fetchall()
    l=len(result)
    if l!=5:
        print("\nEnter all CAT exam and semester marks to compare !!!\n")
    else:
        command1="""SELECT total FROM {userid}"""
        command2=command1.format(userid=user)
        cursor.execute(command2)
        result=cursor.fetchall()
        labels=["CAT1","CAT2","CAT3","SEM"]
        marks=[result[1][0],result[2][0],result[3][0],result[4][0]]
        y_positions=range(len(labels))
        plt.bar(y_positions,marks,color=["orange","red","cyan","green"])
        plt.xticks(y_positions,labels)
        plt.ylabel("TOTAL MARKS: 500")
        plt.xlabel("EXAM")
        plt.title("CAT vs SEMESTER")
        plt.show()
        visualize(user)

home()
