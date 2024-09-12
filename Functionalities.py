from tkinter import *
import tkinter

def Search():
    root1 = Toplevel()
    root1.geometry('700x700')
    root1.configure(bg='#1a1d1e')
    search_bar = Entry(root1)
    search_bar.place(x=250,y=70,width=200)
    b0=Button(root1,text='<- Back',command=root1.destroy,bg='#444442',fg='#ffffff').grid(row=1,column=1)
    mylabel1 = Label(root1,text="Search Tool",bg='#1a1d1e',fg='#ffffff',font="comicsans 26 bold").place(x=247,y=0)
    mylabel2 = Label(root1,text="Chords and Scales",bg='#1a1d1e',fg='#ffffff',font="comicsans 10 bold").place(x=285,y=35)
    
    from PIL import ImageTk,Image
    global img
    img = Label(root1,width=700,bg='#1a1d1e')
    img.place(x=0,y=125)

    from tkinter import messagebox
    
    def clicked():
        search_text=search_bar.get()
        query = search_text.split(" ")
        
        chord_type_list = ['M','5','7','maj7','m7','sus2','sus4','add9','9','_m']
        d={'Bb':'A#','Db':'C#','Eb':'D#','Gb':'F#','Ab':'G#'}

        try:
            type_query=query[2].lower()
            if query[0] not in ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','Bb','Db','Eb','Gb','Ab']:
                messagebox.askretrycancel("Try Again!!", "Chord Name is Wrong!!")            
            elif type_query=='chord':
                if query[1] not in chord_type_list:
                    messagebox.askretrycancel("Try Again!!", "Chord Type Doesn't Exist!!")
                else:
                    if query[0] in d.keys():
                        chord_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Chords/{d[query[0]]+query[1]}.png"))
                        img.configure(image=chord_img)
                        img.image = chord_img
                    elif query[1]=='_m':
                        chord_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Chords/{query[0]+'_m'}.png"))
                        img.configure(image=chord_img)
                        img.image = chord_img
                    elif query[0] in d.keys() and query[1]=='_m':
                        chord_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Chords/{d[query[0]]+'_m'}.png"))
                        img.configure(image=chord_img)
                        img.image = chord_img
                    else:
                        chord_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Chords/{query[0]+query[1]}.png"))
                        img.configure(image=chord_img)
                        img.image = chord_img
            elif type_query=='scale':
                if query[1] in ['5','7','maj7','m7','sus2','sus4','add9','9']:
                    messagebox.showinfo("Important Message!!", "Scale Type not included in Database")
                elif query[1] not in ['M','5','7','maj7','m7','sus2','sus4','add9','9','_m']:
                    messagebox.askretrycancel("Try Again!!", "Scale Type doesn't Exist!!")
                else:
                    if query[0] in d.keys():
                        scale_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Scales/{d[query[0]]+query[1]}.png"))
                        img.configure(image=scale_img)
                        img.image = scale_img
                    elif query[1]=='_m':
                        scale_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Scales/{query[0]+'_m'}.png"))
                        img.configure(image=scale_img)
                        img.image = scale_img
                    elif query[0] in d.keys() and query[1]=='_m':
                        scale_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Scales/{d[query[0]]+'_m'}.png"))
                        img.configure(image=scale_img)
                        img.image = scale_img
                    else:
                        scale_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Scales/{query[0]+query[1]}.png"))
                        img.configure(image=scale_img)
                        img.image = scale_img
            else:
                messagebox.askretrycancel("Try Again!!", "Didn't Specify chord or scale!!")
        except IndexError:
            messagebox.askretrycancel("Try Again!!", "Didn't leave Space!!")
    search_button = Button(root1,text='Search',command=clicked,width=15,height=1,bg='#444442',fg='#ffffff').place(x=290,y=100)
    instruction_label = Label(root1,text='Instruction:\nChord_Name   Chord_type   Chord/Scale\nLeave Space between these three Keywords',bg='#1a1d1e',fg='#ffffff',font="comicsans 8",justify='left').place(x=0,y=70)

