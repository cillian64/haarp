"""
Colour runner pattern

Looks as if a coloured pole is running through The Grid!  Imagine: grid is set
to all blue.  Suddenly, one of them is red, and the co-ordinates of the red
pole changes, leaving a fading red trail in its wake.  The colour of the runner
(the red pole) changes, as does the background colour.  Exciting!
"""

import numpy as np
import logging
logger = logging.getLogger(__name__)

from ..pattern import Pattern, register_pattern


@register_pattern("[COLOUR] Runner")
class ColourRunner(Pattern):
    """Colour runner pattern"""

    def __init__(self, config, ui):
        super().__init__(config, ui)
        self.grid_gen = self.generate_grid()

    @staticmethod
    def runner_location():
        """Yields (x, y) co-ordinates of the runner"""
        pass

    def update(self):
        return next(self.grid_gen), 1/10

    def generate_grid(self):
        """
        Yields 7x7x6 numpy array representing grid pole configurations

        Yields a 7x7x6 numpy array, with each entry representing the
        configuration of a pole in The Grid.  The centre pole will be set to
        the first colour in the colour gradient, then each of the surrounding
        rectangles of poles will be set to successive colours in the gradient.
        """
        grid = np.zeros((7, 7, 6), dtype=np.uint8)
        yield grid
