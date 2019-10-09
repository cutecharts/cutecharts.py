from cutecharts.charts.basic import BasicChart


class Scatter(BasicChart):

    CHART_TYPE = "XY"

    def set_options(self, x_label, y_label):
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["options"] = {"yTickCount": 2}

    def add_series(self, name, data):
        pairs = [{"x": item[0], "y": item[1]} for item in data]
        self.opts["data"]["datasets"].append({"label": name, "data": pairs})
