import json
import uuid
from typing import Optional

from cutecharts.render.engine import RenderEngine, remove_key_with_none_value


class BasicChart(RenderEngine):
    def __init__(
        self, title: Optional[str] = None, width: str = "800px", height: str = "600px"
    ):
        self.width = width
        self.height = height
        self.chart_id = uuid.uuid4().hex
        self.opts: dict = {"title": title}
        self.opts.update(data={"datasets": []})

    def before_render(self):
        self.opts = remove_key_with_none_value(self.opts)
        json_content = json.dumps(self.opts)
        self.opts = json_content

    def _switch_pos(self, pos: str) -> int:
        if pos == "upLeft":
            return 1
        elif pos == "upRight":
            return 2
        elif pos == "downLeft":
            return 3
        elif pos == "downRight":
            return 4