def Introduction():
    root1 = Toplevel()
    root1.geometry('700x700')
    root1.configure(bg='#1a1d1e')

    b0=Button(root1,text='<- Back',command=root1.destroy,bg='#444442',fg='#ffffff').place(x=0,y=0)
    mylabel = Label(root1,text="Introduction",fg='#ffffff', bg='#1a1d1e',font="comicsans 26 bold").place(x=247,y=25)

    mylabel1 = Label(root1, text="A guitar is a stringed musical instrument with a typically wooden body and six strings. It is played by plucking or strumming the strings, and the pitch of the sound is controlled by pressing the strings against frets on the neck. Guitars are versatile instruments used in various music genres.", fg='#ffffff', bg='#1a1d1e',justify='left',pady=8,wraplength=700,font="comicsans 13",anchor="w")
    mylabel1.place(x=0,y=75)

    from PIL import ImageTk,Image
    global img
    img = Label(root1,width=700,bg='#1a1d1e')
    img.place(x=0,y=170)

    chord_img =ImageTk.PhotoImage(Image.open("E:/Coding Folder/GuitHub/guitar_intro3.png"))
    img.configure(image=chord_img)
    img.image = chord_img

    mylabel2 = Label(root1, text="Parts of the Guitar:\nBody: The main part of the guitar.\nNeck: Extends from the body and holds the fretboard.\nFretboard: The flat surface where you press down on the strings to change the pitch.\nFrets: Metal strips on the fretboard that divide it into segments.\nHeadstock: The top section of the guitar where the tuning pegs are located.\nTuning Pegs: Used to adjust the tension of the strings, affecting their pitch.\n\nTypes of Guitars:\nAcoustic Guitar: Produces sound acoustically without the need for an amplifier.\nElectric Guitar: Requires an amplifier to produce sound, often used in rock and pop music.\n\nTuning:\nLearn how to tune your guitar. Standard tuning for a six-string guitar from low to high is E, A, D, G, B, E.", fg='#ffffff', bg='#1a1d1e',justify='left',pady=8,wraplength=700,font="comicsans 13",anchor="w")
    mylabel2.place(x=0,y=400)

