from Tkinter import *
import threading
import tkFont
import numpy as np
from datetime import datetime


class App:

    def __init__(self, master):

        global act
        self.customFont = tkFont.Font(family="Helvetica", size=180)
        self.customFont2 = tkFont.Font(family="Helvetica", size=48)
        self.time = Label(master, text="NULL", bg="#153847", fg="#fff", font=self.customFont)
        self.act = Label(master, text=act, bg="#153847", fg="#fff", font=self.customFont2)
        self.done = Button(master, text="", bg="#153847", fg="#fff", command=self.quit, bd=0, activeforeground="#fff",
                           activebackground="#10688F", highlightthickness=0)

        self.time.pack(expand=1, fill=BOTH)
        self.done.pack(side=BOTTOM, fill=X)
        self.act.pack(side=BOTTOM, fill=X)

        now = datetime.now()
        self.start = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

        #master.bind("<Left>", self.left)
        #master.bind("<Right>", self.right)

    def print_time(self):
        t = threading.Timer(1.0, self.print_time)
        t.daemon = True
        t.start()
        self.time.configure(bg="#333")
        self.act.configure(bg="#333")
        self.done.configure(bg="#333")

        now = datetime.now()
        current = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        m, s = divmod(int(self.start + 15*60 - current), 60)
        h, m = divmod(m, 60)
        if h > 0:
            tm = "%d:%02d:%02d" % (h, m, s)
        else:
            tm = "%02d:%02d" % (m, s)

        self.time.configure(text=tm)
        #self.act.configure(text=" ")

        if (self.start + 15 * 60 - current < 1):
            self.quit()


    def quit(self):
        root.destroy()

    #def left(self, event):
        '''self.time.configure(bg="#333")
        self.act.configure(bg="#333")
        self.done.configure(bg="#333")
        global left
        left = 1
        global start
        now = datetime.now()
        start = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()'''

    #def right(self, event):
        '''global left
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
        left = 0'''


def close(event):
    root.destroy()

global act
act = raw_input("Enter the current activity: ")


root = Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1)
root.attributes('-fullscreen', True)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.title("Schedule")
root.bind("<Escape>", close)


app = App(root)
app.print_time()

root.mainloop()
