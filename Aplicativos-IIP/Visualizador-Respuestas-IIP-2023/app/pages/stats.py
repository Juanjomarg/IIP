from assets.libraries import *
from assets.commons import *
from assets.cards import *

dash.register_page(__name__, path='/stats')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(children=['Estadísticas'])
            ],
            width=9,
        ),
        dbc.Col([
            html.Span('Estadísticas del IIP 2023')
            ],
            width=3,

        )
        ],
        justify="end"
    )
    ]
)