import re

regularEx = r"\baños\b"

palabra = "En un lugar hace cincuenta años."

resultado = re.findall(regularEx, palabra)
print(resultado)