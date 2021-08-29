from tkinter import *
from tkinter.ttk import Progressbar

def select(event):
    b=event.widget
    value=b['text']
    
    for i in range(15):
        if value==correct_answers[i]:
            if value==correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()
                
                def playagain():
                    root2.destroy()
                    questionArea.delete(1.0,END)
                    questionArea.insert(END,questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])

                    amountLabel.config(image=amountimage)
                
                root2=Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('you won 0 rupay')
                imgLabel=Label(root2,image=centerImage,bd=0)
                imgLabel.pack(pady=30)

                winLabel=Label(root2,text='you win',font=('arial',40,'bold'),bg='black',fg='white')
                winLabel.pack()

                playagainButton=Button(root2,text='play Again',font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=playagain)
                playagainButton.pack()

                closeButton=Button(root2,text='close',font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=close)
                closeButton.pack()

                happyimage = PhotoImage(file='happy.png')
                sadlabel = Label(root2,image=happyimage, bg='black')
                sadlabel.place(x=400, y=280)
                sadlabel1 = Label(root2,image=happyimage, bg='black')
                sadlabel1.place(x=30, y=280)

                root2.mainloop()
                break

            
            questionArea.delete(1.0,END)
            questionArea.insert(END, questions[i+1])
 
            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLabel.config(image=amountImages[i])
            
        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()
            def tryagain():
                root1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])

                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])

                amountLabel.config(image=amountimage)
                
            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('you won 0 rupay')
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=30)

            loseLabel=Label(root1,text='you Lose',font=('arial',40,'bold'),bg='black',fg='white')
            loseLabel.pack()

            tryagainButton=Button(root1,text='Try Again',font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=tryagain)
            tryagainButton.pack()

            closeButton=Button(root1,text='close',font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=close)
            closeButton.pack()

            sadimage = PhotoImage(file='sad.png')
            sadlabel = Label(root1,image=sadimage, bg='black')
            sadlabel.place(x=400, y=280)
            sadlabel1 = Label(root1,image=sadimage, bg='black')
            sadlabel1.place(x=30, y=280)

            root1.mainloop()
            break
        
def lifeline50():
    lifeline50Button.config(image=image50x,state=DISABLED)
    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton4.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=80)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=30)

        progressbarB.config(value=70)

        progressbarC.config(value=90)

        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=80)

        progressbarB.config(value=10)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=20)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=10)

        progressbarB.config(value=70)

        progressbarC.config(value=50)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=90)

        progressbarB.config(value=80)

        progressbarC.config(value=70)

        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)

        progressbarB.config(value=50)

        progressbarC.config(value=70)

        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=40)

        progressbarB.config(value=20)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=90)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=20)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)

        progressbarB.config(value=35)

        progressbarC.config(value=40)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=90)

        progressbarD.config(value=80)

    

def audiencePoleLifeline():
    progressbarA.place(x=580,y=190)
    progressbarB.place(x=620,y=190)
    progressbarC.place(x=660,y=190)
    progressbarD.place(x=700,y=190)

    progressbarLableA.place(x=580,y=320)
    progressbarLableB.place(x=620,y=320)
    progressbarLableC.place(x=680,y=320)
    progressbarLableD.place(x=700,y=320)

    if questionArea.get(1.0,'end-1c')==questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)


    
questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

correct_answers = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "7:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]

root = Tk()
root.geometry('1270x652+0+0')
root.title('kon bane ga roadpati')
root.config(bg="black")





leftframe= Frame(root,bg='black',padx=90)
leftframe.grid(row=0,column=0)

topframe= Frame(leftframe,bg='black',pady=15)
topframe.grid()

centerframe= Frame(leftframe,bg='black',pady=15)
centerframe.grid(row=1,column=0)

bottomframe= Frame(leftframe)
bottomframe.grid(row=2,column=0)

rightframe= Frame(root,pady=25,padx=50,bg='black')
rightframe.grid(row=0,column=1)

