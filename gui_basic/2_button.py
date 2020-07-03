from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로 + x 좌표 + y 좌표

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 ( 창 크기 변경 불가 )

root.mainloop() # 메인 루프를 통해 창이 닫히지 않도록 한다.