def IT():
    from tkinter import Toplevel, Scrollbar, Text, Button, Y

    root1 = Toplevel()
    root1.geometry('700x700')
    root1.configure(bg='#1a1d1e')

    scrollbar = Scrollbar(root1)
    scrollbar.pack(side=RIGHT, fill=Y)

    b0 = Button(root1, text='<- Back', command=root1.destroy, bg='#444442', fg='#ffffff')
    b0.place(x=0, y=0)

    mylabel = Label(root1, text="Interval Theory", fg='#ffffff', bg='#1a1d1e', font="comicsans 26 bold")
    mylabel.place(x=220, y=25)

    mytext = Text(root1, wrap="word", fg='#ffffff', bg='#1a1d1e', font="comicsans 13", height=31, width=73)
    mytext.insert("10.0", """In music theory, an interval is a difference in pitch between two sounds. An interval may be described as horizontal, linear, or melodic if it refers to successively sounding tones, such as two adjacent pitches in a melody, and vertical or harmonic if it pertains to simultaneously sounding tones, such as in a chord. In physical terms, an interval is the ratio between two sonic frequencies. For example, any two notes an octave apart have a frequency ratio of 2:1. This means that successive increments of pitch by the same interval result in an exponential increase of frequency, even though the human ear perceives this as a linear increase in pitch. For this reason, intervals are often measured in cents, a unit derived from the logarithm of the frequency ratio.\n\nSize:\nThe size of an interval (also known as its width or height) can be represented using two alternative and equivalently valid methods, each appropriate to a different context: frequency ratios or cents.\n1. Frequency ratios - The size of an interval between two notes may be measured by the ratio of their frequencies.\n2. Cents - The standard system for comparing interval sizes is with cents.\n\nMain intervals:\nBelow Listed are some Main intervals:\n1. Perfect unison\n2. Minor second\n3. Major second\n4. Minor third\n5. Major third\n6. Perfect fourth\n\nInterval Number and Quality:\n1. Number - The number of an interval is the number of letter names or staff positions (lines and spaces) it encompasses, including the positions of both notes forming the interval. Intervals with larger numbers are called compound intervals. There is a one-to-one correspondence between staff positions and diatonic-scale degrees (the notes of diatonic scale). This means that interval numbers can also be determined by counting diatonic scale degrees, rather than staff positions, provided that the two notes that form the interval are drawn from a diatonic scale. Namely, C–G is a fifth because in any diatonic scale that contains C and G, the sequence from C to G includes five notes. For instance, in the A♭-major diatonic scale, the five notes are C–D♭–E♭–F–G (see figure). This is not true for all kinds of scales. For instance, in a chromatic scale, the notes from C to G are eight (C–C♯–D–D♯–E–F–F♯–G). This is the reason interval numbers are also called diatonic numbers, and this convention is called diatonic numbering.\n2. Quality - The name of any interval is further qualified using the terms perfect (P), major (M), minor (m), augmented (A), and diminished (d). This is called its interval quality. It is possible to have doubly diminished and doubly augmented intervals, but these are quite rare, as they occur only in chromatic contexts. The quality of a compound interval is the quality of the simple interval on which it is based. Some other qualifiers like neutral, subminor, and supermajor are used for non-diatonic intervals.\n\nShorthand Notation:\nIntervals are often abbreviated with a P for perfect, m for minor, M for major, d for diminished, A for augmented, followed by the interval number. The indications M and P are often omitted. The octave is P8, and a unison is usually referred to simply as a 'unison' but can be labeled P1. The tritone, an augmented fourth or diminished fifth is often TT. The interval qualities may be also abbreviated with perf, min, maj, dim, aug.\n\nInversion:\nA simple interval (i.e., an interval smaller than or equal to an octave) may be inverted by raising the lower pitch an octave or lowering the upper pitch an octave. There are two rules to determine the number and quality of the inversion of any simple interval:\n1. The interval number and the number of its inversion always add up to nine (4 + 5 = 9, in the example just given).\n2. The inversion of a major interval is a minor interval, and vice versa; the inversion of a perfect interval is also perfect; the inversion of an augmented interval is a diminished interval, and vice versa; the inversion of a doubly augmented interval is a doubly diminished interval, and vice versa.\n\nClassification:\n1. Minute intervals - There are also a number of minute intervals not found in the chromatic scale or labeled with a diatonic function, which have names of their own. They may be described as microtones, and some of them can be also classified as commas, as they describe small discrepancies, observed in some tuning systems, between enharmonically equivalent notes.\n2. Compound intervals - A compound interval is an interval spanning more than one octave. Conversely, intervals spanning at most one octave are called simple intervals (see Main intervals below).""")
    mytext.place(x=10, y=90)

    mytext.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=mytext.yview)

def CC():
    root1 = Toplevel()
    root1.geometry('700x700')
    root1.configure(bg='#1a1d1e')
    b0=Button(root1,text='<- Back',command=root1.destroy,bg='#444442',fg='#ffffff').grid(row=1,column=1)
    mylabel = Label(root1,text="Chord Classifications",fg='#ffffff', bg='#1a1d1e', font="comicsans 26 bold")
    mylabel.place(x=175, y=25)
    mylabel1 = Label(root1,text="1. Major Chords -\nA major chord contains a root, major third, and a perfect fifth and is considered to sound quite upbeat or happy.\n\n2. Minor Chords -\nA minor chord contains a root, minor third, and a perfect fifth and is considered to sound quite melancholic or sad.\n\n3. Diminished Chords -\nA diminished triad uses two minor 3rd intervals stacked on top of each other. For a full diminished add another minor 3rd interval on top.\n\n4. Augmented Chords -\nAn augmented chord is where you start with a major chord and raise the fifth by a semitone.",justify='left',pady=8,wraplength=700,bg='#1a1d1e',fg="white",font="comicsans 13",anchor="w")
    mylabel1.place(x=0,y=75)
    
    from tkinter import ttk
    tree = ttk.Treeview(root1, columns=("Chord", "Formula", "Example"), show="headings")
    tree.heading("Chord", text="Chord")
    tree.heading("Formula", text="Formula")
    tree.heading("Example", text="Example")

    data = [
        ("Major", "1, 3, 5", "C Maj - C E G"),
        ("Minor", "1, b3, 5", "C min - C Eb G"),
        ("Dimnished", "1, b3, b5", "C Dim - C Eb Gb"),
        ("Augmented", "1, 3, #5", "C Aug - C E G#")
    ]

    for row in data:
        tree.insert("", "end", values=row)

    tree.column("Chord", width=100)
    tree.column("Formula", width=100)
    tree.column("Example", width=120)
    tree.place(x=200, y=450)
    
