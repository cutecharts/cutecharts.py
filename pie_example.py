from cutecharts import Pie

pie = Pie("This is title")
pie.set_options(
    labels=["商家A", "商家B", "商家C", "商家D", "商家E", "商家F"],
)
pie.add_series([10, 20, 21, 41, 13, 14])
pie.render()
