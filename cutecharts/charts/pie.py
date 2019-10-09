from typing import Iterable, Optional

from cutecharts.charts.basic import BasicChart


class Pie(BasicChart):

    CHART_TYPE = "Pie"

    def set_options(
        self,
        labels: Iterable,
        inner_radius: float = 0.5,
        legend_pos: str = "upLeft",
        colors: Optional[Iterable] = None,
        font_family: Optional[str] = None,
    ):
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {
            "innerRadius": inner_radius,
            "legendPosition": legend_pos,
            "dataColors": colors,
            "fontFamily": font_family,
        }

    def add_series(self, data):
        self.opts["data"]["datasets"].append({"data": data})
