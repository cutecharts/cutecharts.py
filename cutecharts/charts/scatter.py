from typing import Iterable, Optional

from cutecharts.charts.basic import BasicChart


class Scatter(BasicChart):

    CHART_TYPE = "XY"

    def set_options(
        self,
        x_label: str = "",
        y_label: str = "",
        x_tick_count: int = 3,
        y_tick_count: int = 3,
        is_show_line: bool = False,
        dot_size: int = 1,
        time_format: Optional[str] = None,
        legend_pos: str = "upLeft",
        colors: Optional[Iterable] = None,
        font_family: Optional[str] = None,
    ):
        """
        :param x_label: X 坐标轴名称
        :param y_label: Y 坐标轴名称
        :param x_tick_count: X 轴刻度分割段数
        :param y_tick_count: Y 轴刻度分割段数
        :param is_show_line: 是否显示辅助线
        :param dot_size: 散点大小
        :param time_format: 日期格式
        :param legend_pos: 图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
        :param colors: label 颜色数组
        :param font_family: CSS font-family
        """
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["options"] = {
            "xTickCount": x_tick_count,
            "yTickCount": y_tick_count,
            "legendPosition": self._switch_pos(legend_pos),
            "dataColors": colors,
            "fontFamily": font_family,
            "showLine": is_show_line,
            "dotSize": dot_size,
            "timeFormat": time_format,
        }
        return self

    def add_series(self, name: str, data: Iterable):
        """
        :param name: series 名称
        :param data: series 数据列表，[(x1, y1), (x2, y2)]
        """
        pairs = [{"x": item[0], "y": item[1]} for item in data]
        self.opts["data"]["datasets"].append({"label": name, "data": pairs})
        return self
