import tkinter as tk
import tkinter.ttk
from tkinter import *
from tkinter import ttk
import threading
import queue
import time

import makejson
import client_sub_class as sub


class Pubframe(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.button1 = tk.Button(self.parent, text="new", width=25, command=self.new_parent)
        self.button1.pack()

        self.values = [str(i) + "번" for i in range(1, 101)]
        self.combobox = tk.ttk.Combobox(self.parent, height=15, values=self.values)
        self.combobox.pack()
        self.combobox.set("목록선택")

    def new_parent(self):
        self.newparent = tk.Toplevel(self.parent)


class Subframe(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.label1 = tk.Label(self.parent, text="Loaded MQTT List")
        self.label1.pack()
        # self.label1.grid(row=0, column=1, sticky='n')

        '''self.style = ttk.Style(self.parent)
        self.style.configure('Calendar.Treeview', height=400)  # SOLUTION'''
        self.treeview = tkinter.ttk.Treeview(self, columns=["one", "two", "three"], displaycolumns=["one", "two", "three"])
        self.treeview.pack(fill='x', expand=True)
        # self.treeview.grid(row=2, column=2)

        self.treeview.column("#0", width=20)
        self.treeview.heading("#0", text="num", anchor='w')

        self.treeview.column("one", width=100, anchor="w")
        self.treeview.heading("one", text="topic", anchor="w")

        self.treeview.column("#2", width=50, anchor="w")
        self.treeview.heading("two", text="state", anchor="w")

        self.treeview.column("three", width=200, anchor="w")
        self.treeview.heading("three", text="payload", anchor="w")

        self.treelist = [("A", 50), ("B", 66)]

        for i in range(len(self.treelist)):
            self.treeview.insert('', 'end', text=i, values=self.treelist[i], iid=str(i) + "번")

        self.top = self.treeview.insert('', 'end', text=str(len(self.treelist)), iid="5번", tags="tag1")
        self.top_mid1 = self.treeview.insert(self.top, 'end', text="5-2", values=["SOH", 1], iid="5번-1")

        self.treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>")
        self.treeview.bind("<Double-1>", self.OnDoubleClick)
        self.treeview.bind("<Button-3>", self.popup)

        '''self.ysb = ttk.Scrollbar(self.treeview, orient='vertical', command=self.treeview.yview)
        self.treeview.configure(yscroll=self.ysb.set)
        self.ysb.pack(side='right', fill='y')

        self.xsb = ttk.Scrollbar(self.treeview, orient='horizontal', command=self.treeview.xview)
        self.treeview.configure(xscroll=self.xsb.set)
        self.xsb.pack(side='bottom', fill='x')'''

        '''self.scrollbar = tk.Scrollbar(self.parent)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar["command"] = self.treeview.yview'''

        self.popup_menu = tkinter.Menu(self, tearoff=0)
        self.popup_menu.add_command(label="Delete", command=self.delete_selected)
        self.popup_menu.add_command(label="Select All", command=self.select_all)


    def OnDoubleClick(self, event):
        # item = self.treeview.selection()[0]
        item = self.treeview.identify('item',event.x,event.y)
        print("you clicked on", self.treeview.item(item, "text"))
        if self.treeview.item(item, "text") is not None:
            self.newparent = tk.Toplevel(self.parent)

    def popup(self, event):

        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()
        '''lid = self.treeview.identify_row(event.y)
        if lid:
            self.treeview.selection_set(lid)
            self.contextMenu.post(event.x_root, event.y_root)
        else:
            pass'''

    def delete_selected(self):
        for i in self.curselection()[::-1]:
            self.delete(i)

    def select_all(self):
        self.selection_set(0, 'end')


class Listboxframe(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.scrollbar = tk.Scrollbar(self.parent)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox = tk.Listbox(self.parent, selectmode='extendeed', height=0, yscrollcommand=self.scrollbar.set)
        self.listbox.insert(0, "1번")
        self.listbox.insert(1, "2번")
        self.listbox.insert(3, "3번")
        for line in range(1, 100):
            self.listbox.insert(line, str(line) + "/1000")
        self.listbox.pack(side="left", fill="both", expand=True)

        self.scrollbar["command"] = self.listbox.yview


class Menubar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.menubar = tk.Menu(self)
        self.FileTab = FileTab(self)

        self.menu1 = tk.Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="JSON 불러오기", command=self.FileTab.display)
        self.menu1.add_separator()
        self.menu1.add_command(label="Exit", command=self.close)
        self.menubar.add_cascade(label="File", menu=self.menu1)

        self.menu2 = tk.Menu(self.menubar, tearoff=0, selectcolor="red")
        self.menu2.add_command(label="JSON작성")
        self.menubar.add_cascade(label="Meta정보", menu=self.menu2)

    @staticmethod
    def close():
        sys.exit(0)


class FileTab(tk.Frame):
    def __init__(self, parent, *args, **kewargs):
        tk.Frame.__init__(self, parent, *args, **kewargs)

        self.mighty = tk.LabelFrame(self, text='File')
        self.mighty.pack(expand=1, fill='both', side="right")

        '''slf1 = tk.LabelFrame(self.mighty)
        slf1.pack(side="left", fill='both')
        slf2 = tk.LabelFrame(self.mighty)
        slf2.pack(side="left", fill="both")
        slabel1 = tk.Label(slf1, text="Subscriber", font='bold')
        slabel2 = tk.Label(slf2, text="Topic's name")
        slabel1.pack()
        slabel2.pack()'''
        sshowlabel = tk.Label(self.mighty, text="입력한 결과 : ", relief="groove")
        sshowlabel.pack(anchor='nw', side='top')
        self.topiclabelframe = tk.LabelFrame(self, text="topic")
        self.topiclabelframe.pack()
        self.topiclabel = tk.Label(self.topiclabelframe,text="topic", relief="groove")
        '''label_topic = tk.Label(self.mighty, text="topic : ", padx=5)
        label_topic.pack(anchor='nw', side='top')'''
        label_json = tk.Label(self.mighty, text="tototototo", padx=5)
        label_json.pack(anchor='n', side='top')
        label_topic = tk.Label(self.mighty, text="dev_name : ", padx=5)
        label_topic.pack(anchor='nw', side='top')
        label_topic = tk.Label(self.mighty, text="sensor_name : ", padx=5)
        label_topic.pack(anchor='nw', side='top')
        label_topic = tk.Label(self.mighty, text="interface : ", padx=5)
        label_topic.pack(anchor='nw', side='top')
        label_topic = tk.Label(self.mighty, text="sensor_type : ", padx=5)
        label_topic.pack(anchor='nw', side='top')
        label_topic = tk.Label(self.mighty, text="data_type : ", padx=5)
        label_topic.pack(anchor='nw', side='top')
        label_topic = tk.Label(self.mighty, text="delay_time : ", padx=5)
        label_topic.pack(anchor='nw')

    def display(self):
        makejson.loadjson()
        print(makejson.json_data)


class InfoTab(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.mighty = tk.LabelFrame(self, text='Information')
        # self.mighty.grid(column=0, row=0, padx=8, pady=4)
        self.mighty.pack(expand=1, fill='both', side="right")

        self.btn = Button(self.mighty, text="이미지 불러오기")
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")
        self.btn = Button(self.mighty, text="Mask 좌표 불러오기")
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")
        self.btn = Button(self.mighty, text="Mask 좌표 찍기")
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")
        self.btn = Button(self.mighty, text="Mask 좌표 조절")
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")
        self.btn = Button(self.mighty, text="Mask 좌표 저장")
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")
        self.btn = Button(self.mighty, text="Mask 좌표 삭제", state='disable')
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")


class ActuTab(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.mighty2 = tk.LabelFrame(self, text='Actuator Tab', padx=5, pady=5)
        # self.mighty2.grid(column=0, row=0, padx=8, pady=4)
        self.mighty2.pack(expand=1, fill='both', side='right')

        self.btn = Button(self.mighty2, text="거실 전등", state='disable')
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")
        self.btn = Button(self.mighty2, text="LCD", state='disable')
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")
        self.btn = Button(self.mighty2, text='세탁기', state='disable')
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")
        self.btn = Button(self.mighty2, text="창문", state='disable')
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")
        self.btn = Button(self.mighty2, text="Bbox 좌표 저장", state='disable')
        self.btn.pack(side="top", anchor="center", expand="yes", padx="10", pady="10")


class DDSTab(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.mighty2 = tk.LabelFrame(self, text='Bbox Tab', padx=5, pady=5)
        # self.mighty2.grid(column=0, row=0, padx=8, pady=4)
        self.mighty2.pack(expand=1, fill='both', side='right')

        self.dds = DDS(self.mighty2)
        self.dds.pack()

        
class DDS(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        frame1 = tk.Frame(self.parent, relief="solid", bd=2)
        frame1.pack(side="left", fill="both", expand=True)

        frame2 = tk.Frame(self.parent, relief="solid", bd=2)
        frame2.pack(side="left", fill="both", expand=True)

        frame3 = tk.Frame(self.parent, relief="solid", bd=2)
        frame3.pack(side="left", fill="both", expand=True)

        label1 = tk.Label(frame1, text="Received messages")
        label1.pack()

        label2 = tk.Label(frame2, text="Send message")
        label2.pack()

        label3 = tk.Label(frame3, text="Device")
        label3.pack()

        button1 = tk.Button(frame1, text="Subscribe", pady=5)
        button1.pack(side="bottom", pady=5)
        # button1.bind("<B1-Motion>", publish)

        button2 = tk.Button(frame2, text="Publish", pady=5)
        button2.pack(side="bottom", pady=5)
        # button2.bind("<B1-Motion>", subscribe)

        # Subscribe side
        slf1 = tk.LabelFrame(frame1)
        slf1.pack()
        slf2 = tk.LabelFrame(frame1)
        slf2.pack()
        slabel1 = tk.Label(slf1, text="Subscriber")
        slabel2 = tk.Label(slf2, text="Topic's name")
        slabel1.pack(side="left")
        slabel2.pack(side="left")
        se1 = Entry(slf1)
        se2 = Entry(slf2)
        se1.pack()
        se2.pack()
        sshowlabel = tk.Label(frame1, text="입력한 결과 : "+"\n")
        sshowlabel.pack()
        '''self.button1 = tk.Button(frame1, text="불러오기", command=makejson.loadjson)
        self.button1.pack()'''
        self.button2 = tk.Button(frame1, text="setjson", command=self.setjson)
        self.button2.pack()
        self.sstatlabel = tk.Label(frame1, relief="groove", background="snow", height=20, width=45)
        self.sstatlabel.pack(fill="both")

        '''sT = Text(frame1, height=10, width=45)
        sT.pack(side="bottom")'''

        # Publish side
        plf1 = tk.LabelFrame(frame2)
        plf1.pack()
        plf2 = tk.LabelFrame(frame2)
        plf2.pack()
        self.plabel1 = tk.Label(plf1, text="Publisher")
        self.plabel2 = tk.Label(plf2, text="Topic's name")
        self.plabel1.pack(side="left")
        self.plabel2.pack(side="left")
        self.pe1 = Entry(plf1)
        self.pe1.bind("<Return>", self.calculate)
        self.pe2 = Entry(plf2)
        self.pe2.bind("<Return>", self.calculate)
        self.pe1.pack()
        self.pe2.pack()
        self.pshowlabel = tk.Label(frame2, text="입력한 결과 : "+"\n")
        self.pshowlabel.pack()
        self.pstatlabel = tk.Label(frame2, relief="groove", background="snow", height=20, width=45)
        self.pstatlabel.pack(fill="both")

        '''pT = Text(frame2, height=10, width=45)
        pT.pack(side="bottom")'''

        # Function side
        flf1 = LabelFrame(frame3)
        flf1.pack(fill="both", pady=5)
        flf2 = LabelFrame(frame3)
        flf2.pack(fill="both", pady=5)
        flf3 = LabelFrame(frame3)
        flf3.pack(fill="both", pady=5)

        airLB = Label(flf1, text="Air conditioner")
        airLB.pack()
        airStateLB = Label(flf1, text="On")
        airStateLB.pack()
        airBon = Button(flf1, text="On")
        airBon.pack()
        # airBon.bind("<Button-1>", airBClick)
        airBoff = Button(flf1, text="Off")
        airBoff.pack()

        ledLB = Label(flf2, text="Lamp")
        ledLB.pack()
        ledStateLB = Label(flf2, text="On")
        ledStateLB.pack()
        ledon = Button(flf2, text="On")
        ledon.pack()
        ledoff = Button(flf2, text="Off")
        ledoff.pack()

        SprinklerLB = Label(flf3, text="TV")
        SprinklerLB.pack()
        SprinStateLB = Label(flf3, text="Off")
        SprinStateLB.pack()
        Sprinkleron = Button(flf3, text="On")
        Sprinkleron.pack()
        Sprinkleroff = Button(flf3, text="Off")
        Sprinkleroff.pack()

    def setjson(self):
        makejson.loadjson()
        self.statlabel.config(text=makejson.json_data)

    def calculate(self, *args):
        self.pshowlabel.configure(text="결과: " + str(eval(self.pe1.get())) + str(eval(self.pe2.get())))


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.queue = queue.Queue()
        self.listbox = tk.Listbox(self, width=20, height=5)
        self.progressbar = ttk.Progressbar(self, orient='horizontal',
                                           length=300, mode='determinate')
        self.button = tk.Button(self, text="Start", command=self.spawnthread)
        self.listbox.pack(padx=10, pady=10)
        self.progressbar.pack(padx=10, pady=10)
        self.button.pack(padx=10, pady=10)

    def spawnthread(self):
        self.button.config(state="disabled")
        self.thread = ThreadedClient(self.queue)
        self.thread.start()
        self.periodiccall()

    def periodiccall(self):
        self.checkqueue()
        if self.thread.is_alive():
            self.after(100, self.periodiccall)
        else:
            self.button.config(state="active")

    def checkqueue(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.listbox.insert('end', msg)
                self.progressbar.step(25)
            except Queue.Empty:
                pass


class ThreadedClient(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for x in range(1, 5):
            time.sleep(2)
            msg = "Function %s finished..." % x
            self.queue.put(msg)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # create gui here
        # self.Pubframe = Pubframe(self)
        self.Subframe = Subframe(self)
        # self.Selectframe = Selectframe(self)
        # self.Controlframe = Controlframe(self)
        # self.Listboxframe = Listboxframe(self)
        # self.Stateframe = Stateframe(self)
        # self.DDS = DDS(self)

        self.tabControl = ttk.Notebook(self.parent, height=400)
        self.Filetab = FileTab(self.tabControl)
        self.InfoTab = InfoTab(self.tabControl)
        self.ActuTab = ActuTab(self.tabControl)
        self.DDSTab = DDSTab(self.tabControl)
        self.tabControl.add(self.Filetab, text="File")
        self.tabControl.add(self.InfoTab, text="Information")
        self.tabControl.add(self.ActuTab, text="Actuator Tab")
        self.tabControl.add(self.DDSTab, text="DDS Tab")
        self.tabControl.pack(side='bottom', fill='both')
        # self.tabControl.grid(row=1, column=0)
        # self.Listboxframe.pack(side="left", fill="both", anchor="w")
        # self.Pubframe.pack(side="left", fill="both", expand=True)
        self.Subframe.pack(side="bottom", fill="both", expand=True)
        # self.Subframe.grid(row=0, column=1)
        # self.Selectframe.pack(side="bottom", expand=True)
        # self.Controlframe.pack(side="bottom", fill="both", expand=True)
        # self.Stateframe.pack(side="right",anchor="e")
        # self.DDS.pack()

        self.Menubar = Menubar(self)
        self.parent.config(menu=self.Menubar.menubar)


def run():
    root = tk.Tk()
    root.title("Smart home")
    MainApplication(root).pack(fill='both', expand=TRUE)
    root.mainloop()


def run2():
    print('Thread2222')


if __name__ == "__main__":
    mq = sub.MyMQTTClass()
    '''root = tk.Tk()
    root.title("Smart home")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
'''
    run()