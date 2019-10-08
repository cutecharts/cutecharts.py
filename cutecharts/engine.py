from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("chart.html")


def render_chart(dest: str, c):
    with open(dest, "w+", encoding="utf8") as f:
        f.write(template.render(c=c))
