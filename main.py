from tkinter import *

# 사용자 이름 저장, 테스트 시작 함수
def sendUserName() :
    global user_name
    user_name = entry_name.get()

# --------------------------------시작 화면 구현----------------------------
#-------------------- 시작 윈도우 생성 ---------------
start_screen = Tk()
start_screen.geometry("400x700")
start_screen.title("대학생 유형 테스트")
start_screen.resizable(False, False)
# -----------------------------------------------------

# -------------------------- 시작 화면 디자인 ---------
# 타이틀 이미지 배치
title_photo = PhotoImage(file="assets/title.png")
title_label = Label(start_screen, image=title_photo)
title_label.place(x=100, y=110)
# 이름 입력 설명 배치
text_label = Label(start_screen, text="테스트를 시작하기 전에\n당신의 이름을 입력해주세요!")
text_label.place(x=125, y=330)
# 이름 엔트리 박스 배치
entry_name = Entry(start_screen, width=10)
entry_name.place(x=165, y=370)
# 시작 버튼 배치
start_photo = PhotoImage(file="assets/startbutton.png")
start_button = Button(start_screen, image=start_photo, command=sendUserName)
start_button.place(x=130, y=420)
# 하단 footer 배치
author_label = Label(start_screen, text="제작: 한성대학교 IT공과대학 2171110 나은정")
author_label.place(x=75, y=670)
# ---------------------------------------------------------------------------
start_screen.mainloop()