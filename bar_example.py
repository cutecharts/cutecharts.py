from cutecharts import Bar

bar = Bar("This is title")
bar.set_options(
    labels=["商家A", "商家B", "商家C", "商家D", "商家E", "商家F"],
    x_label="I'm xlabel",
    y_label="I'm ylabel",
)
bar.add_series("seriesA", [10, 20, 21, 41, 13, 14])
bar.add_series("seriesB", [14, 28, 51, 41, 36, 21])
bar.render()
