from src.entidades.patinador import get_patinadores

equipes = {}

def get_equipes():
    return equipes

def inserir_equipe(equipe):
    nome_id = equipe.nome_equipe
    if nome_id not in equipes.keys():
        equipes[nome_id] = equipe
    else:
        print('Equipe ' + nome_id + ' já tem cadastro no sistema')

class Equipe:
    def __init__(self, nome_equipe, pais, estilo_equipe):
        self.nome_equipe = nome_equipe
        self.pais = pais
        self.estilo_equipe = estilo_equipe
        self.id = self.título()
        self.patinadores = {}

    def __str__(self):
        formato = '{:<25} {:<15} {:<20}'
        equipe_formatada = formato.format(self.nome_equipe, self.pais, self.estilo_equipe)
        return equipe_formatada

    def título(self):
        return self.nome_equipe + ' (' + self.pais + ')'

    def inserir_patinadores(self, chaves_patinadores):
        for nome_patinador in chaves_patinadores:
            if nome_patinador in get_patinadores().keys():
                self.patinadores[nome_patinador] = get_patinadores()[nome_patinador]
            else:
                print('Atleta ' + nome_patinador + ' não tem cadastro')