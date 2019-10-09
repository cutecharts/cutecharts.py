from typing import Iterable, Optional

from cutecharts.charts.basic import BasicChart


class Line(BasicChart):

    CHART_TYPE = "Line"

    def set_options(
        self,
        labels: Iterable,
        x_label: str = "",
        y_label: str = "",
        y_tick_count: int = 3,
        legend_pos: str = "upLeft",
        colors: Optional[Iterable] = None,
        font_family: Optional[str] = None,
    ):
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {
            "yTickCount": y_tick_count,
            "legendPosition": self._switch_pos(legend_pos),
            "dataColors": colors,
            "fontFamily": font_family,
        }

    def add_series(self, name, data):
        self.opts["data"]["datasets"].append({"label": name, "data": data})
