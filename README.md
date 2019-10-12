<p align="center">
    <img src="https://user-images.githubusercontent.com/19553554/66697551-27384b00-ed09-11e9-9fe8-210918fdeb77.png" alt="pyecharts logo" width=600/>
</p>

<p align="center">
    <i>📉 Hand drawing style charts library for Python.</i>
</p>

<p align="center">
    <a href="https://travis-ci.org/chenjiandongx/cutecharts">
        <img src="https://travis-ci.org/chenjiandongx/cutecharts.svg?branch=master" alt="Travis Build Status">
    </a>
    <a href="https://ci.appveyor.com/project/chenjiandongx/cutecharts">
        <img src="https://ci.appveyor.com/api/projects/status/81cbsfjpfryv1cl8/branch/master?svg=true" alt="Appveyor Build Status">
    </a>
    <a href="https://codecov.io/gh/chenjiandongx/cutecharts">
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
     <a href="https://github.com/chenjiandongx/cutecharts/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

## 📣 初衷

在闲逛 Github 的时候，发现了一个十分有趣的图表库 [chart.xkcd](https://github.com/timqian/chart.xkcd)，该库的图表的手绘风格很可爱。所以有了一个将 chart.xkcd 和 Python 相结合的想法，这个想法最终变成了你现在所看到的 [cutecharts](https://github.com/chenjiandongx/cutecharts)。

chart.xkcd 的图表类型相对 Echarts 来说少得多，只支持几种基本的图表且没有太多的配置项，想使用更丰富的图表的话 [pyecharts](https://github.com/pyecharts/pyecharts) 或许是个更好的选择。cutecharts 我个人的想法是作为一个学习如何将 Javascript 与 Python/Notebook 相结合的项目。毋庸置疑，JS 库在交互性以及动画效果上有天然的优势，若能够将其优势与 Notebook 环境结合起来的话，那将能够产生很多有趣的项目。

cutecharts 的项目结构与 pyecharts 基本保持一致，拥有 pyecharts 的所有核心功能。但是整体更加小巧，代码更加精简。如果把 cutecharts 代码读完了，再去看 pyecharts 的代码，可能就会发现，其实也就那样，根本就没什么神秘的东西。在这里也是抛砖引玉，希望 Python 社区有更多地将 JS 与 Python/Notebook 结合的优秀第三方库。**cutecharts 的学习价值远大于它的使用价值。**

## 🔰 安装

**pip 安装**
```shell
$ pip(3) install cutecharts
```

**源码安装**
```shell
$ git clone https://github.com/chenjiandongx/cutecharts.git
$ cd cutecharts
$ pip install -r requirements.txt
$ python setup.py install
```

## 📝 使用

* 图表文档：[docs/charts.md](./docs/charts.md)
* 组件文档：[docs/components.md](./docs/components.md)

### 本地环境

#### 生成 HTML

```python
from cutecharts.charts import Line


chart = Bar("某商场销售情况")
chart.set_options(
    labels=["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"], 
    x_label="I'm xlabel", 
    y_label="I'm ylabel",
)
chart.add_series("series-A", [57, 134, 137, 129, 145, 60, 49])
chart.add_series("series-B", [114, 55, 27, 101, 125, 27, 105])
chart.render()
```

`render` 方法会在本地生成一个 render.html 文件，使用浏览器打开。

<p align="center">
    <img src="https://user-images.githubusercontent.com/19553554/66697904-34a30480-ed0c-11e9-8827-656e2c274ca2.png"  width="85%" />
</p>

### Notebook 环境

#### Jupyter Notebook

![](https://user-images.githubusercontent.com/19553554/66697950-8f3c6080-ed0c-11e9-99db-4337e82bc682.png)


## 🔖 Demo

> Demo 代码位于 example 文件夹下。

<div align="center">
    <img src="https://user-images.githubusercontent.com/19553554/66558121-9f760380-eb85-11e9-8b37-6d4dbd39f2e8.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558192-bddbff00-eb85-11e9-8cf1-bef4b93434af.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558265-db10cd80-eb85-11e9-8450-1535b6e68bc7.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558482-317e0c00-eb86-11e9-96f9-4de0f1611c3d.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558545-4ce91700-eb86-11e9-9cda-402e1e6f19b1.png" width="33%"/>
    <img src="https://user-images.githubusercontent.com/19553554/66558614-6c803f80-eb86-11e9-8386-46315c5f0843.png" width="33%"/>
</div>

## ⛏ 代码质量

### 单元测试

```shell
$ pip install -r test/requirements.txt
$ test
```

### 集成测试

使用 [Travis CI](https://travis-ci.org/) 和 [AppVeyor](https://ci.appveyor.com/) 持续集成环境。

### 代码规范

使用 [flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) 以及 [pylint](https://www.pylint.org/) 提升代码质量。

## 📃 License

MIT [©chenjiandongx](https://github.com/chenjiandongx)
