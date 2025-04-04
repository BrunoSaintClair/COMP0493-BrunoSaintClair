#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Função para calcular a distância entre dois pontos
float distanciaEntrePontos(float x1, float y1, float x2, float y2) {
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

// Função para calcular a distância entre um ponto e uma reta
float distanciaPontoReta(float x, float y, float a, float b, float c) {
    return fabs(a * x + b * y + c) / sqrt(a * a + b * b);
}

