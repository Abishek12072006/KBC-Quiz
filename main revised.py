from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import random

questions1=['India has held the WCC how many times?', 'Who won the noble price in Economics,2023?',
           'Who is the only indian to win the Nobel prize in Economics?', 'Who awards the Nobel prize in Economics?',
           'The largest sugar mill in Asia is located in?', 'International Commonwealth Day is celebrated on',
           'The Maitree Express and Bandhan Express trains connect India with',
           'Which Minister presented the railway budget 6 times in a row?', 'The largest producer of Bauxite in the world is:',
           'Where is the Indian Railway Institute of Civil Engineering?', 'Which day is celebrated as World Suicide Prevention Day?',
           'National Science day in India is celebrated on:', 'Kudankulam Nuclear Power Plant is in:', 'National Youth Day is marked on',
           'Which of the following is our National Anthem?']
first_option1=['once', 'Claudia Gold', 'Abhijit Banerjee', 'Finland', 'Karnataka', '22 May',
              'Mynamar', 'John Mathai', 'U.S.A', 'Vadodara', '17 July', '30th April', 'Maharashtra', '12 January', 'Jana Gana Mana']
second_option1=['twice','Esther Duflo','Amartya', 'Norway',
               'UP','23 May','Pakistan','Lalu Prasad Yadav',' Jamaica','Jamalpur',
               '23 August','14 February','Kerala','9 January','Vandhematharam']
third_option1=['thrice','Oliver William','Raghuram Rajan','Sweden',
              'West Bengal','24 May','Nepal',' Nitish Kumar','Chile','Nasik',
              '9 September','28th February','Andhra Pradesh',
              '15 January','Sare jaha']
fourth_option1=['None','None','None','None',
               'Maharashtra','25 May','Bangladesh',' Mamata Banerjee',
               'Australia','Pune','10 September','23th March',
               'Tamilnadu','18 January','Jhanda Uncha Rahe']
correct_answers1=['once','Claudia Gold','Amartya','Sweden',
                 'UP','24 May','Bangladesh','Lalu Prasad Yadav','Australia',
                 'Pune','10 September','28th February','Tamilnadu','12 January','Jana Gana Mana']

questions2=['National Income estimates in India are prepared by', 'MS-Word is an example of','The staple food of the Vedic Aryan was',
            'Ctrl, Shift and Alt are called .......... keys.','The tropic of cancer does not pass through?','Fathometer is used to measure',
            'The purest form of iron is','The working principle of a washing machine is','A computer cannot "boot" if it does not have the',
            'Who is the author of the book "Freedom Behind Bars"?','Which river of India is called Vridha Ganga?','Which latitude passes through the middle of India?',
            'Hydrogen bomb is based on the principle of','Epsom(England) is the place associated with','Which country is closest to Andaman Islands']
first_option2=['Commission','An OS','Barley, Rice','modifier','MP','Earthquakes',
               'wrought iron','osmosis','Compiler','Kiran Bedi','Krishna','Equator','fission','Snooker','Sri Lanka']
second_option2=['RBI','processing','Milk products','function','West Bengal','Rainfall',
                'steel','diffusion','Loader','Nehru','Godavari','Arctic Circle','fusion','Shooting','Indonesia']
third_option2=['CSO','Application','Rice, Pulses','alphanumeric','Rajasthan','Ocean depth',
               'pig iron','centrifuge','OS','Mandela','Kaveri','Tropic Capricorn','radioactivity','Polo','Myanmar']
fourth_option2=['ISI','input device','Vegies, Fruits','adjustment','Odisha','Sound intense',
                'nickel steel','dialysis','Assembler','Abdullah','Narmada','Tropic Cancer','alpha ray','Horse Racing','Pakistan']
correct_answers2=['CSO','Application','Milk products','modifier','Odisha','Ocean depth',
                  'wrought iron','centrifuge','OS','Kiran Bedi','Godavari','Tropic Cancer','fusion','Horse Racing','Myanmar']

questions3=['The purest form of iron is','Hydrogen bomb is based on',
            'Maximum covalent character is shown by','SI unit of equivalent conductance',
            'A non-metal that remains liquid at room temperature','Silver Mirror test is given by:',
            'Which is not a mixture','Which pair has the highest electronegativity difference?',
            'Among the given nutrients, milk is a poor source of','A "breath test" used by traffic police to check drunken driving uses:',
            'Brass gets discoloured in air because of:','What is the structure of IF7?',
            'which of the following are chemical changes?','Formaldehyde and Potassium Hydroxide heated gives:',
            'Who stated that matter can be converted into energy']
