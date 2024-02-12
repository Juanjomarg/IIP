from assets.libraries import *

LOGO_LAB='./static/logolab.png'
LOGO_IIP='./static/logoiip.png'
PREGUNTAS_TODAS=    ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39']
PREGUNTAS_BINARIAS= ['p1','p2','p13','p14','p15','p16',            'p19','p20',            'p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39']
PREGUNTAS_BUCLES=   ['p1','p2','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24_1','p24_2','p24_3','p24_4','p24_5','p25','p26','p27','p28',            'p31','p32','p33','p34','p35','p36','p37','p38','p39']
ENTIDAD_INICIAL='Veeduria Distrital'
PREGUNTA_INICIAL='p1'

UBI_AR={
    'p1':'./files/separadas/repeat_p1.xlsx',
    'p2':'./files/separadas/repeat_p2.xlsx',
    'p13':'./files/separadas/repeat_p13.xlsx',
    'p14':'./files/separadas/repeat_p14.xlsx',
    'p15':'./files/separadas/repeat_p15.xlsx',
    'p16':'./files/separadas/repeat_p16.xlsx',
    'p17':'./files/separadas/repeat_p17.xlsx',
    'p18':'./files/separadas/repeat_p18.xlsx',
    'p19':'./files/separadas/repeat_p19.xlsx',
    'p20':'./files/separadas/repeat_p20.xlsx',
    'p21':'./files/separadas/repeat_p21.xlsx',
    'p22':'./files/separadas/repeat_p22.xlsx',
    'p23':'./files/separadas/repeat_p23.xlsx',
    'p24_1':'./files/separadas/repeat_p24_1.xlsx',
    'p24_2':'./files/separadas/repeat_p24_2.xlsx',
    'p24_3':'./files/separadas/repeat_p24_3.xlsx',
    'p24_4':'./files/separadas/repeat_p24_4.xlsx',
    'p24_5':'./files/separadas/repeat_p24_5.xlsx',
    'p25':'./files/separadas/repeat_p25.xlsx',
    'p26':'./files/separadas/repeat_p26.xlsx',
    'p27':'./files/separadas/repeat_p27.xlsx',
    'p28':'./files/separadas/repeat_p28.xlsx',
    'p31':'./files/separadas/repeat_p31.xlsx',
    'p32':'./files/separadas/repeat_p32.xlsx',
    'p33':'./files/separadas/repeat_p33.xlsx',
    'p34':'./files/separadas/repeat_p34.xlsx',
    'p35':'./files/separadas/repeat_p35.xlsx',
    'p36':'./files/separadas/repeat_p36.xlsx',
    'p37':'./files/separadas/repeat_p37.xlsx',
    'p38':'./files/separadas/repeat_p38.xlsx',
    'p39':'./files/separadas/repeat_p39.xlsx',
    'preguntas':'./files/preguntas/leyenda_columnas.xlsx',
    'respuestas_2021':'./files/respuestas/2021/respuestas_2021.xlsx',
    'respuestas_2023':'./files/respuestas/2023/respuestas_2023.xlsx',
    'resultados_2021':'./files/resultados/2021/resultados_2021.xlsx',
    'resultados_2023':'./files/resultados/2023/resultados_2023.xlsx',
    }


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

CRITS_PREGUNTAS_BASE={
    'p1':{},
    'p2':{'c1':0,'c2':0,'c3':0},
    'p3':{},
    'p4':{'c1':0,'c2':0},
    'p5':{},
    'p6':{'c1':0,'c2':0},
    'p7':{},
    'p8':{'c1':0,'c2':0},
    'p9':{},
    'p10':{},
    'p11':{'c1':0,'c2':0},
    'p12':{},
    'p13':{'c1':0,'c2':0},
    'p14':{'c1':0,'c2':0},
    'p15':{'c1':0,'c2':0},
    'p16':{'c1':0,'c2':0},
    'p17':{'c1':0,'c2':0},
    'p18':{'c1':0,'c2':0},
    'p19':{'c1':0,'c2':0},
    'p20':{'c1':0,'c2':0},
    'p21':{'c1':0,'c2':0},
    'p22':{'c1':0,'c2':0},
    'p23':{'c1':['c1'],'c2':['c2'],'c3':['c3'],'c4':['c4']},
    'p24':{'c1':0,'c2':0,'c3':0,'c4':0},
    'p25':{'c1':0,'c2':0},
    'p26':{'c1':0,'c2':0},
    'p27':{'c1':0},
    'p28':{'c1':0,'c2':0,'c3':0,'c4':['c4'],'c5':['c5']},
    'p29':{'c1':0},
    'p30':{'c1':0},
    'p31':{},
    'p32':{'c1':0,'c2':0},
    'p33':{'c1':0,'c2':0},
    'p34':{'c1':0,'c2':0},
    'p35':{'c1':0,'c2':0},
    'p36':{'c1':0,'c2':0},
    'p37':{'c1':0,'c2':0},
    'p38':{'c1':0,'c2':0},
    'p39':{'c1':0,'c2':0},
    }