from assets.commons import *
from assets.cards import *

import dash
import dash_bootstrap_components as dbc
from dash import html

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

dash.register_page(__name__, path='/')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(children=['Home'])
            ],
            width=9,
        ),
        dbc.Col([
            html.Span('Bienvenida al IIP 2023')
            ],
            width=3,

        )
        ],
        justify="end"
    )
    ]
)