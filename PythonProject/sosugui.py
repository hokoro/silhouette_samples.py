import tkinter as Tk
import tkinter.scrolledtext as tkst
from tkinter import Menu
from tkinter import ttk
import tkinter
import tkinter.font
sosuMain = tkinter.Tk()
sosuMain.title("소수/합성수 판별기")
sosuMain.geometry("500x500+100+100")
sosuMain.resizable(False,False)



#font set
sosuLabelfont = tkinter.font.Font(family = "맑은 고딕",size = 20 , slant = "italic")
sosuInputfont = tkinter.font.Font(family = "Arial",size = 15 , slant = "italic")
soinsuLabelfont = tkinter.font.Font(family = "Arial",size = 15 , slant = "italic")
#sosu label
sosuLabel = tkinter.Label(sosuMain,text = "소수/합성수 판별기",font = sosuLabelfont)
sosuLabel.grid(row = 0 , column = 0)


#sosu input
sosuInput = tkinter.Label(sosuMain,text = "입력",justify = "left",font = sosuInputfont)
sosuInput.grid(row = 1 , column = 0)


#sosu input textfield 
sosuText = tkinter.Text(sosuMain,width = 20 , height = 2)
sosuText.grid(row = 1 , column = 1)

#sosu button
sosuButton = tkinter.Button(sosuMain,text = "실행",overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
sosuButton.grid(row =2 , column = 1)
#soinsu buhae label
soinsuLabel = tkinter.Label(sosuMain,text = "결과",font = soinsuLabelfont)
soinsuLabel.grid(row = 3, column = 0)


sosuMain.mainloop()