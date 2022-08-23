# O que é
- Python
	- linguagem de propósito geral
	- fácil e intuitiva
	- multiplataformas
	- livre
	- organizada
	- orientada a objetos
- Principais Áreas
	- Inteligência artificial
	- biotecnologia
	- computação 3D

# Tipos de Dados
- Todos os dados que se originam de um input do usuário são considerados uma string
- Toda variável é um objeto mas nem todo objeto é uma variável
## Tipos de dados
- Int = números inteiros
-  Float = números com virgula/ponto
- Bool = verdadeiro (True) ou falso (Falso)
- String = palavras
## Métodos de teste de tipo
- .isalpha pra saber se o val é alfabético
- .isalnum pra saber se é número
- isascii() pra saber se é um caractere ascii
- isdecimal() pra saber se é decimal
- isdigit() pra saber se é digito
- isidentifier() pra saber se é um identificador
- islower() pra saber se é lowecase
- isnumeric() pra saber se é numérico
- isprintable() pra saber se é printavel
- isspace() pra saber se é whitespace
- istitle() pra saber se segue as regras de um título
- isupper() pra saber se é capitalizado

> [!info] ex003-004
# Operadores aritméticos
+ adição
+ subtração
+  *multiplicação
+ / divisão
+  ** potência
+ // divisão inteira
	- divisão sem vírgula
-  % resto da divisão
	- o resto da divisão sem vírgula
- == igualdade
## Ordem de precedência
1. ()
2.  ** 
3.  */ // & na ordem que aparecem
4.  adição  & subtração
> [!info] ex005-015
# Módulos
- import {} = todas as variáveis do módulo
- from {} import {} = pega uma variável especifica do módulo

> [!info] ex016-021
# Manipulando Texto
## Fatiamento de String
- coloca a variável[{ }] pra pegar um caractere especifico
	- funciona no array/lista, mas é por objeto
- variável[9:13] e para em um antes do 13 (então 12)
- variável[9:21:2] de nove até 20 saltando de dois em dois
- variável[:5] quando o início é omitido ele começa da caractere 0
- variável[15:] quando o final é omitido ele termina no fim das caracteres
- variável[9::3] começa no nove e vai até o final pulando de três em três
## Análise:
- len() = qual o comprimento da variável/ return the number of items in a list:
- count() = n.count('o') conta quantas letras 'o' tem na variável
	- n.count('o', 0, 13) conta os 'o' entre o caractere 0 e 12
- find() = n.find('deo') encontra a letra/palavra na variável e mostra quando ela começa e termina
	- devolve -1 quando não existe
- in = vai te dizer se existe na variável com true/false
## Transformação:
- replace() = reposiciona n.replace('Pythin', 'Js') substitui python por js na variável
- upper() = transforma as letras minúsculas em maiúsculas
- lower(); = transforma as letras maiúsculas em minúsculas
- capitalize() = só o primeiro caractere fica maiúsculo
- title() = capitaliza todas as palavras
- strip() = remove todos os espaços no início e no fim da string
- rtrip() = remove todos os espaços na direita
- lstrip() = remove todos os espaços na esquerda
## Divisão: 
- split() = considera os espaços e faz uma divisão, colocando eles em um array/lista
 ## Junção:
- join() = junta as strings em uma lista ' 'join(n)

> [!info] ex022-027
# Condições
```python
if {}:
	bloco True
else:
	bloco False
```
```python
print('...' if {} == True else '!!!')
```

# Resources
> [!summary] Libraries
> [datetime](https://docs.python.org/3/library/datetime.html)
> [random](https://docs.python.org/3/library/random.html)
> [math](https://docs.python.org/3/library/math.html)
