from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile

class Frontend:
    def select_file(self):
        file = askopenfile(parent=self.root, mode='rb', title='File Explorer')
        return file

    def frontend(self):
        self.root = Tk()
        self.root.title('TypeGrad')
        coolgrey = '#464a4f'
        canvas1 = Canvas(self.root, width=370, height=300, bg='#ffffff',
                            bd=10)

        canvas1.pack()
        self.root.maxsize(370,300)
        self.root.minsize(370,300)
        image1 = r'C:\Users\gsbaw\PycharmProjects\TypeGrad\Lib\2207.jpg'

        img1 = ImageTk.PhotoImage(Image.open(image1))
        panel1 = Label(self.root, image=img1, borderwidth=0)

        panel1.place(x=122, y=16)
        button1 = Button(text='Select File',command=self.select_file, bg='#464a4f', fg='white', width=40,
                            height=5, border=5, font=('Aharoni', 8, 'bold'))
        canvas1.create_window(185, 235, window=button1)
        filemenu = Menu(Menu(), tearoff=10)
        self.root.config(menu=filemenu)
        self.root.mainloop()


