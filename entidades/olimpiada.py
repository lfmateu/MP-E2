olimpiadas = []


def get_olimpiadas():
    return olimpiadas


def inserir_olimpiada(olimpiada):
    olimpiadas.append(olimpiada)


class Olimpiada:

    def __init__(self, id, nome, ano, internacional):
        self.id = id
        self.nome = nome
        self.ano = ano
        self.internacional = internacional

    def __str__(self):
        internacional_txt = "internacional" if self.internacional else ""
        formato = '{:<5} {:<15} {:<5} {:<3}'
        olimpiada_formatado = formato.format(
            self.id,
            self.nome,
            self.ano,
            internacional_txt
        )
        return olimpiada_formatado
