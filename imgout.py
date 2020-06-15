import pyecharts.options as opts
from pyecharts.charts import Line
from datesourcedata import Source
import datetime

end = datetime.date.today()
start = datetime.date.today() - datetime.timedelta(days=7)
d = Source()
x1 = d.sourcedatas().keys()
y1, y2, y3, y4 = [v[0] for k, v in d.sourcedatas().items()], [v[1] for k, v in d.sourcedatas().items()], [v[2] for k, v in d.sourcedatas().items()], [format(100 - v[3], '.3f') for k, v in d.sourcedatas().items()]

c = (
    Line()
    .add_xaxis(list(x1))
    .add_yaxis("总访问量", y1, is_connect_nones=True)
    .add_yaxis("正常访问量", y2, is_connect_nones=True)
    .add_yaxis("错误访问量", y3, is_connect_nones=True)
    .add_yaxis("不可用率", y4, is_connect_nones=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="slb-zuul"))
)
c.render(str(end) + ".html")
