import numpy as np
import json
from root import Root
import math

'''
Notes
Average Handwriting Rightward Slant [60,75] degrees
'''

class utils(Root):
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

    def get_section(self, width, heightstart, heightstop, pixels, iterindex):
        section = []
        fp = r'C:\Users\gsbaw\PycharmProjects\TypeGrad\Lib'
        if iterindex != -1:
            widthindexer = 0
        else:
            widthindexer = width - 1
        # pull every fourth line
        while widthindexer < width:
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

        with open(r"{}\Storage{}.json".format(fp, 'Len' if iterindex == -1 else iterindex), 'r+') as firstfile:
            fal = json.loads(firstfile.read())
            fal["Sections"].append(section)
            serialized = json.dumps(fal)
            with open(r"{}\Storage{}.json".format(fp, 'Len' if iterindex == -1 else iterindex), 'w') as file:
                file.write(serialized)

        return section
