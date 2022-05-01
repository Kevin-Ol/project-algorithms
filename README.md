# Projeto Algorithms

Projeto feito como critério avaliativo na escola de programação Trybe.

Foi utilizada a linguagem de programação Python.

O objetivo do projeto foi consolidar o conhecimento em complexidade de algoritmos e recursividade. Foram realizados vários desafios lógicos, buscando
sua solução com menor complexidade, menor tempo de execução e/ou usando recursividade.

## Instruções para reproduzir o projeto

#### Pré Requisitos

Possuir Python instalado

---

1. Clone o repositório
  * `git@github.com:Kevin-Ol/project-algorithms.git`.
  * Entre na pasta do repositório que você acabou de clonar:
    * `cd project-tech-news`

2. Inicie e ative um ambiente virtual
  * `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências
  * `python3 -m pip install -r dev-requirements.txt`

obs: caso haja algum problema na instalação do pacote wheel, reinstale-o com o comando
  * `python3 -m pip install wheel`
---

Os requisitos desenvolvidos no projeto são:

`challenges/challenge_study_schedule.py`

- Função `study_schedule`: possui como parâmetro uma lista de tuplas e um número. O objetivo do desafio é retornar o número de estudantes acessando uma
plataforma de estudo ao mesmo tempo. Para isso são informados um lista de tuplas, contendo o horário de entrada e saída de cada estudante, e um número
informando o horário desejado, retornando assim a quantidade de alunos que estavam presentes, como no exemplo abaixo. A função também deve retornar o
valor None caso não seja inserido um número válido em alguma das entradas.

```bash
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 3 
saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário
```

`challenges/challenge_palindromes_recursive.py`

- Função `is_palindrome_recursive`: possui como parâmetro uma string, o índice de sua primeira letra e o índice de sua última letra. O objetivo do desafio
foi verificar, de forma recursiva, se a palavra informada é um palíndromo, retornando True ou False. Um palíndromo é uma palavra que possui o mesmo sentido
sendo lida da esquerda para a direita, ou da direita para a esquerda:

```bash
word = "REVIVER"
saída: True

word = "COXINHA"
saída: False
```

`challenges/challenge_anagrams.py`

- Função `is_anagram`: possui como parâmetro 2 strings. O objetivo do desafio foi verificar, se as palavras informadas são anagramas, retornando True ou 
False. Um anagrama é quando 2 ou mais palavras podem ser formadas utilizando a mesma quantidade de cada uma das letras que formam as palavras:

```bash
first_string = "amor"
second_string = "roma"
saída: True

first_string = "coxinha"
second_string = "empada"
saída: False
```

`challenges/challenge_find_the_duplicate.py`

- Função `find_duplicate`: possui como parâmetro uma lista de números. O objetivo do desafio foi verificar, qual dos números da lista se repete, 
retornando-o. Caso haja erro na validação da entrada ou não haja números repetidos, deve retornar o valor False.

```bash
nums = [3, 1, 3, 4, 2]
saída: 3

nums = [1, 2]
saída: False
```

`challenges/challenge_palindromes_iterative.py`

- Função `is_palindrome_iterative`: possui como parâmetro uma string. O objetivo do desafio foi verificar, de forma iterativa, se a palavra informada 
é um palíndromo, retornando True ou False. Um palíndromo é uma palavra que possui o mesmo sentido sendo lida da esquerda para a direita, ou da 
direita para a esquerda:

```bash
word = "REVIVER"
saída: True

word = "COXINHA"
saída: False
```
