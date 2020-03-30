from nose.tools import assert_equal, assert_false, assert_true

from cutecharts.charts import Bar, Line
from cutecharts.components import Page


def gen_bar_base() -> Bar:
    c = Bar("Bar")
    c.set_options(labels=["A", "B"], x_label="I'm xlabel", y_label="I'm ylabel")
    c.add_series("series-A", ["1", "2"])
    return c


def gen_line_base() -> Line:
    c = Line("Line")
    c.set_options(labels=["A", "B"], x_label="I'm xlabel", y_label="I'm ylabel")
    c.add_series("series-A", ["1", "2"])
    return c


def test_page_iter():
    charts = [gen_bar_base(), gen_line_base()]
    p = Page()
    p.add(*charts)

    for idx, c in enumerate(p):
        assert_equal(c, charts[idx])

    assert_equal(len(p), len(charts))


def test_page_before_render():
    charts = [gen_bar_base(), gen_line_base()]
    p = Page()
    p.add(*charts)

    assert_false(hasattr(p, "local_cfg"))
    assert_false(hasattr(p, "notebook_cfg"))
    p.before_render()
    assert_true(hasattr(p, "local_cfg"))
    assert_true(hasattr(p, "notebook_cfg"))
