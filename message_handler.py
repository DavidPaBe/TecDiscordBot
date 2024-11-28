import json
import unicodedata

def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def save_data(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def check_synonyms(synonyms, content):
    content = remove_accents(content).lower()
    for synonym in synonyms:
        if remove_accents(synonym).lower() in content:
            #print(f"¡Sinónimo encontrado! Synonym: {synonym}, Contenido: {content}")  # Depuración
            return True
    return False

def find_response(data, content):
    if isinstance(data, str):
        return data

    elif isinstance(data, dict):
        for key, value in data.items():
            print(key)
            if key in content or (isinstance(value, dict) and check_synonyms(value.get('synonyms', []), content)):
                if isinstance(value, dict) and 'responses' in value:
                    return find_response(value['responses'], content)
                elif isinstance(value, str):
                    return value
                else:
                    return "Formato inesperado en los datos. Intenta con otra pregunta."
            elif key == "_":
                return value
    else:
        return "Formato de contenido no soportado."
    return "No se encontró"

def handle_message(message):
    data = load_data()

    content = remove_accents(message).lower()
    response = find_response(data, content)

    return response

def add_synonym_to_json(category, new_synonym):
    data = load_data()

    if category in data['categories']:
        if new_synonym not in data['categories'][category]['synonyms']:
            data['categories'][category]['synonyms'].append(new_synonym)
            save_data(data)
            return f"Se ha agregado '{new_synonym}' como sinónimo de '{category}'."
        else:
            return f"El sinónimo '{new_synonym}' ya existe para '{category}'."
    else:
        return f"La categoría '{category}' no existe."

def process_user_response(message, category, new_synonym):
    if message.lower() in ['sí', 'si', 'yes']:
        response = add_synonym_to_json(category, new_synonym)
        return response
    else:
        return "No se ha agregado el sinónimo."

async def process_message_without_prefix(message):
    suggestion_response = handle_message(message.content)
    await message.channel.send(suggestion_response)
