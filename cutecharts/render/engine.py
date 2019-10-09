from cutecharts.globals import CurrentConfig


class RenderEngine:
    def render(self, dest: str = "render.html", template_name: str = "basic.html"):
        template = CurrentConfig.GLOBAL_ENV.get_template(template_name)
        with open(dest, "w+", encoding="utf8") as f:
            f.write(template.render(chart=self))

    def render_notebook(self):
        pass
