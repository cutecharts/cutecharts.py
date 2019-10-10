from typing import Iterable, Optional

from cutecharts.charts.basic import BasicChart


class Bar(BasicChart):

    CHART_TYPE = "Bar"

    def set_options(
        self,
        labels: Iterable,
        x_label: str = "",
        y_label: str = "",
        y_tick_count: int = 3,
        colors: Optional[Iterable] = None,
        font_family: Optional[str] = None,
    ):
        """
        :param labels: X 坐标轴标签数据
        :param x_label: X 坐标轴名称
        :param y_label: Y 坐标轴名称
        :param y_tick_count: Y 轴刻度分割段数
        :param colors: label 颜色数组
        :param font_family: CSS font-family
        """
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["data"]["labels"] = labels
        self.opts["options"] = {
            "yTickCount": y_tick_count,
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
