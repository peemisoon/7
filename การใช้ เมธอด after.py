import tkinter as tk


root = tk.Tk()
root.title("Countdown Example")
root.geometry("400x300")


label = tk.Label(root, text="", font=("TH Sarabun New", 20))
label.pack(pady=50)


def countdown(time_left):
    if time_left > 0:
        label.config(text=f"เหลือเวลา: {time_left} วินาที")
        root.after(1000, countdown, time_left - 1)  
    else:
        
        label.config(
            text="ชื่อ-นามสกุล : ไอศูรย์ อนุศักดิ์ชัยกุล\n"
                 "ชื่อเล่น : ภีม\n"
                 "ห้องเรียน : ม.5/8 เลขที่ 6\n"
                 "แผนการเรียน : วิทย์-คณิต\n"
                 "อยากเรียนคณะ : กราฟิกดีไซน์"
        )


countdown(10)


root.mainloop()
