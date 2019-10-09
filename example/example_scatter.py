from cutecharts.charts import Scatter
from cutecharts.components import Page


def scatter_base() -> Scatter:
    chart = Scatter("This is title", width="800px")
    chart.set_options(x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("seriesA", [(11, 22), (22, 33), (33, 44), (44, 55), (55, 66)])
    return chart


def scatter_dotsize_tickount():
    pass


page = Page()
page.add(scatter_base())
page.render()
