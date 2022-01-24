import random

random_number = random.randint(1, 10)
# escolhe um número aleatório entre 1 e 10
guess = ""

while guess != random_number:
    # enquanto não adivinhar o número
    guess = int(input("Qual o seu palpite? "))
    # pergunte a pessoa usuária um número

print("O número sorteado era: ", guess)

# Para rodar o exemplo acima, não crie um arquivo chamado random para inserir o código, pois o módulo que estamos importando se chama random , e isso pode ocasionar num erro! Lembre-se que, para rodar o código, você deve executar, no terminal, o comando python3 nome_do_arquivo.py .
# Fazemos uma conversão do palpite para um número inteiro, pois entrada de dados é sempre str .
