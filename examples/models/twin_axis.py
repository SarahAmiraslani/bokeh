''' This example demonstrates how to create a plot with two y-axes.

.. bokeh-example-metadata::
    :apis: bokeh.plotting.figure.circle, bokeh.models.sources.ColumnDataSource, bokeh.models.markers.Circle
    :refs: :ref:`ug_basic_scatters`, :ref:`ug_basic_axes_twin`
    :keywords: twin axis, circle

'''

from numpy import arange, linspace, pi, sin

from bokeh.document import Document
from bokeh.embed import file_html
from bokeh.models import (Circle, ColumnDataSource, LinearAxis,
                          PanTool, Plot, Range1d, WheelZoomTool)
from bokeh.resources import INLINE
from bokeh.util.browser import view

x = arange(-2*pi, 2*pi, 0.1)
y = sin(x)
y2 = linspace(0, 100, len(y))

source = ColumnDataSource(
    data=dict(x=x, y=y, y2=y2)
)

plot = Plot(x_range=Range1d(start=-6.5, end=6.5), y_range=Range1d(start=-1.1, end=1.1), min_border=80)

plot.extra_x_ranges = {"qux": Range1d(start=100, end=0)}
plot.extra_y_ranges = {"foo": Range1d(start=0, end=100)}

plot.add_layout(LinearAxis(axis_label="default range"), 'above')
plot.add_layout(LinearAxis(axis_label="qux range", x_range_name="qux"), 'above')

plot.add_layout(LinearAxis(axis_label="default range"), 'below')
plot.add_layout(LinearAxis(axis_label="qux range", x_range_name="qux"), 'below')

plot.add_layout(LinearAxis(axis_label="default range"), 'left')
plot.add_layout(LinearAxis(axis_label="foo range", y_range_name="foo"), 'left')

plot.add_layout(LinearAxis(axis_label="default range"), 'right')
plot.add_layout(LinearAxis(axis_label="foo range", y_range_name="foo"), 'right')

circle = Circle(x="x", y="y", fill_color="red", size=5, line_color="black")
plot.add_glyph(source, circle)

circle2 = Circle(x="x", y="y2", fill_color="blue", size=5, line_color="black")
plot.add_glyph(source, circle2, y_range_name="foo")

plot.add_tools(PanTool(), WheelZoomTool())

doc = Document()
doc.add_root(plot)

if __name__ == "__main__":
    doc.validate()
    filename = "twin_axis.html"
    with open(filename, "w") as f:
        f.write(file_html(doc, INLINE, "Twin Axis Plot"))
    print(f"Wrote {filename}")
    view(filename)
