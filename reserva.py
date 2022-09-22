"""
Faça um programa de um terminal que exibe ao usuário uma lista dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.

`quartos.txt`
# codigo, nome, preco
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simple,50

O programa pergunta para o usuario o nome, qual o numero do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

o programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
# cliente, quarto, dias
Brunom,3,12

Se outro usuario tentar reservar o mesmo quarto o programa deve exibir uma
msg informando que já esta reservado
"""
import sys
import logging

ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupado[int(num_quarto)] = {
            "nome": nome,
            "dias": dias, #TODO: Decimal
            
        }
except FileNotFoundError:
    logging.error("Arquivo reserva.txt nao existe")
    sys.exit(1)

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[codigo] = {
            "nome": nome,
            "preco": float(preco), #TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo nao quartos.txt existe")
    sys.exit(1)


print("Reserva Hotel Pythonico")
print("-" * 40)
print("Lista de quartos disponíveis:")
nome = input("Nome do cliente: ").strip()

for codigo, dados in quartos.items():
    nome_quarto = dados['nome']
    preco = dados['preco']
    disponivel = dados['disponivel'] # TODO: colocar emoji
    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f}")

print("-" * 40)

try:
   num_quarto = int(input("Numero do quarto: ").strip())
   if not quartos[num_quarto]['disponivel']:
       print(f"O quarto {num_quarto} está ocupado.")
       sys.exit(1)
except ValueError:
    logging.error("Número inválido, digite apenas digitos")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)

try:
    dias = int(input("Numero de dias : ").strip())
except ValueError:
    logging.error("Número inválido, digite apenas digitos")
    sys.exit(1)

nome_quarto = quarto[num_quarto]['nome']
preco_quarto = quarto[num_quarto]['preco']
disponivel = quarto[num_quarto]['disponivel']
total = preco_quarto * dias

with open("reserva.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n")

print(f"{nome} voce escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}")