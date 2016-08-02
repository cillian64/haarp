"""
Colour ripple pattern

Colours will rippple from the centre of The Grid, with the colour changing
gradually through the spectrum.  Pretty!  Hopefully.
"""

import collections
import copy
import numpy as np
import logging
from ..pattern import Pattern, register_pattern
logger = logging.getLogger(__name__)


@register_pattern("ColourRipple")
class ColourRipple(Pattern):
    """
    This class will have self.config set from the register_pattern argument,
    and self.ui set as a reference to the global UI helper.
    If you override __init__(), please call super().__init__().
    """

    def __init__(self, config, ui):
        super().__init__(config, ui)
        self.grid_gen = self.generate_grid()

    @staticmethod
    def colour_gradient(start_rgb=[0, 0, 0], end_rgb=[255, 255, 255], n=100):
        """Yields deque containing four RGB tuples."""
        colours = collections.deque(maxlen=4)
        for _ in range(4):
            colours.appendleft(tuple(start_rgb))

        while True:
            for channel in range(3):
                for i in range(n):
                    rgb = copy.deepcopy(start_rgb)
                    rgb[channel] = int(start_rgb[channel] + i/n *
                                       (end_rgb[channel] - start_rgb[channel]))
                    colours.appendleft(tuple(rgb))
                    yield colours

    def update(self):
        """
        The update() method is called by the main control loop on a time basis
        you can specify. You should compute the new grid state in this method.

        The grid shape is specified by a (7, 7, 6) numpy array of type uint8,
        with the first two dimensions specifying the (x, y) pole coordinate,
        and the third dimension giving (red, green, blue, sound type, sound
        frequency, sound volume).

        Sound types:
            0: silent
            1: sine
            2: square
            3: triangle
            4: noise
            5: click

        Sound frequencies and volumes range 0-255 and are scaled in hardware to
        meet the available sounder response.

        The time until next update is specified in seconds.

        Return a tuple of (new_grid, update_time).
        """
        return next(self.grid_gen), 1/10

    def generate_grid(self):
        colour_gradient = self.colour_gradient()
        grid = np.zeros((7, 7, 6), dtype=np.uint8)

        while True:
            colours = copy.deepcopy(next(colour_gradient))
            grid[3][3] = colours.popleft() + (0, 0, 0)

            for i, j in zip([2, 1, 0], [4, 5, 6]):
                c = colours.popleft()
                grid[:, i] = c + (0, 0, 0)
                grid[:, j] = c + (0, 0, 0)
                grid[i, :] = c + (0, 0, 0)
                grid[j, :] = c + (0, 0, 0)

            yield grid
