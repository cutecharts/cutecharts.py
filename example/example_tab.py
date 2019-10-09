from cutecharts.components import Tab
from example.example_bar import bar_base
from example.example_line import line_base
from example.example_pie import pie_base

tab = Tab()
tab.add("Bar", bar_base())
tab.render()
