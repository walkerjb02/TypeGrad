from utils import *
import json


class GetLoc(Root):
    def bounds(self, inputheight, dimension):
        heightidx = 1
        bounds = []
        if dimension == 1:
            colorthresh = 16
        elif dimension == 3:
            colorthresh = 21
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

    def cut_long(self, letters):
        letteridx = 0
        while letteridx < len(letters):
            if len(letters[letteridx]) < 1:
                pass
            elif len(letters[letteridx]) >= 1:
                boundidx = 0
                while boundidx < len(letters[letteridx]):
                    if letters[letteridx][boundidx][1] - letters[letteridx][boundidx][0] > (56 * 2) or letters[letteridx][boundidx][1] - letters[letteridx][boundidx][0] <= 15:
                        del letters[letteridx][boundidx]

                    elif letters[letteridx][boundidx][1] - letters[letteridx][boundidx][0] >= (56 * 1.5):
                        avg = int((letters[letteridx][boundidx][1] + letters[letteridx][boundidx][0]) / 2)
                        second_half = [avg, letters[letteridx][boundidx][1]]
                        letters[letteridx].append(second_half)
                        letters[letteridx][boundidx] = [letters[letteridx][boundidx][0], avg]
                        boundidx += 1

                    elif letters[letteridx][boundidx][1] - letters[letteridx][boundidx][0] > 56:
                        avg = int((letters[letteridx][boundidx][1] + letters[letteridx][boundidx][0]) / 2)
                        letters[letteridx][boundidx] = [avg - 28, avg + 28]
                        boundidx += 1

                    else:
                        boundidx += 1


            letteridx += 1
        return letters

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
            output.append([bounds[indexer][1] - error, bounds[indexer + 1][0] + error + 9])
            indexer += 1

        return output

    def condense(self, transformation, widthstart, widthstop):
        with open('StorageLen.json', 'r+') as file:
            init = json.loads(file.read())
            indexer = 0
            output = []
            while indexer < len(init["Bounds"]):
                bounds = init["Bounds"][indexer]
                condensed = []
                section = Utils().get_section(widthstart=widthstart, widthstop=widthstop, heightstart=bounds[0], heightstop=bounds[1], pixels=self.pixels, iterindex=indexer)
                sectionidx = 0
                while sectionidx < len(section):
                    condensed.append((sum(section[sectionidx]) / len(section[sectionidx]) - transformation))
                    sectionidx += 1
                output.append([condensed])
                indexer += 1
            return output

    def clear_noise(self, words):
        boundidx = 0
        while boundidx < len(words):
            if words[boundidx][1] - words[boundidx][0] <= 10:
                del words[boundidx]
            else:
                boundidx += 1

        return words

