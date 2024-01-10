import js2py

js2py.translate_file("./romanized_to_hangul.js", "./r2h.py")
from r2h import *
print(r2h.performConversion("OH Dae han"))

js2py.translate_file("./romanized_to_cyrillic.js", "./r2c.py")
from r2c import *
print(r2c.performConversion("KANAYEVA Alua"))

## Output
# 옿 대 한
# КАНАЫЕВА Алуа