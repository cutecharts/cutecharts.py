<p align="center">
    <img src="https://user-images.githubusercontent.com/19553554/66697551-27384b00-ed09-11e9-9fe8-210918fdeb77.png" alt="cutecharts.py logo" width=600/>
</p>

<p align="center">
    <i>📉 Hand drawing style charts library for Python.</i>
</p>

<p align="center">
    <a href="https://travis-ci.org/chenjiandongx/cutecharts.py">
        <img src="https://travis-ci.org/chenjiandongx/cutecharts.svg?branch=master" alt="Travis Build Status">
    </a>
    <a href="https://ci.appveyor.com/project/chenjiandongx/cutecharts.py">
        <img src="https://ci.appveyor.com/api/projects/status/a6jp4db3mvm8d6mo/branch/master?svg=true" alt="Appveyor Build Status">
    </a>
    <a href="https://codecov.io/gh/chenjiandongx/cutecharts.py">
        <img src="https://codecov.io/gh/chenjiandongx/cutecharts/branch/master/graph/badge.svg" alt="Codecov">
    </a>
    <a href="https://badge.fury.io/py/cutecharts">
        <img src="https://badge.fury.io/py/cutecharts.svg" alt="Package version">
    </a>
    <a href="https://pypi.org/project/cutecharts/">
        <img src="https://img.shields.io/pypi/pyversions/cutecharts.svg?colorB=brightgreen" alt="PyPI - Python Version">
    </a>
</p>

<p align="center">
    <a href="https://pypi.org/project/cutecharts">
        <img src="https://img.shields.io/pypi/format/cutecharts.svg" alt="PyPI - Format">
    </a>
     <a href="https://github.com/chenjiandongx/cutecharts.py/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

## 📣 Idea

[chart.xkcd](https://github.com/timqian/chart.xkcd) is an interesting visualization library written in Javascript, the chart style of chart.xkcd is so cute that I love it at first sight. 

There is no doubt that Javascript has more advantages in interaction as well as visual effect. Besides that, as we all know, Python is an expressive language and is loved by data science community. Hence I want to combine the strength of both technologies, as the result of this idea, [cutecharts.py](https://github.com/cutecharts/cutecharts.py) is born.

Unfortunately, chart.xkcd only supports a few chart types as a visualization libraray, thus if you have more needs in various kind of chart, [pyecharts](https://github.com/pyecharts/pyecharts) is better.

What's worth pointing out is that cutecharts is more about a library used to learn how to combine Javascript world with Python/notebook. The project structure of cutecharts is the same as pyecharts and it supports all core features with pyecharts while being more lightweight also more concise overall.

The aim of this project is showing others that it's not difficult to write a pyecharts-like project. In fact, pyecharts does have no magic in its source code. As a member of Python cummunity, I sincerely hope more and more developers can use their creativity to make lots of related projects for our favorite Python world.

## 🔰 Installation

**pip install**
```shell
$ pip(3) install cutecharts
```

**install from source**
```shell
$ git clone https://github.com/cutecharts/cutecharts.py.git
$ cd cutecharts.py
$ pip install -r requirements.txt
$ python setup.py install
```

## 📝 Usage

* charts: [docs/charts.md](./docs/charts.md)
* components: [docs/components.md](./docs/components.md)
* changelog: [docs/changelog.md](./docs/changelog.md)

### Render HTML

```python
from cutecharts.charts import Line


chart = Line("某商场销售情况")
chart.set_options(
    labels=["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"], 
    x_label="I'm xlabel", 
    y_label="I'm ylabel",
)
chart.add_series("series-A", [57, 134, 137, 129, 145, 60, 49])
chart.add_series("series-B", [114, 55, 27, 101, 125, 27, 105])
chart.render()
```

And the `render.html` is rendered as below. Isn't that cool！

<p align="center">
    <img src="https://user-images.githubusercontent.com/19553554/66697904-34a30480-ed0c-11e9-8827-656e2c274ca2.png"  width="85%" />
</p>

### Notebook

#### Jupyter Notebook

![](https://user-images.githubusercontent.com/19553554/66697950-8f3c6080-ed0c-11e9-99db-4337e82bc682.png)

#### JupyterLab

There are some jupyterlab details that you should pay attention to.
```python
# 1. imoport this on the top.
from cutecharts.globals import use_jupyter_lab; use_jupyter_lab()

# 2. call the `load_javascript` function when you renders chart first time.
chart.load_javascript()
```

![](https://user-images.githubusercontent.com/19553554/66731058-e581de80-ee87-11e9-971b-ee6c460b94c5.png)


## 🔖 Demo

> All demo codes are under examples directory.

<div align="center">
    <img src="https://user-images.githubusercontent.com/19553554/66558121-9f760380-eb85-11e9-8b37-6d4dbd39f2e8.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558192-bddbff00-eb85-11e9-8cf1-bef4b93434af.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558265-db10cd80-eb85-11e9-8450-1535b6e68bc7.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558482-317e0c00-eb86-11e9-96f9-4de0f1611c3d.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558545-4ce91700-eb86-11e9-9cda-402e1e6f19b1.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558614-6c803f80-eb86-11e9-8386-46315c5f0843.png" width="33%"/>
</div>

## ⛏ Software development

### Unit tests

```shell
$ pip install -r tests/requirements.txt
$ test
```

### CI/CD

[Travis CI](https://travis-ci.org/) and [AppVeyor](https://ci.appveyor.com/) is place for continuous integration.

### Coding styles

[flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) and [pylint](https://www.pylint.org/) are used.

## 📃 License

MIT [©chenjiandongx](https://github.com/chenjiandongx)
