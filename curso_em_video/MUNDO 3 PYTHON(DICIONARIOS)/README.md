# 🗂️ Treinamento de Dicionários em Python (Aula 19)

Este repositório contém os exercícios de fixação e testes práticos desenvolvidos durante o estudo do **Módulo 3 (Fase 19 - Dicionários)** do curso de Python do Curso em Vídeo.

## 🚀 Objetivo do Treino
O arquivo `ex.19(treino_a).py` foi criado estrategicamente para consolidar os fundamentos da estrutura de dados composta conhecida como **Dicionários (Dicts)** em Python, antes de avançar para os desafios principais.

## 🧠 Conceitos Praticados

O script foi dividido em 3 etapas fundamentais:

1. **🚗 Treino 1: Criação e Acesso Estático**
   - Declaração de dicionários utilizando chaves `{}`.
   - Atribuição de pares de **Chave: Valor** (`marca`, `modelo`, `ano`).
   - Acesso individual a dados usando colchetes `[]`.
   - Exibição de dados formatados com *f-strings* utilizando aspas duplas internas para chaves.

2. **🎨 Treino 2: Manipulação Dinâmica e Laços**
   - Alteração de valores existentes de forma direta (`carro['ano'] = 2027`).
   - Adição de novos elementos na memória sem a necessidade do método `.append()` (`carro['cor'] = 'Preto'`).
   - Varredura e iteração completa do dicionário usando o laço `for k, v in carro.items()`.

3. **🔧 Treino 3: Destruição de Dados**
   - Remoção permanente de chaves e valores utilizando o comando nativo `del`.

---

## 💻 Resultado Esperado no Console

Ao executar o arquivo `ex.19(treino_a).py`, o sistema renderiza a seguinte saída organizada:

```text
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
         TREINANDO DICIONÁRIOS         
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

--- Treino 1 ---
chevrolet
onix
2026
Eu tenho um onix da chevrolet ano 2026.

--- Treino 2 ---
marca: chevrolet
modelo: onix
ano: 2027
cor: Preto

--- Treino 3 ---
{'modelo': 'onix', 'ano': 2027, 'cor': 'Preto'}

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=