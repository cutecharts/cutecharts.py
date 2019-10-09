from nose.tools import assert_equal

from cutecharts.charts import Line
from cutecharts.render.engine import remove_key_with_none_value


def gen_line_base() -> Line:
    c = Line("Line")
    c.set_options(labels=["A", "B"], x_label="I'm xlabel", y_label="I'm ylabel")
    c.add_series("series-A", ["1", "2"])
    return c


def test_line_base_before_render():
    c = gen_line_base()
    expected = {
        "title": "Line",
        "data": {
            "datasets": [{"label": "series-A", "data": ["1", "2"]}],
            "labels": ["A", "B"],
        },
        "xLabel": "I'm xlabel",
        "yLabel": "I'm ylabel",
        "options": {
            "dataColors": None,
            "fontFamily": None,
            "legendPosition": 1,
            "yTickCount": 3,
        },
    }
    assert_equal(c.opts, expected)


def test_line_base_after_render():
    c = gen_line_base()
    c.opts = remove_key_with_none_value(c.opts)
    expected = {
        "title": "Line",
        "data": {
            "datasets": [{"label": "series-A", "data": ["1", "2"]}],
            "labels": ["A", "B"],
        },
        "xLabel": "I'm xlabel",
        "yLabel": "I'm ylabel",
        "options": {"legendPosition": 1, "yTickCount": 3},
    }

    assert_equal(c.opts, expected)
