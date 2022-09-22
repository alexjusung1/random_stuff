import numpy as np


class Board:
    def __init__(self, height, width):
        self.dims = height, width
        self.path = ''
    
    @classmethod
    def build_copy(cls, other_board: 'Board'):
        copy = cls(*other_board.dims)
        