#Label 에 대해서 
'''
label 은 삽입하는 이미지나 도표 그림 등에 사용되는 주석문을 생성가능 하게 한다 

'''
import tkinter

window= tkinter.Tk()
window.title("Cheon Young Sung")
window.geometry("640x400+100+100")
window.resizable(0,0)

label = tkinter.Label(window,text = "파이썬",width = 10 , height = 5,fg = "red",relief = "solid")
label.pack()

'''
tkinter.label(원도우창 , 파라미터 1, 파라미터 2 ,파라미터 3 ....) 
라벨의 속성을 표현 할수 있다 
'''

window.mainloop()

'''
Label Parameter

String setting 
---------------------
text = "문자열" = 라벨에 표시할 문자열 
textvariable = 라벨에 표시할 문자열을 가져올 변수 
anchor = 라벨 안의 문자열 또는 이미지의 위치 (default = center ,속성 = n, ne, e, se, s, sw, w, nw, center )
justify = 라벨의 문자열이 여러줄일 경우 정렬 방법 (default = center,속성 = center, left, right)
wraplength = 자동 줄내림 설정 너비 (default = 0 속성 = 상수)
-----------------------

label shape setting 
--------------------
width	라벨의 너비	0	상수
height	라벨의 높이	0	상수
relief	라벨의 테두리 모양	flat	flat, groove, raised, ridge, solid, sunken
borderwidth=bd	라벨의 테두리 두께	2	상수
background=bg	라벨의 배경 색상     SystemButtonFace	  color                  
foreground=fg	라벨의 문자열 색상   SystemButtonFace	  color                  
padx	라벨의 테두리와 내용의 가로 여백	1	상수
pady	라벨의 테두리와 내용의 세로 여백	1	상수

---------------------

label Type setting 
---------------------
이름	의미	                  기본값	 속성
bitmap	라벨에 포함할 기본 이미지	-	info, warning, error, question, questhead, hourglass, gray12, gray25, gray50, gray75
image	라벨에 포함할 임의 이미지	-	-
compound	라벨에 문자열과 이미지를 동시에 표시할 때 이미지의 위치	none	bottom, center, left, none, right, top
font	라벨의 문자열 글꼴 설정	TkDefaultFont	font
cursor	라벨의 마우스 커서 모양	-	커서 속성
---------------------

label state setting 
----------------------
이름	의미	기본값	속성
state	상태 설정	normal	normal, active, disabled
activebackground	active 상태일 때 라벨의 배경 색상	SystemButtonFace	color
activeforeground	active 상태일 때 라벨의 문자열 색상	SystemButtonText	color
disabledforeground	disabeld 상태일 때 라벨의 문자열 색상	SystemDisabledText	color
----------------------


label highlights setting
-------------------------
이름	의미	기본값	속성
highlightcolor	라벨이 선택되었을 때 색상	SystemWindowFrame	color
highlightbackground	라벨이 선택되지 않았을 때 색상	SystemButtonFace	color
highlightthickness	라벨이 선택되었을 때 두께 (두께 설정)	0	상수
-------------------------
'''