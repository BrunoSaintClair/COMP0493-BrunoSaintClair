#include <stdio.h>
#include <stdlib.h>

// Estrutura para itens da mochila
typedef struct {
    int peso;
    int valor;
    double valorPorPeso;
} Item;

int compararItens(const void *a, const void *b) {
    Item *itemA = (Item *)a;
    Item *itemB = (Item *)b;
    if (itemB->valorPorPeso > itemA->valorPorPeso) return 1;
    if (itemB->valorPorPeso < itemA->valorPorPeso) return -1;
    return 0;
}

// Mochila Fracionária
double mochilaFracionaria(Item itens[], int n, int capacidade) {
    qsort(itens, n, sizeof(Item), compararItens);

    double valorTotal = 0.0;
    for (int i = 0; i < n; i++) {
        if (capacidade >= itens[i].peso) {
            valorTotal += itens[i].valor;
            capacidade -= itens[i].peso;
        } else {
            valorTotal += itens[i].valorPorPeso * capacidade;
            break;
        }
    }
    return valorTotal;
}

// Problema do Troco
void problemaDoTroco(int moedas[], int n, int valor) {
    qsort(moedas, n, sizeof(int), (int (*)(const void *, const void *))compararItens);

    printf("Moedas usadas:\n");
    for (int i = n - 1; i >= 0; i--) {
        while (valor >= moedas[i]) {
            valor -= moedas[i];
            printf("%d ", moedas[i]);
        }
    }
    printf("\n");
}

// Estrutura para tarefas
typedef struct {
    int id;
    int deadline;
    int lucro;
} Tarefa;

int compararTarefas(const void *a, const void *b) {
    Tarefa *tarefaA = (Tarefa *)a;
    Tarefa *tarefaB = (Tarefa *)b;
    return tarefaB->lucro - tarefaA->lucro;
}

// Escalonamento de Tarefas
int escalonamentoDeTarefas(Tarefa tarefas[], int n) {
    qsort(tarefas, n, sizeof(Tarefa), compararTarefas);

    int maxDeadline = 0;
    for (int i = 0; i < n; i++) {
        if (tarefas[i].deadline > maxDeadline)
            maxDeadline = tarefas[i].deadline;
    }

    int *agenda = (int *)calloc(maxDeadline + 1, sizeof(int));
    int lucroTotal = 0;

    for (int i = 0; i < n; i++) {
        for (int j = tarefas[i].deadline; j > 0; j--) {
            if (agenda[j] == 0) {
                agenda[j] = tarefas[i].id;
                lucroTotal += tarefas[i].lucro;
                break;
            }
        }
    }

    free(agenda);
    return lucroTotal;
}
