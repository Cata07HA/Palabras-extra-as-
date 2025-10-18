meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma", 
    "SHEESH": "ligera desaprobación", 
    "CREEPY": "aterrador, siniestro", 
    "AGGRO": "ponerse agresivo/enojado",
    "DE CHILL": "una expresión para reflejar tranquilidad"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict:
    print(meme_dict[word])
else:
    print("Palabra no encontrada")
