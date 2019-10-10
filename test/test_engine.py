from nose.tools import assert_in

from cutecharts.charts.basic import BasicChart
from cutecharts.globals import AssetsHost


def test_engine_render():
    basic = BasicChart()
    html = basic.render()
    assert_in(AssetsHost.DEFAULT_HOST, html)
    assert_in("chartXkcd", html)
