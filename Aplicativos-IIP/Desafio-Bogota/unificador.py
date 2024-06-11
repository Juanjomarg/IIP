import os
import time
import pandas as pd
import json

import tkinter as tk

from tkinter import filedialog as fd

def export_uuid_a_entidades(ents):
  with open(f"{ents}") as json_file:
      diccionario_uuids_entidades = json.load(json_file)

  return diccionario_uuids_entidades

print(f'Bienvenido al aplicativo para mapear UUIDs a entidades\n')

print('''    1. para modo unitario
    2. para modo carpeta''')
mode=str(input('''
Presione la tecla correspondiente al modo de operación deseado:'''))

print('\nEscoja el archivo JSON con las entidades')

ents = fd.askopenfilename()
diccionario_uuids_entidades=export_uuid_a_entidades(ents)


if mode == '1':
  print('\nEscoja el archivo en formato Excel (.xlsx) a mapear:')
  ruta = fd.askopenfilename()

  target_df=pd.read_excel(f'{ruta}')

  target_df['entidad'] = target_df['_submission__uuid'].map(diccionario_uuids_entidades)
  entidad_column = target_df.pop('entidad')
  target_df.insert(0, 'entidad', entidad_column)
  target_df.rename(mapper={'entidad':'Entidad'},inplace=True,axis=1)

  target_df.to_excel(f'{ruta}',index=False)

  
elif mode == '2':
  print('\nEscoja la carpeta donde están los archivos en formato Excel (.xlsx) a mapear:')
  ruta = fd.askdirectory()
  print(f'''\nSe van a mapear todas las entidades en:
    {ruta}
\nCon el archivo:
    {ents}\n\n''')

  for i in os.listdir(ruta):
    print(f'Mapeando {i}')
    target_df=pd.read_excel(f'{i}')

    target_df['entidad'] = target_df['_submission__uuid'].map(diccionario_uuids_entidades)
    entidad_column = target_df.pop('entidad')
    target_df.insert(0, 'entidad', entidad_column)
    target_df.rename(mapper={'entidad':'Entidad'},inplace=True,axis=1)

    target_df.to_excel(f'{i}',index=False)

else:
   print('Esa no es una opción')


