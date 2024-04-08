from assets.libraries import *
from assets.commons import *
from assets.cards import *
from assets.criteria import *

dash.register_page(__name__, path='/explorer')

par_spacer='1rem'
progress_thickness='.8rem'

selector_pregunta = dcc.Dropdown(
    id="selector_pregunta",
    options=[{'label': x, 'value': x} for x in PREGUNTAS_TODAS],
    placeholder='Seleccione la pregunta a analizar',
    value=PREGUNTA_INICIAL
)

tarjeta_resumen_2021 = dbc.Card(
    [
        
        dbc.CardBody(
            [
                
                html.H3(children='Posición 2021: ', className="card-title me-2",style={'display':'inline-block'}),
                html.H3(id='posicion_2021',children='', className="card-title",style={'display':'inline-block','font-weight':'bold'}),

                
                
                html.Div(
                    [
                        html.P(children='Total: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='st',value=0,label='',style={"height": f"{progress_thickness}"},color="success"),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C1: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc1',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C2: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc2',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C3: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc3',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C4: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc4',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),
            ]
        ),
    ],
)

tarjeta_resumen_2023 = dbc.Card(
    [
        
        dbc.CardBody(
            [
                
                html.H3(children='Posición 2023: ', className="card-title me-2",style={'display':'inline-block'}),
                html.H3(id='posicion_2023',children='', className="card-title",style={'display':'inline-block','font-weight':'bold'}),

                
                
                html.Div(
                    [
                        html.P(children='Total: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='st_2023',value=0,label='',style={"height": f"{progress_thickness}"},color="success"),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C1: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc1_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C2: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc2_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C3: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc3_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        html.P(children='C4: ', className="card-title me-2",style={'display':'inline-block','font-weight':'bold'}),
                        dbc.Progress(id='sc4_2023',value=0,label='',style={"height": f"{progress_thickness}"}),
                        html.Br()
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),

                html.Div(
                    [
                        dbc.Button(id='btn_actualizar_tablas',children='Actualizar componentes', style={'width':'100%'}),
                    ],
                    className="card-text",
                    style={'line-height':f'{par_spacer}'}
                ),
            ]
        ),
    ],
)

###############################################################################################################################################################################################################
# LAYOUT    
###############################################################################################################################################################################################################

layout = dbc.Container([

    #FILA 1
    dbc.Row([
        
        dcc.Store(id='pregunta_seleccionada',storage_type='memory'),

        dcc.Store(id='val1',storage_type='memory'),
        dcc.Store(id='val2',storage_type='memory'),
        dcc.Store(id='val3',storage_type='memory'),
        dcc.Store(id='val4',storage_type='memory'),
        dcc.Store(id='val5',storage_type='memory'),
        dcc.Store(id='val6',storage_type='memory'),
        dcc.Store(id='val7',storage_type='memory'),
        dcc.Store(id='val8',storage_type='memory'),

        #Nombre entidad seleccionada
        dbc.Col([
            html.H1(children=[],id='nom_ent',style={'font-weight':'bold'}),
            html.Br(),
            ],
            width=9,
        ),

        #Selector pregunta
        dbc.Col([
            selector_pregunta
            ],
            width=3,
        )
        ],
        justify="between",
        
    ),

    #FILA 2
    dbc.Row([

        #Mision, visión, pregunta, respuesta, criterio, respuesta 2021 y respuesta 2023
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Mision'),
                        html.P(id='mision',children=[])
                    ],                        
                    style={'padding':f'0rem 2rem 0rem 0rem','text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
                dbc.Col([
                    html.Div([
                        html.H3('Vision'),
                        html.P(id='vision',children=[])
                    ],
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
            ]),

            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Pregunta'),
                        html.P(id='pregunta',children=[]),
                    ],                        
                    style={'padding':f'0rem 2rem 0rem 0rem','text-justify':'auto','text-align': 'justify'}
                    ),
                ]),

                dbc.Col([
                    html.Div([
                        html.H3('Respuesta 2021'),
                        html.P(id='respuesta_2021',children=[]),
                    ],
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
            ]),

            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3(f'Respuesta 2023'),
                        html.Div(id='respuesta_2023',children='',),
                    ]),
                ]),
            ]),
        ],
        width=9,
        style={'padding':f'0rem 1.5rem 0rem 0rem'}
        ),
            
        #Tarjeta resumen 2021, zona de peligro, zona de descarga
        dbc.Col([
            tarjeta_resumen_2021,
            html.Br(),
            tarjeta_resumen_2023
        ],
        width=3
        )

    ],
    justify="end",
    ),
])

