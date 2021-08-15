#Entry을 이용하여 텍스트를 입력받거나 출력하기 위한 기입창을 생성할 수 있습니다

import tkinter
from math import *

win = tkinter.Tk()
win.title("Cheon Young Sung")
win.geometry("640x480+100+100")
win.resizable(False,False)


def calc(event):
    label.config(text = "결과="+str(eval(entry.get())))
    print(eval(entry.get()))
#eval 함수 math 패키지에 있는 메소드로 모든 계산 수식을 해주는 함수이다

entry = tkinter.Entry(win) # 입력창 객체 생성
entry.bind("<Return>",calc) # 결과 창 보여주기
entry.pack() #입력창 추가

label = tkinter.Label(win) #label 객체 생성
label.pack() #label 추가 

win.mainloop()

