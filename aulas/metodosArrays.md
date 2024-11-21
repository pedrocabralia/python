# alguns métodos para vetores/listas

**UTILIZAÇÃO PRÁTICA DE VETORES/LISTA**
[URNA](../../projeto_urna/index.js)

[Ver](file:///home/pedroale/%C3%81rea%20de%20Trabalho/IFTO/Sistemas%20para%20internet/projeto_urnaIFTO/index.html)




## O que é um Método?

> Na programação, um método é como uma instrução que ensina algo (um objeto ou uma coisa) a fazer uma tarefa. É como um botão que você aperta para o robô fazer algo que ele já aprendeu.

### Somando valores de uma lista `sum()`

```python
notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]

soma_das_notas = sum(notas)

print(soma_das_notas)

```
* Esse código é mais eficiente do que usar laço de repetição. 

### Retornando o tamnho da lista `len()`

```python
qtd_de_notas = len(notas)
print(qtd_de_notas)
```

### Contando quantas vezes um elemento aparece na lista `count()`

```python
qtd_de_setes = notas.count(7.0)
print(qtd_de_setes)
```
###  Adicionando um elemento no final na lista `append()`

```python
alimentos = ["arroz", "feijão"]

alimentos.append("peixe")

print(alimentos)
```


###  Adicionando um elemento em uma posição específica na lista `insert()`

```python
alimentos = ["arroz", "feijão"]

alimentos.insert(0,"peixe")
```
###  Remover o primeiro elemento igual ao valor especificado. `remove()`

```python
alimentos = ["arroz", "feijão"]

alimentos.remove("arroz")

print(alimentos)
```


###  Remover e retornar o elemento de uma posição específica. `pop()`

```python
alimentos = ["arroz", "feijão"]

alimentos.pop(0)

print(alimentos)
```
###  Ordena os elementos da lista `sort()`

```python
numeros = [10,5,6,8]

numeros.sort()

print(numeros)
```



###  Inverte a ordem dos elementos na lista. `reverse()`

```python
numeros = [5, 2, 9, 1, 7]
numeros.sort(reverse=True)
print(numeros) 
```

### Pegando o maior e o menor número:

```python
numeros = [5, 2, 9, 1, 7]

maior = max(numeros)
menor = min(numeros)

print("Maior número:",maior)  # Saída: Maior número: 9
print("Menor número: ",menor)  # Saída: Menor número: 1

```






### Referências:
[alura](https://www.alura.com.br/artigos/listas-no-python?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conte%C3%BAdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=164240702375&hsa_ad=703853654617&hsa_src=g&hsa_tgt=dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiA0fu5BhDQARIsAMXUBOInw9y01b73szjzKsE2nQ2V00Kav5W9G1mf4VZ4pmxTIGyw_FDf7Y8aAoNXEALw_wcB)  

[Rocketseat](https://blog.rocketseat.com.br/listas-no-python-e-seus-principais-metodos/)