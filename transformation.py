from init import Root

class Transformations(Root):
    def brightness(self, section, factor):
        sectionidx = 0
        while sectionidx < len(section):
            idx = 0
            while idx < len(section[sectionidx]):
                section[sectionidx][idx] = section[sectionidx][idx] - factor
                idx += 1
            sectionidx += 1

    def enlarge_image(self, pil_image):
        enlarged = pil_image.resize((56, 56))
        return enlarged
