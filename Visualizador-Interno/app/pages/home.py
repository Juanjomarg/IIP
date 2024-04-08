from assets.libraries import *
from assets.commons import *
from assets.cards import *

import datetime
import os
import io
import itertools
import time

import statistics
import pandas as pd

import zipfile

import dash
import dash_bootstrap_components as dbc
from dash import html,Input,Output,dcc

import plotly.graph_objects as go

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