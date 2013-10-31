"""
Create two lines. One straight and one elliptic.
"""

import unittest
import os
import time

import numpy as np
import matplotlib.pyplot as plt

from ..core import Diagram

from . import TestDiagram

basename = os.path.splitext(os.path.basename(__file__))[0]

class TestOperator(TestDiagram):

    def test_triangle(self):

        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot(111)
        
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
        ax.set_xticks([])
        ax.set_yticks([])
        
        dia = Diagram(ax)

        v1 = dia.verticle(xy=(.2,.6), marker='')
        v2 = dia.verticle(xy=(.2,.4), marker='')

        v3 = dia.verticle(xy=(.3,.6))
        v4 = dia.verticle(xy=(.3,.4))

        l1 = dia.line(v1, v3)
        l2 = dia.line(v2, v4)

        v5 = dia.verticle(xy=(.3 + .2 * np.sqrt(3) / 2, .5))

        triangle = dia.operator([v3, v4, v5])

        v6 = dia.verticle(xy=(.8, .5), marker='')
        l3 = dia.line(v5, v6, linestyle='wiggly', nwiggles=4)
        
        dia.plot()

        self.show_pdf(basename)
