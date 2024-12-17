# evaluation.py

def evaluate_response(response: str, criteria: dict) -> float:
    """
    Evalúa la respuesta según criterios simples:
    Cada criterio es una clave con una descripción.
    Aquí buscaremos palabras clave en la respuesta.
    Devuelve un puntaje entre 0 y 1.
    """
    if not criteria:
        return 1.0

    checks = 0
    total = len(criteria)
    for c in criteria.values():
        # Evaluamos si la respuesta contiene ciertos patrones esperados
        # Para simplicidad, buscaremos si las palabras clave están incluidas
        # Esta es una evaluación muy rudimentaria.
        # En la práctica, podría ser más compleja.
        keywords = c.split("'")
        # Por ejemplo, si c = "contiene 'find'", separamos por comillas
        # y obtenemos ["contiene ", "find", ""]
        # Tomamos la segunda parte como palabra clave.
        if len(keywords) > 1:
            keyword = keywords[1]
            if keyword.lower() in response.lower():
                checks += 1
        else:
            # Si no está entre comillas, intentamos directamente
            if c.lower() in response.lower():
                checks += 1

    return checks / total if total > 0 else 1.0