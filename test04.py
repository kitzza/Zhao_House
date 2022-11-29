from pyecharts.charts import Bar
from pyecharts import options as opts

bar = (
    Bar()
    .add_xaxis(["周喜悦1号", "周汐悦2号", "周汐悦3号", "周汐悦4号", "周汐悦5号", "周汐悦6号", "周汐悦7号"])
    .add_yaxis("一班", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("二班", [57, 134, 137, 129, 145, 60, 49])
    .add_yaxis("三班c", [113, 55, 27, 101, 125, 27, 105])
    .set_global_opts(title_opts=opts.TitleOpts(title="周汐悦情况"))
)
bar.render()