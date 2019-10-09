from cutecharts.render.engine import RenderEngine


class Page(RenderEngine):
    def __init__(self):
        self.charts = []

    def add(self, *charts):
        for c in charts:
            self.charts.append(c)

    def render(self, dest: str = "render.html", template_name: str = "page.html"):
        super().render(dest, template_name)
