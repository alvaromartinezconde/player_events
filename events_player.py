import pandas as pd
import matplotlib.pyplot as plt
import matplotlib; matplotlib.style.use('ggplot')
from paint_field import paint_field

ruta_jugadores = "inputs/eventos_2020_2021.csv"
df = pd.read_csv(ruta_jugadores)


dfmatch = (
    
    ((df['team']=='Atletico de Madrid') | (df['team']=='Cadiz CF')) & ((df['year']==2021) & (df['month']==1) & (df['day']==31)))


df_match = df[dfmatch]

eventos_Atl = ((df_match['team']=='Atletico de Madrid'))

Luis_suarez_zona1 = (
    
    ((df_match['team']=='Atletico de Madrid')) & ((df_match['player']=='Luis Suárez') & (df_match['x']<=17))).copy()

Luis_suarez_zona2 = (
    
    ((df_match['team']=='Atletico de Madrid')) & ((df_match['player']=='Luis Suárez') & (df_match['x']>17) & (df_match['x']<=50))).copy()

Luis_suarez_zona3 = (
    
    ((df_match['team']=='Atletico de Madrid')) & ((df_match['x']>50) & (df_match['x']<=83))).copy()

Luis_suarez_zona4 = (
    
    ((df_match['team']=='Atletico de Madrid')) & ((df_match['player']=='Luis Suárez') & (df_match['x']>83))).copy()


luiszona1 = df_match[Luis_suarez_zona1]
luiszona2 = df_match[Luis_suarez_zona2]
luiszona3 = df_match[Luis_suarez_zona3]
luiszona4 = df_match[Luis_suarez_zona4]


color_campo = 'green'

paint_field.field_position_events(color_campo, luiszona1, luiszona2, luiszona3, luiszona4)
