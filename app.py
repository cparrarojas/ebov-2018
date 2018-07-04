import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

import matplotlib
from matplotlib import cm
import numpy as np

linecolours = ['rgba(0,114,178,1.)', 'rgba(230,159,0,1.)']

magma_cmap = cm.get_cmap('magma')

magma_rgb = []

norm = matplotlib.colors.Normalize(vmin=0, vmax=255)

for i in range(0, 255):
       k = matplotlib.colors.colorConverter.to_rgb(magma_cmap(norm(i)))
       magma_rgb.append(k)

def matplotlib_to_plotly(cmap, pl_entries):
    h = 1.0/(pl_entries-1)
    pl_colorscale = []

    for k in range(pl_entries):
        C = list(map(np.uint8, np.array(cmap(k*h)[:3])*255))
        pl_colorscale.append([k*h, 'rgb'+str((C[0], C[1], C[2]))])

    return pl_colorscale

magma = matplotlib_to_plotly(magma_cmap, 255)

app = dash.Dash()

df = pd.read_csv('app_data.csv')

df_like = pd.read_csv('likelihood.csv')

data_ebov = pd.read_csv('https://raw.githubusercontent.com/calthaus/Ebola/master/DRC%20(GitHub%202018)/Ebola_outbreak_DRC2018_data.csv')['Cumulative'].values

best_params = [df.iloc[-1]['beta'], df.iloc[-1]['k']]

variables = ['cumulative', 'E', 'I']
labels = ['cumulative incidence', 'exposed individuals', 'infectious individuals']

app.layout = html.Div([
html.Div(children=[
    html.H1(children='2018 Ebola outbreak in the Democratic Republic of Congo')]),
html.Div([
#
    html.Div([
        dcc.Dropdown(
            id='variable',
            options=[{'label': labels[i], 'value': j} for i, j in enumerate(variables)],
            value='cumulative'
        ),
    ],
    style={'width': '49%', 'display': 'inline-block'}),
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(
            id='landscape',
            hoverData={'points': [{'x': best_params[0], 'y': best_params[1]}]},
            figure={
            'data': [go.Scatter(
                        x=df_like['beta'],
                        y=df_like['k'],
                        text=df_like['likelihood'],
                        #customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
                        mode='markers',
                        marker={
                            'size': 18,
                            'opacity': 0.8,
                            #'line': {'width': 0.5, 'color': 'white'},
                            'color': df_like['likelihood'],
                            'colorscale': magma
                        }
                    )],
                    'layout': go.Layout(
                        title='',
                        titlefont=dict(
                            family='Old Standard TT, serif',
                            size=35
                            ),
                        xaxis={
                            'title': 'beta',
                            'type': 'linear',
                            'titlefont' : dict(
                                family='Old Standard TT, serif',
                                size=25
                                ),
                            'automargin': True,
                            'fixedrange': True
                            },
                        yaxis={
                            'title': 'k',
                            'type': 'linear',
                            'titlefont' : dict(
                                family='Old Standard TT, serif',
                                size=25
                                ),
                            'automargin': True,
                            'fixedrange': True
                        },
                        margin={'l': 40, 'b': 30, 't': 60, 'r': 0},
                        height=800,
                        hovermode='closest',
                        annotations=[{
                            'x': 0.5, 'y': 1., 'xanchor': 'center', 'yanchor': 'bottom',
                            'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                            'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 1.)',
                            'text': 'likelihood', 'font': dict(color = "black", size = 35, family='Old Standard TT, serif')
                        }]
                    )
                }
        )
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='time-series'),
        dcc.Graph(id='R_t'),
    ], style={'display': 'inline-block', 'width': '45%'})#,
])

def create_time_series(dff, variable, title):
    if variable == 'R_t':
        xtitle = 'days since 5 April 2018'
        xticklabels = True,
        thedata = [go.Scatter(
            x=dff['time'],
            y=dff[variable],
            mode='lines',
            line=dict(width=1.5, color=linecolours[0]),
            showlegend=False,
            hoverinfo='x+y'
        ),
        go.Scatter(
            x=dff['time'],
            y=np.ones(len(dff['time'])),
            mode='lines',
            line=dict(width=1.5, color=linecolours[1], dash='dash'),
            showlegend=False,
            hoverinfo='x+y'
        )]
    else:
        xtitle = ''
        xticklabels = False,
        thedata = [go.Scatter(
            x=dff['time'],
            y=dff[variable + ' m'],
            mode='lines',
            line=dict(width=1.5, color=linecolours[0]),
            showlegend=False,
            hoverinfo='x+y'
        ),
        go.Scatter(
            x=dff['time'],
            y=dff[variable + ' p'],
            mode='lines',
            line=dict(width=1.5, color=linecolours[0]),
            showlegend=False,
            fill='tonexty',
            hoverinfo='x+y'
        )]
    if variable=='cumulative':
        thedata.append(go.Scatter(
            x=dff['time'][:len(data_ebov)],
            y=data_ebov,
            name='data',
            mode='markers',
            marker=dict(size=10,color=linecolours[1], opacity=0.8),
            showlegend=True,
            hoverinfo='x+y'
        ))
    return {
        'data': thedata,
        'layout': {
            'height': 390,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 20},
            'yaxis': {'type': 'linear', 'title': title, 'titlefont' : dict(family='Old Standard TT, serif', size=25), 'automargin': True, 'fixedrange': True},
            'xaxis': {'type': 'linear', 'title': xtitle, 'titlefont' : dict(family='Old Standard TT, serif', size=25), 'showgrid': False, 'showticklabels': xticklabels, 'automargin': True, 'fixedrange': True},
            'legend': dict(font=dict(family='Old Standard TT, serif', size=18, color='black'))
            }
    }


@app.callback(
    dash.dependencies.Output('time-series', 'figure'),
    [dash.dependencies.Input('landscape', 'hoverData'),
     dash.dependencies.Input('variable', 'value')])#,
def update_x_timeseries(hoverData, variable):
    beta = hoverData['points'][0]['x']
    k = hoverData['points'][0]['y']
    dff = df[(df['beta'] == beta) & (df['k'] == k)]
    dff = dff[['time', variable, variable+' m', variable+' p']]
    if variable == 'cumulative':
        title = 'cumulative incidence'
    elif variable == 'E':
        title = 'exposed individuals'
    else:
        title = 'infectious individuals'
    return create_time_series(dff, variable, title)


@app.callback(
    dash.dependencies.Output('R_t', 'figure'),
    [dash.dependencies.Input('landscape', 'hoverData')])
def update_y_timeseries(hoverData):
    beta = hoverData['points'][0]['x']
    k = hoverData['points'][0]['y']
    dff = df[(df['beta'] == beta) & (df['k'] == k)]
    dff = dff[['time', 'R_t']]
    return create_time_series(dff, 'R_t', 'reproductive number')


if __name__ == '__main__':
    app.run_server()
