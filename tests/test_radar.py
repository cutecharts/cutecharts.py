from nose.tools import assert_equal

from cutecharts.charts import Radar
from cutecharts.render.engine import remove_key_with_none_value


def gen_radar_base() -> Radar:
    c = Radar("Radar")
    c.set_options(labels=["A", "B"])
    c.add_series("series-A", ["1", "2"])
    return c


def test_radar_opts_before():
    c = gen_radar_base()
    expected = {
        "title": "Radar",
        "data": {
            "datasets": [{"label": "series-A", "data": ["1", "2"]}],
            "labels": ["A", "B"],
        },
        "options": {
            "showLegend": True,
            "showLabel": True,
            "tickCount": 3,
            "legendPosition": 1,
            "dataColors": None,
            "fontFamily": None,
        },
    }

    assert_equal(c.opts, expected)


def test_radar_opts_after():
    c = gen_radar_base()
    c.opts = remove_key_with_none_value(c.opts)
    expected = {
        "title": "Radar",
        "data": {
            "datasets": [{"label": "series-A", "data": ["1", "2"]}],
            "labels": ["A", "B"],
        },
        "options": {
            "showLegend": True,
            "showLabel": True,
            "tickCount": 3,
            "legendPosition": 1,
        },
    }

    assert_equal(c.opts, expected)
