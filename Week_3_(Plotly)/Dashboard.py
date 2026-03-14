

import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
import warnings
warnings.filterwarnings('ignore')

# ── Load & Clean Data ─────────────────────────────────────────────
df = pd.read_csv('gapminder_cleaned.csv')
for col in ['gdp', 'hdi_index', 'co2_consump']:
    df[col] = df[col].fillna(df[col].median())

df_2007 = df[df['year'] == 2007].copy()
df_2007['hdi_index'] = df_2007['hdi_index'].fillna(df_2007['hdi_index'].median())
df_2007['life_exp']  = df_2007['life_exp'].fillna(df_2007['life_exp'].median())

life_trend    = df.groupby(['year', 'continent'])['life_exp'].mean().reset_index()
co2_trend     = df.groupby(['year', 'continent'])['co2_consump'].mean().reset_index()
gdp_cont_year = df.groupby(['year', 'continent'])['gdp'].mean().reset_index()
services_cont = df_2007.groupby('continent')['services'].mean().reset_index().sort_values('services', ascending=False)
selected      = ['United States', 'China', 'India', 'Brazil', 'Germany', 'Nigeria']
df_selected   = df[df['country'].isin(selected)]
top10         = df_2007.nlargest(10, 'gdp').sort_values('gdp', ascending=True)

# ── Build All Figures ─────────────────────────────────────────────
fig_hist = px.histogram(df_2007, x='gdp', color='continent', nbins=35,
    title='1. GDP per Capita Distribution (2007)',
    labels={'gdp': 'GDP per Capita (USD)'},
    template='plotly_white', barmode='overlay', opacity=0.75)

fig_line = px.line(life_trend, x='year', y='life_exp', color='continent', markers=True,
    title='2. Avg Life Expectancy by Continent Over Time',
    labels={'life_exp': 'Life Expectancy (yrs)', 'year': 'Year'},
    template='plotly_white')

fig_scatter = px.scatter(df_2007, x='gdp', y='life_exp', color='continent',
    hover_name='country', size='hdi_index', size_max=20,
    title='3. GDP vs Life Expectancy (2007)',
    labels={'gdp': 'GDP per Capita (USD)', 'life_exp': 'Life Expectancy (yrs)'},
    template='plotly_white')

fig_bar_top20 = px.bar(df_2007.nlargest(20, 'gdp').sort_values('gdp'),
    x='gdp', y='country', color='continent', orientation='h',
    title='4. Top 20 Countries by GDP per Capita (2007)',
    labels={'gdp': 'GDP per Capita (USD)', 'country': 'Country'},
    template='plotly_white')

fig_map = px.choropleth(df_2007, locations='country', locationmode='country names',
    color='life_exp', hover_name='country', color_continuous_scale='RdYlGn',
    title='5. World Map — Life Expectancy (2007)',
    labels={'life_exp': 'Life Exp (yrs)'}, template='plotly_white')
fig_map.update_layout(geo=dict(showframe=False))

fig_box_life = px.box(df_2007, x='continent', y='life_exp', color='continent',
    points='all', hover_name='country',
    title='6. Life Expectancy Distribution by Continent (2007)',
    labels={'life_exp': 'Life Expectancy (years)'}, template='plotly_white')

fig_box_gdp = px.box(df_2007, x='continent', y='gdp', color='continent',
    points='outliers', hover_name='country',
    title='7. GDP Distribution by Continent (2007)',
    labels={'gdp': 'GDP per Capita (USD)'}, template='plotly_white')

fig_co2_gdp = px.scatter(df_2007, x='gdp', y='co2_consump', color='continent',
    hover_name='country', size='life_exp', size_max=20,
    title='8. CO₂ Consumption vs GDP per Capita (2007)',
    labels={'gdp': 'GDP per Capita (USD)', 'co2_consump': 'CO₂ per Capita (metric tons)'},
    template='plotly_white')

fig_hdi = px.scatter(df_2007, x='hdi_index', y='life_exp', color='continent',
    hover_name='country', trendline='ols',
    title='9. HDI Index vs Life Expectancy (2007)',
    labels={'hdi_index': 'HDI Index', 'life_exp': 'Life Expectancy (years)'},
    template='plotly_white')

fig_services = px.bar(services_cont, x='continent', y='services', color='continent',
    title='10. Avg Services Sector (% of GDP) by Continent (2007)',
    labels={'services': 'Services (% of GDP)'}, template='plotly_white', text_auto='.1f')

