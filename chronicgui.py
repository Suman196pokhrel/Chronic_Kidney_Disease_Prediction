from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox as tmsg
import tkinter.filedialog as fldg
import tkinter.font as tkFont
# import saved_model
from sklearn.preprocessing import LabelEncoder

from CHRONIC_OOP import ChronicClass
import sys
import pandas as pd
import random
import numpy as np


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(font=("comic sans ms", 10))


class ChronicKidneyGui(Tk):

    def __init__(self):
        super().__init__()
        # logo_image1 = ImageTk.open('300Logo.png')
        # self.myimage = ImageTk.PhotoImage(Image.open('300Logo.png'))
        # self.iconphoto(False,self.myimage)

        # Window Geometry
        self.geometry('1110x570')

        # Window Title
        self.title('Chronic Kidney Disease Prediction')

        # Root Color
        self.configure(bg='#2C3539')

        # Fonst Style
        self.fontStyle = tkFont.Font(family="comic sans ms", size=15)

        # Menu Bar
        self.mainmenue = Menu(self, font=self.fontStyle)
        self.filemenue = Menu(self.mainmenue, tearoff=False)
        self.filemenue.add_command(label="Open", command=lambda: print('Its Working'))
        self.filemenue.add_command(label='Save As', command=lambda: print('Its woring'))
        self.filemenue.add_command(label='Exit', command=self.quit)
        self.config(menu=self.mainmenue)
        self.mainmenue.add_cascade(label='File', menu=self.filemenue)

        self.Edit_menu = Menu(self.mainmenue, tearoff=False)
        self.Edit_menu.add_command(label="Clear All", command=lambda: print('Its Working'))
        self.Edit_menu.add_command(label="Find Number of text", command=lambda: print('Its Working'))
        self.Edit_menu.add_command(label="Replace text", command=lambda: print('Its Working'))
        self.config(menu=self.mainmenue)
        self.mainmenue.add_cascade(label="Edit", menu=self.Edit_menu)

        self.view_menu = Menu(self.mainmenue, tearoff=False)
        self.zoom_menu = Menu(self.view_menu, tearoff=False)
        self.zoom_menu.add_command(label="Increase font", command=lambda: print("Its woring"))
        self.zoom_menu.add_command(label="Decrease Font", command=lambda: print("Its woring"))
        self.zoom_menu.add_command(label="Restore To Default", command=lambda: print("Its woring"))
        self.view_menu.add_cascade(label="Change Font Size", menu=self.zoom_menu)
        self.config(menu=self.mainmenue)
        self.mainmenue.add_cascade(label="View", menu=self.view_menu)

        self.Format_menu = Menu(self.mainmenue, tearoff=False)
        self.Format_menu.add_command(label="Default Theme", command=lambda: print("Its woring"))
        self.Format_menu.add_command(label="Dark Theme", command=lambda: print("Its woring"))
        self.config(menu=self.mainmenue)
        self.mainmenue.add_cascade(label="Format", menu=self.Format_menu)

        # configuring Menue Items

        #

        # Widgets Inside The main Window

        self.frame_1 = Frame(self, borderwidth=4, relief='groove', bg='#98AFC7')
        # self.frame_1.grid(row=0, column=0,padx=5)
        self.frame_1.place(relx=0.001, rely=0)

        self.label_First_info = Label(self.frame_1, text="Fill The Data On The Fields",
                                      font=("comic sans ms", 15, "italic", 'underline'), borderwidth=2, relief='groove')
        self.label_First_info.grid(row=0, column=0, padx=10, pady=10, columnspan=6)

        self.label_sg = Label(self.frame_1, text="Sg(Ex:1.02):", font=("comic sans ms", 10, "italic"))
        self.label_sg.grid(row=1, column=0, padx=1, pady=10)

        self.entry_wid_sg = Entry(self.frame_1, width=15, borderwidth=3)
        self.entry_wid_sg.grid(row=1, column=1)

        self.label_al = Label(self.frame_1, text="Al(Ex:4) :", font=("comic sans ms", 10, "italic"))
        self.label_al.grid(row=2, column=0, padx=1, pady=10)

        self.entry_wid_al = Entry(self.frame_1, width=15, borderwidth=3)
        self.entry_wid_al.grid(row=2, column=1)

        self.label_sc = Label(self.frame_1, text="Sc(Ex:3.8) :", font=("comic sans ms", 10, "italic"))
        self.label_sc.grid(row=3, column=0, padx=1, pady=10)

        self.entry_wid_sc = Entry(self.frame_1, width=15, borderwidth=3)
        self.entry_wid_sc.grid(row=3, column=1)

        self.label_hemo = Label(self.frame_1, text=" Hemo (Ex:11.2):", font=("comic sans ms", 10, "italic"))
        self.label_hemo.grid(row=4, column=0, padx=1, pady=10)

        self.entry_wid_hemo = Entry(self.frame_1, width=15, borderwidth=3)
        self.entry_wid_hemo.grid(row=4, column=1)

        self.label_pcv = Label(self.frame_1, text="Pcv (Ex:32):", font=("comic sans ms", 10, "italic"))
        self.label_pcv.grid(row=5, column=0, padx=1, pady=10)

        self.entry_wid_pcv = Entry(self.frame_1, width=15, borderwidth=3)
        self.entry_wid_pcv.grid(row=5, column=1)

        self.label_wbcc = Label(self.frame_1, text="Wbcc (Ex:6700):", font=("comic sans ms", 10, "italic"))
        self.label_wbcc.grid(row=6, column=0, padx=1, pady=10)

        self.entry_wid_wbcc = Entry(self.frame_1, width=15, borderwidth=3)
        self.entry_wid_wbcc.grid(row=6, column=1)

        self.label_rbcc = Label(self.frame_1, text="Rbcc (Ex:3.9):", font=("comic sans ms", 10, "italic"))
        self.label_rbcc.grid(row=7, column=0, padx=1, pady=10)

        self.entry_wid_rbcc = Entry(self.frame_1, width=15, borderwidth=3)
        self.entry_wid_rbcc.grid(row=7, column=1)

        self.label_htn = Label(self.frame_1, text="Htn (Ex:yes or no):", font=("comic sans ms", 10, "italic"))
        self.label_htn.grid(row=8, column=0, padx=1, pady=10)

        self.entry_wid_htn = Entry(self.frame_1, width=15, borderwidth=3)
        self.entry_wid_htn.grid(row=8, column=1)

        self.submit_btn = Button(self.frame_1, text='Run Diagnostics', font=("comic sans ms", 10, "italic"),
                                 command=self.run_diagnosis)
        self.submit_btn.grid(row=9, column=1, pady=10)

        # Second Frame On The Right Side

        self.frame_2 = Frame(self, borderwidth=4, relief='groove', bg='#437C17')
        # self.frame_2.grid(row=0, column=1,sticky=N)
        self.frame_2.place(x=290, y=0)

        self.label_result = Label(self.frame_2, text="Results On Console",
                                  font=("comic sans ms", 15, "italic", 'underline'), borderwidth=2, relief='groove')
        self.label_result.grid(row=0, column=1)

        self.text_wid_output = Text(self.frame_2, borderwidth=4, relief='groove', height=18, width=100)
        self.text_wid_output.grid(row=1, column=1)
        self.text_wid_output.tag_configure('stdout', )
        sys.stdout = TextRedirector(self.text_wid_output, "stdout")
        # sys.stderr = TextRedirector(self.text_wid_output, "stderr")

        # # Final Frame For Showing Prediction
        #
        self.frame_3 = Frame(self, borderwidth=4, relief='groove', bg='#4088C7')
        # self.frame_3.grid(row=1, column=1,sticky=NW)
        self.frame_3.place(x=290, y=343)

        self.label_result = Label(self.frame_3, text="Final Classification",
                                  font=("comic sans ms", 15, "italic", 'underline'), borderwidth=2, relief='groove')
        self.label_result.grid(row=0, column=0)

        self.text_wid_final_classification_output = Text(self.frame_3, height=2, width=50, borderwidth=4,
                                                         relief='groove', font=("comic sans ms", 20))
        self.text_wid_final_classification_output.grid(row=1, column=0)

        # Some Extra Features
        self.frame_4 = Frame(self, borderwidth=4, relief='groove', bg='#98AFC7')
        self.frame_4.place(x=290, y=300)

        # self.label_extra_featues = Label(self.frame_4, text="Extra Features", borderwidth=3, relief='groove',
        #                                 font=("comic sans ms", 12, "italic"))
        # self.label_extra_featues.grid(row=0, column=0)

        self.extra_btn_plot_output = Button(self, text='Plot The Output', font=("comic sans ms", 10, "italic"))
        self.extra_btn_plot_output.place(x=200,y=477)

        self.extra_btn_plot_models_efficiency = Button(self, text="Plot Model's Efficiency",
                                                       font=("comic sans ms", 10, "italic"))
        self.extra_btn_plot_models_efficiency.place(x=320,y=477)

        # FInal Dummy Area
        self.button_dummy_generate = Button(self, text='Generate Data', font=("comic sans ms", 10, "italic"),
                                   command=self.data_generation)
        self.button_dummy_generate.place(x=1, y=477)

        self.button_dummy_insert = Button(self, text='Insert Data', font=("comic sans ms", 10, "italic"),
                                   command=self.insert_data)
        self.button_dummy_insert.place(x=110, y=477)

    def run_diagnosis(self):
        self.text_wid_final_classification_output.delete('1.0', 'end')
        self.text_wid_output.delete('1.0','end')
        self.feature_list_1 = []
        f1 = float(self.entry_wid_sg.get())
        f2 = float(self.entry_wid_al.get())
        f3 = float(self.entry_wid_sc.get())
        f4 = float(self.entry_wid_hemo.get())
        f5 = float(self.entry_wid_pcv.get())
        f6 = float(self.entry_wid_wbcc.get())
        f7 = float(self.entry_wid_rbcc.get())
        f8 = float(self.entry_wid_htn.get())
        self.feature_list_1.append([f1, f2, f3, f4, f5, f6, f7, f8])
        logic_obj = ChronicClass()
        self.predicted_value = logic_obj.predict_fun(feature_list=self.feature_list_1)
        output = ''
        print(self.predicted_value)
        if self.predicted_value == 0:
            output = 'NOT SUFFERING\n FROM CKD'
            self.text_wid_final_classification_output.configure(fg='green')
        else:
            output = 'SUFFERING FROM CDK'
            self.text_wid_final_classification_output.configure(fg='red')

        self.text_wid_final_classification_output.insert('1.0', output)

    def data_generation(self):
        self.dff = pd.read_csv('C:\Imp softwares\Pycharm\Pycharm projects\Chronic kidney disease\data_generate.csv')
        self.dff = self.dff.dropna(axis=0)

        for column in self.dff.columns:
            if self.dff[column].dtype == np.number:
                continue
            self.dff[column] = LabelEncoder().fit_transform(self.dff[column])

        self.random_index = random.randint(0, 159)
        self.random_row = self.dff.iloc[self.random_index]
        # print(self.random_row)
        self.sg = self.random_row['Specific Gravity']
        self.al = self.random_row['Albumin']
        self.sc = self.random_row['Serum Creatinine']
        self.hemo = self.random_row['Hemoglobin']
        self.pcv = self.random_row['Packed Cell Volume']
        self.wbc = self.random_row['White Blood Cell Count']
        self.rbc = self.random_row['Red Blood Cell Count']
        self.htn = self.random_row['Hypertension']
        self.Output_2 = self.random_row['Class']



        self.label_dummy = Label(self, text=f'Values from Different Dataset\nIndex_Number => {self.random_index}  sg => {self.sg}      al => {self.al}     sc => {self.sc}    hemo => {self.hemo}     pcv => {self.pcv}    wbc => {self.wbc}     rbc => {self.rbc}    htn => {self.htn}     ', font=("comic sans ms", 10, "italic"))
        self.label_dummy.place(x=1, y=513)

    def insert_data(self):
        # Clearing all entry fields
        self.entry_wid_sg.delete(0,'end')
        self.entry_wid_al.delete(0, 'end')
        self.entry_wid_sc.delete(0, 'end')
        self.entry_wid_hemo.delete(0, 'end')
        self.entry_wid_pcv.delete(0, 'end')
        self.entry_wid_wbcc.delete(0, 'end')
        self.entry_wid_rbcc.delete(0, 'end')
        self.entry_wid_htn.delete(0, 'end')

        # Inserting Data on all Entry fields
        self.entry_wid_sg.insert(0, self.sg)
        self.entry_wid_al.insert(0, self.al)
        self.entry_wid_sc.insert(0, self.sc)
        self.entry_wid_hemo.insert(0, self.hemo)
        self.entry_wid_pcv.insert(0, self.pcv)
        self.entry_wid_wbcc.insert(0, self.wbc)
        self.entry_wid_rbcc.insert(0, self.rbc)
        self.entry_wid_htn.insert(0, self.htn)









if __name__ == '__main__':
    mainwin = ChronicKidneyGui()

    mainwin.mainloop()
