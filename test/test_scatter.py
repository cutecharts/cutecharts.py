from nose.tools import assert_equal

from cutecharts.charts import Scatter
from cutecharts.render.engine import remove_key_with_none_value


def gen_scatter_base() -> Scatter:
    c = Scatter("Scatter")
    c.set_options(x_label="I'm xlabel", y_label="I'm ylabel")
    c.add_series("series-A", [("1", 1), ("2", 2)])
    return c


def test_scatter_base_before_render():
    c = gen_scatter_base()
    expected = {
        "title": "Scatter",
        "data": {
            "datasets": [
                {"label": "series-A", "data": [{"x": "1", "y": 1}, {"x": "2", "y": 2}]}
            ]
        },
        "xLabel": "I'm xlabel",
        "yLabel": "I'm ylabel",
        "options": {
            "xTickCount": 3,
            "yTickCount": 3,
            "legendPosition": 1,
            "dataColors": None,
            "fontFamily": None,
            "showLine": False,
            "dotSize": 1,
            "timeFormat": None,
        },
    }

    assert_equal(c.opts, expected)


def test_scatter_base_after_render():
    c = gen_scatter_base()
    c.opts = remove_key_with_none_value(c.opts)
    expected = {
        "title": "Scatter",
        "data": {
            "datasets": [
                {"label": "series-A", "data": [{"x": "1", "y": 1}, {"x": "2", "y": 2}]}
            ]
        },
        "xLabel": "I'm xlabel",
        "yLabel": "I'm ylabel",
        "options": {
            "xTickCount": 3,
            "yTickCount": 3,
            "legendPosition": 1,
            "showLine": False,
            "dotSize": 1,
        },
    }

    assert_equal(c.opts, expected)
