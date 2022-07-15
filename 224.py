from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import gtts
from tika import parser


class f_path:
    def __init__(self,master):
        self.master=master
        self.master.geometry("135x120")
        self.master.resizable(width=False, height=False)

        self.mainframe=Frame(master)
        self.mainframe.pack()
        
        self.language = IntVar()
        self.language.set(1)

        ins_but = Button(master, text='Выбрать файл', command=self.insert_file)
        ins_but.pack(pady = 5)
        ru = Radiobutton(master, text="Русский", variable=self.language, value=1)
        ru.pack()
        en = Radiobutton(master, text="English", variable=self.language, value=2)
        en.pack()
        button = Button(master, text="Перевести",command=self.sel_lang)
        button.pack()

    def sel_lang(self):
        if self.language.get() == 1:
            self.lang = 'ru'
        else:
            self.lang = 'en'
        self.output_file()

            
    def insert_file(self):
        try:
            self.file_name = fd.askopenfilename(filetypes=[('PDF files', '*.pdf')])
            self.pdf = parser.from_file(self.file_name)
        except PermissionError:
            mb.showerror("Error", "Вы не выбрали файл")


    def output_file(self):
        output_file = gtts.gTTS(self.pdf['content'], lang = self.lang)
        output_file.save('output_file.mp3')
            
root = Tk()
my_gui = f_path(root)
root.mainloop()
