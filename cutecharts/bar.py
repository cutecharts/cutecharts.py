from typing import Optional
from cutecharts.engine import render_chart


class Bar:

    CHART = "Bar"
    CHART_CLASS = "bar-chart"

    def __init__(self, title: Optional[str] = None):
        self.opts: dict = {"title": title}
        self.opts.update(data={"datasets": []})

    def set_options(self, labels, x_label, y_label):
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {"yTickCount": 2}

    def add_series(self, name, data):
        self.opts["data"]["datasets"].append({"name": name, "data": data})

    def render(self, dest="render.html"):
        render_chart(dest, self)
