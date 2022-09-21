#!/usr/bin/env python3
"""
Hello World Multi LInguas.

Dependendo da lingua configurada no  ambiente o programa exibe a mensagem
correspondente

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = '0.1.2'
__author__ = 'cassianodescovi'
__license__ = 'Unlicense'

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)




arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
	try:
		key, value = arg.split("=")
	except ValueError as e:
		log.error(
			"You need to use ´=´, you passed %s, try --key=value: %s",
			arg,
			str(e)
		)
		sys.exit(1)
		
	key = key.lstrip("-").strip()
	value = value.strip()
	# Validacao
	if key not in arguments:
		print(f"Invalid Option`{key}`")
		sys.exit()
	arguments[key] = value
	

current_language = arguments["lang"]
if current_language is None:
	# TODO: Usar repeticao
	if "LANG" in os.environ:
		current_language = os.getenv("LANG")
	else:
	# TODO: usar repetição
		current_language = input("Choose a language")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Holla, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

print(msg[current_language] * int(arguments["count"]))
# LANG=fr_FR python3 hello.py