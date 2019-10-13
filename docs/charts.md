# Charts 图表详情

cutecharts 提供的图表类型如下。

### Commons

不同图表有着部分相同的方法。

**`__init__`**

```
Params                                          Desc
------                                          ----
title: Optional[str] = None                     图表标题
width: str = "800px"                            图表宽度
height: str = "600px"                           图表高度
assets_host: Optional[str] = None               引用资源 Host
```

**`render`**

```
Params                                          Desc
------                                          ----
dest: str = "render.html"                       渲染的文件路径
template_name: str = "basic_local.html"         渲染使用的模板，一般不需要修改   
```


**`render_notebook`**

```
Params                                          Desc
------                                          ----
template_name: str = "basic_notebook.html"      渲染使用的模板，一般不需要修改   
```


### Bar（柱状图）

> cutecharts.charts.Bar

#### API

> cutecharts.charts.Bar.set_options

```
Params                                          Desc
------                                          ----
labels: Iterable                                X 坐标轴标签数据
x_label: str = ""                               X 坐标轴名称
y_label: str = ""                               Y 坐标轴名称
y_tick_count: int = 3                           Y 轴刻度分割段数
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family
```

> cutecharts.charts.Bar.add_series

```
Params                                          Desc
------                                          ----
name: str                                       series 名称
data: Iterable                                  series 数据列表
```

#### Demo

> Bar-基本示例

