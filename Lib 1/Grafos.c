#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100

// BFS e DFS em Matriz de Adjacência
void BFS_matriz(int grafo[MAX][MAX], int n, int inicio) {
    bool visitado[MAX] = {false};
    int fila[MAX], front = 0, rear = 0;

    fila[rear++] = inicio;
    visitado[inicio] = true;

    printf("BFS (Matriz de Adjacência): ");
    while (front < rear) {
        int atual = fila[front++];
        printf("%d ", atual);

        for (int i = 0; i < n; i++) {
            if (grafo[atual][i] && !visitado[i]) {
                fila[rear++] = i;
                visitado[i] = true;
            }
        }
    }
    printf("\n");
}

void DFS_matriz_util(int grafo[MAX][MAX], int n, int atual, bool visitado[MAX]) {
    printf("%d ", atual);
    visitado[atual] = true;

    for (int i = 0; i < n; i++) {
        if (grafo[atual][i] && !visitado[i]) {
            DFS_matriz_util(grafo, n, i, visitado);
        }
    }
}

void DFS_matriz(int grafo[MAX][MAX], int n, int inicio) {
    bool visitado[MAX] = {false};
    printf("DFS (Matriz de Adjacência): ");
    DFS_matriz_util(grafo, n, inicio, visitado);
    printf("\n");
}

// BFS e DFS em Lista de Adjacência
typedef struct Node {
    int vertice;
    struct Node* prox;
} Node;

typedef struct {
    Node* cabeca;
} ListaAdj;

void adicionarAresta(ListaAdj lista[], int origem, int destino) {
    Node* novoNode = (Node*)malloc(sizeof(Node));
    novoNode->vertice = destino;
    novoNode->prox = lista[origem].cabeca;
    lista[origem].cabeca = novoNode;
}

void BFS_lista(ListaAdj lista[], int n, int inicio) {
    bool visitado[MAX] = {false};
    int fila[MAX], front = 0, rear = 0;

    fila[rear++] = inicio;
    visitado[inicio] = true;

    printf("BFS (Lista de Adjacência): ");
    while (front < rear) {
        int atual = fila[front++];
        printf("%d ", atual);

        for (Node* adj = lista[atual].cabeca; adj != NULL; adj = adj->prox) {
            if (!visitado[adj->vertice]) {
                fila[rear++] = adj->vertice;
                visitado[adj->vertice] = true;
            }
        }
    }
    printf("\n");
}

void DFS_lista_util(ListaAdj lista[], int atual, bool visitado[MAX]) {
    printf("%d ", atual);
    visitado[atual] = true;

    for (Node* adj = lista[atual].cabeca; adj != NULL; adj = adj->prox) {
        if (!visitado[adj->vertice]) {
            DFS_lista_util(lista, adj->vertice, visitado);
        }
    }
}

void DFS_lista(ListaAdj lista[], int n, int inicio) {
    bool visitado[MAX] = {false};
    printf("DFS (Lista de Adjacência): ");
    DFS_lista_util(lista, inicio, visitado);
    printf("\n");
}
