from assets.commons import *

import dash
import dash_bootstrap_components as dbc
from dash import html,Input,Output,dcc

preguntas_df=pd.read_excel(UBI_AR['preguntas'])

respuestas_2021_df=pd.read_excel(UBI_AR['respuestas_2021'])
respuestas_2023_df=pd.read_excel(UBI_AR['respuestas_2023'])

resultados_2021_df=pd.read_excel(UBI_AR['resultados_2021'])
resultados_2023_df=pd.read_excel(UBI_AR['resultados_2023'])

p1_df=pd.read_excel(UBI_AR['p1'])
p2_df=pd.read_excel(UBI_AR['p2'])
p13_df=pd.read_excel(UBI_AR['p13'])
p14_df=pd.read_excel(UBI_AR['p14'])
p15_df=pd.read_excel(UBI_AR['p15'])
p16_df=pd.read_excel(UBI_AR['p16'])
p17_df=pd.read_excel(UBI_AR['p17'])
p18_df=pd.read_excel(UBI_AR['p18'])
p19_df=pd.read_excel(UBI_AR['p19'])
p20_df=pd.read_excel(UBI_AR['p20'])
p21_df=pd.read_excel(UBI_AR['p21'])
p22_df=pd.read_excel(UBI_AR['p22'])
p23_df=pd.read_excel(UBI_AR['p23'])
p24_1_df=pd.read_excel(UBI_AR['p24_1'])
p24_2_df=pd.read_excel(UBI_AR['p24_2'])
p24_3_df=pd.read_excel(UBI_AR['p24_3'])
p24_4_df=pd.read_excel(UBI_AR['p24_4'])
p24_5_df=pd.read_excel(UBI_AR['p24_5'])
p25_df=pd.read_excel(UBI_AR['p25'])
p26_df=pd.read_excel(UBI_AR['p26'])
p27_df=pd.read_excel(UBI_AR['p27'])
p28_df=pd.read_excel(UBI_AR['p28'])
p31_df=pd.read_excel(UBI_AR['p31'])
p32_df=pd.read_excel(UBI_AR['p32'])
p33_df=pd.read_excel(UBI_AR['p33'])
p34_df=pd.read_excel(UBI_AR['p34'])
p35_df=pd.read_excel(UBI_AR['p35'])
p36_df=pd.read_excel(UBI_AR['p36'])
p37_df=pd.read_excel(UBI_AR['p37'])
p38_df=pd.read_excel(UBI_AR['p38'])
p39_df=pd.read_excel(UBI_AR['p39'])

entidades_2023=list(respuestas_2023_df['entidad'].sort_values())

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.COSMO, dbc.icons.FONT_AWESOME],
    use_pages=True
)
server=app.server

selector_entidad = dcc.Dropdown(
    id="selector_entidad",
    options=[{'label': x, 'value': x} for x in entidades_2023],
    placeholder='Seleccione una entidad',
    value=ENTIDAD_INICIAL,
)

navbar = dbc.Navbar(
    dbc.Container(
        dbc.Row([
            dbc.Col(
                html.A(
                    [
                        dbc.NavbarBrand("Gestor de respuestas IIP 2023")
                    ],
                    href="/",
                    style={"textDecoration": "none"},
                ),
                width=4
            ),
            dbc.Col(
                html.Div(selector_entidad),
                width=5
            )
        ],
        justify="between",
        align="center",
        style={'width':'100%'}
        ),
    fluid=True,
    style={'height':'80px'}
    ),
    color="#f8f9fa",
)

sidebar = html.Div(
    [
        html.A([
                    html.Img(height="50px",src=LOGO_LAB,className='logolab',style={'max-width':'14.5em','object-fit': 'contain'}),
                    html.Img(height="50px",src=LOGO_IIP,className='logoiip'),
                    ],
                    href="/",
                    style={"textDecoration": "none"},
                    
                ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-house me-2"), 
                        html.Span("Inicio")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-chart-simple me-2"),
                        html.Span("Estadísticas"),
                    ],  
                    href="/stats",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-magnifying-glass me-2"),
                        html.Span("Explorador"),
                    ],
                    href="/explorer",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

app.layout = dbc.Container(
    [
        dcc.Store(id='entidad_seleccionada',data=[],storage_type='memory'),
        dcc.Store(id='entidad_seleccionada_nom',data=[],storage_type='memory'),
        navbar,
        sidebar,
        html.Div(
            [
                dash.page_container
            ],
            className="content",
        ),
    ]
)

@dash.callback(
    Output('entidad_seleccionada', 'data'),
    Input('selector_entidad', 'value')
)
def sel_entidad(value):
    
    if value != None:
        ent=list(respuestas_2023_df[respuestas_2023_df['entidad'] == value]['_uuid'])[0]
        #print(f'{value} -> {ent}\n')
        return ent
    
    else:
        value = entidades_2023[0]
        ent=list(respuestas_2023_df[respuestas_2023_df['entidad'] == value]['_uuid'])[0]
        #print(f'{value} -> {ent}\n')
        return ent
    
if __name__ == "__main__":
    app.run_server(debug=False)