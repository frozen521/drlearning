import tkinter
win=tkinter.Tk()
win.title('hello wodk')
win.geometry('400x300')
def showinfo():
    # 获取输入的内容
    print(entry.get())
entry = tkinter.Entry(win)
entry.pack()
button = tkinter.Button(win, text="按钮", command=showinfo)
button.pack()
win.mainloop()