from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile

def select_file():
    file = askopenfile(parent=root, mode='rb', title='File Explorer')
    return file

root = Tk()
root.title('TypeGrad')
coolgrey = '#464a4f'
canvas1 = Canvas(root, width=370, height=300, bg='#006df2', relief='groove',
                    bd=10)
canvas1.pack()
root.maxsize(370,300)
root.minsize(370,300)
image = r'C:\Users\gsbaw\PycharmProjects\PointsOrganizer\background.png'
image1 = r'C:\Users\gsbaw\PycharmProjects\TypeGrad\Lib\2207.jpg'
img = ImageTk.PhotoImage(Image.open(image))
panel = Label(root, image=img)
panel.place(x=0, y=0)
img1 = ImageTk.PhotoImage(Image.open(image1))
panel1 = Label(root, image=img1)
panel1.place(x=115, y=16)
button1 = Button(text='Select File',command=select_file, bg='#464a4f', fg='white', width=40,
                    height=5, border=5, font=('Aharoni', 8, 'bold'))
canvas1.create_window(185, 235, window=button1)
filemenu = Menu(Menu(), tearoff=10)
filemenu.add_command(label="TypeGrad", command=None, font=('Aharoni', 90, 'bold'))
filemenu.add_separator()
root.config(menu=filemenu)
root.mainloop()
