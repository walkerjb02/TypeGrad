from getloc import *
from utils import *

class Prep(Root):
    def get_bounds(self):
        bounds = GetLoc().bounds(Utils().get_section(48, 48, 0, self.height, self.pixels, iterindex=-1), dimension=1)
        revisedbounds = GetLoc().stitch_bounds(bounds)
        finalizedbounds = GetLoc().assemble_bounds(bounds=revisedbounds)
        Utils().to_json("Len", "Bounds", finalizedbounds)
        return finalizedbounds

    def get_words(self, bounds, transformation, widthstart, widthstop, dimension):
        # Condense section into array thats stored into Storage
        sections = GetLoc().condense(transformation, widthstart, widthstop)
        idx = 0
        wordloc = []
        while idx < len(bounds):
            # Feeding condensed section stored in Storages into GetLoc
            words = GetLoc().bounds(sections[idx], dimension=dimension)
            words = GetLoc().clear_noise(words)
            wordloc.append(words)
            Utils().to_json(idx, "Words", words)
            idx += 1
        return wordloc

    def get_letters(self, bounds):
        letters = self.get_words(bounds, 0, 0, self.width, 3)
        letters = GetLoc().cut_long(letters)
        return letters

    def prep_main(self):
        Utils().clear_json(0)
        bounds = self.get_bounds()
        words = self.get_letters(bounds)
        finalized = Utils().get_for_network(words)
        return finalized
