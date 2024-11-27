import json
import unicodedata

# Cargar el archivo JSON
def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

# Guardar los cambios en el JSON
def save_data(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Función para quitar los acentos de las palabras
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

# Función para verificar si una palabra o frase contiene alguna de las palabras clave
def check_synonyms(synonyms, content):
    content = remove_accents(content).lower()  # Convertir el contenido a minúsculas y sin acentos
    for synonym in synonyms:
        if remove_accents(synonym).lower() in content:
            #print(f"¡Sinónimo encontrado! Synonym: {synonym}, Contenido: {content}")  # Depuración
            return True
    return False

def find_response(data, content):
    if isinstance(data, str):  # Si es un string, retorna directamente
        return data

    elif isinstance(data, dict):  # Si es un diccionario, recorre sus claves
        for key, value in data.items():
            print(key)
            # Verifica si el contenido coincide con los sinónimos o la clave directamente
            if key in content or (isinstance(value, dict) and check_synonyms(value.get('synonyms', []), content)):
                # Si tiene la clave 'responses', llama recursivamente
                if isinstance(value, dict) and 'responses' in value:
                    return find_response(value['responses'], content)
                # Si no tiene 'responses' pero es un string, retorna el valor
                elif isinstance(value, str):
                    return value
                # Si no hay una estructura esperada, puede manejarse un caso predeterminado
                else:
                    return "Formato inesperado en los datos. Intenta con otra pregunta."
            elif key == "_":
                return value
    else:  # Manejo de tipos no soportados
        return "Formato de contenido no soportado."
    return "No se encontró"

# Función principal que simula el bot respondiendo
def handle_message(message):
    # Aquí deberías cargar tu JSON de datos
    data = load_data()

    # Llamada a la función para encontrar la respuesta
    content = remove_accents(message).lower()
    response = find_response(data, content)

    return response

# Función para agregar un sinónimo al JSON
def add_synonym_to_json(category, new_synonym):
    data = load_data()

    # Buscar la categoría correspondiente
    if category in data['categories']:
        # Verificar si el nuevo sinónimo ya existe
        if new_synonym not in data['categories'][category]['synonyms']:
            data['categories'][category]['synonyms'].append(new_synonym)
            save_data(data)
            return f"Se ha agregado '{new_synonym}' como sinónimo de '{category}'."
        else:
            return f"El sinónimo '{new_synonym}' ya existe para '{category}'."
    else:
        return f"La categoría '{category}' no existe."

# Ejemplo de función para procesar la respuesta del usuario
def process_user_response(message, category, new_synonym):
    # Si el usuario responde "sí", agregamos el sinónimo al JSON
    if message.lower() in ['sí', 'si', 'yes']:
        response = add_synonym_to_json(category, new_synonym)
        return response
    else:
        return "No se ha agregado el sinónimo."

# Función principal de manejo de mensajes
# Función principal de manejo de mensajes
async def process_message_without_prefix(message):
    # Llamar a la función que maneja el mensaje y devuelve la respuesta
    suggestion_response = handle_message(message.content)
    await message.channel.send(suggestion_response)
