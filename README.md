# English-to-Hangul-or-Cyrillic-Python
## What is this repo?
I took scripts to convert English to Hangul, English to Cyrillic, used js2py as a wrapper to run these Javascript snippets in Python.

Hangul script is from
https://www.mauvecloud.net/charsets/hangulgenerator.html

Cyrillic script is from
https://www.lexilogos.com/keyboard/russian.htm

## Requirements
```pip install js2py```

## Usage
```python
import js2py

js2py.translate_file("./romanized_to_hangul.js", "./r2h.py")
from r2h import *
print(r2h.performConversion("OH Dae han"))

js2py.translate_file("./romanized_to_cyrillic.js", "./r2c.py")
from r2c import *
print(r2c.performConversion("KANAYEVA Alua"))
```
