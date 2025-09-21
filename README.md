# Python-challenge

# INTEGRANTES

Pietro Vitor Pezzente - RM557284
Luciano Henrique Meriato Junior - RM554546
Vinicius Henrique - RM556908
Eric Darakjian - RM557082
Enzo Vinicios - RM558225

# Objetivo 

Demonstrar, em um único programa, o uso integrado de Fila (FIFO), Pilha (LIFO), Busca Sequencial, Busca Binária, Merge Sort e Quick Sort para processar o consumo de insumos em unidades de diagnóstico.

⚙️ Funcionalidades
1️⃣ Fila – FIFO

Uso: Registra os consumos na ordem cronológica em que ocorreram.

Implementação: append() para enfileirar e pop(0) para desenfileirar.

Finalidade: Garante rastreabilidade fiel ao histórico (os primeiros a entrar são os primeiros a sair).

2️⃣ Pilha – LIFO

Uso: Permite consultar rapidamente os consumos mais recentes.

Implementação: append() para inserir e pop() para remover.

Finalidade: Útil para verificar ou desfazer ações recentes.

3️⃣ Busca Sequencial

Uso: Localiza registros com base em um predicado qualquer (ex.: nome e setor).

Complexidade: O(n).

Quando usar: Listas pequenas ou dados muito dinâmicos.

4️⃣ Busca Binária

Uso: Localiza registros rapidamente em uma lista previamente ordenada (por nome).

Complexidade: O(log n).

Quando usar: Consultas frequentes em bases relativamente estáticas.

5️⃣ Merge Sort – Estável

Uso: Ordena consumos por validade para priorizar reposições.

Complexidade: O(n log n) no pior caso.

Vantagem: Preserva a ordem relativa de elementos iguais.

6️⃣ Quick Sort – Rápido em Média

Uso: Ordena consumos por quantidade para identificar picos de uso.

Complexidade: Médio caso O(n log n); pior caso O(n²).

Vantagem: Geralmente mais rápido e consome menos memória.

🧠 Fluxo do Programa

Fila: Cria uma fila cronológica e processa os dois registros mais antigos.

Pilha: Cria uma pilha para consulta rápida e mostra os dois últimos registros.

Ordenação:

Merge Sort lista os três insumos mais próximos do vencimento.

Quick Sort destaca os três maiores consumos.

Buscas:

Sequencial: Procura “Gaze Estéril” no setor Laboratório.

Binária: Localiza “Álcool 70%” após ordenar a base por nome.

Relatório Final: Mostra totais, fila restante, item mais urgente e maior consumo.
