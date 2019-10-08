from typing import Optional

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

template = env.get_template("chart.html")


class Pie:
    CHART = "Pie"
    CHART_CLASS = "pie-chart"

    def __init__(self, title: Optional[str] = None):
        self.opts: dict = {"title": title}
        self.opts.update(data={"datasets": []})

    def set_options(self, labels):
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {"yTickCount": 3}

    def add_series(self, data):
        self.opts["data"]["datasets"].append({"data": data})

    def render(self, dest="render.html"):
        with open(dest, "w+", encoding="utf8") as f:
            f.write(template.render(c=self))
