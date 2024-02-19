import os
import time
import pandas as pd
import json

import tkinter as tk

from tkinter import filedialog as fd

ents = fd.askopenfilename()

def export_uuid_a_entidades(ents):
  with open(f"{ents}") as json_file:
      diccionario_uuids_entidades = json.load(json_file)

  return diccionario_uuids_entidades

diccionario_uuids_entidades=export_uuid_a_entidades(ents)

ruta = fd.askopenfilename()

target_df=pd.read_excel(f'{ruta}')

target_df['entidad'] = target_df['_submission__uuid'].map(diccionario_uuids_entidades)
entidad_column = target_df.pop('entidad')
target_df.insert(0, 'entidad', entidad_column)
target_df.rename(mapper={'entidad':'Entidad'},inplace=True,axis=1)

target_df.to_excel(f'{ruta}',index=False)
