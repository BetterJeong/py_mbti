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

logo_photo = tkinter.PhotoImage(file="assets/logo.png")
restest_button_photo = tkinter.PhotoImage(file="assets/retestButton.png")

# font 설정
font_main = font.Font(family = "Arial", size = 14, weight = "bold")
font_small_title = font.Font(family = "Arial", size = 12)
font_text = font.Font(family = "Arial", size = 10)

def go_main() :
    print("well")


infp_frame = tkinter.Frame(main_screen, width=400, height=700)
infp_frame.place(x = 0,y = 0)

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

main_screen.mainloop()