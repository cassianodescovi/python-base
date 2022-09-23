#!/usr/bin/env python3
""" Calculadora infix.

Funcionamento:

[operação][n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1:5
n2:
9

Os resultados serão salvos em `infixcalc.log`
"""
__version__ = "0.1.0"

import os
import sys
from datetime import datetime

while True:
	arguments = sys.argv[1:]

	if not arguments:
	    operation = input("choose the operation (sum, sub, mul div): ")
	    n1 = input("n1: ")
	    n2 = input("n2: ")
	    arguments = [operation, n1, n2]
	elif len(arguments) != 3:
	    print("Número de argumentos inválidos")
	    print("ex: `sum 5 5`")
	    sys.exit(1)

	operation, *nums = arguments

	valid_operations = ("sum", "sub", "mul", "div")
	if operation not in valid_operations:
		print("Operação inválida")
		print(valid_operations)
		sys.exit(1)

	validated_nums = []
	for num in nums:
		if not num.replace(".", "").isdigit():
			print(f"Numero inválido {num}")
			sys.exit(1)
		if "." in num:
			num = float(num)
		else:
			num = int(num)
		validated_nums.append(num)

	n1, n2 = validated_nums

	if operation == "sum":
		result = n1 + n2
	elif operation == "sub":
		result = n1 - n2
	elif operation == "mul":
		result = n1 * n2
	elif operation == "div":
		if n2 == 0:
			print("não há divisão por 0")
			sys.exit(1)
		else:
			result = n1 / n2

	print(f"o resultado é {result}")
	
	path = os.curdir
	filepath = os.path.join(path, "infixcalc.log")
	timestamp = datetime.now().isoformat()
	user = os.getenv('USER','anonymous')

	try:
		with open(filepath, "a") as file_:
			file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
	except PermissionError as e:
		#TODO: logging
		print(str(e))
		sys.exit(1)
	
	if input("Pressione enter para continuar ou qualquer tecla pra sair"):
		break







		