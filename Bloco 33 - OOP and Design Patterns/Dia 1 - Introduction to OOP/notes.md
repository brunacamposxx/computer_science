# Introdução à Programação Orientada a Objetos

## Exemplo: recuperação de senha


### Exercício de Fixação

Antes de sair escrevendo, pense. Como você acha que faz sentido organizar o código da sua funcionalidade? Desenhe, faça um esqueminha das entidades/arquivos/funções/o que for que você criará!

Cronometre ⏲️ cinco minutos para pensar e siga adiante!

Ponto de partida:

 **Quem**  quer fazer **o que** e com **o que** ?

No nosso caso, um **User** quer **recuperar sua senha** com **seu email** . 

Se partirmos daí, o que temos?
- Uma entidade User
- Uma ação ou entidade de enviar emails
- Uma ação ou entidade de recuperar senhas


## **Entidade ou Classes** 
As entidades criadas na POO se chamam **Classes**.
As **Classes** representam as **entidades**. Nesse caso, se chama **User**

## **Construtor**
A Classe User tem um **contrutor** (um molde) com essa sintaxe: __ init __ 
E esse construtor tem **atributos** que são *informações* acerca da entidade.

## **Atributos**
Caracteristicas do objeto

Exemplo:

```python
class User: # entidade 
    name = 'Bruna' # atributo / informação
    
    # atributos - coisas que ela sabe
    def __init__(self, name, email, password):
        self.name = name # atributo
        self.email = email # atributo
        self.password = password # atributo

    # método - coisas que a classe faz
    def diga_seu_nome(self):
        return self.name

# instanciar um objeto
scott = User('Scott', 'scott@email.com', 'super-senha')
print(scott.name) # atributo
print(scott.email) # atributo
print(scott.password) # atributo

retorno_do_metodo = meu_user.diga_seu_nome() # invocando um método
print(retorno_do_metodo)

```


**Variavel que contém a entidade dentro: Objeto!**


## Objetos no Python
O que nós fizemos na seção anterior foi definir uma entidade de forma geral e criar uma entidade específica para nossa variável. Usando a nomenclatura correta, dizemos que definimos uma *classe* ("entidade de forma geral") e criamos, a partir dela, um *objeto* ("uma entidade específica", criada a partir de uma definição geral de entidade, ou seja, de uma classe).

Toda classe capaz de criar objetos deve possuir um método *construtor* , que será chamado quando o objeto estiver sendo criado. No caso de Python, o método construtor é, sempre, definido com o nome __init__ no topo da classe que se está criando. Por trás dos panos, o Python utilizará a sua lógica para criar e retornar um objeto para você ou quem for. Ou seja:


```python
class User:
    def __init__(self, name, email, password):
        """ Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!"""
        self.name = name
        self.email = email
        self.password = password

# Para invocar o método construtor, a sintaxe é NomeDaClasse(parametro 1, parametro 2)
# Repare que o parâmetro self foi pulado -- um detalhe do Python.
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")

# A variável `meu_user` contém o objeto criado pelo construtor da classe User!
```

## *Enviar E-mails:*
Se temos uma entidade User que quer enviar emails de recuperação de senha, em princípio faz sentido que essa entidade saiba enviar emails, certo?

```python
class User:
    def __init__(self, name, email, password):
        """ Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!"""
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        print("Envia email de reset de senha")


meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()
```
Se definimos numa classe uma função, podemos chamar ela a partir do objeto que criamos! Quando pedimos para um objeto fazer algo, dizemos que estamos enviando uma mensagem àquele objeto . Atenção para isso! Na essência, toda lógica da orientação a objetos parte do envio de mensagens entre objetos.


No código acima, estamos pedindo para meu_user resetar sua senha! Não nos interessa como a ação será feita, só nos interessa que ela será feita! Imagine duas pessoas escrevendo esse código. A pessoa que cria o objeto e pede que ele resete sua senha não precisa saber como ele faz isso! Temos uma classe bem nomeada, com uma função bem nomeada, e isso basta! Ao invés de gastar tempo precioso entendendo seu código, a pessoa pode usá-lo sem esse esforço!


```python
class User:
    # Não preciso saber como a classe funciona, lalalalala

    def reset_password(self):
      # A classe tem essa função? Ótimo! Pra mim basta!


# Já sei o suficiente pra agir!
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()
```

Agora pause e imagine uma aplicação com dez entidades. Vinte. Cinquenta. Imagine ter que saber como cada uma funciona para codar e utilizá-las. Agora imagine que basta saber qual função usar e o resto acontece automagicamente? Esse é o poder da Programação Orientada a Objetos! Se você já chamou a função de um Service, numa aplicação **MSC** , e a usou sem saber como ela estava feita, saiba que, no fundo, o que você fez foi usufruir do benefício da Programação Orientada a Objetos, que embasa o **MSC**!


Toda arquitetura que tenha como base a Programação Orientada a Objeto quer isso. Quer que você defina entidades e as use sem entender como elas funcionam . Faz sentido? Pois saiba que você acabou de conhecer **dois dos quatro pilares da Programação Orientada a Objetos.** O pilar de definir entidades chama-se **Abstração** . O pilar de usá-las sem entender como elas funcionam se chama **Encapsulamento** .


# Pilares da POO

## Abstração: 
Crie entidades que conterão, cada uma, parte da lógica de seu programa

## Encapsulamento:
Exposição somente do que é necessário para uso dos objetos de uma classe.


__init__ método especial construtor/inicializador - dunder?





Exercício em breakout rooms:

```python
class Liquidificador:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor


    def ligar():
        pass


    def pulsar():
        pass


    def desligar():
        pass

```




Obs da aula ao vivo:
para usar os parametros do contrutor, usar (self). Ex:

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._pin = "123"

    
    def setPassword(self, new_pint):
        pass


    def verifyPassword(self, pint):
        pass


cliente1 = Customer('Isaac Alvim', 'isaac@email.com')
print(cliente1.name)
cliente2 = Customer('Bruna Campos', 'bruna@email.com')
cliente2.show()
cliente3.email = 'scott@email.com'

``` 


account.py:
```python
class Account:
    def __init__(self, customers, number, balance=0):
        self._balance = 0 # definindo ou criando um atributo
        self._customers = customers
        self._number = number
        self._transactions = []
        self.deposit(balance)
    
    # método
    def status(self):
        print(f"Número da conta: {self._number} Saldo: {self._balance:10.2f}")
    

    def withdraw(self, amount):
        if self._balance >= amount:
        self._balance -= amount
        self._transactions.append(["SAQUE", amount]])

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(["DEPÓSITO", amount]])

    def details(self):
        print(f"Extrato da conta número: {self._number}\n")
        for t in self._transactions:
            print(f"{t[0]: 10s} {t[1]: 10.2f}")
        print(f"\n Saldo: {self._balance:10.2f}\n")

```

```python
from accounts.py import Account 

cliente1 = Customer('bruna campos', 'burna@email')
conta_1 = Account([cliente1], "01017769-7", 100)
conta_1.status()
conta_1.deposit(20)
conta_1.status()
conta_1.withdraw(99)
conta_1.status()
conta_1._customers[0].show()
conta_1.details()
conta_1.withdraw(15)
conta_1.details()

```