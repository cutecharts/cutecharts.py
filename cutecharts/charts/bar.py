from cutecharts.charts.basic import BasicChart


class Bar(BasicChart):

    CHART_TYPE = "Bar"

    def set_options(self, labels: list, x_label, y_label):
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {"yTickCount": 2}

    def add_series(self, name, data):
        self.opts["data"]["datasets"].append({"label": name, "data": data})
