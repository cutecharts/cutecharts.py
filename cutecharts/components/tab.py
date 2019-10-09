from cutecharts.render.engine import RenderEngine


class Tab(RenderEngine):
    def __init__(self):
        self._charts = []

    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

    def add(self, name, chart):
        chart.tab_name = name
        self._charts.append(chart)

    def render(self, dest: str = "render.html", template_name: str = "tab.html"):
        super().render(dest, template_name)