image50=PhotoImage(file='50-50.png')
image50x=PhotoImage(file='50-50-x.png')

lifeline50Button =Button(topframe, image=image50,bg='black',bd=0,activebackground='black',width=180,height=180,command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole=PhotoImage(file='audiencePole.png')

audiencePoleButton =Button(topframe, image=audiencePole,bg='black',bd=0,activebackground='black',width=180,height=180,command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage=PhotoImage(file='phoneAFriend.png')

phoneLifeLineButton =Button(topframe, image=phoneImage,bg='black',bd=0,activebackground='black',width=180,height=180)
phoneLifeLineButton.grid(row=0, column=2)

centerImage=PhotoImage(file='center.png')

logoLabel =Label(centerframe, image=centerImage,bg='black',width=300,height=200)
logoLabel.grid(row=0, column=0)

amountimage=PhotoImage(file='Picture0.png')
amountimage1=PhotoImage(file='Picture1.png')
amountimage2=PhotoImage(file='Picture2.png')
amountimage3=PhotoImage(file='Picture3.png')
amountimage4=PhotoImage(file='Picture4.png')
amountimage5=PhotoImage(file='Picture5.png')
amountimage6=PhotoImage(file='Picture6.png')
amountimage7=PhotoImage(file='Picture7.png')
amountimage8=PhotoImage(file='Picture8.png')
amountimage9=PhotoImage(file='Picture9.png')
amountimage10=PhotoImage(file='Picture10.png')
amountimage11=PhotoImage(file='Picture11.png')
amountimage12=PhotoImage(file='Picture12.png')
amountimage13=PhotoImage(file='Picture13.png')
amountimage14=PhotoImage(file='Picture14.png')
amountimage15=PhotoImage(file='Picture15.png')

amountImages=[amountimage1,amountimage2,amountimage3,amountimage4,amountimage5,amountimage6,amountimage7,amountimage8,amountimage9,amountimage10,amountimage11,amountimage12,amountimage13,amountimage14,amountimage15]




amountLabel =Label(rightframe, image=amountimage,bg='black')
amountLabel.grid(row=0, column=0)

layoutImage=PhotoImage(file='lay.png')

layoutLabel =Label(bottomframe, image=layoutImage,bg='black')
layoutLabel.grid(row=0, column=0)

questionArea=Text(bottomframe,font=('arial',18,'bold'),width=34,height=2,wrap='word',bg='black',fg='white',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END, questions[0])

labelA=Label(bottomframe,text='A:',bg='black',fg='white',font=('arial',16,'bold'))
labelA.place(x=60, y=110)

optionButton1=Button(bottomframe,text=first_option[0],bg='black',bd=0,fg='white',font=('arial',18,'bold'),activebackground='black',activeforeground='white',cursor='hand2')
optionButton1.place(x=100, y=100)

labelB=Label(bottomframe,text='B:',bg='black',fg='white',font=('arial',16,'bold'))
labelB.place(x=330, y=110)

optionButton2=Button(bottomframe,text=second_option[0],bg='black',bd=0,fg='white',font=('arial',18,'bold'),activebackground='black',activeforeground='white',cursor='hand2')
optionButton2.place(x=370, y=100)

labelC=Label(bottomframe,text='C:',bg='black',fg='white',font=('arial',16,'bold'))
labelC.place(x=60, y=190)

optionButton3=Button(bottomframe,text=third_option[0],bg='black',bd=0,fg='white',font=('arial',18,'bold'),activebackground='black',activeforeground='white',cursor='hand2')
optionButton3.place(x=100, y=180)

labelD=Label(bottomframe,text='D:',bg='black',fg='white',font=('arial',16,'bold'))
labelD.place(x=330, y=190)

optionButton4=Button(bottomframe,text=fourth_option[0],bg='black',bd=0,fg='white',font=('arial',18,'bold'),activebackground='black',activeforeground='white',cursor='hand2')
optionButton4.place(x=370, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarB = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarC = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarD = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')


optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)















root.mainloop()

