import tkinter
from tkinter import font

# 전역 변수 선언
user_name = "유저"  # 유저 이름
E_and_I_count = 0   #       각 질문에서 E, N, T, P 성향 답변이면 숫자를 1 올림
N_and_S_count = 0   #       숫자가 2 이상이면 E, N, T, P
T_and_F_count = 0   #       이하면 I, S, F, J
P_and_J_count = 0

# 위젯을 지우는 함수
def delete(A) :
    A.destroy()

def delete_E_I() :
    global answer_E_button
    global answer_I_button
    delete(answer_E_button)
    delete(answer_I_button)

# 테스트 시작 함수
def sendUserName() :
    # 유저 이름 전역 변수로 저장
    global user_name
    user_name = entry_name.get()

    # 윈도우의 위젯 모두 삭제
    delete(title_label)
    delete(text_label)
    delete(entry_name)
    delete(start_button)

    # 첫 번째 질문
    question01()

# 첫 번째 질문 함수
def question01() :
    que01_label = tkinter.Label(start_screen, text="1. 질문내용질문내용질문내용질문내용\n질문질문내질문내용질문내용용질문내용", font = font)
    que01_label.place(x=20, y=200)
    print(user_name)
    global answer_E_button
    global answer_I_button
    answer_E_button = tkinter.Button(start_screen, text = "답변답변답변답변답변", font = font, command = answer_E())
    answer_I_button = tkinter.Button(start_screen, text = "답변답변답변답변답변", font = font, command = answer_I())
    answer_E_button.place(x=20, y=500)
    answer_I_button.place(x=20, y=600)

# 답변이 E 경향일 때 카운트를 1 올리고 다음 질문으로 넘어가는 함수
def answer_E() :
    global E_and_I_count
    E_and_I_count += 1
    delete_E_I()

# 답변이 I 경향일 때 카운트를 수정하지 않고 다음 질문으로 넘어가는 함수
def answer_I() :
    delete_E_I()

# --------------------------------시작 화면 구현----------------------------
#-------------------- 시작 윈도우 생성 ---------------
start_screen = tkinter.Tk()
start_screen.geometry("400x700")
start_screen.title("대학생 유형 테스트")
start_screen.resizable(False, False)
# -----------------------------------------------------

# -------------------------- 시작 화면 디자인 ---------
# 타이틀 이미지 배치
title_photo = tkinter.PhotoImage(file="assets/title.png")
title_label = tkinter.Label(start_screen, image=title_photo)
title_label.place(x=100, y=110)
# 이름 입력 설명 배치
text_label = tkinter.Label(start_screen, text="테스트를 시작하기 전에\n당신의 이름을 입력해주세요!")
text_label.place(x=125, y=330)
# 이름 엔트리 박스 배치
entry_name = tkinter.Entry(start_screen, width=10)
entry_name.place(x=165, y=370)
# 시작 버튼 배치
start_photo = tkinter.PhotoImage(file="assets/startbutton.png")
start_button = tkinter.Button(start_screen, image=start_photo, command=sendUserName)
start_button.place(x=130, y=420)
# 하단 footer 배치
author_label = tkinter.Label(start_screen, text="제작: 한성대학교 IT공과대학 2171110 나은정")
author_label.place(x=75, y=670)
#font 설정
font = font.Font(family = "Arial", size = 14, weight = "bold")

start_screen.mainloop()