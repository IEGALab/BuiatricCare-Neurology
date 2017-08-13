#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Aug 13, 2017 10:51:14 AM
from heapq import nlargest as nlargest



s1= False
s2= False
s3= False
s4= False



import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import Buiatria_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    Buiatria_support.set_Tk_var()
    top = New_Toplevel_1 (root)
    Buiatria_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    Buiatria_support.set_Tk_var()
    top = New_Toplevel_1 (w)
    Buiatria_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):

        global s1
        global s2
        global s3
        global s4
        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+470+157")
        top.title("New Toplevel 1")
        top.configure(background="#d9d9d9")

        

        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)


        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.13, rely=0.27, relheight=0.06
                , relwidth=0.1)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#8cb993")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''Febre''')
        self.Checkbutton1.configure(command = self.atvs1)

        

        self.Checkbutton2 = Checkbutton(top)
        self.Checkbutton2.place(relx=0.13, rely=0.38, relheight=0.06
                , relwidth=0.08)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#8cb993")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Dor''')
        self.Checkbutton2.configure(command = self.atvs2)


        self.Checkbutton3 = Checkbutton(top)
        self.Checkbutton3.place(relx=0.13, rely=0.49, relheight=0.06
                , relwidth=0.11)
        self.Checkbutton3.configure(activebackground="#d9d9d9")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(background="#d9d9d9")
        self.Checkbutton3.configure(disabledforeground="#8cb993")
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='''Edema''')
        self.Checkbutton3.configure(command = self.atvs3)


        self.Checkbutton4 = Checkbutton(top)
        self.Checkbutton4.place(relx=0.13, rely=0.6, relheight=0.06
                , relwidth=0.12)
        self.Checkbutton4.configure(activebackground="#d9d9d9")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(background="#d9d9d9")
        self.Checkbutton4.configure(disabledforeground="#8cb993")
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify=LEFT)
        self.Checkbutton4.configure(text='''Tontura''')
        self.Checkbutton4.configure(command = self.atvs4)


        self.Message1 = Message(top)
        self.Message1.place(relx=0.08, rely=0.16, relheight=0.05, relwidth=0.32)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#bbf7c4")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Selecione seus sintomas:''')
        self.Message1.configure(width=190)

        
 


        self.Button1 = Button(top)
        self.Button1.place(relx=0.32, rely=0.8, height=24, width=197)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command = self.new_jan)
        self.Button1.configure(disabledforeground="#8cb993")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Diagnosticar''')
        self.Button1.configure(width=197)


    def atvs1(self):
        global s1
        s1 = not s1



    def atvs2(self):
        global s2
        s2 = not s2


    def atvs3(self):
        global s3
        s3 = not s3


    def atvs4(self):
        global s4
        s4 = not s4
        
    def new_jan(self):

        global s1
        global s2
        global s3
        global s4
        doenca=[0,0]

        
        dfi=0
        if s1 is True:
            dfi=dfi+1
        if s2 is True:
            dfi=dfi+1
        if s3 is True:
            dfi=dfi+1
        if s4 is True:
            dfi = dfi+1
        dfi = (dfi/4)*100
        doenca[0]=dfi
        print (doenca[0])

        
        dpd=0
        if s1 is False:
            dpd=dpd+1
        if s2 is False:
            dpd=dpd+1
        if s3 is True:
            dpd=dpd+1
        if s4 is True:
            dpd = dpd+1
        dpd = (dpd/4)*100
        doenca[1]=dpd
        print (doenca[1])
        
        doenca=sorted(nlargest(1, doenca))
        porcentagem=doenca[0]
        print (doenca)
        
        jan=Tk()
        if porcentagem == dfi:
            self.l=Label(jan, text='A doença é Flegmão com %s de chance'%porcentagem )
        if porcentagem == dpd:
            self.l=Label(jan, text='A doença Pododermatite com %s de chance'%porcentagem )
        
        self.l.grid()
        jan.geometry('300x200')
        









if __name__ == '__main__':
    vp_start_gui()


