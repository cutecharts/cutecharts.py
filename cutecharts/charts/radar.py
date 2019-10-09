from cutecharts.charts.basic import BasicChart


class Radar(BasicChart):

    CHART_TYPE = "Radar"

    def set_options(self, labels, x_label, y_label):
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {"showLegend": "true", "showLabel": "true"}

    def add_series(self, name, data):
        self.opts["data"]["datasets"].append({"label": name, "data": data})