def CC_7():
    root1 = Toplevel()
    root1.geometry('700x700')
    root1.configure(bg='#1a1d1e')
    b0=Button(root1,text='<- Back',command=root1.destroy,bg='#444442',fg='#ffffff').place(x=0,y=0)

    mylabel = Label(root1,text="7th Chord Classification",bg='#1a1d1e',fg="white",font="comicsans 26 bold").place(x=150,y=25)
    mylabel1=Label(root1,text="A seventh chord is a chord consisting of a triad plus a note forming an interval of a seventh above the chord's root. When not otherwise specified, a seventh chord usually means a dominant seventh chord: a major triad together with a minor seventh. The most common chords are tertian, constructed using a sequence of major thirds (spanning 4 semitones) and/or minor thirds (3 semitones). Since there are 3 third intervals in a seventh chord (4 notes) and each can be major or minor, there are 8 possible combinations. The five commonly found in western music are the major seventh, the minor (or minor/minor) seventh, the dominant (or major/minor) seventh, the half-diminished seventh, and the diminished seventh. The less commonly found tertian is the minor/major seventh.",justify='left',pady=8,wraplength=700,bg='#1a1d1e',fg="white",font="comicsans 13",anchor="w").place(x=0,y=75)
    mylabel2=Label(root1,text="While the dominant seventh chord is typically built on the fifth (or dominant) degree of a major scale, the minor seventh chord is built on the second, third, or sixth degree. A minor seventh chord contains the same notes as an added sixth chord. For example, C–E♭–G–B♭ can function as both a C minor seventh and an E♭ added sixth .Major seventh chords are usually constructed on the first or fourth degree of a scale, (in C or G major: C–E–G–B). Due to the major seventh interval between the root and seventh (C–B, an inverted minor second), this chord can sometimes sound dissonant, depending on the voicing used.",justify='left',wraplength=700,pady=8,bg='#1a1d1e',fg="white",font="comicsans 13").place(x=0,y=270)

    from tkinter import ttk
    tree = ttk.Treeview(root1, columns=("Chord", "Formula", "Example"), show="headings")
    tree.heading("Chord", text="Chord")
    tree.heading("Formula", text="Formula")
    tree.heading("Example", text="Example")

    data = [
        ("Major 7", "1, 3, 5, 7", "C Maj7 - C E G B"),
        ("Minor 7", "1, b3, 5, b7", "C min7 - C Eb G Bb"),
        ("Min Maj 7", "1, b3, 5, 7", "C Dim7 - C Eb G B"),
        ("Dominant 7/ 7", "1, 3, 5, b7", "C Dom7/ 7 - C E G Bb")
    ]

    for row in data:
        tree.insert("", "end", values=row)

    tree.column("Chord", width=100)
    tree.column("Formula", width=100)
    tree.column("Example", width=120)
    tree.place(x=190, y=450)