first_option3=['wrought iron','fusion','MgCl2','ohm/cm','Chlorine','Benzophenone','Air','F-F','Calcium','Turmeric',
               'H2S','Triagonal','Cooking Food','Acetylene','Avogadro']
second_option3=['steel','alpha rays','FeCl2','Siemens m2','Bromine','Acetaldehyde','Mercury','Ca-F','Starch',
                'Silica gel','Nitrogen','Pentagonal','Water heated','Methane','Lavoisier']
third_option3=['Pig iron','radioactivity','SnCl2','Siemens','Iodine','Acetone','Cement','Na-F','Carbohydrates',
               'KMnO4+H2SO4','Oxygen','Tetrahedral','None','CH3OH','Einstein']
fourth_option3=['nickel steel','fission','AlCl3','mho/cm','Helium','Ethane','Milk','H-F','Vitamin-C','KCr2(SO4)',
                'Carbon','Square','Freezing of water','Ethyl formate','Boyle']
correct_answers3=['wrought iron','fusion','AlCl3','Siemens m2','Bromine','Acetaldehyde','Mercury','Na-F','Vitamin-C',
                  'KCr2(SO4)','H2S','Pentagonal','Cooking Food','CH3OH','Einstein']

questions4=['The green planet in the solar system is?','The largest public sector undertakingis',
            'At which place on Earth are the days and nights equal?','What is the pH value of the human body?',
            'What kind of government does India have?','When is National Science Day observed?','What is the colour of light related to?',
            'The International Monetary Fund is headquartered at?','The largest lake on earthis:',
            'Microphone is a device that transforms','X-rays region lies between','Which is the largest river in the world?',
            'When is international yoga day celebrated?','Who is the current Finance Minister of India?','Which city is known as the forbidden city?']
first_option4=['Mars','Railways','Equator','9.2-9.8','Monarchy','July 12th','Wavelength','New York','Lake Ladogo','sound-current',
               'UV, visible','Amazon River','June 23rd','Mr. Modi','Lhasa']
second_option4=['Earth','Airways','Poles','7.0-7.8','Oligarchy','September 13th','Frequency','W DC','Lake Erie',
                'current-sound','visible, IR','River Ganges','June 21st','Ms. Seth','Rome']
third_option4=['Uranus','Roadways','Prime Meridian','6.1-6.3','Aristrocracy','February 28th','Quality','London','Dal Lake','sound-light',
               'Gamma, UV','Yellow River','November 29th','Ms. Nirmala','Ome']
fourth_option4=['Venus','Iron and Steel','Nowhere','5.4-5.6','Democracy','July 28th','Velocity','Tokyo','Caspian Sea',
                'light-sound','radio','River Nile','February 7th','Ms. Sathyanarayanan','Hawang Ho']
correct_answers4=['Uranus','Railways','Equator','7.0-7.8','Democracy','February 28th','Wavelength','W DC','Caspian Sea',
                  'sound-current','Gamma, UV','River Nile','June 21st','Ms. Nirmala','Lhasa']

z=random.randint(1,4)
if z==1:
    questions=questions1
    first_option=first_option1
    second_option=second_option1
    third_option=third_option1
    fourth_option=fourth_option1
    correct_answers=correct_answers1
elif z==2:
    questions=questions2
    first_option=first_option2
    second_option=second_option2
    third_option=third_option2
    fourth_option=fourth_option2
    correct_answers=correct_answers2
elif z==3:
    questions=questions3
    first_option=first_option3
    second_option=second_option3
    third_option=third_option3
    fourth_option=fourth_option3
    correct_answers=correct_answers3
elif z==4:
    questions=questions4
    first_option=first_option4
    second_option=second_option4
    third_option=third_option4
    fourth_option=fourth_option4
    correct_answers=correct_answers4

root=Tk() #opens the window

root.geometry("1270x652+0+0")
root.title("KBC")
root.config(bg="black")

#creating frames (a left frame and a right frame, then all the lifelines and questions and stuff as top center and bottom in the left frame)
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

