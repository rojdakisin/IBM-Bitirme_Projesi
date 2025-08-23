#GÖREV 1: Bir Fırlatma Yeri Açılır Giriş Bileşeni Ekleyin
#GÖREV 2: Seçilen yer açılır menüsüne göre success-pie-chart‘ı render etmek için bir geri çağırma işlevi ekleyin
#GÖREV 3: Yükü Seçmek için Bir Aralık Kaydırıcısı Ekleyin
#GÖREV 4: success-payload-scatter-chart dağılım grafiğini render etmek için bir geri çağırma işlevi ekleyin

# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout                              
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center', 'color': '#503D36','font-size': 40}),

    # GÖREV 1: Launch Site seçimi için açılır menü
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'Tüm Siteler', 'value': 'ALL'}] +
                [{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()],
        value='ALL',
        placeholder='Buradan Bir Lansman Yeri Seçin',
        searchable=True
    ),

    html.Br(),

    # GÖREV 2: Başarı oranı pasta grafiği
    dcc.Graph(id='success-pie-chart'),

    html.Br(),

    # GÖREV 3: Payload aralığı seçim kaydırıcısı
    html.P("Yük Aralığı (Kg):"),
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: f'{i} kg' for i in range(0, 10001, 2500)},
        value=[min_payload, max_payload]
    ),

    html.Br(),

    # GÖREV 4: Payload ve Başarı ilişkisinin dağılım grafiği
    dcc.Graph(id='success-payload-scatter-chart')
])
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Tüm sitelerdeki başarılı fırlatmaları göster
        fig = px.pie(
            spacex_df[spacex_df['class'] == 1],
            names='Launch Site',
            title='Tüm Fırlatma Sitelerinde Başarılı Fırlatmalar'
        )
    else:
        # Seçilen site için başarı ve başarısızlık sayıları
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        counts = filtered_df['class'].value_counts().reset_index()
        counts.columns = ['class', 'count']
        counts['class'] = counts['class'].replace({1: 'Başarılı', 0: 'Başarısız'})
        fig = px.pie(
            counts,
            names='class',
            values='count',
            title=f'{selected_site} için Başarılı ve Başarısız Fırlatmalar'
        )
    return fig

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(selected_site, payload_range):
    low, high = payload_range

    # Payload aralığına göre filtre
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]

    if selected_site == 'ALL':
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Tüm Siteler için Yük ve Başarı İlişkisi',
            hover_data=['Launch Site']
        )
    else:
        filtered_site_df = filtered_df[filtered_df['Launch Site'] == selected_site]
        fig = px.scatter(
            filtered_site_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'{selected_site} için Yük ve Başarı İlişkisi',
            hover_data=['Launch Site']
        )
    return fig

                                
# Run the app
if __name__ == '__main__':
    app.run()
