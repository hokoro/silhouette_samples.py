import tkinter 
win = tkinter.Tk()
win.title("Cheon Young Sung")
win.geometry("640x480+100+100")
win.resizable(False,False)

def flash():
    checkbutton1.flash() #버튼을 누르면 깜박임이 있는 함수 



CheckVariety_1 = tkinter.IntVar() #채크버튼의 상태를 제어하는 속성 
CheckVariety_2 = tkinter.IntVar()

checkbutton1 = tkinter.Checkbutton(win,text = "O",variable = CheckVariety_1,activebackground = "blue")
checkbutton2 = tkinter.Checkbutton(win,text = "△",variable = CheckVariety_2)
checkbutton3 = tkinter.Checkbutton(win,text = "X",variable = CheckVariety_2,command = flash)
#activebackground = 버튼이 눌렸을때 어떤 색깔로 깜박임이 있는지 지정해주는 변수 
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

win.mainloop()