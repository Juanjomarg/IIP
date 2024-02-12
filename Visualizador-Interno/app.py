from assets.libraries import *
from assets.commons import *
import flask

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
    app.run_server(debug=True)