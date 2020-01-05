from flask import Flask, render_template
from pyecharts.charts import Line,Map,Timeline,Pie, WordCloud
from pyecharts import options as opts
import pandas as pd
import pyecharts.options as opts

from pyecharts.charts import Line


app = Flask(__name__)

df=pd.read_csv('death_reason.csv')
words = [
    ("Unsafe water source", 3886.421),
    ("Poor sanitation", 2405.459),
    ("No access to handwashing facility", 5348.404),
    ("Indoor air pollution", 271089.3),
    ("Charter Communications", 2467),
    ("Non-exclusive breastfeeding", 2674.242),
    ("Discontinued breastfeeding", 100.923),
    ("Child wasting", 17742.47),
    ("Child stunting", 1636.863),
    ("Low birth weight", 39334.55),
    ("Secondhand smoke", 386641.4),
    ("Alcohol use", 670297.3),
    ("Drug use", 129306.3),
    ("Diet low in fruits", 718507.1),
    ("Diet low in vegetables", 277782.2),
    ("Unsafe sex", 73366.9),
    ("Low physical activity", 249699.3),
    ("High blood sugar", 891047.2),
    ("Obesity", 823869.3),
    ("High blood pressure", 2542365),
    ("Smoking", 2197653),
    ("Iron deficiency", 325.329),
    ("Zinc deficiency", 147.4667),
    ("Vitamin-A deficiency", 1690.184),
    ("Low bone mineral density", 68054.92),
    ("Air pollution (outdoor & indoor)", 1242987),
    ("Outdoor air pollution", 1029848),
]
@app.route('/')
def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape = 'diamond')
        .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    return render_template('ciyun.html')


df2 = pd.read_csv('death_smoke.csv')
@app.route('/yx',methods=['GET'])
def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2000, 2017):
        map0 = (
            Map()
                .add(
                "", list(zip(list(df2.国家), list(df2["{}".format(i)]))), "world", is_map_symbol_show=False
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="2000年-2017年世界各国因吸烟死亡人数".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="black", font_size=16,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(max_=266, min_=15),

            )
        )
        tl.add(map0, "{}年".format(i))
    return render_template('yx.html')


df=pd.read_csv('death.csv')
@app.route('/wx',methods=['GET'])
def pie_position() -> Pie:
    b = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(list(df.death),(df['2017']))],
            center=["50%", "62%"],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="按危险因素统计的死亡人数"),
            legend_opts=opts.LegendOpts(pos_left="30%"),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    death = {'水污染': '3886.420648',
                 '室内空气污染': '271089.3473',
                 '非排他性母乳喂养': '1636.863121',
                 '低出生体重': '39334.54966',
                 '二手烟': '386641.4086',
                 '饮酒': '670297.3078',
                 '药物死亡': '129306.3197',
                 '不安全性行为': '73366.89943',
                 '高血糖': '891047.2355',
                 '肥胖': '823869.2608',
                 '高血压': '2542365.122',
                 '吸烟': '2197652.614',
                 '缺铁': '325.3290396',
                 '缺锌': '147.4666519',
                 '缺维他命': '1690.183543',
                 '低骨密度': '68054.92344',
                 '室内室外空气污染': '1242986.55',
                 '室外空气污染': '1029847.77', }
    return render_template('wx.html',the_death =death)


df3=pd.read_csv('smoke_cancer.csv')
@app.route('/xy',methods=['GET'])
def map_world() -> Map:
    c = (
        Map()
        .add("死亡比例", [list(z) for z in zip(list(df3.国家),(df3['2017']))], "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="吸烟导致癌症死亡比例"),
            visualmap_opts=opts.VisualMapOpts(max_=57.1,min_=2.2),
        )
    )

    return render_template('xy.html')


df4=pd.read_csv('smoking_age.csv',index_col="age")
x轴 = [int(x)for x in df4.columns.values]
七十岁以上 =list(df4.loc["70岁以上"].values)
十五至四十九岁 =list(df4.loc["15至49岁"].values)
五十至六十九岁 =list(df4.loc["50至69岁"].values)
@app.route('/nl',methods=['GET'])
def line_areastyle_boundary_gap() -> Line:
    c = (
        Line()
        .add_xaxis(["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"])
        .add_yaxis("70+ years old",七十岁以上, is_smooth=True)
        .add_yaxis("15-49 years old",十五至四十九岁, is_smooth=True)
        .add_yaxis("50-69 years old",五十至六十九岁, is_smooth=True)
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="按年龄划分的吸烟死亡人数"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
        )
    )
    return render_template('nl.html')



df6=pd.read_csv("China_smoke.csv",index_col="死亡原因")
吸烟=list(df6.loc["吸烟"].values)
@app.route('/xyzx',methods=['GET'])
def line_itemstyle() -> Line:
    c = (
        Line()
        .add_xaxis(xaxis_data=["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"])
        .add_yaxis(
            "吸烟死亡比例",
            吸烟,
            symbol="triangle",
            symbol_size=20,
            linestyle_opts=opts.LineStyleOpts(color="green", width=4, type_="dashed"),
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=3, border_color="yellow", color="blue"
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国因吸烟死亡比例"),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
        )
    )
    return render_template('xyzx.html')





@app.route('/result',methods=['GET'])
def index():
  return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True,port = 8001)