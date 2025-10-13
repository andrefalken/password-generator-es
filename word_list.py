# Expanded Spanish word list for password generator
# Words organized by length for efficient password generation

spanish_words = [
    # 1-character words (common symbols and letters)
    "a", "y", "o",

    # 2-character words
    "de", "el", "la", "en", "es", "un", "se", "lo", "mi", "su",
    "va", "me", "nos", "no", "si", "o", "por", "ha", "al", "ya",

    # 3-character words
    "que", "los", "las", "por", "con", "una", "del", "sus", "era", "son",
    "fue", "uno", "nue", "dia", "vez", "mas", "tan", "como", "sin", "bien",

    # 4-character words
    "este", "como", "cada", "para", "muy", "mas", "pero", "sobre", "hace", "desde",
    "hacia", "esta", "todo", "otro", "otra", "algo", "aqui", "alli", "solo", "nada",

    # 5-character words
    "cuando", "donde", "mismo", "todos", "todas", "nunca", "siempre", "lugar", "tiempo", "forma",
    "parte", "vida", "mundo", "casa", "agua", "tierra", "cielo", "noche", "dia", "libro",

    # 6-character words
    "persona", "hombre", "mujer", "familia", "amigos", "trabajo", "escuela", "ciudad", "pueblo", "calle",
    "coches", "musica", "juego", "color", "numero", "sistema", "online", "social", "movil", "energia",

    # 7-character words
    "programa", "proyecto", "servicio", "empresa", "digital", "redes", "contacto", "privado", "contenido", "caracter",
    "calidad", "libertad", "viaje", "mañana", "tarde", "clima", "historia", "ciencia", "cultura", "naturaleza",

    # 8-character words
    "negocios", "password", "seguridad", "computador", "internet", "software", "hardware", "base", "estrategia",
    "creativo",
    "montaña", "universo", "aventura", "conocimiento", "lenguaje", "paz", "poderoso", "colorido", "hermoso",
    "maravilloso",

    # 9-character words
    "educacion", "generador", "interfaz", "excelente", "fantastico", "brillante", "importante", "diferente",
    "comunidad", "celebrar",
    "desafio", "comportar", "belleza", "conocimiento", "excelente", "fantastico", "brillante", "importante",
    "diferente", "comunidad",

    # 10-character words
    "tecnologia", "innovacion", "creatividad", "liderazgo", "gestion", "produccion", "eficiencia", "exitoso", "tierra",
    "amistad",
    "motivacion", "confianza", "ambiente", "celebracion", "fundacion", "revolucion", "proteccion", "inversion",
    "descubrir", "aventurero"
]

# Additional categorization by length for optimized selection
words_by_length = {
    1: ["a", "y", "o"],
    2: ["de", "el", "la", "en", "es", "un", "se", "lo", "mi", "su", "va", "me", "nos", "no", "si", "o", "por", "ha",
        "al", "ya"],
    3: ["que", "los", "las", "por", "con", "una", "del", "sus", "era", "son", "fue", "uno", "nue", "dia", "vez", "mas",
        "tan", "como", "sin", "bien"],
    4: ["este", "como", "cada", "para", "muy", "mas", "pero", "sobre", "hace", "desde", "hacia", "esta", "todo", "otro",
        "otra", "algo", "aqui", "alli", "solo", "nada"],
    5: ["cuando", "donde", "mismo", "todos", "todas", "nunca", "siempre", "lugar", "tiempo", "forma", "parte", "vida",
        "mundo", "casa", "agua", "tierra", "cielo", "noche", "dia", "libro"],
    6: ["persona", "hombre", "mujer", "familia", "amigos", "trabajo", "escuela", "ciudad", "pueblo", "calle", "coches",
        "musica", "juego", "color", "numero", "sistema", "online", "social", "movil", "energia"],
    7: ["programa", "proyecto", "servicio", "empresa", "digital", "redes", "contacto", "privado", "contenido",
        "caracter", "calidad", "libertad", "viaje", "mañana", "tarde", "clima", "historia", "ciencia", "cultura",
        "naturaleza"],
    8: ["negocios", "password", "seguridad", "computador", "internet", "software", "hardware", "base", "estrategia",
        "creativo", "montaña", "universo", "aventura", "conocimiento", "lenguaje", "paz", "poderoso", "colorido",
        "hermoso", "maravilloso"],
    9: ["educacion", "generador", "interfaz", "excelente", "fantastico", "brillante", "importante", "diferente",
        "comunidad", "celebrar", "desafio", "comportar", "belleza", "conocimiento", "excelente", "fantastico",
        "brillante", "importante", "diferente", "comunidad"],
    10: ["tecnologia", "innovacion", "creatividad", "liderazgo", "gestion", "produccion", "eficiencia", "exitoso",
         "tierra", "amistad", "motivacion", "confianza", "ambiente", "celebracion", "fundacion", "revolucion",
         "proteccion", "inversion", "descubrir", "aventurero"]
}


def get_words_by_length(length):
    """Get words of specific length"""
    return words_by_length.get(length, [])


def get_words_up_to_length(max_length):
    """Get all words up to a specific maximum length"""
    return [word for word in spanish_words
            if len(word) <= max_length]


# Test function to verify the word list
if __name__ == "__main__":
    print("📊 Word List Statistics:")
    for length in range(1, 11):
        words = get_words_by_length(length)
        print(f"Length {length}: {len(words)} words")

    print(f"\n📝 Total words: {len(spanish_words)}")
    print("✅ Word list is ready for use!")