```python
from cutecharts.charts import Bar
from cutecharts.components import Page
from cutecharts.faker import Faker


def bar_base() -> Bar:
    chart = Bar("Bar-基本示例")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    return chart

bar_base().render()
```
![](https://user-images.githubusercontent.com/19553554/66558121-9f760380-eb85-11e9-8b37-6d4dbd39f2e8.png)

> Bar-调整颜色

```python
def bar_tickcount_colors():
    chart = Bar("Bar-调整颜色")
    chart.set_options(labels=Faker.choose(), y_tick_count=10, colors=Faker.colors)
    chart.add_series("series-A", Faker.values())
    return chart
```
![](https://user-images.githubusercontent.com/19553554/66558148-abfa5c00-eb85-11e9-8fe8-e33fef1a73de.png)


### Line（折线图）

> cutecharts.charts.Line

#### API

> cutecharts.charts.Line.set_options

```
Params                                          Desc
------                                          ----
labels: Iterable                                X 坐标轴标签数据
x_label: str = ""                               X 坐标轴名称
y_label: str = ""                               Y 坐标轴名称
y_tick_count: int = 3                           Y 轴刻度分割段数
legend_pos: str = "upLeft"                      图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family
```

> cutecharts.charts.Line.add_series

```
Params                                          Desc
------                                          ----
name: str                                       series 名称
data: Iterable                                  series 数据列表
```

#### Demo

> Line-基本示例

```python
from cutecharts.charts import Line
from cutecharts.components import Page
from cutecharts.faker import Faker


def line_base() -> Line:
    chart = Line("Line-基本示例")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart
line_base().render()
```
![](https://user-images.githubusercontent.com/19553554/66558192-bddbff00-eb85-11e9-8cf1-bef4b93434af.png)

> Line-Legend 位置

```python
def line_legend():
    chart = Line("Line-Legend 位置")
    chart.set_options(labels=Faker.choose(), legend_pos="upRight")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart
```
![](https://user-images.githubusercontent.com/19553554/66558232-cdf3de80-eb85-11e9-9081-a116b25b18df.png)

> Line-调整颜色

```python
def line_tickcount_colors():
    chart = Line("Line-调整颜色")
    chart.set_options(labels=Faker.choose(), colors=Faker.colors, y_tick_count=8)
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart
```
![](https://user-images.githubusercontent.com/19553554/66558265-db10cd80-eb85-11e9-8450-1535b6e68bc7.png)


### Pie（饼图）

> cutecharts.charts.Pie

#### API

> cutecharts.charts.Pie.set_options

```
Params                                          Desc
------                                          ----
labels: Iterable                                数据标签列表
inner_radius: float = 0.5                       Pie 图半径
legend_pos: str = "upLeft"                      图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family
```

> cutecharts.charts.Pie.add_series

```
Params                                          Desc
------                                       ----
data: Iterable                                  series 数据列表
```

#### Demo

> Pie-基本示例

```python
from cutecharts.charts import Pie
from cutecharts.components import Page
from cutecharts.faker import Faker


def pie_base() -> Pie:
    chart = Pie("Pie-基本示例")
    chart.set_options(labels=Faker.choose())
    chart.add_series(Faker.values())
    return chart


pie_base().render()
```
![](https://user-images.githubusercontent.com/19553554/66558305-ecf27080-eb85-11e9-91ff-ed2cf669f9c0.png)

> Pie-Legend

```python
def pie_legend_font():
    chart = Pie("Pie-Legend")
    chart.set_options(
        labels=Faker.choose(),
        legend_pos="downLeft",
        font_family='"Times New Roman",Georgia,Serif;',
    )
    chart.add_series(Faker.values())
    return chart
```
![](https://user-images.githubusercontent.com/19553554/66558482-317e0c00-eb86-11e9-96f9-4de0f1611c3d.png)

> Pie-Radius

```python
def pie_radius():
    chart = Pie("Pie-Radius")
    chart.set_options(
        labels=Faker.choose(),
        inner_radius=0,
    )
    chart.add_series(Faker.values())
    return chart
```
![](https://user-images.githubusercontent.com/19553554/66558513-3e9afb00-eb86-11e9-8e54-ce9ab1f40132.png)


### Radar（雷达图）

> cutecharts.charts.Radar

#### API

> cutecharts.charts.Radar.set_options

```
Params                                          Desc
------                                          ----
labels: Iterable                                数据标签列表
is_show_label: bool = True                      是否显示标签
is_show_legend: bool = True                     是否显示图例
tick_count: int = 3                             坐标系分割刻度
legend_pos: str = "upLeft"                      图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family
```

> cutecharts.charts.Radar.add_series

```
Params                                          Desc
------                                          ----
name: str                                       series 名称
data: Iterable                                  series 数据列表
```

#### Demo

> Radar-基本示例

```python
from cutecharts.charts import Radar
from cutecharts.components import Page
from cutecharts.faker import Faker


def radar_base() -> Radar:
    chart = Radar("Radar-基本示例")
    chart.set_options(labels=Faker.choose())
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart


radar_base().render()
```
![](https://user-images.githubusercontent.com/19553554/66558545-4ce91700-eb86-11e9-9cda-402e1e6f19b1.png)

> Radar-颜色调整

```python
def radar_legend_colors():
    chart = Radar("Radar-颜色调整")
    chart.set_options(labels=Faker.choose(), colors=Faker.colors, legend_pos="upRight")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart
```
![](https://user-images.githubusercontent.com/19553554/66558572-596d6f80-eb86-11e9-8023-2520948dadc2.png)


### Scatter（散点图）

> cutecharts.charts.Scatter

#### API

> cutecharts.charts.Scatter.set_options

```
Params                                          Desc
------                                          ----
x_label: str = ""                               X 坐标轴名称
y_label: str = ""                               Y 坐标轴名称
x_tick_count: int = 3                           X 轴刻度分割段数
y_tick_count: int = 3                           Y 轴刻度分割段数
is_show_line: bool = False                      是否将散点连成线
dot_size: int = 1                               散点大小
time_format: Optional[str] = None               日期格式
legend_pos: str = "upLeft"                      图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family
```

> cutecharts.charts.Scatter.add_series

```
Params                                          Desc
------                                          ----
name: str                                       series 名称
data: Iterable                                  series 数据列表，[(x1, y1), (x2, y2)]
```

#### Demo

> Scatter-基本示例

```python
from cutecharts.charts import Scatter
from cutecharts.components import Page
from cutecharts.faker import Faker


def scatter_base() -> Scatter:
    chart = Scatter("Scatter-基本示例")
    chart.set_options(x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart


scatter_base().render()
```
![](https://user-images.githubusercontent.com/19553554/66558614-6c803f80-eb86-11e9-8386-46315c5f0843.png)

> Scatter-散点大小

```python
def scatter_dotsize_tickcount():
    chart = Scatter("Scatter-散点大小")
    chart.set_options(dot_size=2, y_tick_count=8)
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart
```
![](https://user-images.githubusercontent.com/19553554/66558626-71dd8a00-eb86-11e9-9ead-8f81984680f6.png)

> Scatter-散点连成线

```python
def scatter_show_line():
    chart = Scatter("Scatter-散点连成线")
    chart.set_options(y_tick_count=8, is_show_line=True)
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart
```
![](https://user-images.githubusercontent.com/19553554/66558656-7f930f80-eb86-11e9-9e1d-4cb00ea5fc3e.png)
