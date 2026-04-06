equipes = {}

def get_equipes():
    return equipes

def inserir_equipe(equipe):
    nome_equipe = equipe.nome_equipe
    if nome_equipe not in equipes:
        equipes[nome_equipe] = equipe
    else:
        print(f'Equipe {nome_equipe} já tem cadastro no sistema.')

class Equipe:
    def __init__(self, nome_equipe, país, estilo_equipe):
        self.nome_equipe = nome_equipe
        self.país = país
        self.estilo_equipe = estilo_equipe
        self.patinadores = {}

    def inserir_patinadores(self, chaves_patinadores):
        from src.entidades.patinador import get_patinadores

        for nome_patinador in chaves_patinadores:
            if nome_patinador in get_patinadores():
                self.patinadores[nome_patinador] = get_patinadores()[nome_patinador]
            else:
                print('Atleta' + str(nome_patinador) + 'não tem cadastro')

    def __str__(self):
        formato = '{:<20} {:<20} {:<5}'
        return formato.format(self.nome_equipe, self.país, self.estilo_equipe)