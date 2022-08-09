from utils import *
from get_loc import *
import numpy as np

class Prep(Root):
    def get_bounds(self):
        bounds = get_loc().bounds(utils().get_section(48, 0, self.height, self.pixels, iterindex=-1),dimension=1)
        revisedbounds = get_loc().stitch_bounds(bounds)
        finalizedbounds = get_loc().assemble_bounds(bounds=revisedbounds)
        utils().to_json("Len", "Bounds", finalizedbounds)
        return finalizedbounds

    def get_words(self, bounds):
        get_loc().condense()
        idx = 0
        while idx < len(bounds):
            with open(f'Storage{idx}.json', 'r') as file:
                section = json.loads(file.read())["Sections"]
                words = get_loc().bounds(section,dimension=2)
                words = get_loc().clear_noise(words)
                print(words)

                utils().to_json(idx, "Sections", words)
                idx += 1

    def run(self):
        utils().clear_json(40)
        bounds = self.get_bounds()
        words = self.get_words(bounds)
        print(words)
        idx = 0
        with open(f'Storage{idx}.json','r+') as file:
            wordbounds = json.loads(file.read())["Bounds"]
