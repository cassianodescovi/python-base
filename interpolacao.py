#! usr/bin/env python3
"""Imprime a msg de um e-mail

NÃO MANDE SPAM!
"""
__version__ = "0.1.1"

import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatpath = os.path.join(path, templatename) # email_tmpl.txt

for line in open(filepath):
    name, email = line.split(",")

    # TODO: Substituir por envio de email
    print()
    print(f"Enviando email para {email}")
    print()
    print(
        open(templatpath).read()
        % {
        "nome":name, 
        "produtos":"caneta", 
        "texto": "Escrever muito bem", 
        "link": "https://canetasleagais.com",
        "quantidade":1, 
        "preco": 50.5,}
    )
    print("-" * 50)





       