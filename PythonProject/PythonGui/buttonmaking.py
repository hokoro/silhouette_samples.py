import tkinter
win = tkinter.Tk()
win.title("Cheon Young Sung")
win.resizable(False,False)

count = 0
def countUp():
    global count #전역변수 로 선언한 변수를 사용할려면 함수내에서 global keyword 를 사용해야 한다 
    count+=1
    label.config(text = str(count)) #label.config() 윈도우 창에서 보여주는 text 나 image 출력 


label = tkinter.Label(win,text = "0") #label 을 윈도우창에 추가 + text =초기값 0으로 설정
label.pack() # 라벨 추가

button = tkinter.Button(win,overrelief = "solid",width = 15,command = countUp,repeatdelay = 1000 , repeatinterval = 100)
'''
tkinter.Button(win,overrelief = "solid",width = 15,command = countUp,repeatdelay = 1000 , repeatinterval = 100)
win : win 객체 설정을 따른다
overrelief : 마우스가 버튼 위로 올라갔을때 solid 진한 선 형태의 모양을 띄운다
width = 버튼의 넓이 15
command = 버튼을 눌렀을떄 발생하는 함수 나 명령어 실행 
repeatdelay = 버튼이 눌러진 상태에서 다음 command 까지 대기 시간  1000 ms 
repeatinterval = 버튼이 눌러진 상태에서 command 실행의 반복시간 = 100 ms

'''
button.pack() # 버튼 추가
win.mainloop() # 원도우창 띄우기 


