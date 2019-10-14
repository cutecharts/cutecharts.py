# Components 组件详情

cutecharts 提供的组件类型如下。


### Page（顺序多图）

> cutecharts.components.Page

```
Params                                          Desc
------                                          ----
assets_host: Optional[str] = None               引用资源 Host
```

#### API

> cutecharts.components.Page.add

```
Params                                          Desc
------                                          ----
*charts                                         charts 类型图表实例
```

> cutecharts.components.Page.render

```
Params                                          Desc
------                                          ----
dest: str = "render.html"                       渲染的文件路径
template_name: str = "page_local.html"          渲染使用的模板，一般不需要修改   
```

> cutecharts.components.Page.render_notebook

```
Params                                          Desc
------                                          ----
template_type: str = "page"                     渲染使用的模板类型，一般不需要修改 
```

> cutecharts.components.Page.load_javascript

```
加载 JS 依赖，在 JupyterLab 渲染时使用。
```

#### Demo

```python
from cutecharts.charts import Bar, Line
from cutecharts.faker import Faker
from cutecharts.components import Page

def bar_base() -> Bar:
    chart = Bar("Bar-基本示例")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    return chart

def line_base() -> Line:
    chart = Line("Line-基本示例")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart

page = Page()
page.add(bar_base(), line_base())
page.render()
```
![](https://user-images.githubusercontent.com/19553554/66559323-c46b7600-eb87-11e9-96f0-eb0b5b84c31f.png)
