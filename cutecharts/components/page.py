import json
import uuid
from typing import Optional

from cutecharts.globals import CurrentConfig
from cutecharts.render.engine import RenderEngine, remove_key_with_none_value


class Page(RenderEngine):
    def __init__(self, assets_host: Optional[str] = None):
        super().__init__()
        self._charts: list = []
        self.assets_host = assets_host or CurrentConfig.ASSETS_HOST
        self.assets_deps = []

    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

    def add(self, *charts):
        for c in charts:
            for dep in c.assets_deps:
                if dep not in self.assets_deps:
                    self.assets_deps.append(dep)
            self._charts.append(c)

    def before_render(self):
        for chart in self._charts:
            chart.chart_id = uuid.uuid4().hex
            chart.opts = remove_key_with_none_value(chart.opts)
            json_content = json.dumps(chart.opts)
            chart.opts = json_content
        self.local_cfg, self.notebook_cfg = self._produce_assets_cfg()

    def render(self, dest: str = "render.html", template_name: str = "page_local.html"):
        super().render(dest, template_name)

    def render_notebook(self, template_type="page"):
        return super().render_notebook(template_type)
