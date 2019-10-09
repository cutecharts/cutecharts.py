from nose.tools import assert_equal

from cutecharts.charts import Pie
from cutecharts.render.engine import remove_key_with_none_value


def gen_pie_base() -> Pie:
    c = Pie("Pie")
    c.set_options(labels=["A", "B"])
    c.add_series(["1", "2"])
    return c


def test_pie_base_before_render():
    c = gen_pie_base()
    expected = {
        "title": "Pie",
        "data": {"datasets": [{"data": ["1", "2"]}], "labels": ["A", "B"]},
        "options": {
            "dataColors": None,
            "fontFamily": None,
            "innerRadius": 0.5,
            "legendPosition": "upLeft",
        },
    }
    assert_equal(c.opts, expected)


def test_pie_base_after_render():
    c = gen_pie_base()
    c.opts = remove_key_with_none_value(c.opts)
    expected = {
        "title": "Pie",
        "data": {"datasets": [{"data": ["1", "2"]}], "labels": ["A", "B"]},
        "options": {"innerRadius": 0.5, "legendPosition": "upLeft"},
    }

    assert_equal(c.opts, expected)
