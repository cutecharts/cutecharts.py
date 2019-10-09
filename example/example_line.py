from cutecharts.charts import Line
from cutecharts.components import Page


def line_base() -> Line:
    line = Line("This is title")
    line.set_options(
        labels=["商家A", "商家B", "商家C", "商家D", "商家E", "商家F"],
        x_label="I'm xlabel",
        y_label="I'm ylabel",
    )
    line.add_series("seriesA", [10, 20, 21, 41, 13, 14])
    line.add_series("seriesB", [14, 28, 51, 41, 36, 21])
    return line


page = Page()
page.add(line_base())
page.render()
