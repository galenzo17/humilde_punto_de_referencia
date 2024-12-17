# runner.py

import json
import csv
import argparse
import datetime
from evaluation import evaluate_response

# Nota: Esta es una simulación. En un caso real, aquí llamarías a la API del modelo LLM.
# Por ejemplo, podrías tener una función `call_model_api(prompt, model_name)` que retorne la respuesta.
# Aquí creamos una función simulada.

def call_model_api(prompt: str, model_name: str) -> str:
    # Simulación de llamada al modelo:
    # Dependiendo del prompt, devolvemos algo simple.
    # En un entorno real, aquí se haría una petición a la API, por ejemplo con requests:
    # response = openai.ChatCompletion.create(...)
    # return response["choices"][0]["message"]["content"]

    # Para test_01, devolvemos un script ficticio:
    if "terminal Linux" in prompt:
        return """#!/bin/bash
find /home/user/docs -name '*.txt' -mtime -7 -print0 | xargs -0 tar -czf backup.tar.gz
mv backup.tar.gz /home/user/backups
"""
    # Para test_02, devolvemos un texto que mencione papers y diferentes enfoques
    if "aprendizaje por refuerzo profundo" in prompt:
        return """En los últimos años, especialmente en los últimos 3, se han publicado numerosos papers sobre aprendizaje por refuerzo profundo.
Un estudio reciente (2022) compara el método A basado en políticas con el método B basado en valor.
El paper 'Deep Reinforcement Learning: State of the Art' analiza las diferencias entre ambos enfoques y su aplicabilidad en robótica."""
    
    # Si el prompt no coincide con ninguno de los casos, retornamos algo genérico
    return "Respuesta genérica del modelo"

def main():
    parser = argparse.ArgumentParser(description="Ejecuta las pruebas sobre un modelo y guarda resultados en CSV.")
    parser.add_argument("--config", required=True, help="Ruta al archivo de configuración (JSON).")
    parser.add_argument("--output", default="results.csv", help="Archivo CSV de salida.")
    parser.add_argument("--model", default="gpt-4", help="Nombre del modelo a evaluar.")

    args = parser.parse_args()

    # Cargar el archivo de configuración
    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    tests = config.get("tests", [])

    # Abrir el CSV para escritura (append si se quiere ir sumando)
    # Incluir encabezados si el archivo está vacío
    fieldnames = ["test_id", "role", "prompt", "model_name", "response", "evaluation_score", "timestamp"]
    write_header = False
    try:
        with open(args.output, "r", encoding="utf-8") as f:
            pass
    except FileNotFoundError:
        write_header = True

    with open(args.output, "a", encoding="utf-8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()

        for test in tests:
            prompt = test["prompt"]
            role = test["role"]
            test_id = test["id"]
            criteria = test.get("criteria", {})

            # Llamar al modelo
            response = call_model_api(prompt, args.model)

            # Evaluar la respuesta
            score = evaluate_response(response, criteria)

            # Guardar resultado en CSV
            result_row = {
                "test_id": test_id,
                "role": role,
                "prompt": prompt,
                "model_name": args.model,
                "response": response,
                "evaluation_score": score,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }

            writer.writerow(result_row)

    print(f"Pruebas completadas. Resultados guardados en {args.output}.")

if __name__ == "__main__":
    main()