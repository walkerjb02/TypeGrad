from PIL import Image


class Root():
    def __init__(self):
        img = Image.open(r'C:\Users\gsbaw\PycharmProjects\TypeGrad\Lib\000{}.jpg'.format(1))
        self.pixels = img.load()
        self.width, self.height = img.size
        self.num_lines = int(self.height * 0.75)
