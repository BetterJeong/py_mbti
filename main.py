# -*- coding: utf-8 -*-

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
# 3번 질문 프레임
q3_frame = tkinter.Frame(main_screen, width=400, height=700)
q3_frame.place(x = 0,y = 0)
# 4번 질문 프레임
q4_frame = tkinter.Frame(main_screen, width=400, height=700)
q4_frame.place(x = 0,y = 0)
# 5번 질문 프레임
q5_frame = tkinter.Frame(main_screen, width=400, height=700)
q5_frame.place(x = 0,y = 0)
# 6번 질문 프레임
q6_frame = tkinter.Frame(main_screen, width=400, height=700)
q6_frame.place(x = 0,y = 0)
# 7번 질문 프레임
q7_frame = tkinter.Frame(main_screen, width=400, height=700)
q7_frame.place(x = 0,y = 0)
# 8번 질문 프레임
q8_frame = tkinter.Frame(main_screen, width=400, height=700)
q8_frame.place(x = 0,y = 0)
# 9번 질문 프레임
q9_frame = tkinter.Frame(main_screen, width=400, height=700)
q9_frame.place(x = 0,y = 0)
# 10번 질문 프레임
q10_frame = tkinter.Frame(main_screen, width=400, height=700)
q10_frame.place(x = 0,y = 0)
# 11번 질문 프레임
q11_frame = tkinter.Frame(main_screen, width=400, height=700)
q11_frame.place(x = 0,y = 0)
# 12번 질문 프레임
q12_frame = tkinter.Frame(main_screen, width=400, height=700)
q12_frame.place(x = 0,y = 0)
# 테스트 끝 프레임
r_button_frame = tkinter.Frame(main_screen, width=400, height=700)
r_button_frame.place(x = 0,y = 0)
# ----------------------- 결과지 프레임 ----------------------
# intj
intj_frame = tkinter.Frame(main_screen, width=400, height=700)
intj_frame.place(x = 0,y = 0)
# intp
intp_frame = tkinter.Frame(main_screen, width=400, height=700)
intp_frame.place(x = 0,y = 0)
# entj
entj_frame = tkinter.Frame(main_screen, width=400, height=700)
entj_frame.place(x = 0,y = 0)
# entp
entp_frame = tkinter.Frame(main_screen, width=400, height=700)
entp_frame.place(x = 0,y = 0)
#infj
infj_frame = tkinter.Frame(main_screen, width=400, height=700)
infj_frame.place(x = 0,y = 0)
#infp
infp_frame = tkinter.Frame(main_screen, width=400, height=700)
infp_frame.place(x = 0,y = 0)
# enfj
enfj_frame = tkinter.Frame(main_screen, width=400, height=700)
enfj_frame.place(x = 0,y = 0)
#enfp
enfp_frame = tkinter.Frame(main_screen, width=400, height=700)
enfp_frame.place(x = 0,y = 0)
#istj
istj_frame = tkinter.Frame(main_screen, width=400, height=700)
istj_frame.place(x = 0,y = 0)
#isfj
isfj_frame = tkinter.Frame(main_screen, width=400, height=700)
isfj_frame.place(x = 0,y = 0)
#estj
estj_frame = tkinter.Frame(main_screen, width=400, height=700)
estj_frame.place(x = 0,y = 0)
#esfj
esfj_frame = tkinter.Frame(main_screen, width=400, height=700)
esfj_frame.place(x = 0,y = 0)
#istp
istp_frame = tkinter.Frame(main_screen, width=400, height=700)
istp_frame.place(x = 0,y = 0)
#isfp
isfp_frame = tkinter.Frame(main_screen, width=400, height=700)
isfp_frame.place(x = 0,y = 0)
#estp
estp_frame = tkinter.Frame(main_screen, width=400, height=700)
estp_frame.place(x = 0,y = 0)
#esfp
esfp_frame = tkinter.Frame(main_screen, width=400, height=700)
esfp_frame.place(x = 0,y = 0)
# ------------------------------------------------------------
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

#---------------------- 결과 저장 변수 ----------------------
global result_mbti
result_mbti = [0, 0, 0, 0]
#------------------------------------------------------------------------

# --------------------------- 카운팅 검산 함수 -------------------------
def cnt_test() :
    print("---------------")
    print("E 카운트: ", cnt_E,"\nN 카운트: ", cnt_N, "\nT 카운트: ", cnt_T, "\nP 카운트: ", cnt_P)
    print("---------------")
# ----------------------------------------------------------------------

