import json

# Cargar el archivo JSON
def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Guardar los cambios en el JSON
def save_data(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Función para procesar el mensaje y sugerir preguntas
def suggest_and_add_synonym(message):
    data = load_data()
    content = message.lower()

    # Ejemplo de preguntas sugeridas
    suggested_questions = {
        "donde": ["¿Dónde está la cafetería?", "¿Dónde se encuentra el laboratorio de electrónica?"],
        "cuando": ["¿Cuándo abre la biblioteca?", "¿Cuándo puedo ver el laboratorio?"],
        "como": ["¿Cómo puedo inscribirme en una carrera?", "¿Cómo acceder al laboratorio de electrónica?"],
        "que": ["¿Qué carreras se ofrecen?", "¿Qué hay en el laboratorio de electrónica?"],
        "quien": ["¿Quién es responsable del laboratorio de electrónica?", "¿Quién puede ayudarme con la inscripción?"],
        "por que": ["¿Por qué la cafetería cierra temprano?", "¿Por qué debo usar mi credencial para el laboratorio?"]
    }

    # Verificar si el mensaje es una de las preguntas sugeridas
    for category, questions in suggested_questions.items():
        for question in questions:
            if question in content:
                response = f"¿Quieres agregar la pregunta '{question}' como sinónimo para '{category}'? Responde sí o no."
                return response

    # Si no hay coincidencias con las preguntas sugeridas
    return "No reconozco esa pregunta. ¿Quieres que te sugiera algunas preguntas?"

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

# Ejemplo de uso
message = "¿Dónde está la cafetería?"
suggestion_response = suggest_and_add_synonym(message)
print(suggestion_response)  # El bot sugiere agregar el sinónimo.

# El siguiente paso sería capturar la respuesta del usuario y procesarla:
user_response = "sí"  # Supongamos que el usuario responde "sí"
category = "donde"
new_synonym = "¿Dónde se encuentra el comedor?"

response = process_user_response(user_response, category, new_synonym)
print(response)  # Confirmación de que se agregó el sinónimo al JSON
