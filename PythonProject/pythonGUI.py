import tkinter

window = tkinter.Tk()

window.title("CHEON YOUNG SUNG")
window.geometry("640x400+100+100")
window.resizable(False,False)

label = tkinter.Label(window,text = "안녕하세요.")
label.pack()
window.mainloop()