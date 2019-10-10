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
        """
        :param labels: 数据标签列表
        :param inner_radius: Pie 图半径
        :param legend_pos: 图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
        :param colors: label 颜色数组
        :param font_family: CSS font-family
        """
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {
            "innerRadius": inner_radius,
            "legendPosition": legend_pos,
            "dataColors": colors,
            "fontFamily": font_family,
        }
        return self

    def add_series(self, data: Iterable):
        """
        :param data:
        """
        self.opts["data"]["datasets"].append({"data": data})
        return self