def lifeline50():
    lifeline50.config(image=new_imagex, state=DISABLED)
    if QuestionSpace.get(1.0, "end-1c")==questions[0]:
        Option2.config(text=" ")
        Option4.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[1]:
        Option2.config(text=" ")
        Option3.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[2]:
        Option1.config(text=" ")
        Option3.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[3]:
        Option2.config(text=" ")
        Option4.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[4]:
        Option1.config(text=" ")
        Option4.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[5]:
        Option1.config(text=" ")
        Option2.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[6]:
        Option1.config(text=" ")
        Option2.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[7]:
        Option3.config(text=" ")
        Option4.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[8]:
        Option1.config(text=" ")
        Option3.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[9]:
        Option2.config(text=" ")
        Option3.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[10]:
        Option2.config(text=" ")
        Option3.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[11]:
        Option2.config(text=" ")
        Option4.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[12]:
        Option1.config(text=" ")
        Option3.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[13]:
        Option2.config(text=" ")
        Option3.config(text=" ")
    if QuestionSpace.get(1.0, "end-1c")==questions[14]:
        Option2.config(text=" ")
        Option4.config(text=" ")

img=(Image.open("50-50-lifeline.png"))
resized_image=img.resize((180,120))
new_image=ImageTk.PhotoImage(resized_image)
imgx=(Image.open("50-50-lifeline-removed.png"))
resized_imagex=imgx.resize((180,120))
new_imagex=ImageTk.PhotoImage(resized_imagex)
lifeline50=Button(top,image=new_image, bg="black", bd=0, activebackground="black", command=lifeline50)
lifeline50.grid(row=0, column=1)

Logo=(Image.open("kbc-logo.png"))
resized_Logo=Logo.resize((300,200))
new_Logo=ImageTk.PhotoImage(resized_Logo)
LogoLabel=Label(center, image=new_Logo, bg="black", activebackground="black")
LogoLabel.grid()

Money=PhotoImage(file="Picture0.png")
Money1=PhotoImage(file="Picture1.png")
Money2=PhotoImage(file="Picture2.png")
Money3=PhotoImage(file="Picture3.png")
Money4=PhotoImage(file="Picture4.png")
Money5=PhotoImage(file="Picture5.png")
Money6=PhotoImage(file="Picture6.png")
Money7=PhotoImage(file="Picture7.png")
Money8=PhotoImage(file="Picture8.png")
Money9=PhotoImage(file="Picture9.png")
Money10=PhotoImage(file="Picture10.png")
Money11=PhotoImage(file="Picture11.png")
Money12=PhotoImage(file="Picture12.png")
Money13=PhotoImage(file="Picture13.png")
Money14=PhotoImage(file="Picture14.png")
Money15=PhotoImage(file="Picture15.png")

MoneyImages=[Money, Money1, Money2, Money3, Money4, Money5, Money6, Money7, Money8, Money9, Money10, Money11, Money12, Money13, Money14, Money15]

MoneyLabel=Label(right, image=Money, bg="black")
MoneyLabel.grid()

Layout=PhotoImage(file="lay.png")
LayoutLabel=Label(bottom, image=Layout, bg="black")
LayoutLabel.grid()

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

