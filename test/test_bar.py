from nose.tools import assert_equal

from cutecharts.charts import Bar


def test_bar_base():
    c = Bar("Bar")
    c.set_options(labels=["A", "B"], x_label="I'm xlabel", y_label="I'm ylabel")
    c.add_series("series-A", ["1", "2"])

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
