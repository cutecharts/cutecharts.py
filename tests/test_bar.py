from nose.tools import assert_equal

from cutecharts.charts import Bar
from cutecharts.render.engine import remove_key_with_none_value


def gen_bar_base() -> Bar:
    c = Bar("Bar")
    c.set_options(labels=["A", "B"], x_label="I'm xlabel", y_label="I'm ylabel")
    c.add_series("series-A", ["1", "2"])
    return c


def test_bar_opts_before():
    c = gen_bar_base()
    expected = {
        "title": "Bar",
        "data": {
            "datasets": [{"label": "series-A", "data": ["1", "2"]}],
            "labels": ["A", "B"],
        },
        "xLabel": "I'm xlabel",
        "yLabel": "I'm ylabel",
        "options": {"yTickCount": 3, "dataColors": None, "fontFamily": None},
    }
    assert_equal(c.opts, expected)


def test_bar_opts_after():
    c = gen_bar_base()
    c.opts = remove_key_with_none_value(c.opts)
    expected = {
        "title": "Bar",
        "data": {
            "datasets": [{"label": "series-A", "data": ["1", "2"]}],
            "labels": ["A", "B"],
        },
        "xLabel": "I'm xlabel",
        "yLabel": "I'm ylabel",
        "options": {"yTickCount": 3},
    }

    assert_equal(c.opts, expected)