def CC_9():
    root1 = Toplevel()
    root1.geometry('700x700')
    root1.configure(bg='#1a1d1e')
    b0=Button(root1,text='<- Back',command=root1.destroy,bg='#444442',fg='#ffffff').place(x=0,y=0)
    mylabel = Label(root1,text="9th Chord Classification",bg='#1a1d1e',fg="white",font="comicsans 26 bold").place(x=150,y=50)
    mylabel1=Label(root1,text="A ninth chord is a seventh chord with one extra note added. That note is called the 9th—which is the same thing as the 2nd scale degree, only an octave higher. In the key of C, the 2nd scale degree is D. Therefore, the 9th scale degree is also D. When you see the chord symbol C9, that means you should play the notes C - E - G - Bb - D.A minor ninth chord is just like a ninth chord, only it’s based on a minor triad. C minor ninth is written as Cm9 or C-9, and its notes are C - Eb - G - Bb - D.",bg='#1a1d1e',wraplength=700,fg="white",pady=8,anchor="w",font="comicsans 13",justify="left").place(x=0,y=125)
    mylabel2=Label(root1,text="The ninth chord could be alternatively notated as seventh added second chord (C7add2), from where omitting the 3rd produces the seventh suspended second chord (C7sus2).An added ninth chord is a major triad with an added ninth – Cadd9 consists of C, E, G and D. Added ninth chords differ from other ninth chords because the seventh is not included.",justify="left",wraplength=700,fg="white",pady=8,anchor="w",font="comicsans 13",bg='#1a1d1e').place(x=0,y=250)

    from tkinter import ttk
    tree = ttk.Treeview(root1, columns=("Chord", "Formula", "Example"), show="headings")
    tree.heading("Chord", text="Chord")
    tree.heading("Formula", text="Formula")
    tree.heading("Example", text="Example")

    data = [
        ("Major 9", "1, 3, 7, 9", "C Maj9 - C E B D"),
        ("Minor 9", "1, 5, b7, 9", "C min9 - C G Bb D"),
        ("Min Maj 9", "1, 3, b7, 9", "C Dim9 - C E Bb D"),
        ("Dominant 9/ 9", "1, 5, 7, 9", "C Dom9/ 9 - C G B D")
    ]

    for row in data:
        tree.insert("", "end", values=row)

    tree.column("Chord", width=100)
    tree.column("Formula", width=100)
    tree.column("Example", width=120)
    tree.place(x=190, y=370)

def CC_11():
    root1 = Toplevel()
    root1.geometry('700x700')
    root1.configure(bg='#1a1d1e')
    b0=Button(root1,text='<- Back',command=root1.destroy,bg='#444442',fg='#ffffff').grid(row=0,column=10)
    mylabel = Label(root1,text="11th Chord Classification",fg="white",font="comicsans 26 bold", bg='#1a1d1e').place(x=150,y=25)
    mylabel1=Label(root1,text="In music theory, an eleventh chord is a chord that contains the tertian extension of the eleventh. Typically found in jazz, an eleventh chord also usually includes the seventh and ninth, and elements of the basic triad structure. Variants include the dominant eleventh (C11, C–E–G–B♭–D–F), minor eleventh (Cm11, C–E♭–G–B♭–D–F), and major eleventh chord (Cmaj11, C–E–G–B–D–F).[1] Using an augmented eleventh produces the dominant sharp eleventh (C9♯11, C–E–G–B♭–D–F♯) and major sharp eleventh (Cmaj9♯11, C–E–G–B–D–F♯) chords.",justify="left",bg='#1a1d1e',wraplength=700,fg="white",pady=8,anchor="w",font="comicsans 13").place(x=0,y=70)
    mylabel2=Label(root1,text="A perfect eleventh creates a highly dissonant minor ninth interval with the major third of major and dominant chords.As its upper extensions (7th, 9th, 11th) constitute a triad, a dominant eleventh chord with the third and fifth omitted can be notated as a compound chord with a bass note. So C–B♭–D–F is written as B♭/C, emphasizing the ambiguous dominant/subdominant character of this voicing.",justify="left",wraplength=700,fg="white",pady=8,anchor="w",font="comicsans 13",bg='#1a1d1e').place(x=0,y=220)

    from tkinter import ttk
    tree = ttk.Treeview(root1, columns=("Chord", "Formula", "Example"), show="headings")
    tree.heading("Chord", text="Chord")
    tree.heading("Formula", text="Formula")
    tree.heading("Example", text="Example")

    data = [
        ("Major 11", "1, 3, 7, 11", "C Maj11 - C E B D"),
        ("Minor 11", "1, 5, b7, 11", "C min11 - C G Bb D"),
        ("Min Maj 11", "1, 3, b7, 11", "C Dim11 - C E Bb D"),
        ("Dominant 11/ 11", "1, 5, 7, 11", "C Dom11/ 11 - C G B D")
    ]

    for row in data:
        tree.insert("", "end", values=row)

    tree.column("Chord", width=100)
    tree.column("Formula", width=100)
    tree.column("Example", width=150)
    tree.place(x=190, y=330)

