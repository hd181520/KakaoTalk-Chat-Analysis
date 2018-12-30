import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from colour import Color
import csv, operator

names = {}
start, end = '', ''
with open('data.csv') as f:
    next(f)
    rdr = csv.reader(f)
    for chat in rdr:
        if not start: 
            start = chat[0]
        end = chat[0]
        if chat[1] in names:
            names[chat[1]] += 1
        else:
            names[chat[1]] = 1
names = sorted(names.items(), key=operator.itemgetter(1), reverse=True)

labels = [i[0] for i in names]
values = [i[1] for i in names]

colors = [c.hex for c in list(Color('white').range_to(Color('black'), len(names)))]

trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=20),
               marker=dict(colors=colors),
               title=start + ' ~ ' + end)

plotly.offline.plot([trace], filename='result.html')
