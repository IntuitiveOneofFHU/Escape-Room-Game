import pygame

class NumberLock:
    def __init__(self, answer, image, top_left, bottom_right):
        self.answer = answer
        self.cur_code = []
        for space in self.answer:
            self.cur_code.append(0)
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.image = image
    def load_image(self):
        return pygame.image.load(self.image).convert_alpha()