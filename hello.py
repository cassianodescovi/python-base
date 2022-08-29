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

current_language = os.getenv("LANG")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Holla, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

print(msg[current_language])