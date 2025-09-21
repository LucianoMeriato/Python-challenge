from typing import List, Dict, Callable, Any

consumos: List[Dict[str, Any]] = [
    {"data":"2025-09-14","nome":"Álcool 70%","qtd":10,"validade":"2026-01-10","setor":"Recepção","lote":"L101-1"},
    {"data":"2025-09-15","nome":"Luva Nitrílica","qtd":25,"validade":"2025-10-05","setor":"Laboratório","lote":"L245-3"},
    {"data":"2025-09-16","nome":"Gaze Estéril","qtd":15,"validade":"2025-12-20","setor":"Almoxarifado","lote":"L333-2"},
    {"data":"2025-09-17","nome":"Kit PCR","qtd":8,"validade":"2025-09-30","setor":"Laboratório","lote":"L509-4"},
    {"data":"2025-09-18","nome":"Reagente X","qtd":40,"validade":"2026-03-15","setor":"Laboratório","lote":"L777-1"},
    {"data":"2025-09-19","nome":"Gaze Estéril","qtd":12,"validade":"2025-12-20","setor":"Recepção","lote":"L333-3"},
    {"data":"2025-09-20","nome":"Álcool 70%","qtd":18,"validade":"2026-01-10","setor":"Administração","lote":"L101-2"},
]


def fila_enfileirar(fila: List[Dict[str, Any]], item: Dict[str, Any]) -> None:
    fila.append(item)  

def fila_desenfileirar(fila: List[Dict[str, Any]]) -> Dict[str, Any] | None:
    if fila:
        return fila.pop(0)  
    return None

def pilha_push(pilha: List[Dict[str, Any]], item: Dict[str, Any]) -> None:
    pilha.append(item)  

def pilha_pop(pilha: List[Dict[str, Any]]) -> Dict[str, Any] | None:
    if pilha:
        return pilha.pop()  
    return None


def busca_sequencial(lista: List[Dict[str, Any]], pred: Callable[[Dict[str, Any]], bool]) -> Dict[str, Any] | None:
    for item in lista:
        if pred(item):
            return item
    return None

def busca_binaria(lista_ordenada: List[Dict[str, Any]], chave: Callable[[Dict[str, Any]], Any], valor: Any) -> Dict[str, Any] | None:
    i, j = 0, len(lista_ordenada) - 1
    while i <= j:
        m = (i + j) // 2
        k = chave(lista_ordenada[m])
        if k == valor:
            return lista_ordenada[m]
        if k < valor:
            i = m + 1
        else:
            j = m - 1
    return None


def merge_sort(lista: List[Dict[str, Any]], key: Callable[[Dict[str, Any]], Any]) -> List[Dict[str, Any]]:
    if len(lista) <= 1:
        return lista[:]
    meio = len(lista) // 2
    L = merge_sort(lista[:meio], key)
    R = merge_sort(lista[meio:], key)
    res: List[Dict[str, Any]] = []
    i = j = 0
    while i < len(L) and j < len(R):
        if key(L[i]) <= key(R[j]):
            res.append(L[i]); i += 1
        else:
            res.append(R[j]); j += 1
    res.extend(L[i:]); res.extend(R[j:])
    return res

def quick_sort(lista: List[Dict[str, Any]], key: Callable[[Dict[str, Any]], Any]) -> List[Dict[str, Any]]:
    if len(lista) <= 1:
        return lista[:]
    p = key(lista[len(lista)//2])
    menores = [x for x in lista if key(x) < p]
    iguais  = [x for x in lista if key(x) == p]
    maiores = [x for x in lista if key(x) > p]
    return quick_sort(menores, key) + iguais + quick_sort(maiores, key)


def resolver_problema(base: List[Dict[str, Any]]) -> None:
    print("=== 1) Registro Cronológico (FILA – FIFO) ===")
    fila: List[Dict[str, Any]] = []
    for c in base:
        fila_enfileirar(fila, c)
    print(f"Fila criada com {len(fila)} registros (em ordem de chegada).")

    for _ in range(min(2, len(fila))):
        saiu = fila_desenfileirar(fila)
        print(" - Processado (saiu da fila):", saiu)

    print("\n=== 2) Consulta Rápida (PILHA – LIFO) ===")
    pilha: List[Dict[str, Any]] = []
    for c in base:
        pilha_push(pilha, c)
    print(f"Pilha criada com {len(pilha)} registros (últimos no topo).")

    for _ in range(min(2, len(pilha))):
        topo = pilha_pop(pilha)
        print(" - Último registro (pop):", topo)

    print("\n=== 3) Ordenação por Validade (Merge Sort – estável) ===")
    por_validade = merge_sort(base, key=lambda x: (x['validade'], x['nome'], x['lote']))
    for c in por_validade[:3]:
        print(" - Próximos do vencimento (top 3):", c)

    print("\n=== 4) Ordenação por Quantidade (Quick Sort – rápido em média) ===")
    por_qtd = quick_sort(base, key=lambda x: x['qtd'])
    maiores = por_qtd[-3:] if len(por_qtd) >= 3 else por_qtd
    for c in maiores:
        print(" - Maiores consumos (top 3):", c)

    print("\n=== 5) Buscas ===")
    alvo_nome = 'Gaze Estéril'
    achou_seq = busca_sequencial(base, lambda x: x['nome'] == alvo_nome and x['setor'] == 'Laboratório')
    print(f" - Busca Sequencial por '{alvo_nome}' no setor Laboratório:", achou_seq)

    base_por_nome = merge_sort(base, key=lambda x: (x['nome'], x['data'], x['lote']))
    achou_bin = busca_binaria(base_por_nome, chave=lambda x: x['nome'], valor='Álcool 70%')
    print(" - Busca Binária por nome='Álcool 70%':", achou_bin)

    print("\n=== 6) Relatório Sumário ===")
    print(f"Registros totais: {len(base)}")
    print(f"Fila restante após 2 processamentos: {len(fila)}")
    if por_validade:
        print('Mais urgente (validade mais próxima):', por_validade[0])
    if maiores:
        print('Maior consumo do período:', maiores[-1])

if __name__ == '__main__':
    resolver_problema(consumos)
