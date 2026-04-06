olimpiadas = {}

def get_olimpiadas():
    """Retorna o dicionário de olimpíadas cadastradas."""
    return olimpiadas

def inserir_olimpiada(olimpiada):
    id_olimpiada = olimpiada.id
    if id_olimpiada not in olimpiadas.keys():
        olimpiadas[id_olimpiada] = olimpiada
    else:
        print(f'Olimpíada com ID {id_olimpiada} já tem cadastro no sistema.')

class Olimpiada:
    def __init__(self, id, nome, ano, internacional):
        self.id = id
        self.nome = nome
        self.ano = ano
        self.internacional = internacional

    def __str__(self):
        internacional_txt = "Sim" if self.internacional else ""
        formato = '{:<5} {:<15} {:<6} {:<10}'
        return formato.format(self.id, self.nome, self.ano, internacional_txt)