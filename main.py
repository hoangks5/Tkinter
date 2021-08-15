import tkinter as tk
from tkinter.constants import W
from PIL import Image, ImageTk


# Khởi tạo của sổ
root = tk.Tk()
root.title("Tiêu đề")
root.configure(background="pink")

# Chỉnh kích thước của cửa sổ
canvas = tk.Canvas(root,width=600,height=800)
canvas.grid(columnspan=3,rowspan=4)

# Ảnh Background
logo = Image.open('0.png') # '0.png' Đường dẫn file ảnh
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

# Text
ins = tk.Label(root,text="Ảo ma Canada",font="Ralaway")
ins.grid(columnspan=3,column=0,row=1)

# Textbox
textentry = tk.Entry(root,width=20,bg="white")
textentry.grid(column=1,row=2,sticky=W)

# Nút nhấn
but_text = tk.StringVar()
but_btn = tk.Button(root,textvariable=but_text,font="Raleway")
but_text.set("Ấn vào đây")
but_btn.grid(column=1,row=3)

# Chạy
root.mainloop()