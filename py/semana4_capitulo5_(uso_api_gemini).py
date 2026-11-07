import os
from google import genai
from google.genai import types
from pydantic import BaseModel


# Inicializa el cliente.
# Si GEMINI_API_KEY está definida en el sistema, la tomará automáticamente.
# También puedes pasarla de forma explícita: genai.Client(api_key="tu_api_key")
client = genai.Client(api_key="api_key")

# Llamada básica para generar contenido
"""response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explica brevemente qué es una API REST.",
)

print(response.text)"""

# Llamada básica con contexto
"""respuesta = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Explícame en 3 puntos clave qué es una API REST usando una analogía de un restaurante.",
        config=types.GenerateContentConfig(
            system_instruction="Eres un profesor universitario didáctico. Responde siempre en español claro y conciso."
        )
    )
print(respuesta.text)"""

# Llamada básica con contexto y memoria
"""chat = client.chats.create(model="gemini-3.5-flash-lite")
    
r1 = chat.send_message("Hola, estoy programando una app en Python para finanzas personales.")
print("🤖 Turno 1:", r1.text)
    
r2 = chat.send_message("¿Qué librerías gratuitas me recomiendas para el proyecto que te acabo de mencionar?")
print("\n🤖 Turno 2 (Recuerda el contexto):", r2.text)"""

# Llamada básica con contexto, memoria y esquema de respuesta

"""# 1. Defines la estructura exacta que quieres recibir
class AnalisisProducto(BaseModel):
    nombre_producto: str
    sentimiento: str
    puntos_positivos: list[str]
    calificacion_1_a_5: int

TEXTO_RESENA = "Compré el teclado mecánico KeyPro X. Las teclas son súper suaves y la batería dura 3 semanas, aunque el cable es un poco corto. Le doy un 4 de 5."

respuesta = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"Analiza esta reseña: {TEXTO_RESENA}",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AnalisisProducto,
        )
    )

print(respuesta.text)"""

# Búsqueda en Google en Tiempo Real (Grounding) y Tus Propias Funciones (Function Calling)

"""# Defines cualquier función en Python con tipos y docstring claro:
def calcular_descuento_impuesto(precio_base: float, porcentaje_descuento: float) -> dict:
    #Calcula el precio final aplicando un descuento y luego el 16% de IVA.
    precio_con_desc = precio_base * (1 - porcentaje_descuento / 100)
    total_con_iva = round(precio_con_desc * 1.16, 2)
    return {"precio_con_descuento": round(precio_con_desc, 2), "total_con_iva": total_con_iva}

# El SDK ejecuta la función automáticamente y devuelve la respuesta final:
respuesta = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="¿Cuánto pagaré en total por una laptop de $850 si tiene 20% de descuento más IVA?",        config=types.GenerateContentConfig(tools=[calcular_descuento_impuesto])
)    
print(respuesta.text)"""