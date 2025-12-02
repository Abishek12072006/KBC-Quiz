from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer

questions=['Which keyword is used to create an object in Java?','In Java, which keyword prevents a class from being subclassed?','Which Python data structure maintains insertion order starting from version 3.7?','Which of these is the default value of a boolean in Java?','Which of these is not a valid state of a Java thread?','In Python, what will list(range(2,10,2)) produce?','Which package is imported by default in every Java program?','What is the default access specifier for members of a C++ class?','Which Java collection guarantees that keys remain in sorted order?','In Python, which of the following is immutable?',
           'Which of these is a marker interface in Java?','Which of these is not a principle of Object-Oriented Programming?','In Java, which package contains the Stream API for functional-style operations?','What is the time complexity of accessing an element by index in a Python list?','Which C++11 feature allows functions to infer return type automatically?']
first_option=['new','static','dict','true','Runnable','[2,4,6,8,10]','util','public','HashMap','list','Cloneable','Abstraction',
              'java.sql','O(1)','decltype']
second_option=['this','final','set','false','Waiting','[2,4,6,8]','lang','internal','LinkedHashMap','set','Runnable','Polymorphism',
               'java.io','O(log n)','auto']
third_option=['void','const','frozenset','null','Running','[2,3,4,5,6,7,8,9]','io','protected','TreeMap','dict','Serializable','Recursion','java.util.stream','O(n)','constexpr']
fourth_option=['super','abstract','tuple','zero','Terminated','[2,6,10]','sql','private','EnumMap','tuple','Comparable','Encapsulation','java.lang','O(n log n)','template']
correct_answers=['new','final','dict','false','Running','[2,4,6,8]','lang','private','TreeMap','tuple','Cloneable','Recursion','java.util.stream','O(1)','auto']

root=Tk() #opens the window

# ----------------- FULLSCREEN -----------------
root.title("KBC")
root.config(bg="black")
root.attributes('-fullscreen', True)
# ---------------------------------------------

# Creating frames
left=Frame(root, bg="black", padx=90)
left.grid()
right=Frame(root, bg="black")
right.grid(row=0, column=1)
top=Frame(left, pady=15, bg="black")
top.grid()
center=Frame(left, pady=15, bg="black")
center.grid(row=1, column=0)
bottom=Frame(left, bg="black")
bottom.grid(row=2, column=0)

# ----------------- Lifeline -----------------
def lifeline50():
    lifeline50.config(image=new_imagex, state=DISABLED)
    q = QuestionSpace.get(1.0, "end-1c")
    if q==questions[0]: Option2.config(text=" "); Option4.config(text=" ")
    elif q==questions[1]: Option1.config(text=" "); Option3.config(text=" ")
    elif q==questions[2]: Option2.config(text=" "); Option3.config(text=" ")
    elif q==questions[3]: Option1.config(text=" "); Option4.config(text=" ")
    elif q==questions[4]: Option1.config(text=" "); Option4.config(text=" ")
    elif q==questions[5]: Option1.config(text=" "); Option3.config(text=" ")
    elif q==questions[6]: Option1.config(text=" "); Option3.config(text=" ")
    elif q==questions[7]: Option3.config(text=" "); Option2.config(text=" ")
    elif q==questions[8]: Option1.config(text=" "); Option4.config(text=" ")
    elif q==questions[9]: Option2.config(text=" "); Option3.config(text=" ")
    elif q==questions[10]: Option2.config(text=" "); Option3.config(text=" ")
    elif q==questions[11]: Option2.config(text=" "); Option4.config(text=" ")
    elif q==questions[12]: Option1.config(text=" "); Option2.config(text=" ")
    elif q==questions[13]: Option2.config(text=" "); Option3.config(text=" ")
    elif q==questions[14]: Option3.config(text=" "); Option4.config(text=" ")

img=(Image.open("50-50-lifeline.png"))
resized_image=img.resize((360,240))
new_image=ImageTk.PhotoImage(resized_image)
imgx=(Image.open("50-50-lifeline-removed.png"))
resized_imagex=imgx.resize((360,240))
new_imagex=ImageTk.PhotoImage(resized_imagex)
lifeline50=Button(top,image=new_image, bg="black", bd=0, activebackground="black", command=lifeline50)
lifeline50.grid(row=0, column=1)

# ----------------- Logo -----------------
Logo=(Image.open("kbc-logo.png"))
resized_Logo=Logo.resize((300,200))
new_Logo=ImageTk.PhotoImage(resized_Logo)
LogoLabel=Label(center, image=new_Logo, bg="black", activebackground="black")
LogoLabel.grid()

# ----------------- Money Ladder -----------------
Money=PhotoImage(file="Picture0.png")
MoneyImages=[PhotoImage(file=f"Picture{i}.png") for i in range(16)]
MoneyLabel=Label(right, image=MoneyImages[0], bg="black")
MoneyLabel.grid()

# ----------------- Layout -----------------
Layout=PhotoImage(file="lay.png")
LayoutLabel=Label(bottom, image=Layout, bg="black")
LayoutLabel.grid()

# ----------------- Questions -----------------
QuestionSpace=Text(bottom, font=('arial', 18, 'bold'), width=34, height=2, wrap="word", bg="black", fg="white", bd=0)
QuestionSpace.place(x=70, y=10)
QuestionSpace.insert(END, questions[0])

