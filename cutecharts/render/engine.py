import os

from jinja2 import Environment, FileSystemLoader

ENV = Environment(
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "templates")
    ),
)


class RenderEngine:
    def render(self, dest: str = "render.html", template_name: str = "basic.html"):
        template = ENV.get_template(template_name)
        with open(dest, "w+", encoding="utf8") as f:
            f.write(template.render(chart=self))
