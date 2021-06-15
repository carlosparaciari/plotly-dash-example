# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from dash.dependencies import Input, Output

# Style dicts
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig_style = {
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font_color': colors['text']
}

text_style = {
    'textAlign': 'center',
    'color': colors['text'],
    'marginLeft': 'auto',
    'marginRight': 'auto'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Useful functions


def generate_table(dataframe, style_param, max_rows=5):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ],
        style=style_param
    )


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Europe dataframe and static figure
df_europe = px.data.gapminder().query("continent == 'Europe'")
df_europe.drop(columns=['continent', 'iso_num'], inplace=True)

fig_europe = px.bar(
    df_europe, 
    x="pop", 
    range_x=[0,int(8.5e7)],
    y="country", 
    color="country",
    animation_frame='year')

fig_europe.update_layout(**fig_style)

df_table_europe = df_europe.query('year == 2007').drop(columns=['year'])
df_table_europe.sort_values(by='pop', inplace=True, ascending=False)

# Americas dataframe and dropdown options
df_americas = px.data.gapminder().query("continent == 'Americas'")

options_americas = [
    {'label': country, 'value': iso}
    for country, iso in df_americas[['country', 'iso_alpha']].drop_duplicates().to_numpy()
]

# App layout
app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
    html.H1(
        children='Visualisation example with Dash',
        style=text_style
    ),

    html.Div(
        children='''
        In this example, we use the `gapminder` dataset to visualize
        some interesting statistics about Europe and the Americas.''',
        style=text_style
    ),

    html.Br(),

    html.H4(
        children='Population in Europe',
        style=text_style
    ),

    dcc.Graph(
        id='europe-population',
        figure=fig_europe
    ),

    html.Br(),

    html.H4(
        children='Population in Europe (2007)',
        style=text_style
    ),

    generate_table(df_table_europe, text_style),

    html.Br(),

    html.H4(
        children='GDP per capita in the Americas',
        style=text_style
    ),

    html.Label(
        children='American Countries',
        style={'color': colors['text'],}
    ),


    dcc.Dropdown(
        options=options_americas,
        value=['CAN', 'MEX'],
        multi=True,
        id='input-americas-country',
        style={'width': '50%'}
    ),

    html.Div([
        html.Div([
            html.H3('GDP in American coutries', style=text_style),
            dcc.Graph(id='americas-GDP')
        ],
            className="six columns"
        ),
        html.Div([
            html.H3('Population in American coutries (2007)', style=text_style),
            dcc.Graph(id='americas-pop')
        ],
            className="six columns"
        )
    ], className="row")

])

# App callbacks


@app.callback(
    Output(component_id='americas-GDP', component_property='figure'),
    Output(component_id='americas-pop', component_property='figure'),
    Input(component_id='input-americas-country', component_property='value')
)
def update_output_div(countries_iso_list):

    bool_countries = df_americas['iso_alpha'].isin(countries_iso_list)
    df_countries = df_americas.loc[bool_countries]

    fig_americas_line = px.line(
        df_countries,
        x='year',
        y='gdpPercap',
        color='country'
    )
    fig_americas_line.update_layout(**fig_style)

    df_countries_recent = df_countries.query("year == 2007")

    fig_americas_bar = px.bar(
        df_countries_recent,
        x='pop',
        y='country',
        color='country'
    )
    fig_americas_bar.update_layout(**fig_style)

    return fig_americas_line, fig_americas_bar


if __name__ == '__main__':
    app.run_server(debug=True)
