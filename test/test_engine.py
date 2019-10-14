from nose.tools import assert_equal, assert_in

from cutecharts.charts.basic import BasicChart
from cutecharts.faker import Faker
from cutecharts.globals import AssetsHost


def test_engine_render():
    basic = BasicChart()
    html = basic.render()
    assert_in(AssetsHost.DEFAULT_HOST, html)
    assert_in("chartXkcd", html)


def test_engine_render_notebook():
    basic = BasicChart()
    html = basic.render_notebook().__html__()
    assert_in(AssetsHost.DEFAULT_HOST, html)
    assert_in("chartXkcd", html)


def test_load_javascript():
    basic = BasicChart()
    expected = ['https://cdn.jsdelivr.net/npm/chart.xkcd@1.1/dist/chart.xkcd.min.js']
    assert_equal(basic.load_javascript().lib, expected)


def test_faker():
    attrs = Faker.choose()
    values = Faker.values()
    assert_equal(len(attrs), len(values))