#----------------------------- 프레임 전환 함수 ------------------------
# 시작 화면에서 첫 번째 질문 화면으로 전환
def set_frame_q1() :
    q1_frame.tkraise()
# 1번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q1_E() :
    global cnt_E
    cnt_E += 1
    cnt_test()
    q2_frame.tkraise()
def q1_I() :
    cnt_test()
    q2_frame.tkraise()
# 2번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q2_F() :
    cnt_test()
    q3_frame.tkraise()
def q2_T() :
    global cnt_T
    cnt_T += 1
    cnt_test()
    q3_frame.tkraise()
# 3번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q3_S() :
    cnt_test()
    q4_frame.tkraise()
def q3_N() :
    global cnt_N
    cnt_N += 1
    cnt_test()
    q4_frame.tkraise()
# 4번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q4_E() :
    global cnt_E
    cnt_E += 1
    cnt_test()
    q5_frame.tkraise()
def q4_I() :
    cnt_test()
    q5_frame.tkraise()
# 5번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q5_P() :
    global cnt_P
    cnt_P += 1
    cnt_test()
    q6_frame.tkraise()
def q5_J() :
    cnt_test()
    q6_frame.tkraise()
# 6번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q6_S() :
    cnt_test()
    q7_frame.tkraise()
def q6_N() :
    global cnt_N
    cnt_N += 1
    cnt_test()
    q7_frame.tkraise()
# 7번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q7_F() :
    cnt_test()
    q8_frame.tkraise()
def q7_T() :
    global cnt_T
    cnt_T += 1
    cnt_test()
    q8_frame.tkraise()
# 8번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q8_P() :
    global cnt_P
    cnt_P += 1
    cnt_test()
    q9_frame.tkraise()
def q8_J() :
    cnt_test()
    q9_frame.tkraise()
# 9번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q9_S() :
    cnt_test()
    q10_frame.tkraise()
def q9_N() :
    global cnt_N
    cnt_N += 1
    cnt_test()
    q10_frame.tkraise()
# 10번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q10_F() :
    cnt_test()
    q11_frame.tkraise()
def q10_T() :
    global cnt_T
    cnt_T += 1
    cnt_test()
    q11_frame.tkraise()
# 11번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q11_E() :
    global cnt_E
    cnt_E += 1
    cnt_test()
    q12_frame.tkraise()
def q11_I() :
    cnt_test()
    q12_frame.tkraise()
# 12번 질문에서 버튼 클릭 시 다음 화면으로 전환
def q12_P() :
    global cnt_P
    cnt_P += 1
    cnt_test()
    r_button_frame.tkraise()
def q12_J() :
    cnt_test()
    r_button_frame.tkraise()
# 결과 보기 버튼 클릭 시 해당하는 결과 페이지로 이동
def send_result() :
    global result_mbti
    # 카운트 숫자에 따라 배열에 유형 저장
    if (cnt_E >= 2) :
        result_mbti[0] = "E"
    elif (cnt_E < 2) :
        result_mbti[0] = "I"
    if (cnt_N >= 2) :
        result_mbti[1] = "N"
    elif (cnt_N < 2) :
        result_mbti[1] = "S"
    if (cnt_T >= 2) :
        result_mbti[2] = "T"
    elif (cnt_T < 2) :
        result_mbti[2] = "F"
    if (cnt_P >= 2) :
        result_mbti[3] = "P"
    elif (cnt_P < 2) :
        result_mbti[3] = "J"
    print(result_mbti)

    # 결과에 따라 각각 결과지 이동
    if (result_mbti[0] == "I" and result_mbti[1] == "N" and result_mbti[2] == "T" and result_mbti[3] == "J") :
        intj_frame.tkraise()
    elif (result_mbti[0] == "I" and result_mbti[1] == "N" and result_mbti[2] == "T" and result_mbti[3] == "P") :
        intp_frame.tkraise()
    elif (result_mbti[0] == "E" and result_mbti[1] == "N" and result_mbti[2] == "T" and result_mbti[3] == "J") :
        entj_frame.tkraise()
    elif (result_mbti[0] == "E" and result_mbti[1] == "N" and result_mbti[2] == "T" and result_mbti[3] == "P") :
        entp_frame.tkraise()
    elif (result_mbti[0] == "I" and result_mbti[1] == "N" and result_mbti[2] == "F" and result_mbti[3] == "J") :
        infj_frame.tkraise()
    elif (result_mbti[0] == "I" and result_mbti[1] == "N" and result_mbti[2] == "F" and result_mbti[3] == "P") :
        infp_frame.tkraise()
    elif (result_mbti[0] == "E" and result_mbti[1] == "N" and result_mbti[2] == "F" and result_mbti[3] == "J") :
        enfj_frame.tkraise()
    elif (result_mbti[0] == "E" and result_mbti[1] == "N" and result_mbti[2] == "F" and result_mbti[3] == "P") :
        enfp_frame.tkraise()
    elif (result_mbti[0] == "I" and result_mbti[1] == "S" and result_mbti[2] == "T" and result_mbti[3] == "J") :
        istj_frame.tkraise()
    elif (result_mbti[0] == "I" and result_mbti[1] == "S" and result_mbti[2] == "F" and result_mbti[3] == "J") :
        isfj_frame.tkraise()
    elif (result_mbti[0] == "E" and result_mbti[1] == "S" and result_mbti[2] == "T" and result_mbti[3] == "J") :
        estj_frame.tkraise()
    elif (result_mbti[0] == "E" and result_mbti[1] == "S" and result_mbti[2] == "F" and result_mbti[3] == "J") :
        esfj_frame.tkraise()
    elif (result_mbti[0] == "I" and result_mbti[1] == "S" and result_mbti[2] == "T" and result_mbti[3] == "P") :
        istp_frame.tkraise()
    elif (result_mbti[0] == "I" and result_mbti[1] == "S" and result_mbti[2] == "F" and result_mbti[3] == "P") :
        isfp_frame.tkraise()
    elif (result_mbti[0] == "E" and result_mbti[1] == "S" and result_mbti[2] == "T" and result_mbti[3] == "P") :
        estp_frame.tkraise()
    elif (result_mbti[0] == "E" and result_mbti[1] == "S" and result_mbti[2] == "T" and result_mbti[3] == "P") :
        estp_frame.tkraise()
