from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import gtts
from tika import parser


class f_path:
    def __init__(self):
        self.master=Tk()
        self.master.geometry("135x120")
        self.master.resizable(width=False, height=False)

        self.mainframe=Frame(self.master)
        self.mainframe.pack()
        
        self.language = IntVar()
        self.language.set(1)

        ins_but = Button(self.mainframe, text='Выбрать файл', command=self.insert_file)
        ins_but.pack(pady = 5)
        ru = Radiobutton(self.mainframe, text="Русский", variable=self.language, value=1)
        ru.pack()
        en = Radiobutton(self.mainframe, text="English", variable=self.language, value=2)
        en.pack()
        button = Button(self.mainframe, text="Перевести",command=self.sel_lang)
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
            
if __name__ == '__main__':
    f_path()
