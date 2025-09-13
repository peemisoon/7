import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        base = float(entry_base.get())
        height = float(entry_height.get())
        area = 0.5 * base * height
        label_result.config(text=f"พื้นที่สามเหลี่ยม = {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกตัวเลขให้ถูกต้อง")


root = tk.Tk()
root.title("โปรแกรมคำนวณพื้นที่สามเหลี่ยม")
root.geometry("300x200")


label_base = tk.Label(root, text="กรอกความยาวฐาน:")
label_base.pack(pady=5)
entry_base = tk.Entry(root)
entry_base.pack()


label_height = tk.Label(root, text="กรอกความสูง:")
label_height.pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()


btn_calculate = tk.Button(root, text="คำนวณพื้นที่", command=calculate_area)
btn_calculate.pack(pady=10)


label_result = tk.Label(root, text="พื้นที่สามเหลี่ยม = ")
label_result.pack(pady=5)


root.mainloop()
