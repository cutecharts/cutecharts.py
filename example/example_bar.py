from cutecharts.charts import Bar
from cutecharts.components import Page


def bar_base() -> Bar:
    chart = Bar("This is title", width="800px")
    chart.set_options(
        labels=["商家A", "商家B", "商家C", "商家D", "商家E", "商家F"],
        x_label="I'm xlabel",
        y_label="I'm ylabel",
    )
    chart.add_series("seriesA", [10, 20, 21, 41, 13, 14])
    chart.add_series("seriesB", [14, 28, 51, 41, 36, 21])
    return chart


page = Page()
page.add(bar_base())
page.render()
