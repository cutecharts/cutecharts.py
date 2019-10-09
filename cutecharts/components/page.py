import json

from cutecharts.render.engine import RenderEngine, remove_key_with_none_value


class Page(RenderEngine):
    def __init__(self):
        self._charts: list = []

    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

    def add(self, *charts):
        for c in charts:
            self._charts.append(c)

    def before_render(self):
        for chart in self._charts:
            chart.opts = remove_key_with_none_value(chart.opts)
            json_content = json.dumps(chart.opts)
            chart.opts = json_content

    def render(self, dest: str = "render.html", template_name: str = "page_local.html"):
        super().render(dest, template_name)

    def render_notebook(self, template_name: str = "page_notebook.html"):
        return super().render_notebook(template_name)