fig_country_trend = px.line(df_selected, x='year', y='life_exp', color='country', markers=True,
    title='11. Life Expectancy Trend for Selected Countries (1998–2007)',
    labels={'life_exp': 'Life Expectancy (years)', 'year': 'Year'},
    template='plotly_white')

fig_co2_trend = px.line(co2_trend, x='year', y='co2_consump', color='continent', markers=True,
    title='12. Avg CO₂ Consumption by Continent Over Time',
    labels={'co2_consump': 'CO₂ per Capita (metric tons)', 'year': 'Year'},
    template='plotly_white')

fig_hdi_hist = px.histogram(df_2007, x='hdi_index', color='continent', nbins=30,
    title='13. HDI Index Distribution (2007)',
    labels={'hdi_index': 'Human Development Index'},
    template='plotly_white', barmode='overlay', opacity=0.75)

fig_top10 = px.bar(top10, x='gdp', y='country', color='continent', orientation='h',
    title='14. Top 10 Countries by GDP per Capita (2007)',
    labels={'gdp': 'GDP per Capita (USD)', 'country': 'Country'},
    template='plotly_white', text_auto='.0f')

fig_gdp_time = px.bar(gdp_cont_year, x='year', y='gdp', color='continent', barmode='group',
    title='15. Avg GDP per Capita by Continent Over Time',
    labels={'gdp': 'Avg GDP per Capita (USD)', 'year': 'Year'},
    template='plotly_white')

# ── Build Dash App ────────────────────────────────────────────────
app = dash.Dash(__name__)

card = {'width': '49%', 'display': 'inline-block', 'padding': '10px'}
full = {'width': '99%', 'display': 'inline-block', 'padding': '10px'}

app.layout = html.Div([

    # Header
    html.Div([
        html.H1('🌍 Global Development Dashboard',
                style={'textAlign': 'center', 'color': '#2c3e50', 'fontFamily': 'Arial'}),
        html.P('Gapminder Dataset — All 15 Visualizations | Plotly & Dash',
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontFamily': 'Arial'})
    ], style={'padding': '20px 0 10px 0', 'borderBottom': '2px solid #ecf0f1'}),

    # Row 1
    html.Div([
        html.Div([dcc.Graph(figure=fig_hist)],  style=card),
        html.Div([dcc.Graph(figure=fig_line)],  style=card),
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),

    # Row 2
    html.Div([
        html.Div([dcc.Graph(figure=fig_scatter)],   style=card),
        html.Div([dcc.Graph(figure=fig_bar_top20)], style=card),
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),

    # Row 3 — Full width map
    html.Div([
        html.Div([dcc.Graph(figure=fig_map)], style=full),
    ], style={'display': 'flex'}),

    # Row 4
    html.Div([
        html.Div([dcc.Graph(figure=fig_box_life)], style=card),
        html.Div([dcc.Graph(figure=fig_box_gdp)],  style=card),
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),

    # Row 5
    html.Div([
        html.Div([dcc.Graph(figure=fig_co2_gdp)], style=card),
        html.Div([dcc.Graph(figure=fig_hdi)],      style=card),
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),

    # Row 6
    html.Div([
        html.Div([dcc.Graph(figure=fig_services)],      style=card),
        html.Div([dcc.Graph(figure=fig_country_trend)], style=card),
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),

    # Row 7
    html.Div([
        html.Div([dcc.Graph(figure=fig_co2_trend)], style=card),
        html.Div([dcc.Graph(figure=fig_hdi_hist)],  style=card),
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),

    # Row 8
    html.Div([
        html.Div([dcc.Graph(figure=fig_top10)],    style=card),
        html.Div([dcc.Graph(figure=fig_gdp_time)], style=card),
    ], style={'display': 'flex', 'flexWrap': 'wrap'}),

    # Footer
    html.Div(
        html.P('Data Source: Gapminder Foundation | Built with Plotly Dash',
               style={'textAlign': 'center', 'color': '#95a5a6', 'fontFamily': 'Arial'}),
        style={'borderTop': '1px solid #ecf0f1', 'padding': '15px 0'}
    )

], style={'backgroundColor': '#f9f9f9', 'minHeight': '100vh'})

# ── Run Server ────────────────────────────────────────────────────
if __name__ == '__main__':
    print("Dashboard running at: http://127.0.0.1:8050")
    app.run(debug=True, port=8050)