def CL():
    root1 = Toplevel()
    root1.geometry('700x700')
    root1.configure(bg='#1a1d1e')
    b0=Button(root1,text='<- Back',command=root1.destroy,bg='#444442',fg='#ffffff').place(x=0,y=0)
    mylabel = Label(root1,text="Chord Library",bg='#1a1d1e',fg='#ffffff',font="comicsans 20 bold").place(x=240,y=0)
    
    chord_list = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    chord_type_list = ['M','m','5','7','maj7','m7','sus2','sus4','add9','9']
    chord_nota = ['#','b']

    chord_menu= StringVar()
    chord_menu.set("Select Chord")
    drop_chord= OptionMenu(root1, chord_menu,*chord_list)
    drop_chord.config(width=15,bg='#444442',fg='#ffffff')
    drop_chord.place(x=0,y=50)

    chord_type_menu= StringVar()
    chord_type_menu.set("Select Chord Type")
    drop_chord_type= OptionMenu(root1, chord_type_menu,*chord_type_list)
    drop_chord_type.config(width=15,bg='#444442',fg='#ffffff')
    drop_chord_type.place(x=195,y=50)

    def change_note(dummy=None):
        global chord_list
        selected_nota = chord_nota_menu.get()
        if selected_nota == "#":
            chord_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        elif selected_nota == "b":
            chord_list = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        else:
            print('Could not update')
        
        drop_chord['menu'].delete(0, 'end')
        for chord in chord_list:
            drop_chord['menu'].add_command(label=chord, command=tkinter._setit(chord_menu, chord))

    chord_nota_menu= StringVar()
    chord_nota_menu.set("#")
    drop_nota_type= OptionMenu(root1, chord_nota_menu,*chord_nota,command=change_note)
    drop_nota_type.config(width=19,bg='#444442',fg='#ffffff')
    drop_nota_type.place(x=390,y=50)

    from PIL import ImageTk,Image
    global img
    img = Label(root1,width=700,bg='#1a1d1e')
    img.place(x=0,y=80)

    from tkinter import messagebox

    def clicked_chord():
        chord=""
        note_change_l_hash={'A':'A','A#':'A#','B':'B','C':'C','C#':'C#','D':'D','D#':'D#','E':'E','F':'F','F#':'F#','G':'G','G#':'G#'}
        note_change_l_b={'A':'A','Bb':'A#','B':'B','C':'C','Db':'C#','D':'D','Eb':'D#','E':'E','F':'F','Gb':'F#','G':'G','Ab':'G#'}
        try:
            chord_menu=="" or chord_type_menu==""
            if chord_type_menu.get()=='m':
                if chord_menu.get() in note_change_l_hash.keys():    
                    chord+=note_change_l_hash[chord_menu.get()]+'_'+chord_type_menu.get()
                elif chord_menu.get() in note_change_l_b.keys():
                    chord+=note_change_l_b[chord_menu.get()]+'_'+chord_type_menu.get()
                chord_img =ImageTk.PhotoImage(Image.open("E:/Coding Folder/GuitHub/Chords/{}.png".format(chord)))
                img.configure(image=chord_img)
                img.image = chord_img

            else:
                if chord_menu.get() in note_change_l_hash.keys():    
                    chord+=note_change_l_hash[chord_menu.get()]+chord_type_menu.get()
                elif chord_menu.get() in note_change_l_b.keys():
                    chord+=note_change_l_b[chord_menu.get()]+chord_type_menu.get()
                chord_img =ImageTk.PhotoImage(Image.open("E:/Coding Folder/GuitHub/Chords/{}.png".format(chord)))
                img.configure(image=chord_img)
                img.image = chord_img
        except:
            messagebox.askretrycancel("Try Again!!", "Didn't choose Chord or Chord Type!!")
          
    get_chord = Button(root1,text='Get Chord',command=clicked_chord,width=15,height=1,bg='#444442',fg='#ffffff').place(x=585,y=52)

