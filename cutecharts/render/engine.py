from typing import Iterable, Optional

from cutecharts.globals import CurrentConfig, NotebookType


def _flat(obj):
    if isinstance(obj, (list, tuple, set)):
        return obj

    return (obj,)  # tuple


def _expand(dict_generator):
    return dict(list(dict_generator))


def _clean_dict(mydict):
    for key, value in mydict.items():
        if value is not None:
            if isinstance(value, dict):
                value = _expand(_clean_dict(value))

            elif isinstance(value, (list, tuple, set)):
                value = list(_clean_array(value))

            elif isinstance(value, str) and not value:
                # delete key with empty string
                continue

            yield (key, value)


def _clean_array(myarray):
    for value in myarray:
        if isinstance(value, dict):
            yield _expand(_clean_dict(value))

        elif isinstance(value, (list, tuple, set)):
            yield list(_clean_array(value))

        else:
            yield value


def remove_key_with_none_value(incoming_dict):
    if isinstance(incoming_dict, dict):
        return _expand(_clean_dict(incoming_dict))
    elif incoming_dict:
        return incoming_dict
    else:
        return None


class HTML:
    def __init__(self, data: Optional[str] = None):
        self.data = data

    def _repr_html_(self):
        return self.data

    def __html__(self):
        return self._repr_html_()


class RenderEngine:
    def render(
        self, dest: str = "render.html", template_name: str = "basic_local.html"
    ):
        template = CurrentConfig.GLOBAL_ENV.get_template(template_name)

        if hasattr(self, "before_render"):
            self.before_render()

        with open(dest, "w+", encoding="utf8") as f:
            f.write(template.render(chart=self))

    def render_notebook(self, template_name: str = "basic_notebook.html"):
        template = CurrentConfig.GLOBAL_ENV.get_template(template_name)

        if hasattr(self, "before_render"):
            self.before_render()

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_NOTEBOOK:
            return HTML(template.render(chart=self))