###############################################################################################################################################################################################################
# CALLBACKS
###############################################################################################################################################################################################################

#Callback guardar pregunta seleccionada
@dash.callback(
    Output('pregunta_seleccionada', 'data'),
    Input('selector_pregunta', 'value')
)
def seleccion_pregunta(value):
    if value != None:
        salida=value
    else:
        salida = preguntas_df[preguntas_df["codigo 2023"] == "p1"]["codigo 2023"].tolist()[0]
    return salida

#Callback ver respuestas
@dash.callback(
    Output('pregunta', 'children'),
    Output('respuesta_2021', 'children'),
    Output('respuesta_2023', 'children'),

    Input('entidad_seleccionada', 'data'),
    Input('pregunta_seleccionada', 'data'),
)
def visualizacion_respuestas(entidad_seleccionada,pregunta_seleccionada):
  
    def test_empty_pregunta(entidad_seleccionada,pregunta_seleccionada):
        #pregunta textual
        try:
            pregunta = preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['pregunta 2023']
            salida_pregunta=pregunta
            out_pre='Success'
        except Exception as e_pre:
            pregunta = 'N/A'
            salida_pregunta=pregunta
            out_pre=f"|||PREGUNTA||| Couldn't load pregunta due to {e_pre}"
            print(out_pre)

        return salida_pregunta,out_pre
    
    def test_empty_respuesta_2021(entidad_seleccionada,pregunta_seleccionada):
        #respuesta 2021
        try:
            respuesta_2021 = respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][pregunta_seleccionada]
            if respuesta_2021.empty ==False:
                salida_respuesta_2021=respuesta_2021
            else:
                salida_respuesta_2021 = 'N/A'
            out_2021='Success'
        except Exception as e_res_2021:
            salida_respuesta_2021 = respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada]['p1']
            out_2021=f"|||RESPUESTA 2021||| Couldn't load respuesta 2021 due to {e_res_2021}"
            print(out_2021)
        
        return salida_respuesta_2021,out_2021
    
    def test_empty_respuesta_2023(entidad_seleccionada,pregunta_seleccionada):
        #Respuesta 2023
        try:
            respuesta_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][pregunta_seleccionada]
            if respuesta_2023.empty ==False:
                salida_respuesta_2023=respuesta_2023
            else:
                salida_respuesta_2023 = 'N/A'
            out_2023='Success'
        except Exception as e_res_2023:
            salida_respuesta_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p1']
            out_2023=f"|||RESPUESTA 2023||| Couldn't load respuesta 2023 due to {e_res_2023}"
            print(out_2023)

        return salida_respuesta_2023,out_2023

    pregunta,error_pregunta=test_empty_pregunta(entidad_seleccionada,pregunta_seleccionada)
    respuesta_2021,error_2021=test_empty_respuesta_2021(entidad_seleccionada,pregunta_seleccionada)
    respuesta_2023,error_2023=test_empty_respuesta_2023(entidad_seleccionada,pregunta_seleccionada)

    estilo={'display':'flex','flex-wrap': 'wrap','justify-content':'space-between'}
    indices_carousel=[0]
    salida_criterio=indices_carousel

    if pregunta_seleccionada=='p1':

        indices_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p1_p2(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_1()
        
    elif pregunta_seleccionada=='p2':

        indices_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p1_p2(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_2()

    elif pregunta_seleccionada=='p3':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p3_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p3_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p4_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p4_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis=0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent=rel_enti_cos*100/rel_enti_pre
        except:
            res_ent=0
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_3()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p4':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p3_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p3_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p4_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p4_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p3_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p4_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis = 0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent=rel_enti_cos*100/rel_enti_pre
        except:
            res_ent=0

        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_4()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p5':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p5_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p5_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p6_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p6_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis =0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent=rel_enti_cos*100/rel_enti_pre
        except:
            res_ent =0
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_5()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p6':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df[f'p5_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df[f'p5_val_2'].median()
        costo_2021_dis = respuestas_2023_df[f'p6_val_1'].median()
        costo_2022_dis = respuestas_2023_df[f'p6_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p5_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p6_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis = 0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_cos*100/rel_enti_pre
        except:
            res_ent = 0
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_6()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p7':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            funcionarios_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis = 0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_7()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p8':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            funcionarios_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_8()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p9':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p8'])[0]
        except Exception as e:
            funcionarios_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada]['p8']
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_9()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p10':
        
        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            contratistas_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_10()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p11':

        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            contratistas_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])

        salida_criterio=criterio_11()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p12':

        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p11'])[0]
        except Exception as e:
            contratistas_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df[f'p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df[f'p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df[f'p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df[f'p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada]['p11']
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_12()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p13':

        indices_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        costo_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cos']
        soportes_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p13(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        cos_car=list(costo_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_13()
        
    elif pregunta_seleccionada=='p14':

        indices_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][pregunta_seleccionada])[0]
        except:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:

                try:
                    act_4_otr = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]                
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_14()
        
    elif pregunta_seleccionada=='p15':

        indices_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    act_4_otr = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_15()
        
    elif pregunta_seleccionada=='p16':

        indices_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_rom']
        act_1_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    act_4_otr = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_16()
        
    elif pregunta_seleccionada=='p17':
        
        indices_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_can']
        usuarios_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
            
        salida_criterio=criterio_17()
        
    elif pregunta_seleccionada=='p18':

        indices_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act']
        usuarios_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p17'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=["N/A"]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())

        salida_criterio=criterio_18()
        
    elif pregunta_seleccionada=='p19':

        indices_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    act_4_otr = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_19()
        
    elif pregunta_seleccionada=='p20':

        indices_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        act_1_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_1']
        act_2_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_2']
        act_3_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_3']
        act_4_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_4']
        act_5_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act/{pregunta_seleccionada}_act_5']
        acciones_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_post']
        soportes_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    act_4_otr = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_20()
        
    elif pregunta_seleccionada=='p21':

        indices_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_can']
        usuarios_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
            
        salida_criterio=criterio_21()
        
    elif pregunta_seleccionada=='p22':

        indices_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_act']
        usuarios_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'p21'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if indices_carousel.empty == True:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad='N/A'
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
            
        salida_criterio=criterio_22()
        
    elif pregunta_seleccionada=='p23':

        indices_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']
        usr_1_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr/{pregunta_seleccionada}_usr_1']
        usr_2_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr/{pregunta_seleccionada}_usr_2']
        usr_3_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_usr/{pregunta_seleccionada}_usr_3']
        prototipado = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_pro']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                try:
                    vali_usr_1_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val/{pregunta_seleccionada}_val_1']
                    vali_usr_2_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val/{pregunta_seleccionada}_val_2']
                    vali_usr_3_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val/{pregunta_seleccionada}_val_3']
                except:
                    vali_usr_1_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                    vali_usr_2_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                    vali_usr_3_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p23(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        us1_car=list(usr_1_carousel)[i],
                        us2_car=list(usr_2_carousel)[i],
                        us3_car=list(usr_3_carousel)[i],
                        pro_car=list(prototipado)[i],
                        va1_car=list(vali_usr_1_carousel)[i],
                        va2_car=list(vali_usr_2_carousel)[i],
                        va3_car=list(vali_usr_3_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_23()
        
    elif pregunta_seleccionada=='p24':

        p24_1_indices_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_1_codigos_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_nom']
        p24_1_descripciones_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_des']
        p24_1_impartio_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_imp']
        p24_1_asistentes_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_asi']
        p24_1_soportes_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_1_sop']

        p24_2_indices_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_2_codigos_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_nom']
        p24_2_descripciones_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_des']
        p24_2_impartio_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_imp']
        p24_2_asistentes_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_asi']
        p24_2_soportes_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_2_sop']

        p24_3_indices_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_3_codigos_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_nom']
        p24_3_descripciones_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_des']
        p24_3_impartio_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_imp']
        p24_3_asistentes_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_asi']
        p24_3_soportes_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_3_sop']

        p24_4_indices_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_4_codigos_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_nom']
        p24_4_descripciones_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_des']
        p24_4_impartio_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_imp']
        p24_4_asistentes_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_asi']
        p24_4_soportes_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_4_sop']

        p24_5_indices_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_5_codigos_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_nom']
        p24_5_descripciones_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_des']
        p24_5_impartio_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_imp']
        p24_5_asistentes_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_asi']
        p24_5_soportes_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_5_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':

            if p24_1_indices_carousel.empty == False:
                cards1=[]
                for i in range(len(p24_1_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_1_indices_carousel)[i],
                        nom_car=list(p24_1_codigos_carousel)[i],
                        des_car=list(p24_1_descripciones_carousel)[i],
                        imp_car=list(p24_1_impartio_carousel)[i],
                        asi_car=list(p24_1_asistentes_carousel)[i],
                        sop_car=list(p24_1_soportes_carousel)[i])
                    cards1.append(card)
            else:
                cards1=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]
            
            if p24_2_indices_carousel.empty == False:
                cards2=[]
                for i in range(len(p24_2_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_2_indices_carousel)[i],
                        nom_car=list(p24_2_codigos_carousel)[i],
                        des_car=list(p24_2_descripciones_carousel)[i],
                        imp_car=list(p24_2_impartio_carousel)[i],
                        asi_car=list(p24_2_asistentes_carousel)[i],
                        sop_car=list(p24_2_soportes_carousel)[i])
                    cards2.append(card)
            else:
                cards2=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            if p24_3_indices_carousel.empty == False:
                cards3=[]
                for i in range(len(p24_3_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_3_indices_carousel)[i],
                        nom_car=list(p24_3_codigos_carousel)[i],
                        des_car=list(p24_3_descripciones_carousel)[i],
                        imp_car=list(p24_3_impartio_carousel)[i],
                        asi_car=list(p24_3_asistentes_carousel)[i],
                        sop_car=list(p24_3_soportes_carousel)[i])
                    cards3.append(card)
            else:
                cards3=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            if p24_4_indices_carousel.empty == False:
                cards4=[]
                for i in range(len(p24_4_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_4_indices_carousel)[i],
                        nom_car=list(p24_4_codigos_carousel)[i],
                        des_car=list(p24_4_descripciones_carousel)[i],
                        imp_car=list(p24_4_impartio_carousel)[i],
                        asi_car=list(p24_4_asistentes_carousel)[i],
                        sop_car=list(p24_4_soportes_carousel)[i])
                    cards4.append(card)
            else:
                cards4=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]
            
            if p24_5_indices_carousel.empty == False:
                cards5=[]
                for i in range(len(p24_5_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_5_indices_carousel)[i],
                        nom_car=list(p24_5_codigos_carousel)[i],
                        des_car=list(p24_5_descripciones_carousel)[i],
                        imp_car=list(p24_5_impartio_carousel)[i],
                        asi_car=list(p24_5_asistentes_carousel)[i],
                        sop_car=list(p24_5_soportes_carousel)[i])
                    cards5.append(card)
            else:
                cards5=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            salida_respuesta_2023 = html.Div([
                    html.H5('Eventos Auspiciados y/o financiados directamente por esa entidad'),
                    html.Div(children=cards1,style=estilo),
                    html.H5('Eventos Auspiciados y/o financiados directamente por otras entidades'),
                    html.Div(children=cards2,style=estilo),
                    html.H5('Formación Auspiciada y/o financiada directamente por esa entidad'),
                    html.Div(children=cards3,style=estilo),
                    html.H5('Formación Auspiciada y/o financiada directamente por otras entidades'),
                    html.Div(children=cards4,style=estilo),
                    html.H5('Otras actividades de esa entidad'),
                    html.Div(children=cards5,style=estilo),
                ])
            
            salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_24()
        
    elif pregunta_seleccionada=='p25':

        indices_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        recomendacion_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_rec']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p25_p26(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        rec_car=list(recomendacion_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_25()
        
    elif pregunta_seleccionada=='p26':

        indices_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        recomendacion_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_rec']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""
        except:
            salida_respuesta_2021 = 'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p25_p26(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        rec_car=list(recomendacion_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_26()
        
    elif pregunta_seleccionada=='p27':

        indices_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        tematica_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des_001']
        tamano_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_c']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p27(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        tem_car=list(tematica_carousel)[i],
                        tam_car=list(tamano_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_27()
        
    elif pregunta_seleccionada=='p28':

        indices_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'nom_inno']
        implementado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_imp']
        validado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_val']
        metodologia_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'meto']
        beneficia_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_ben']
        ahorro_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_aho']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                if list(beneficia_carousel)[0]=='Si':
                    beneficiados_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'beneficiados']
                else:
                    beneficiados_carousel=['N/A' for x in range(len(indices_carousel)+1)]
                
                if list(ahorro_carousel)[0]=='Si':
                    ahorrado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'recursos_ahorrados']
                else:
                    ahorrado_carousel=['N/A' for x in range(len(indices_carousel)+1)]
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p28(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        imp_car=list(implementado_carousel)[i],
                        val_car=list(validado_carousel)[i],
                        met_car=list(metodologia_carousel)[i],
                        ben_car=list(beneficia_carousel)[i],
                        aho_car=list(ahorro_carousel)[i],
                        b1_car=list(beneficiados_carousel)[i],
                        a1_car=list(ahorrado_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_28()
        
    elif pregunta_seleccionada=='p29':

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            form_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            form_2021 = 'N/A'

        salida_respuesta_2021=f"Funcionarios y contratistas formados: \n {form_2021}"

        total_2021_dis = respuestas_2023_df[f'p7_val_1'].median()
        total_2022_dis = respuestas_2023_df[f'p7_val_2'].median()
        formados_2021_dis = respuestas_2023_df[f'p29_val_1'].median()
        formados_2022_dis = respuestas_2023_df[f'p29_val_2'].median()
        
        total_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_1']
        total_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p7_val_2']
        formados_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p29_val_1']
        formados_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p29_val_2']

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(total_2021_dis), float(total_2022_dis)])
        rel_dist_for = statistics.mean([float(formados_2021_dis), float(formados_2022_dis)])
        try:
            res_dis = rel_dist_for*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(total_2021_ent.iloc[0]), float(total_2022_ent.iloc[0])])
        rel_enti_for = statistics.mean([float(formados_2021_ent.iloc[0]), float(formados_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_for*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p29_p30(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=total_2021_dis,
            can_2022_dis=total_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=formados_2021_dis,
            fun_2022_dis=formados_2022_dis,
            fun_med_dis=rel_dist_for,
            res_dist=res_dis,

            can_2021_ent=list(total_2021_ent)[0],
            can_2022_ent=list(total_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(formados_2021_ent)[0],
            fun_2022_ent=list(formados_2022_ent)[0],
            fun_med_ent=rel_enti_for,
            res_enti=res_ent,
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_29()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p30':

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            form_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]
        except Exception as e:
            form_2021 = 'N/A'

        salida_respuesta_2021=f"Funcionarios y contratistas formados: \n {form_2021}"

        total_2021_dis = respuestas_2023_df[f'p10_val_1'].median()
        total_2022_dis = respuestas_2023_df[f'p10_val_2'].median()
        formados_2021_dis = respuestas_2023_df[f'p30_val_1'].median()
        formados_2022_dis = respuestas_2023_df[f'p30_val_2'].median()
        
        total_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_1']
        total_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p10_val_2']
        formados_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p30_val_1']
        formados_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'p30_val_2']

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(total_2021_dis), float(total_2022_dis)])
        rel_dist_for = statistics.mean([float(formados_2021_dis), float(formados_2022_dis)])
        try:
            res_dis = rel_dist_for*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(total_2021_ent.iloc[0]), float(total_2022_ent.iloc[0])])
        rel_enti_for = statistics.mean([float(formados_2021_ent.iloc[0]), float(formados_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_for*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p29_p30(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=total_2021_dis,
            can_2022_dis=total_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=formados_2021_dis,
            fun_2022_dis=formados_2022_dis,
            fun_med_dis=rel_dist_for,
            res_dist=res_dis,

            can_2021_ent=list(total_2021_ent)[0],
            can_2022_ent=list(total_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(formados_2021_ent)[0],
            fun_2022_ent=list(formados_2022_ent)[0],
            fun_med_ent=rel_enti_for,
            res_enti=res_ent,
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        salida_criterio=criterio_30()
        salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        
    elif pregunta_seleccionada=='p31':

        indices_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p31_p32(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_31()
        
    elif pregunta_seleccionada=='p32':

        indices_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        nombres_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_nom']
        descripciones_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_des']
        soportes_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p31_p32(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_32()
        
    elif pregunta_seleccionada=='p33':

        indices_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_33()
        
    elif pregunta_seleccionada=='p34':

        indices_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_34()
        
    elif pregunta_seleccionada=='p35':

        indices_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_35()
        
    elif pregunta_seleccionada=='p36':

        indices_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_36()
        
    elif pregunta_seleccionada=='p37':

        indices_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_37()
        
    elif pregunta_seleccionada=='p38':

        indices_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_38()
        
    elif pregunta_seleccionada=='p39':

        indices_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'_index']
        codigos_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_cod']
        soportes_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}_sop']

        salida_nota_2021=resultados_2021_df[resultados_2021_df['_uuid']==entidad_seleccionada][pregunta_seleccionada]
        salida_max_2021=preguntas_df[preguntas_df['codigo 2023'] == pregunta_seleccionada]['nota maxima']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{pregunta_seleccionada}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{pregunta_seleccionada}'])[0]}"""

        except Exception as e:
            salida_respuesta_2021 = f'No registra iniciativas'

        if list(respuesta_2023)[0] == 'Si':
            if indices_carousel.empty == True:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                salida_criterios_entidad=[]
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p39(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                salida_criterios_entidad=list(CRITS_PREGUNTAS_BASE[pregunta_seleccionada].keys())
        elif list(respuesta_2023)[0] == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=[]

        salida_criterio=criterio_39()
        
    else:
        salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Caso no definido',
                    color="danger",
                    dismissable=True,
                    is_open=True)])


    if pregunta_seleccionada == 'p3':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p4':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p5':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p6':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p7':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p8':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'
    
    elif pregunta_seleccionada == 'p9':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p10':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p11':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p12':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p24':
        salida_iniciativas=list(itertools.chain(p24_1_indices_carousel,p24_2_indices_carousel,p24_3_indices_carousel,p24_4_indices_carousel))

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p29':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    elif pregunta_seleccionada == 'p30':
        salida_iniciativas=[]

        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    else:
        salida_iniciativas=list(indices_carousel)
        
        try:
            salida_iniciativa_seleccionada=str(salida_iniciativas[0])
        except:
            salida_iniciativa_seleccionada='N/A'


        try:
            salida_criterios_entidad_seleccionado=str(salida_criterios_entidad[0])
        except:
            salida_criterios_entidad_seleccionado='N/A'

    return pregunta,salida_respuesta_2021,salida_respuesta_2023

#Callback nombre, misión y visión
@dash.callback(
    Output('nom_ent', 'children'),
    Output('mision', 'children'),
    Output('vision', 'children'),
    Input('entidad_seleccionada', 'data')
)
def mision_vision_entidad_f(value):

    nom_ent= respuestas_2023_df[respuestas_2023_df['_uuid'] == value]['entidad']
    
    mis = respuestas_2023_df[respuestas_2023_df['_uuid'] == value]['mision']
    vis = respuestas_2023_df[respuestas_2023_df['_uuid'] == value]['vision']

    if mis.empty ==False:
        mis_ent=mis
    else:
        mis_ent = 'N/A'

    if vis.empty ==False:
        vis_ent=vis
    else:
        vis_ent = 'N/A'

    return nom_ent,mis_ent,vis_ent

#Callback resumen 2021 lateral
@dash.callback(
    Output('posicion_2021', 'children'),
    Output('st', 'label'),
    Output('sc1', 'label'),
    Output('sc2', 'label'),
    Output('sc3', 'label'),
    Output('sc4', 'label'),
    Output('st', 'value'),
    Output('sc1', 'value'),
    Output('sc2', 'value'),
    Output('sc3', 'value'),
    Output('sc4', 'value'),
    Input('entidad_seleccionada', 'data')
)
def tabla_resumen_2021(entidad):
    
    pos = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['pos']
    if pos.empty == False:
        pos_2021 = pos
    else:
        pos_2021 = 'N/A'

    total = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['total'].round(2)
    if total.empty == False:
        res_total  = total
        st = total
    else:
        res_total = 'N/A'
        st = 0

    c1 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c1'].round(2)
    if c1.empty == False:
        res_c1 = c1
        sc1 = c1
    else:
        res_c1 = 'N/A'
        sc1 = 0

    c2 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c2'].round(2)
    if c2.empty == False:
        res_c2 = c2
        sc2 = c2
    else:
        res_c2 = 'N/A'
        sc2 = 0

    c3 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c3'].round(2)
    if c3.empty == False:
        res_c3 = c3
        sc3 = c3
    else:
        res_c3 = 'N/A'
        sc3 = 0

    c4 = resultados_2021_df[resultados_2021_df['_uuid'] == entidad]['res_c4'].round(2)
    if c4.empty == False:
        res_c4 = c4
        sc4 = c4
    else:
        res_c4 = 'N/A'
        sc4 = 0

    return pos_2021,res_total,res_c1,res_c2,res_c3,res_c4,st,sc1,sc2,sc3,sc4

#Callback resumen 2023 lateral
@dash.callback(
    Output('posicion_2023', 'children'),
    Output('st_2023', 'label'),
    Output('sc1_2023', 'label'),
    Output('sc2_2023', 'label'),
    Output('sc3_2023', 'label'),
    Output('sc4_2023', 'label'),
    Output('st_2023', 'value'),
    Output('sc1_2023', 'value'),
    Output('sc2_2023', 'value'),
    Output('sc3_2023', 'value'),
    Output('sc4_2023', 'value'),
    Input('entidad_seleccionada', 'data'),
)
def tabla_resumen_2023(entidad_seleccionada):
    resultados_2023_df=pd.read_excel('./files/resultados/2023/resultados_2023.xlsx')

    total = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'total'],2)
    c1 = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c1']*100/25,2)
    c2 = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c2']*100/35,2)
    c3 = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c3']*100/25,2)
    c4 = round(resultados_2023_df.loc[resultados_2023_df['_uuid']==entidad_seleccionada,'res_c4']*100/15,2)

    pos_2021 = total

    res_total = total
    st = total

    res_c1 = c1
    sc1 = c1

    res_c2 = c2
    sc2 = c2

    res_c3 = c3
    sc3 = c3

    res_c4 = c4
    sc4 = c4

    return pos_2021,res_total,res_c1,res_c2,res_c3,res_c4,st,sc1,sc2,sc3,sc4

    path =f'./files/separadas/'
    loczip ='./files/exports/bucles.zip'

    zf = zipfile.ZipFile(loczip, "w")
    for dirname, subdirs, files in os.walk(path):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()

    return dcc.send_file(loczip)