from cutecharts.components import Page
from examples.example_bar import bar_base
from examples.example_line import line_base
from examples.example_pie import pie_base
from examples.example_radar import radar_base
from examples.example_scatter import scatter_base

page = Page()
page.add(bar_base(), line_base(), pie_base(), radar_base(), scatter_base())
page.render()
