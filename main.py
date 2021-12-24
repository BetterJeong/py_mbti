import tkinter
from tkinter import *
from tkinter import font

#-------------------- 시작 윈도우 생성 ---------------
main_screen = tkinter.Tk()
main_screen.geometry("400x700")
main_screen.title("대학생 유형 테스트")
main_screen.resizable(False, False)
# -----------------------------------------------------

#------------------------------ 프레임 선언 ----------------------------
# 1번 질문 프레임
q1_frame = tkinter.Frame(main_screen, width=400, height=700)
q1_frame.place(x = 0,y = 0)
# 2번 질문 프레임
q2_frame = tkinter.Frame(main_screen, width=400, height=700)
q2_frame.place(x = 0,y = 0)
# 시작 화면 프레임
main_frame = tkinter.Frame(main_screen, width=400, height=700)
main_frame.place(x = 0,y = 0)
main_frame.tkraise()
#------------------------------------------------------------------------

#----------------------- 답변 카운팅을 위한 변수 선언 --------------------
global cnt_E
global cnt_N
global cnt_T
global cnt_P
cnt_E = 0
cnt_N = 0
cnt_T = 0
cnt_P = 0
#------------------------------------------------------------------------

#----------------------------- 프레임 전환 함수 ------------------------
# 시작 화면에서 첫 번째 질문 화면으로 전환
def set_frame_q1() :
    q1_frame.tkraise()
# 첫 번째 질문에서 버튼 클릭 시 다음 화면으로 전환
def q1_E() :
    global cnt_E
    cnt_E += 1
    print(cnt_E)
    q2_frame.tkraise()
def q1_I() :
    print(cnt_E)
    q2_frame.tkraise()
#------------------------------------------------------------------------

# -------------------------- 시작 화면 디자인 -------------------------
# 타이틀 이미지 배치
title_photo = tkinter.PhotoImage(file="assets/title.png")
title_label = tkinter.Label(main_frame, image=title_photo)
title_label.place(x=100, y=110)
# 이름 입력 설명 배치
text_label = tkinter.Label(main_frame, text="테스트를 시작하기 전에\n당신의 이름을 입력해주세요!")
text_label.place(x=125, y=330)
# 이름 엔트리 박스 배치
entry_name = tkinter.Entry(main_frame, width=10)
entry_name.place(x=165, y=370)
# 시작 버튼 배치
start_photo = tkinter.PhotoImage(file="assets/startbutton.png")
start_button = tkinter.Button(main_frame, image=start_photo, command=set_frame_q1)
start_button.place(x=130, y=420)
# 하단 footer 배치
author_label = tkinter.Label(main_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정")
author_label.place(x=75, y=670)
# font 설정
font = font.Font(family = "Arial", size = 14, weight = "bold")
# -------------------------------------------------------------------------

# -------------------------- 1번 질문 화면 디자인 -------------------------
# 첫 번째 질문 배치
q01_label = tkinter.Label(q1_frame, text="1. 질문내용질문내용질문내용질문내용\n질문질문내질문내용질문내용용질문내용", font = font)
q01_label.place(x=20, y=200)
# 답변 버튼 배치
answer_E_button = tkinter.Button(q1_frame, text="답변답변답변답변답변", font = font, command=q1_E)
answer_I_button = tkinter.Button(q1_frame, text="답변답변답변답변답변",font = font, command=q1_I)
answer_E_button.place(x=40, y=400)
answer_I_button.place(x=40, y=500)
# -------------------------------------------------------------------------

main_screen.mainloop()