#------------------------------------------------------------------------

#------------------------ 첫 화면으로 돌아가는 함수 ---------------------
def go_main() :
    # 카운팅 모두 0으로 되돌리기
    global cnt_E
    global cnt_N
    global cnt_T
    global cnt_P
    global result_mbti
    cnt_E = 0
    cnt_N = 0
    cnt_T = 0
    cnt_P = 0
    result_mbti = [0, 0, 0, 0]
    cnt_test()
    print(result_mbti)
    # 시작 화면으로 돌아가기
    main_frame.tkraise()
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# font 설정
font_main = font.Font(family = "Arial", size = 14, weight = "bold")
font_small_title = font.Font(family = "Arial", size = 12)
font_text = font.Font(family = "Arial", size = 10)
# -------------------------- 시작 화면 디자인 -------------------------
# 타이틀 이미지 배치
title_photo = tkinter.PhotoImage(file="assets/title.png")
title_label = tkinter.Label(main_frame, image=title_photo)
title_label.place(x=100, y=110)
# 테스트 설명 배치
text_label = tkinter.Label(main_frame, text="이 테스트는 정식 검사가 아니므로\n재미로 즐겨주시기 바랍니다.\n\n자신의 모습과 제일 비슷한 답변을 골라주세요.", font = font_text)
text_label.place(x=75, y=330)
# 시작 버튼 배치
start_photo = tkinter.PhotoImage(file="assets/startButton.png")
start_button = tkinter.Button(main_frame, image=start_photo, command=set_frame_q1)
start_button.place(x=110, y=420)
# 하단 footer 배치
author_label = tkinter.Label(main_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 1번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_photo = tkinter.PhotoImage(file="assets/logo.png")
logo_label = tkinter.Label(q1_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 1번 질문 배치
q01_label = tkinter.Label(q1_frame, text="1. 길었던 수험 생활이 끝나고\n한성대학교 학생이 되었다. 신입생인 나는?", font = font_main)
q01_label.place(x=20, y=200)
# 답변 버튼 배치
answer_E_button = tkinter.Button(q1_frame, text="새로운 사람들을 만나고 친해질\n생각에 설렌다.", font = font_main, command=q1_E)
answer_I_button = tkinter.Button(q1_frame, text="대학에는 어떤 사람들이 있을지\n걱정되고 떨린다.",font = font_main, command=q1_I)
answer_E_button.place(x=60, y=320)
answer_I_button.place(x=60, y=400)
# 하단 footer 배치
author_label = tkinter.Label(q1_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 2번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q2_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 2번 질문 배치
q02_label = tkinter.Label(q2_frame, text="2. 동기들과 저녁 식사를 하기로 했다. \n함께 나눠 먹을 저녁 메뉴를 정해야 하는데,\n어떻게 할까?", font = font_main)
q02_label.place(x=20, y=200)
# 답변 버튼 배치
answer_F_button = tkinter.Button(q2_frame, text="내가 정한 메뉴를 동기들이 좋아하지\n않을 수 있으니, 나는 아무거나\n먹어도 상관 없다.", font = font_main, command=q2_F)
answer_T_button = tkinter.Button(q2_frame, text="내가 먹고 싶은 메뉴가 이미 있다.\n적절히 조율해서 빠르게 결정한다.",font = font_main, command=q2_T)
answer_F_button.place(x=35, y=300)
answer_T_button.place(x=45, y=410)
# 하단 footer 배치
author_label = tkinter.Label(q2_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 3번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q3_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 3번 질문 배치
q03_label = tkinter.Label(q3_frame, text="3. 실습을 하고 있는데, 생소한 내용인\n것 같고 어떻게 하는 건지 기억이 잘 안 난다.\n이럴 때는 어떻게 해야 할까?", font = font_main)
q03_label.place(x=10, y=200)
# 답변 버튼 배치
answer_S_button = tkinter.Button(q3_frame, text="분명 전에 배웠던 내용일 것이다.\n천천히 기억을 되짚어본다.", font = font_main, command=q3_S)
answer_N_button = tkinter.Button(q3_frame, text="기억이 잘 나지 않더라도, 어떻게든\n해결될 것이다. 생각나는 해결\n방법을 시도해본다.",font = font_main, command=q3_N)
answer_S_button.place(x=55, y=320)
answer_N_button.place(x=45, y=410)
# 하단 footer 배치
author_label = tkinter.Label(q3_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 4번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q4_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 4번 질문 배치
q04_label = tkinter.Label(q4_frame, text="4. 슬슬 공부를 해야할 것 같은데, 공부가 손에\n잘 잡히지 않는다. 나에게 잘 맞는\n 공부 방법은?", font = font_main)
q04_label.place(x=10, y=200)
# 답변 버튼 배치
answer_I_button = tkinter.Button(q4_frame, text="공부는 역시 도서관이 제일이야.\n조용한 열람실에서 공부한다.", font = font_main, command=q4_I)
answer_E_button = tkinter.Button(q4_frame, text="다른 친구들이랑 공부 약속을 잡으면\n좀 하겠지? 스터디 모임을 찾는다.",font = font_main, command=q4_E)
answer_I_button.place(x=55, y=320)
answer_E_button.place(x=40, y=410)
# 하단 footer 배치
author_label = tkinter.Label(q4_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 5번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q5_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 5번 질문 배치
q05_label = tkinter.Label(q5_frame, text="5. 강의 도중, 교수님께서 갑자기\n과제를 꼭 제출하라고 하신다. ", font = font_main)
q05_label.place(x=70, y=200)
# 답변 버튼 배치
answer_P_button = tkinter.Button(q5_frame, text="과제? 그런 게 있었어?\n친구에게 급하게 물어본다.", font = font_main, command=q5_P)
answer_J_button = tkinter.Button(q5_frame, text="이미 다 끝냈지! 뿌듯한 마음으로\n과제를 제출한다.",font = font_main, command=q5_J)
answer_P_button.place(x=80, y=320)
answer_J_button.place(x=50, y=400)
# 하단 footer 배치
author_label = tkinter.Label(q5_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 6번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q6_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 6번 질문 배치
q06_label = tkinter.Label(q6_frame, text="6. 친구들과 마니또를 하게 되었다.\n마니또는 제비뽑기로 선정된 상대방에게\n자신을 숨기고 선물, 도움 등을 주는 게임이다.\n친구가 나에게 ‘마니또 들키면 어떡하지?’\n라고 말한다면?", font = font_main)
q06_label.place(x=10, y=160)
# 답변 버튼 배치
answer_N_button = tkinter.Button(q6_frame, text="만약 내가 초콜릿을 몰래 두고 갔는데\n하필 그걸 들켜버리는 거?\n상상의 나래를 펼친다.", font = font_main, command=q6_N)
answer_S_button = tkinter.Button(q6_frame, text="당연히 들키면 안 되지! 안 들키도록\n최대한 열심히 해보자.\n현실적으로 이야기한다.",font = font_main, command=q6_S)
answer_N_button.place(x=40, y=300)
answer_S_button.place(x=45, y=410)
# 하단 footer 배치
author_label = tkinter.Label(q6_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 7번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q7_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 7번 질문 배치
q07_label = tkinter.Label(q7_frame, text="7. 친구의 어떤 행동에 대해 기분이 상했다.\n이걸 어떻게 해야 할까?", font = font_main)
q07_label.place(x=20, y=200)
# 답변 버튼 배치
answer_T_button = tkinter.Button(q7_frame, text="친구에게 솔직하게 말하고\n고쳐달라고 이야기한다.", font = font_main, command=q7_T)
answer_F_button = tkinter.Button(q7_frame, text="내 지적으로 친구도\n기분 나쁘진 않을까? 고민한다.",font = font_main, command=q7_F)
answer_T_button.place(x=90, y=320)
answer_F_button.place(x=65, y=400)
# 하단 footer 배치
author_label = tkinter.Label(q7_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 8번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q8_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 8번 질문 배치
q08_label = tkinter.Label(q8_frame, text="8. 시험이 얼마 남지 않았다. 해야 할 공부가\n한가득! 하지만 공부는 하기 싫고, \n놀기만 하고 싶다.", font = font_main)
q08_label.place(x=20, y=190)
# 답변 버튼 배치
answer_J_button = tkinter.Button(q8_frame, text="공부는 중요하니까 미루면 안 된다.\n일단 차근차근 공부 계획을 세우고,\n목표가 끝나면 놀아야지!", font = font_main, command=q8_J)
answer_P_button = tkinter.Button(q8_frame, text="별로 어려운 시험도 아니고\n시험 전날에 바짝 하면 충분할 것 같다.\n일단 놀자!",font = font_main, command=q8_P)
answer_J_button.place(x=45, y=300)
answer_P_button.place(x=33, y=410)
# 하단 footer 배치
author_label = tkinter.Label(q8_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 9번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q9_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 9번 질문 배치
q09_label = tkinter.Label(q9_frame, text="9. 우연히 공모전(혹은 프로젝트)에 대한\n이야기를 들었다.", font = font_main)
q09_label.place(x=30, y=200)
# 답변 버튼 배치
answer_S_button = tkinter.Button(q9_frame, text="생각보다 어려워 보이고\n도전하고 싶은 마음이 별로 없다.", font = font_main, command=q9_S)
answer_N_button = tkinter.Button(q9_frame, text="내 진로에 관련 없는 일이라도\n뭔가 해보고 싶고 도전하고 싶다.",font = font_main, command=q9_N)
answer_S_button.place(x=53, y=320)
answer_N_button.place(x=53, y=400)
# 하단 footer 배치
author_label = tkinter.Label(q9_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 10번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q10_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 10번 질문 배치
q10_label = tkinter.Label(q10_frame, text="10. 토론 수업에서 우리 팀이 패배하게 되었다.\n토론이 끝난 후 나의 모습은?", font = font_main)
q10_label.place(x=7, y=200)
# 답변 버튼 배치
answer_T_button = tkinter.Button(q10_frame, text="토론에서 어떤 부분이 잘못되었는지\n생각하고 다음에는 이길 수 있도록 \n계획을 짠다.", font = font_main, command=q10_T)
answer_F_button = tkinter.Button(q10_frame, text="일단 같이 토론한 친구들에게\n‘괜찮아, 다음엔 더 잘할 수 있을거야.’\n라며 위로한다.",font = font_main, command=q10_F)
answer_T_button.place(x=40, y=300)
answer_F_button.place(x=35, y=410)
# 하단 footer 배치
author_label = tkinter.Label(q10_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 11번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q11_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 11번 질문 배치
q11_label = tkinter.Label(q11_frame, text="11. 대학 생활을 하면서 사소하거나 큰 고민이\n점점 생겨서 힘들다. 어떻게 할까?", font = font_main)
q11_label.place(x=7, y=200)
# 답변 버튼 배치
answer_I_button = tkinter.Button(q11_frame, text="아무리 친해도 잘 말하지 못하겠다.\n마음 속에만 고이 간직한다.", font = font_main, command=q11_I)
answer_E_button = tkinter.Button(q11_frame, text="힘들었던 일들을 주변 사람들에게\n잘 털어놓는 편이다. 이야기를\n하고나면 마음이 좀 편해진다.",font = font_main, command=q11_E)
answer_I_button.place(x=45, y=320)
answer_E_button.place(x=50, y=400)
# 하단 footer 배치
author_label = tkinter.Label(q11_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 12번 질문 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(q12_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 12번 질문 배치
q12_label = tkinter.Label(q12_frame, text="12. 한성대학교는 1학년 2학기에 트랙을\n결정할 수 있다. 원하는 트랙이 너무 많아서\n고민되는데, 어떻게 할까?", font = font_main)
q12_label.place(x=10, y=190)
# 답변 버튼 배치
answer_P_button = tkinter.Button(q12_frame, text="트랙 신청 기간 마지막 날에 선택해도\n괜찮으니까, 그 전까지 충분히\n고민해보고 결정한다.", font = font_main, command=q12_P)
answer_J_button = tkinter.Button(q12_frame, text="내가 진짜 하고 싶은 건 뭘까?\n나에게 잘 맞는 건 뭘까? 머릿속에\n떠오르는 대로 바로 결정한다.",font = font_main, command=q12_J)
answer_P_button.place(x=33, y=300)
answer_J_button.place(x=48, y=400)
# 하단 footer 배치
author_label = tkinter.Label(q12_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# -------------------------- 결과 보기 화면 디자인 -------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(r_button_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 테스트 종료 안내 문구 배치
r_text_label = tkinter.Label(r_button_frame, text="답변해주셔서 감사합니다!\n결과를 확인해볼까요?", font = font_main)
r_text_label.place(x=90, y=240)
# 결과 보기 버튼 배치
result_show_button_photo = tkinter.PhotoImage(file="assets/resultCheckButton.png")
result_show_button = tkinter.Button(r_button_frame, image=result_show_button_photo, command=send_result)
result_show_button.place(x=125, y=310)
# 하단 footer 배치
author_label = tkinter.Label(r_button_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# ----------------------------- 유형별 결과 화면 --------------------------
# intj 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(intj_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
intj_title = tkinter.PhotoImage(file="assets/intj.png")
intj_label = tkinter.Label(intj_frame, image=intj_title)
intj_label.place(x=11, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(intj_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
intj_info = tkinter.Label(intj_frame, text="무언가를 있는 그대로 받아들이기 보다는 깊게\n분석하고 이해하는 걸 좋아해요. 그리고 논리적인\n탐구 과정을 통해 결과를 이끌어내요.\n\n과정보다는 결과가 중요해요.\n자신이 생각한 이론을 실현해내는 능력이 뛰어나요.\n\n자신의 능력을 믿고 도전하는 데 능숙해요.\n아무리 어려운 목표라도 달성하려고 노력해요.\n\n감수성이 낮고, 감정 표현을 쉽게 하지 않아요.\n덕분에 주변에서 속을 알 수 없다는 말을 종종 들어요.\n\n\n✔ 학교에서 내 모습은?\n자신의 목표를 향해 최선을 다할 수 있는 멋진\n사람이에요. 친구들과 노는 것 보다는 자신의 할 일을\n더 중요하게 여기는 것 같아요. 속을 알 수 없는\n모습도 종종 보이지만, 사실 알고 보면 재밌는 친구예요.", font = font_small_title)
intj_info.place(x=15, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button_photo = tkinter.PhotoImage(file="assets/retestButton.png")
restest_button = tkinter.Button(intj_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(intj_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# intp 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(intp_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
intp_title = tkinter.PhotoImage(file="assets/intp.png")
intp_label = tkinter.Label(intp_frame, image=intp_title)
intp_label.place(x=35, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(intp_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
intp_info = tkinter.Label(intp_frame, text="조용하고 과묵한 성격으로, 말을 많이 하는 편이\n아니에요. 처음 만난 사람에게는 차갑게 보일 수 있어요.\n하지만 사실은 털털하고 개방적인 성격이에요.\n\n추상적이고 논리적인 생각을 하는 걸 좋아해요.\n자신이 관심있는 분야에 대해 끊임없이 사색하고\n분석해요. 비현실적인 상상도 좋아해요.\n\n규칙적이고 체계적인 건 싫어요. 계획을 짜서 움직이는\n스타일은 아니에요. 계획보다는 그때마다 상황에 따라\n즉흥적으로 하는 걸 좋아해요.\n\n\n✔ 학교에서 내 모습은?\n혼자가 좋아! 단체생활은 피곤해요. 인간관계에도\n 큰 관심이 없어요. 혼자 공부하는 게 편하고, 조용한\n도서관 분위기가 좋아요. 놀 때도 혼자 노는 게 좋아요.\n사회적인 활동을 하는 경우는 드물어요.\n도서관에서 자주 보여요.", font = font_small_title)
intp_info.place(x=15, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(intp_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(intp_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# entj 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(entj_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
entj_title = tkinter.PhotoImage(file="assets/entj.png")
entj_label = tkinter.Label(entj_frame, image=entj_title)
entj_label.place(x=11, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(entj_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
entj_info = tkinter.Label(entj_frame, text="자기주장이 확고하고, 대담한 지도력과\n통솔력을 가지고 있어요.\n모임이나 팀플을 적극적으로 주도하고,\n대화를 이끌어나가는 힘이 있어요.\n\n지식을 탐구하는 데 욕심이 있어요.\n직관적인 능력이 뛰어나요.\n어떤 일을 처리할 때 깊게 분석하고\n계획하는 걸 좋아해요.\n그리고 달성을 위해 체계적인 과정을 수립해요.\n\n사회를 뒤엎고 싶어해요.\n신념에 맞지 않는 일에 적극적으로 맞서요.\n\n\n✔ 학교에서 내 모습은?\n팀플을 하면 원하지 않아도 팀장이 돼요.\n사실 내가 팀장을 하는 게 낫겠다 싶어요.\n그리고 특유의 주도적인 성격으로 팀을 잘 이끌어나가요.", font = font_small_title)
entj_info.place(x=15, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(entj_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(entj_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# entp 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(entp_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
entp_title = tkinter.PhotoImage(file="assets/entp.png")
entp_label = tkinter.Label(entp_frame, image=entp_title)
entp_label.place(x=25, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(entp_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
entp_info = tkinter.Label(entp_frame, text="인간 관계에 크게 관심을 갖거나 사교적이지는 않지만,\n토론과 같은 외부 활동을 좋아해요.\n자신의 생각이나 가치관을 잘 말하는 편이에요.\n\n자기 자신에 대한 자신감이 있어요.\n그리고 다른 사람이 나에 대해 어떻게 평가하든\n 관심 없어요. 나한테 참견하는 것도 싫어요.\n 나는 내가 알아서 해요.\n\n공부에는 별로 관심 없어요. 하기 싫은 공부보다는\n내가 좋아하는 분야를 위해 공부하는 게 좋아요.\n반복적이고 꾸준히 해야 하는 일을 별로 안 좋아해요.\n\n\n✔ 학교에서 내 모습은?\n주관이 뚜렷하고 말을 잘하는 친구예요.\n토론에 능하고 논쟁을 즐겨요.\n시험에는 관심 없던 것처럼 보이더니\n벼락치기로 성적은 잘 받아요.", font = font_small_title)
entp_info.place(x=20, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(entp_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(entp_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# infj 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(infj_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
infj_title = tkinter.PhotoImage(file="assets/infj.png")
infj_label = tkinter.Label(infj_frame, image=infj_title)
infj_label.place(x=25, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(infj_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
infj_info = tkinter.Label(infj_frame, text="겉으로 보기엔 차가워 보일 수도 있지만,\n사실은 매우 따뜻해요.\n다정하고 따뜻하다는 말을 많이 들어요.\n\n불의에 대해 민감하게 반응하고\n높은 도덕적 관념을 가지고 있어요.\n모든 상황을 다양한 시각으로 바라보고\n이해하는 능력이 뛰어나요.\n\n몽환적이고, 신비로운,\n어떻게 보면 가장 알 수 없는 유형이에요.\n\n호기심이 많고 열정적이에요.\n스스로에게 매우 엄격하고 자아성찰을 자주 해요.\n\n\n✔ 학교에서 내 모습은?\n종종 무슨 생각을 하는지 잘 모르겠어요.\n하지만 따스한 성격이라는 건 너무 잘 느껴져요.\n주변 고민 상담을 잘 해주고, 신경을 많이 써줘요.", font = font_small_title)
infj_info.place(x=35, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(infj_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(infj_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# infp 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(infp_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
infp_title = tkinter.PhotoImage(file="assets/infp.png")
infp_label = tkinter.Label(infp_frame, image=infp_title)
infp_label.place(x=45, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(infp_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
infp_info = tkinter.Label(infp_frame, text="", font = font_small_title)
infp_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(infp_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(infp_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# enfj 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(enfj_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
enfj_title = tkinter.PhotoImage(file="assets/enfj.png")
enfj_label = tkinter.Label(enfj_frame, image=enfj_title)
enfj_label.place(x=40, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(enfj_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
enfj_info = tkinter.Label(enfj_frame, text="", font = font_small_title)
enfj_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(enfj_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(enfj_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# enfp 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(enfp_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
enfp_title = tkinter.PhotoImage(file="assets/enfp.png")
enfp_label = tkinter.Label(enfp_frame, image=enfp_title)
enfp_label.place(x=15, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(enfp_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
enfp_info = tkinter.Label(enfp_frame, text="", font = font_small_title)
enfp_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(enfp_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(enfp_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# istj 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(istj_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
istj_title = tkinter.PhotoImage(file="assets/istj.png")
istj_label = tkinter.Label(istj_frame, image=istj_title)
istj_label.place(x=15, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(istj_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
istj_info = tkinter.Label(istj_frame, text="", font = font_small_title)
istj_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(istj_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(istj_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# isfj 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(isfj_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
isfj_title = tkinter.PhotoImage(file="assets/isfj.png")
isfj_label = tkinter.Label(isfj_frame, image=isfj_title)
isfj_label.place(x=47, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(isfj_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
isfj_info = tkinter.Label(isfj_frame, text="", font = font_small_title)
isfj_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(isfj_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(isfj_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# estj 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(estj_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
estj_title = tkinter.PhotoImage(file="assets/estj.png")
estj_label = tkinter.Label(estj_frame, image=estj_title)
estj_label.place(x=12, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(estj_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
estj_info = tkinter.Label(estj_frame, text="", font = font_small_title)
estj_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(estj_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(estj_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# esfj 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(esfj_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
esfj_title = tkinter.PhotoImage(file="assets/esfj.png")
esfj_label = tkinter.Label(esfj_frame, image=esfj_title)
esfj_label.place(x=45, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(esfj_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
esfj_info = tkinter.Label(esfj_frame, text="", font = font_small_title)
esfj_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(esfj_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(esfj_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# istp 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(istp_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
istp_title = tkinter.PhotoImage(file="assets/istp.png")
istp_label = tkinter.Label(istp_frame, image=istp_title)
istp_label.place(x=29, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(istp_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
istp_info = tkinter.Label(istp_frame, text="", font = font_small_title)
istp_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(istp_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(istp_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# isfp 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(isfp_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
isfp_title = tkinter.PhotoImage(file="assets/isfp.png")
isfp_label = tkinter.Label(isfp_frame, image=isfp_title)
isfp_label.place(x=5, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(isfp_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
isfp_info = tkinter.Label(isfp_frame, text="", font = font_small_title)
isfp_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(isfp_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(isfp_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# estp 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(estp_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
estp_title = tkinter.PhotoImage(file="assets/estp.png")
estp_label = tkinter.Label(estp_frame, image=estp_title)
estp_label.place(x=0, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(estp_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
estp_info = tkinter.Label(estp_frame, text="삶을 즐기는 자유로운 성격이에요.\n신나고 스릴 넘치는 일들을 좋아해요.\n남들보다 겁이 없고, 위험한 행동을 자주 해요.\n\n미래보다는 현재가 중요해요.\n바로 지금을 즐기며 사는 게 중요하죠.\n\n무슨 일이든 중심에 서서 관심을 받는 것을 좋아해요.\n뭐든 몸으로 부딪혀 보라!\n궁금한 건 직접 경험해보아야 해요.\n\n현실적으로 생각해요.\n빠르게 결정하고 빠르게 행동하는 걸 선호해요.\n\n\n✔ 학교에서 내 모습은?\n활발하고 자유로운 인상이에요.\n하지만 공부에는 별로 관심이 없어요.\n과제할 시간에 내가 하고 싶은 일을\n하는 게 더 좋아요.", font = font_small_title)
estp_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(estp_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(estp_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

# esfp 결과 화면 ----------------------------------------------------------
# 테스트 로고 배치
logo_label = tkinter.Label(esfp_frame, image=logo_photo)
logo_label.place(x=160, y=10)
# 유형 타이틀
esfp_title = tkinter.PhotoImage(file="assets/esfp.png")
esfp_label = tkinter.Label(esfp_frame, image=esfp_title)
esfp_label.place(x=45, y=100)
# 타이틀 텍스트 
title_name_text = tkinter.Label(esfp_frame, text="당신의 유형은", font = font_small_title)
title_name_text.place(x=30, y=95)
# 유형 설명 텍스트
esfp_info = tkinter.Label(esfp_frame, text="", font = font_small_title)
esfp_info.place(x=25, y= 190)
# 처음으로 돌아가는 버튼 배치
restest_button = tkinter.Button(esfp_frame, image=restest_button_photo, command=go_main)
restest_button.place(x=100, y=580)
# 하단 footer 배치
author_label = tkinter.Label(esfp_frame, text="제작: 한성대학교 IT공과대학 2171110 나은정", font = font_text)
author_label.place(x=75, y=670)
# -------------------------------------------------------------------------

main_screen.mainloop()