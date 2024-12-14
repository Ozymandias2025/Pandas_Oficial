# Importamos la biblioteca pandas y la llamamos pd
import pandas as pd
# Creamos una serie de pandas que es como una lista con etiquetas
# Los valores son nombres de jugadores de PSG
# El índice especifica los números de camisetas de esos jugadores

psg_players = pd.Series(
    ['Navas','Mbappe','Neymar','Messi'], # Lista de jugadores
    index = [1,7,10,30] # Lista de Camisetas
)
# Creamos un diccionario que asocia números de camisetas con nombres de jugadores
psg_dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'} # Los diccionarios siempre usan corchetes

# Creamos una serie de pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)

# Imprimimos la serie para ver su contenido
print(psg_players_dict)

# Imprimimos el valor de la posición (índice) 7 (que corresponde a Mbappe) de la serie creada a partir del diccionario
print(psg_players_dict[7])

# Imprimimos los tres primeros valores del diccionario
print(psg_players_dict[0:3])

# Diccionario con datos de jugadores (todo diccionario está compuesto con clave y valor)
dict = {'Jugador':['Navas','Mbappe','Neymar','Messi'],
        'Altura':[183.0, 170.0, 175.0, 165.0],
        'Goles':[2, 200, 150, 300]}

# Creamos un dataframe con el diccionario e índices personalizados
df = pd.DataFrame(dict, index = [1,7,10,30])

# Imprimimos el dataframe
print(df)