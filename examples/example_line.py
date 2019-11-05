from cutecharts.charts import Line
from cutecharts.components import Page
from cutecharts.faker import Faker


def line_base() -> Line:
    chart = Line("Line-基本示例")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart


line_base().render()


def line_legend():
    chart = Line("Line-Legend 位置")
    chart.set_options(labels=Faker.choose(), legend_pos="upRight")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart


def line_tickcount_colors():
    chart = Line("Line-调整颜色")
    chart.set_options(labels=Faker.choose(), colors=Faker.colors, y_tick_count=8)
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart


page = Page()
page.add(line_base(), line_legend(), line_tickcount_colors())
page.render()