def SL():
    root1 = Toplevel()
    root1.geometry('700x700')
    root1.configure(bg='#1a1d1e')
    b0=Button(root1,text='<- Back',command=root1.destroy,bg='#444442',fg='#ffffff').place(x=0,y=0)
    mylabel = Label(root1,text="Scale Library",bg='#1a1d1e',fg='#ffffff',font="comicsans 20 bold").place(x=240,y=0)
    
    scale_list = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    scale_type_list = ['M','m']
    scale_nota = ['#','b']

    scale_menu= StringVar()
    scale_menu.set("Select Scale")
    drop_scale= OptionMenu(root1, scale_menu,*scale_list)
    drop_scale.config(width=15,bg='#444442',fg='#ffffff')
    drop_scale.place(x=0,y=50)

    scale_type_menu= StringVar()
    scale_type_menu.set("Select Scale Type")
    drop_scale_type= OptionMenu(root1, scale_type_menu,*scale_type_list)
    drop_scale_type.config(width=15,bg='#444442',fg='#ffffff')
    drop_scale_type.place(x=195,y=50)

    def change_note(dummy=None):
        global scale_list
        selected_nota = scale_nota_menu.get()
        if selected_nota == "#":
            scale_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        elif selected_nota == "b":
            scale_list = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        else:
            print('Could not update')
        
        drop_scale['menu'].delete(0, 'end')
        for scale in scale_list:
            drop_scale['menu'].add_command(label=scale, command=tkinter._setit(scale_menu, scale))

    scale_nota_menu= StringVar()
    scale_nota_menu.set("#")
    drop_nota_type= OptionMenu(root1, scale_nota_menu,*scale_nota,command=change_note)
    drop_nota_type.config(width=19,bg='#444442',fg='#ffffff')
    drop_nota_type.place(x=390,y=50)

    from PIL import ImageTk,Image
    global img
    img = Label(root1,bg='#1a1d1e')
    img.place(x=0,y=120)

    from tkinter import messagebox

    def clicked_scale():
        scale = ""
        note_change_l_hash={'A':'A','A#':'A#','B':'B','C':'C','C#':'C#','D':'D','D#':'D#','E':'E','F':'F','F#':'F#','G':'G','G#':'G#'}
        note_change_l_b={'A':'A','Bb':'A#','B':'B','C':'C','Db':'C#','D':'D','Eb':'D#','E':'E','F':'F','Gb':'F#','G':'G','Ab':'G#'}
        
        try:
            scale_menu=="" or scale_type_menu==""
            if scale_type_menu.get()=='m':
                if scale_menu.get() in note_change_l_hash.keys():    
                    scale+=note_change_l_hash[scale_menu.get()]+'_'+scale_type_menu.get()
                elif scale_menu.get() in note_change_l_b.keys():
                    scale+=note_change_l_b[scale_menu.get()]+'_'+scale_type_menu.get()
                scale_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Scales/{scale}.png"))
                img.configure(image=scale_img)
                img.image = scale_img

            else :
                if scale_menu.get() in note_change_l_hash.keys():    
                    scale+=note_change_l_hash[scale_menu.get()]+scale_type_menu.get()
                elif scale_menu.get() in note_change_l_b.keys():
                    scale+=note_change_l_b[scale_menu.get()]+scale_type_menu.get()
                scale_img =ImageTk.PhotoImage(Image.open(f"E:/Coding Folder/GuitHub/Scales/{scale}.png"))
                img.configure(image=scale_img)
                img.image = scale_img
        except:
            messagebox.askretrycancel("Try Again!!", "Didn't choose Scale or Scale Type!!")

    get_scale = Button(root1,text='Get Scale',command=clicked_scale,width=15,height=1,bg='#444442',fg='#ffffff').place(x=585,y=52)