#the reason we have to give argument "event" is because when we click on something we get some value, so that value has to be defined
def select(event):
    b=event.widget
    value=b['text']
    for i in range(15):
        if value==correct_answers[i]:
            if value==correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()
                    if mixer.music.get_busy(): mixer.music.stop()
                def playagain():
                    global z
                    global questions
                    global first_option
                    global second_option
                    global third_option
                    global fourth_option
                    global correct_answers
                    if z==1:
                        z=2
                        questions=questions2
                        first_option=first_option2
                        second_option=second_option2
                        third_option=third_option2
                        fourth_option=fourth_option2
                        correct_answers=correct_answers2
                    elif z==2:
                        z=3
                        questions=questions3
                        first_option=first_option3
                        second_option=second_option3
                        third_option=third_option3
                        fourth_option=fourth_option3
                        correct_answers=correct_answers3
                    elif z==3:
                        z=4
                        questions=questions4
                        first_option=first_option4
                        second_option=second_option4
                        third_option=third_option4
                        fourth_option=fourth_option4
                        correct_answers=correct_answers4
                    elif z==4:
                        z=1
                        questions=questions1
                        first_option=first_option1
                        second_option=second_option1
                        third_option=third_option1
                        fourth_option=fourth_option1
                        correct_answers=correct_answers1
                        
                    root2.destroy()
                    if mixer.music.get_busy():
                        mixer.music.stop()

                    QuestionSpace.delete(1.0, END)
                    QuestionSpace.insert(END, questions[0])
                    Option1.config(text=first_option[0])
                    Option2.config(text=second_option[0])
                    Option3.config(text=third_option[0])
                    Option4.config(text=fourth_option[0])
                    MoneyLabel.config(image=MoneyImages[0])

                    if mixer.music.get_busy():
                        mixer.music.stop()

                    mixer.music.load("kbc.mp3")
                    mixer.music.play()

                
                root2=Toplevel()
                root2.overrideredirect(True)
                root2.config(bg="white")
                root2.geometry('500x400+140+30')
                root2.title('You Lost')
                imgLabel=Label(root2, image=new_Logo, bd=0, bg="white")
                imgLabel.pack(pady=30)

                winLabel=Label(root2, text="You Won", font=('arial', 40, 'bold'), bg="white", fg="black")
                winLabel.pack()
                playagainButton=Button(root2, text="Play Again", font=('arial', 20, 'bold'), bg="white", fg="black", bd=0, activebackground="white", activeforeground="black",
                                      cursor="hand2", command=playagain)
                playagainButton.pack()
                closeButton=Button(root2, text="Close", font=('arial', 20, 'bold'), bg="white", fg="black", bd=0, activebackground="white", activeforeground="black",
                                      cursor="hand2", command=close)
                closeButton.pack()
                
                root2.mainloop()
                break #we run the loop 15 times so if we don't break we'll get many windows

            QuestionSpace.delete(1.0,END)
            QuestionSpace.insert(END, questions[i+1])
            Option1.config(text=first_option[i+1])
            Option2.config(text=second_option[i+1])
            Option3.config(text=third_option[i+1])
            Option4.config(text=fourth_option[i+1])
            MoneyLabel.config(image=MoneyImages[i+1])
        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()
                if mixer.music.get_busy(): mixer.music.stop()
            def tryagain():
                global z
                global questions
                global first_option
                global second_option
                global third_option
                global fourth_option
                global correct_answers
                if z==1:
                    z=2
                    questions=questions2
                    first_option=first_option2
                    second_option=second_option2
                    third_option=third_option2
                    fourth_option=fourth_option2
                    correct_answers=correct_answers2
                elif z==2:
                    z=3
                    questions=questions3
                    first_option=first_option3
                    second_option=second_option3
                    third_option=third_option3
                    fourth_option=fourth_option3
                    correct_answers=correct_answers3
                elif z==3:
                    z=4
                    questions=questions4
                    first_option=first_option4
                    second_option=second_option4
                    third_option=third_option4
                    fourth_option=fourth_option4
                    correct_answers=correct_answers4
                elif z==4:
                    z=1
                    questions=questions1
                    first_option=first_option1
                    second_option=second_option1
                    third_option=third_option1
                    fourth_option=fourth_option1
                    correct_answers=correct_answers1
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
            tryagainButton=Button(root1, text="Try Again", font=('arial', 20, 'bold'), bg="white", fg="black", bd=0, activebackground="white", activeforeground="black",
                                  cursor="hand2", command=tryagain)
            tryagainButton.pack()
            closeButton=Button(root1, text="Close", font=('arial', 20, 'bold'), bg="white", fg="black", bd=0, activebackground="white", activeforeground="black",
                                  cursor="hand2", command=close)
            closeButton.pack()
            
            root1.mainloop()
            break #we run the loop 15 times so if we don't break we'll get many windows

Option1.bind('<Button-1>', select)
Option2.bind('<Button-1>', select)
Option3.bind('<Button-1>', select)
Option4.bind('<Button-1>', select)
#<Button-1> represents left click, you're binding it to the select function that we defined above

mixer.init()
mixer.music.load("kbc.mp3")
mixer.music.play()
while mixer.music.get_busy():
    root.update()
if mixer.music.get_busy(): mixer.music.stop()

root.mainloop() #the previous command will just open and close it instantly, this keeps it open
