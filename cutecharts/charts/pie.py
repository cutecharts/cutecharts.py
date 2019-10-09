from cutecharts.charts.basic import BasicChart


class Pie(BasicChart):

    CHART_TYPE = "Pie"

    def set_options(self, labels):
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {"yTickCount": 3}

    def add_series(self, data):
        self.opts["data"]["datasets"].append({"data": data})
