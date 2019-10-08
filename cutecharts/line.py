from typing import Optional

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

template = env.get_template("chart.html")


class Line:
    CHART = "Line"
    CHART_CLASS = "line-chart"

    def __init__(self, title: Optional[str] = None):
        self.opts: dict = {"title": title}
        self.opts.update(data={"datasets": []})

    def set_options(self, labels, x_label, y_label):
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {"yTickCount": 3}

    def add_series(self, name, data):
        self.opts["data"]["datasets"].append({"name": name, "data": data})

    def render(self, dest="render.html"):
        with open(dest, "w+", encoding="utf8") as f:
            f.write(template.render(chart_opts=self.opts))
