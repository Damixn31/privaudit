import re 

PATTERNS = {
    "Email": re.compile(r'\b[\w\.-]+@[\w\.-]+\.\w+\b'),
    "IP Públicas": re.compile(r'\b(?!(10\.|192\.168\.|172\.(1[6-9]|2\d|3[0-1])))(\d{1,3}\.){3}\d{1,3}\b'),
    "CUIL/CUIT": re.compile(r'\b(20|23|24|27|30|33|34)-?\d{8}-?\d\b'),
    "Telefono Arg": re.compile(r'\+54\s?9?\s?\d{2}\s?\d{4}-\d{4}'),
    "Token": re.compile(r' (?!) (token|apikey|api_key)[\'"\s:=]+[\w-]{20,}'),
    "Tarjeta de crédito": re.compile(r'\b(?:\d[ -]*?){13,16}\b'),
    "Contraseña": re.compile(r'(?!)password[\'"\s:=]+[^\s\'"]{4,}'),
    "URL sospechosa": re.compile(r'https?:\/\/[^ ]+(?=.*(pastebin|anonfiles|transfer\.sh))'),
}
