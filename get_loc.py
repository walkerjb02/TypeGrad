from root import Root
from utils import *
import json

class get_loc(Root):
    def bounds(self, inputheight, dimension):
        heightidx = 1
        bounds = []
        if dimension == 1:
            colorthresh = 16
        else:
            colorthresh = 6

        while heightidx < self.height:
            if inputheight[0][heightidx] >= colorthresh:
                ondeck = []
                ondeck.append(heightidx - 1)
                newidx = heightidx
                while inputheight[0][newidx] >= colorthresh or inputheight[0][newidx] < colorthresh and inputheight[0][newidx - 1] >= colorthresh:
                    if inputheight[0][newidx] == self.height - 2:
                        break
                    else:
                        newidx += 1

                heightidx = newidx + 1
                ondeck.append(newidx)
                bounds.append(ondeck)
            else:
                heightidx += 1
        return bounds

    def stitch_bounds(self, bounds):
        idx = 0
        while idx < len(bounds):
            idx1 = idx + 1
            while idx1 < len(bounds):
                if bounds[idx][1] + 5 >= bounds[idx1][0]:
                    bounds[idx] = [bounds[idx][0],bounds[idx1][1]]
                    del bounds[idx1]
                idx1 += 1
            idx += 1
        return bounds

    def assemble_bounds(self, bounds):
        indexer = 0
        output = []
        error = 2
        output.append([0,bounds[indexer][0]])
        while indexer < len(bounds) - 1:
            output.append([bounds[indexer][1] - error, bounds[indexer + 1][0] + error + 0])
            indexer += 1

        return output

    def condense(self):
        with open('StorageLen.json', 'r+') as file:
            init = json.loads(file.read())
            indexer = 0
            while indexer < len(init["Bounds"]):
                bounds = init["Bounds"][indexer]
                condensed = []
                section = utils().get_section(width=self.width,heightstart=bounds[0], heightstop=bounds[1], pixels=self.pixels, iterindex=indexer)
                sectionidx = 0
                while sectionidx < len(section):
                    #TODO apply random weights n-values from normdist
                    #section[sectionidx] = section[sectionidx] * [i * 1e-2 for i in range(0,len(section[sectionidx]))]
                    #print(section[sectionidx])
                    #print('\n\n\n')
                    condensed.append(sum(section[sectionidx]) / len(section[sectionidx]))
                    sectionidx += 1

                utils().to_json(indexer,"Sections",[condensed])
                indexer += 1

            return section

    def clear_noise(self, words):
        boundidx = 0
        while boundidx < len(words):
            if words[boundidx][1] - words[boundidx][0] <= 10:
                del words[boundidx]
            else:
                boundidx += 1

        return words

    def apply_angle(self, section, height):
        idx = 0
        while idx < height:
            section[idx] = section[idx]

            idx += 1
