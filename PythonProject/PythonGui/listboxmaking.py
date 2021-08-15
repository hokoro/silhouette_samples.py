import tkinter 
win = tkinter.Tk()
win.title("Cheon Young Sung")
win.geometry("640x480+100+100")
win.resizable(False,False)


listbox = tkinter.Listbox(win,selectmode = 'extend',height = 0) # 리스트박스 객체 생성 
listbox.insert(0,"1번") #리스트 박스 삽입 메소드
listbox.insert(1,"2번")
listbox.insert(2,"3번")
listbox.insert(3,"4번")
listbox.insert(4,"4번")
listbox.insert(4,"4번") #리스트 박스 삭제 메소드(star_index,end_index)

listbox.delete(3,4)
listbox.pack()

win.mainloop()

