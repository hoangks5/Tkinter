from tkinter import Tk, Frame, BOTH

# Cách khởi tạo 1 chương trình chính

# Lớp Tk được dùng để tạo cửa sổ, lớp Frame dùng để quản lý các widget
class Ex(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,background="white")
        self.parent = parent
        self.initUI()

# Chúng ta định nghĩa lớp Excample kế thừa từ lớp Frame.
# Lớp Frame là một widget dùng để quản lý các widet khác – các lớp kiểu này được gọi chung là containter hoặc layout.
# Trong phương thức khởi tạo __init__() chúng ta gọi lại phương thức khởi tạo từ lớp Frame và đưa vào tham số màu nền.
    def initUI(self):

        # Phương thức title() sẽ thay đổi tiêu đề cửa sổ.
        self.parent.title("Tiêu đề")

        # Phương thức pack() có tác dụng sắp xếp vị trí các widget trước khi gắn chúng lên cửa sổ chính.
        # Tham số fill=BOTH sẽ dãn widget ra theo chiều ngang và chiều rộng, tức là widget đó sẽ chiếm toàn bộ không gian cửa sổ.
        self.pack(fill=BOTH, expand=1)

# Ở dòng trên chúng ta tạo một cửa sổ và gán vào biến root để quản lý.
# Cửa sổ luôn phải được tạo trước khi tạo các widget.
root = Tk()

# Phương thức geometry() quy định kích thước cửa sổ và vị trí hiển thị trên màn hình.
# Hai tham số đầu tiên là kích thước cửa sổ, hai phương thức sau là vị trí của cửa sổ trên màn hình.
root.geometry("250x150+300+300")
app = Ex(root)
root.mainloop()