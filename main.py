from Tkinter import *
import threading
import tkFont
import numpy as np
from datetime import datetime


class App:

    def __init__(self, master):
        self.customFont = tkFont.Font(family="Helvetica", size=100)
        self.customFont2 = tkFont.Font(family="Helvetica", size=32)
        self.time = Label(master, text="NULL", bg="#153847", fg="#fff", font=self.customFont)
        self.act = Label(master, text="ACT", bg="#153847", fg="#fff", font=self.customFont2)
        self.done = Button(master, text="", bg="#153847", fg="#fff", command=self.quit, bd=0, activeforeground="#fff",
                           activebackground="#10688F", highlightthickness=0)

        self.time.pack(expand=1, fill=BOTH)
        self.done.pack(side=BOTTOM, fill=X)
        self.act.pack(side=BOTTOM, fill=X)

        master.bind("<Left>", self.left)
        master.bind("<Right>", self.right)

    def print_time(self):
        t = threading.Timer(1.0, self.print_time)
        t.daemon = True
        t.start()
        global data
        global var
        global txt
        global start
        global left
        global add
        if left:
            #end = data[var][0] * 60 * 60 + data[var][1] * 60 + data[var][2]
            current = start
            now = datetime.now()
            end = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
            m, s = divmod(int(end - current), 60)
            h, m = divmod(m, 60)
            if h > 0:
                tm = "%d:%02d:%02d" % (h, m, s)
            else:
                tm = "%02d:%02d" % (m, s)
            self.time.configure(text=tm)
            self.act.configure(text=txt[0])

        else:
            if var == len(data) - 2:
                end = data[var][0] * 60 * 60 + data[var][1] * 60 + data[var][2]
                now = datetime.now()
                current = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
            elif var == len(data) - 1:
                end = data[var][0] * 60 * 60 + data[var][1] * 60 + data[var][2] + \
                      data[1][0] * 60 * 60 + data[1][1] * 60 + data[1][2]
                now = datetime.now()
                current = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
            else:
                end = data[var][0] * 60 * 60 + data[var][1] * 60 + data[var][2] + add
                now = datetime.now()
                current = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

            '''while int(end - current) < 1:
                var += 1
                if var == len(data):
                    print "0000"
                    var = 0
                elif var == 0:
                    global add
                    add = 0

                if var == len(data) - 2:
                    end = data[var][0] * 60 * 60 + data[var][1] * 60 + data[var][2]
                    now = datetime.now()
                    current = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
                elif var == len(data) - 1:
                    end = data[var][0] * 60 * 60 + data[var][1] * 60 + data[var][2] + \
                          data[1][0] * 60 * 60 + data[1][1] * 60 + data[1][2]
                    now = datetime.now()
                    current = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
                else:
                    end = data[var][0] * 60 * 60 + data[var][1] * 60 + data[var][2] + add
                    now = datetime.now()
                    current = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()'''

            m, s = divmod(int(end - current), 60)
            h, m = divmod(m, 60)
            if h > 0:
                tm = "%d:%02d:%02d" % (h, m, s)
            else:
                tm = "%02d:%02d" % (m, s)
            self.time.configure(text=tm)
            self.act.configure(text=txt[var])

            if int(end - current) < 1:
                var += 1

            if var == 0:
                global add
                add = 0
            elif var == len(data):
                var = 0



    def quit(self):
        root.destroy()

    def left(self, event):
        self.time.configure(bg="#333")
        self.act.configure(bg="#333")
        self.done.configure(bg="#333")
        global left
        left = 1
        global start
        now = datetime.now()
        start = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

    def right(self, event):
        global left
        if left:
            global add
            now = datetime.now()
            add += (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() - start
        else:
            global var
            global add
            var += 1
            if var == len(data):
                var = 0
                add = 0

            else:
                now = datetime.now()
                add = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() - \
                      (data[var - 1][0] * 60 * 60 + data[var - 1][1] * 60 + data[var - 1][2])

        self.time.configure(bg="#153847")
        self.act.configure(bg="#153847")
        self.done.configure(bg="#153847")
        left = 0


def close(event):
    root.destroy()


def read():
    return np.genfromtxt("data.txt", delimiter=",")


def txt_read():
    with open('act.txt', 'r') as myfile:
        dat = myfile.readlines()
    return dat


def ck(a):
    x = 1
    now = datetime.now()
    current = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    while 1:
        if x + 1 < len(a) and abs(a[x+1][0] * 60 * 60 + a[x+1][1] * 60 + a[x+1][2] - current) < abs(a[x][0] * 60 * 60 + \
                        a[x][1] * 60 + a[x][2] - current):
            x += 1
        else:
            break
    return x


root = Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1)
root.attributes('-fullscreen', True)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.title("Schedule")
root.bind("<Escape>", close)

start = 0
left = 0
add = 0
data = read()
txt = txt_read()
var = ck(data)

app = App(root)
app.print_time()

root.mainloop()
