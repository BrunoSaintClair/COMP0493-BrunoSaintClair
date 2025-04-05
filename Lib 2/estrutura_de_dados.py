class FenwickTree:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tree = [0] * (tamanho + 1)

    def build(self, dados):
        for i, valor in enumerate(dados):
            self.update(i, valor)

    def update(self, indice, delta):
        i = indice + 1
        while i <= self.tamanho:
            self.tree[i] += delta
            i += i & -i

    def query(self, indice):
        soma = 0
        i = indice + 1
        while i > 0:
            soma += self.tree[i]
            i -= i & -i
        return soma

    def query_range(self, esquerda, direita):
        return self.query(direita) - self.query(esquerda - 1)


class SegmentTree:
    def __init__(self, dados):
        self.n = len(dados)
        self.dados = dados
        self.soma = [0] * (4 * self.n)
        self.minimo = [float('inf')] * (4 * self.n)
        self.maximo = [float('-inf')] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def build(self, no, inicio, fim):
        if inicio == fim:
            self.soma[no] = self.dados[inicio]
            self.minimo[no] = self.dados[inicio]
            self.maximo[no] = self.dados[inicio]
        else:
            meio = (inicio + fim) // 2
            self.build(2 * no, inicio, meio)
            self.build(2 * no + 1, meio + 1, fim)
            self.soma[no] = self.soma[2 * no] + self.soma[2 * no + 1]
            self.minimo[no] = min(self.minimo[2 * no], self.minimo[2 * no + 1])
            self.maximo[no] = max(self.maximo[2 * no], self.maximo[2 * no + 1])

    def update(self, no, inicio, fim, indice, valor):
        if inicio == fim:
            self.dados[indice] = valor
            self.soma[no] = valor
            self.minimo[no] = valor
            self.maximo[no] = valor
        else:
            meio = (inicio + fim) // 2
            if indice <= meio:
                self.update(2 * no, inicio, meio, indice, valor)
            else:
                self.update(2 * no + 1, meio + 1, fim, indice, valor)
            self.soma[no] = self.soma[2 * no] + self.soma[2 * no + 1]
            self.minimo[no] = min(self.minimo[2 * no], self.minimo[2 * no + 1])
            self.maximo[no] = max(self.maximo[2 * no], self.maximo[2 * no + 1])

    def query_soma(self, no, inicio, fim, l, r):
        if r < inicio or fim < l:
            return 0
        if l <= inicio and fim <= r:
            return self.soma[no]
        meio = (inicio + fim) // 2
        return self.query_soma(2 * no, inicio, meio, l, r) + \
               self.query_soma(2 * no + 1, meio + 1, fim, l, r)

    def query_min(self, no, inicio, fim, l, r):
        if r < inicio or fim < l:
            return float('inf')
        if l <= inicio and fim <= r:
            return self.minimo[no]
        meio = (inicio + fim) // 2
        return min(
            self.query_min(2 * no, inicio, meio, l, r),
            self.query_min(2 * no + 1, meio + 1, fim, l, r)
        )

    def query_max(self, no, inicio, fim, l, r):
        if r < inicio or fim < l:
            return float('-inf')
        if l <= inicio and fim <= r:
            return self.maximo[no]
        meio = (inicio + fim) // 2
        return max(
            self.query_max(2 * no, inicio, meio, l, r),
            self.query_max(2 * no + 1, meio + 1, fim, l, r)
        )

