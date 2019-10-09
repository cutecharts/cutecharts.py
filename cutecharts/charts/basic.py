import uuid
from typing import Optional

from cutecharts.render.engine import RenderEngine


class BasicChart(RenderEngine):
    def __init__(
        self, title: Optional[str] = None, width: str = "800px", height: str = "600px"
    ):
        self.width = width
        self.height = height
        self.chart_id = uuid.uuid4().hex
        self.opts: dict = {"title": title}
        self.opts.update(data={"datasets": []})
