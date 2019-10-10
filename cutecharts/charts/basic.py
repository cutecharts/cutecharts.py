import json
import uuid
from typing import Optional

from cutecharts.globals import CurrentConfig
from cutecharts.render.engine import RenderEngine, remove_key_with_none_value


class BasicChart(RenderEngine):
    def __init__(
        self,
        title: Optional[str] = None,
        width: str = "800px",
        height: str = "600px",
        assets_host: Optional[str] = None,
    ):
        """
        :param title: 图表标题
        :param width: 图表宽度
        :param height: 图表高度
        :param assets_host: 引用资源 Host
        """
        super().__init__()
        self.width = width
        self.height = height
        self.chart_id = uuid.uuid4().hex
        self.opts: dict = {"title": title}
        self.opts.update(data={"datasets": []})
        self.assets_host = assets_host or CurrentConfig.ASSETS_HOST
        self.assets_deps = ["chartXkcd"]

    def before_render(self):
        self.opts = remove_key_with_none_value(self.opts)
        json_content = json.dumps(self.opts)
        self.opts = json_content
        self.local_cfg, self.notebook_cfg = self._produce_assets_cfg()

    def _switch_pos(self, pos: str) -> int:
        if pos == "upLeft":
            return 1
        elif pos == "upRight":
            return 2
        elif pos == "downLeft":
            return 3
        elif pos == "downRight":
            return 4
