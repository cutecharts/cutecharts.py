from cutecharts.charts import Pie
from cutecharts.components import Page


def pie_base() -> Pie:
    pie = Pie("This is title")
    pie.set_options(labels=["商家A", "商家B", "商家C", "商家D", "商家E", "商家F"])
    pie.add_series([10, 20, 21, 41, 13, 14])
    return pie


page = Page()
page.add(pie_base())
page.render()
