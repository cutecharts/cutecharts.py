from cutecharts.components import Page

from .example_bar import bar_base
from .example_line import line_base
from .example_pie import pie_base

page = Page()
page.add(bar_base(), line_base(), pie_base())
page.render()
