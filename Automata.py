import re

# Palabras reservadas del lenguaje nuevo
palabras_reservadas = {
    "let", "if", "then", "elseif", "else", "while", "do", "for", "in",
    "true", "false"
}

# Operadores
operadores = {
    "+=", "-=", "++", "==", "!=", "<=", ">=",
    "+", "-", "*", "/", "=", "<", ">"
}

# Delimitadores y símbolos
simbolos = {
    "(", ")", "{", "}", "[", "]", "<<", ">>", "[[", "]]",
    ",", ";", '"'
}

# Patrones regex para tokens
regex_token = {
    "numero_decimal": r"^-?\d+\.\d+$",
    "numero_entero": r"^-?\d+$",
    "cadena": r'^".*"$',
    "identificador": r"^[a-zA-Z_][a-zA-Z0-9_]*$"
}

def clasificar_token(token):
    if token in palabras_reservadas:
        return "Palabra reservada"
    elif token in operadores:
        return "Operador"
    elif token in simbolos:
        return "Delimitador"
    elif re.match(regex_token["numero_decimal"], token):
        return "Número decimal"
    elif re.match(regex_token["numero_entero"], token):
        return "Número entero"
    elif re.match(regex_token["cadena"], token):
        return "Cadena"
    elif re.match(regex_token["identificador"], token):
        return "Identificador"
    else:
        return "Error léxico"

def analizar_archivo():
    with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
        linea_n = 0
        total_tokens = 0
        errores = 0

        print("🔍 ANALIZADOR LÉXICO - Lenguaje nuevo")
        print("=" * 50)

        for linea in archivo:
            linea_n += 1

            # Regex para extraer todos los tokens incluyendo comentarios
            tokens = re.findall(
                r'#.*|//.*|\'\'\'.*?\'\'\'|/\*.*?\*/|\+=|-=|\+\+|==|!=|<=|>=|<<|>>|\[\[|\]\]|"[^"]*"|[a-zA-Z_][a-zA-Z0-9_]*|-?\d+\.\d+|-?\d+|[^\s]',
                linea)

            if tokens:  # Solo mostrar líneas con tokens
                print(f"\nLínea {linea_n}: {linea.strip()}")

                for token in tokens:
                    total_tokens += 1

                    # Detectar comentarios
                    if (token.startswith('#') or token.startswith('//') or
                            token.startswith("'''") or token.startswith('/*')):
                        print(f"  ✅ {token:<20} ➜ Comentario")
                    else:
                        tipo = clasificar_token(token)
                        if tipo != "Error léxico":
                            print(f"  ✅ {token:<20} ➜ {tipo}")
                        else:
                            print(f"  ❌ {token:<20} ➜ Error léxico")
                            errores += 1

        # Resumen
        print("=" * 50)
        print(f"📊 Total tokens analizados: {total_tokens}")
        print(f"✅ Tokens válidos: {total_tokens - errores}")
        print(f"❌ Errores léxicos: {errores}")

        if errores == 0:
            print("🎉 ¡Análisis completado sin errores!")


# Ejecutar análisis
analizar_archivo()