LabelA=Label(bottom, text="A: ", font=('arial', 16, 'bold'), bg="black", fg="white")
LabelA.place(x=60, y=110)
Option1=Button(bottom, text=first_option[0], font=('arial', 18, 'bold'), bg="black", fg="white", bd=0, activebackground="black")
Option1.place(x=90, y=100)

LabelB=Label(bottom, text="B: ", font=('arial', 16, 'bold'), bg="black", fg="white")
LabelB.place(x=330,y=110)
Option2=Button(bottom, text=second_option[0], font=('arial', 18, 'bold'), bg="black", fg="white", bd=0, activebackground="black")
Option2.place(x=360,y=100)

LabelC=Label(bottom, text="C: ", font=('arial', 16, 'bold'), bg="black", fg="white")
LabelC.place(x=60,y=190)
Option3=Button(bottom, text=third_option[0], font=('arial', 18, 'bold'), bg="black", fg="white", bd=0, activebackground="black")
Option3.place(x=90,y=180)

LabelD=Label(bottom, text="D: ", font=('arial', 16, 'bold'), bg="black", fg="white")
LabelD.place(x=330,y=190)
Option4=Button(bottom, text=fourth_option[0], font=('arial', 18, 'bold'), bg="black", fg="white", bd=0, activebackground="black")
Option4.place(x=360,y=180)

# ----------------- Answer Selection -----------------
def select(event):
    b=event.widget
    value=b['text']
    for i in range(15):
        if value==correct_answers[i]:
            if i==14:  # Last question
                def close():
                    root2.destroy()
                    root.destroy()
                    if mixer.music.get_busy(): mixer.music.stop()
                def playagain():
                    root2.destroy()
                    QuestionSpace.delete(1.0, END)
                    QuestionSpace.insert(END, questions[0])
                    Option1.config(text=first_option[0])
                    Option2.config(text=second_option[0])
                    Option3.config(text=third_option[0])
                    Option4.config(text=fourth_option[0])
                    MoneyLabel.config(image=MoneyImages[0])
                    if mixer.music.get_busy(): mixer.music.stop()
                    mixer.music.load("kbc.mp3")
                    mixer.music.play()
                # YOU WIN POPUP
                root2=Toplevel()
                root2.overrideredirect(True)
                root2.config(bg="white")
                root2.geometry('500x400+140+30')
                root2.title('Congratulations!')
                imgLabel=Label(root2, image=new_Logo, bd=0, bg="white")
                imgLabel.pack(pady=30)
                winLabel=Label(root2, text="YOU WIN!", font=('arial', 40, 'bold'), bg="white", fg="green")
                winLabel.pack(pady=20)
                playagainButton=Button(root2, text="Play Again", font=('arial', 20, 'bold'), bg="white", fg="black",
                                       bd=0, activebackground="white", activeforeground="black", cursor="hand2", command=playagain)
                playagainButton.pack(pady=10)
                closeButton=Button(root2, text="Close", font=('arial', 20, 'bold'), bg="white", fg="black",
                                   bd=0, activebackground="white", activeforeground="black", cursor="hand2", command=close)
                closeButton.pack(pady=10)
                root2.mainloop()
                break
            # Move to next question
            QuestionSpace.delete(1.0,END)
            QuestionSpace.insert(END, questions[i+1])
            Option1.config(text=first_option[i+1])
            Option2.config(text=second_option[i+1])
            Option3.config(text=third_option[i+1])
            Option4.config(text=fourth_option[i+1])
            MoneyLabel.config(image=MoneyImages[i+1])
        elif value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()
                if mixer.music.get_busy(): mixer.music.stop()
            def tryagain():
                lifeline50.config(state=NORMAL, image=new_image)
                root1.destroy()
                QuestionSpace.delete(1.0, END)
                QuestionSpace.insert(END, questions[0])
                Option1.config(text=first_option[0])
                Option2.config(text=second_option[0])
                Option3.config(text=third_option[0])
                Option4.config(text=fourth_option[0])
                MoneyLabel.config(image=MoneyImages[0])
                if mixer.music.get_busy(): mixer.music.stop()
                mixer.music.load("kbc.mp3")
                mixer.music.play()
            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg="white")
            root1.geometry('500x400+140+30')
            root1.title('You Lost')
            imgLabel=Label(root1, image=new_Logo, bd=0, bg="white")
            imgLabel.pack(pady=30)
            loseLabel=Label(root1, text="You Lose", font=('arial', 40, 'bold'), bg="white", fg="black")
            loseLabel.pack()
            tryagainButton=Button(root1, text="Try Again", font=('arial', 20, 'bold'), bg="white", fg="black", bd=0,
                                  activebackground="white", activeforeground="black", cursor="hand2", command=tryagain)
            tryagainButton.pack()
            closeButton=Button(root1, text="Close", font=('arial', 20, 'bold'), bg="white", fg="black", bd=0,
                                  activebackground="white", activeforeground="black", cursor="hand2", command=close)
            closeButton.pack()
            root1.mainloop()
            break

Option1.bind('<Button-1>', select)
Option2.bind('<Button-1>', select)
Option3.bind('<Button-1>', select)
Option4.bind('<Button-1>', select)

# ----------------- Music -----------------
mixer.init()
mixer.music.load("kbc.mp3")
mixer.music.play(-1)  # loop the music

root.mainloop()
