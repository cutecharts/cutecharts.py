from cutecharts.charts import Scatter
from cutecharts.components import Page
from cutecharts.faker import Faker


def scatter_base() -> Scatter:
    chart = Scatter("Scatter-基本示例")
    chart.set_options(x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart


scatter_base().render()


def scatter_dotsize_tickount():
    chart = Scatter("Scatter-散点大小")
    chart.set_options(dot_size=2, y_tick_count=8)
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart


def scatter_show_line():
    chart = Scatter("Scatter-散点连成线")
    chart.set_options(y_tick_count=8, is_show_line=True)
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart


page = Page()
page.add(scatter_base(), scatter_dotsize_tickount(), scatter_show_line())
page.render()
