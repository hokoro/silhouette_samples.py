import tkinter 
win = tkinter.Tk() #GUI 객체 생성 

win.title("Cheon Young Sung")
win.geometry("640x400+100+100") #geometry("너비x높이+x좌표+y좌표") 의 초기 화면을 설정 할수 있다 
win.resizable(False,False) #resizeable(상하,좌우)원도우 창을 띄웠을때 창크기 조절 가능 여부를 설정 가능 
#resizeable 사용시 True = 1 False = 0 로 숫자로 바꿔서 사용도 가능 

#widget 배치 
label = tkinter.Label(win,text = "안녕하세요") 
'''
tkinter.label(윈도우창,text = "내용")
tkinter 에 있는 label 객체를 가져오는데 매개변수 내용은 
윈도우창에 label 의 위젯을 설정 가능함 
'''
label.pack()



win.mainloop()  # 만든 객체 원도우창으로 띄우기 
