from cutecharts.charts.basic import BasicChart


class Bar(BasicChart):

    CHART, CHART_CLASS = "Bar", "bar-chart"

    def set_options(self, labels, x_label, y_label):
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {"yTickCount": 2}

    def add_series(self, name, data):
        self.opts["data"]["datasets"].append({"name": name, "data": data})
