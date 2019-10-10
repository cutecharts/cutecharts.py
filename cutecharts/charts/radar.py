from typing import Iterable, Optional

from cutecharts.charts.basic import BasicChart


class Radar(BasicChart):

    CHART_TYPE = "Radar"

    def set_options(
        self,
        labels: Iterable,
        is_show_label: bool = True,
        is_show_legend: bool = True,
        tick_count: int = 3,
        legend_pos: str = "upLeft",
        colors: Optional[Iterable] = None,
        font_family: Optional[str] = None,
    ):
        """
        :param labels: 数据标签列表
        :param is_show_label: 是否显示标签
        :param is_show_legend: 是否显示图例
        :param tick_count: 坐标系分割刻度
        :param legend_pos: 图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
        :param colors: label 颜色数组
        :param font_family: CSS font-family
        """
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {
            "showLegend": is_show_legend,
            "showLabel": is_show_label,
            "tickCount": tick_count,
            "legendPosition": self._switch_pos(legend_pos),
            "dataColors": colors,
            "fontFamily": font_family,
        }
        return self

    def add_series(self, name: str, data: Iterable):
        """
        :param name: series 名称
        :param data: series 数据列表
        """
        self.opts["data"]["datasets"].append({"label": name, "data": data})
        return self
