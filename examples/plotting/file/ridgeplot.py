''' A `ridgeline plot`_ using the `Perceptions of Probability`_ dataset.
This example demonstrates the uses of categorical offsets to position
categorical values explicitly. This chart shows the distribution of responses
to the prompt *What probability would you assign to the phrase "Highly likely"*.

.. bokeh-example-metadata::
    :sampledata: perceptions
    :apis: bokeh.plotting.figure.patch, bokeh.models.sources.ColumnDataSource
    :refs: :ref:`userguide_categorical` > :ref:`userguide_categorical_offsets`
    :keywords: patch, alpha, categorical, palette, patch, ridgeline

.. _ridgeline plot: https://www.data-to-viz.com/graph/ridgeline.html
.. _Perceptions of Probability: https://github.com/zonination/perceptions

'''
import colorcet as cc
from numpy import linspace
from scipy.stats.kde import gaussian_kde

from bokeh.models import ColumnDataSource, Range1d, FixedTicker, PrintfTickFormatter
from bokeh.plotting import figure, show
from bokeh.sampledata.perceptions import probly

cats = list(reversed(probly.keys()))
palette = [cc.rainbow[i*15] for i in range(17)]

x = linspace(-20, 110, 500)
source = ColumnDataSource(data=dict(x=x))

p = figure(y_range=cats, width=900, x_range=(-5, 105), tools="hover", toolbar_location=None)
p.hover.tooltips.append(("name", "$name"))

for i, cat in enumerate(reversed(cats)):
    target_start = cats.index(cat) + 0.5 # middle of the current category
    target_end = target_start + 20       # arbitrary scaling to make plots pop

    xy = p.subplot(
        x_source=p.x_range,
        y_source=Range1d(start=0, end=1),
        x_target=p.x_range,
        y_target=Range1d(start=target_start, end=target_end),
    )

    pdf = gaussian_kde(probly[cat])
    source.add(pdf(x), cat)

    xy.patch("x", cat, color=palette[i], alpha=0.6, line_color="black", source=source, name=cat)

p.outline_line_color = None
p.background_fill_color = "#efefef"

p.xaxis.ticker = FixedTicker(ticks=list(range(0, 101, 10)))
p.xaxis.formatter = PrintfTickFormatter(format="%d%%")

p.ygrid.grid_line_color = None
p.xgrid.grid_line_color = "#dddddd"
p.xgrid.ticker = p.xaxis.ticker

p.axis.minor_tick_line_color = None
p.axis.major_tick_line_color = None
p.axis.axis_line_color = None

p.y_range.range_padding = 0.12

show(p)
