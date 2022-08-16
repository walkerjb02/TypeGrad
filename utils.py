import numpy as np
import json
from init import Root
from PIL import Image
import math

class Utils(Root):
    def to_json(self, suffix, category, contents):
        fp = r'C:\Users\gsbaw\PycharmProjects\TypeGrad\Lib'
        with open(r'{}\Storage{}.json'.format(fp,suffix),'r+') as file:
            init = json.loads(file.read())
            init[f"{category}"] = contents
            final = json.dumps(init)
            with open(r'{}\Storage{}.json'.format(fp,suffix),'w') as nfile:
                nfile.write(final)

    def clear_json(self, upper):
        keys = ['Len']
        nums = [i for i in range(upper)]
        keys.extend(nums)
        f = keys
        keyindexer = 0
        fp = r'C:\Users\gsbaw\PycharmProjects\TypeGrad\Lib'
        try:
            while keyindexer < len(f):
                with open(r'{}\Storage{}.json'.format(fp,f[keyindexer]), 'w') as file:
                    file.write("""{"Sections": []}""")
                keyindexer += 1

        except Exception:
            pass

    def get_full(self, width, height, pixels):
        lst = []
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                avgval = (255 - ((r + g + b) / 3))
                lst.append(avgval)
        with open('Storage.py', 'w') as file:
            file.write(f'lst = [{lst}]')
        return lst

    def get_section(self, widthstart, widthstop, heightstart, heightstop, pixels, iterindex):
        section = []
        fp = r'C:\Users\gsbaw\PycharmProjects\TypeGrad\Lib'
        if iterindex != -1:
            widthindexer = widthstart
        else:
            widthindexer = widthstop - 1
        # pull every fourth line
        while widthindexer < widthstop:
            indexer = heightstart
            ondeck = []
            while indexer < (heightstop):
                r, g, b = pixels[widthindexer, indexer]
                avgval = (255 - ((r + g + b) / 3))
                ondeck.append(avgval)
                indexer += 1
            ondeck[-1] = 1
            ondeck[-2] = 1
            section.append(ondeck)
            # Writes to storage.json if first time
            widthindexer += 1

        return section

    def to_PIL(self, input_array):
        image = Image.fromarray(np.uint8(input_array))
        return image

    def get_for_network(self, bounds, letters):
        pass
    
    def pad_image(self, array):
        pad_amount = 56 - (array.shape[2])
        padded = np.pad(array, [0, pad_amount], mode='constant')
        return padded

