#/usr/bin/python3.8
"""
This example implements the interaction between Qt Widgets and a 2D
matplotlib plot showing a gaussian curve with scipy.
This app displays a graph inside gui
"""

import sys
import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QtApplication, QWidget, QDoubleSpinBox, QVBoxLayout, QHBoxLayout)

class PlotWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        #create widgets
        self.view = FigureCanvas(Figure(figsize=(5,3)))
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view,self)
        self.avg_input = QDoubleSpinBox()
        self.std_input = QDoubleSpinBox()
        self.avg_input.setPrefix("μ: ")
        self.std_input.setPrefix("σ: ")
        self.std_input.setValue(10)
        #create layout
        input_layout = QHBoxLayout() #widgets are aligned horiz
        input_layout.addWidget(self.avg_input)
        input_layout.addWidget(self.std_input)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.view)
        vlayout.addWidget(self.input_layout)
        self.setLayout(vlayout)

        #connect input with a func
        self.avg_input.valueChanged.connect(self.on_change)
        self.std_input.valueChanged.connect(self.on_change)
        #Exec on_change func
        self.on_change()

    @Slot() #connect to this func
    def on_change(self):
        # Update plot with input values
        avg = self.avg_input.value() #get data from spinbox
        std = self.std_input.value()
        dx = np.linspace(-100,100)
        dy = norm.pdf(x, avg, std)

        self.axes.clear()
        self.axes.plot(dx,dy)
        self.view.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wPlot = PlotWidget()
    wPlot.show()
    sys.exit(app.exec())

