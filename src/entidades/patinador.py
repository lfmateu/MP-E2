patinadores = {}


def get_patinadores():
    return patinadores

def inserir_patinador(patinador):
    nome_patinador = patinador.nome
    if nome_patinador not in patinadores.keys():
        patinadores[nome_patinador] = patinador
    else:
        print(f'Patinador {nome_patinador} já tem cadastro no sistema.')
class Patinador:
    def __init__(self, nome, estilo_patinador, pais, data_nascimento, anos_competição):
        self.nome = nome
        self.estilo_patinador = estilo_patinador
        self.pais = pais if pais in ("Estados Unidos", "Japão") else "Indefinida"
        self.data_nascimento = data_nascimento
        self.anos_competição = anos_competição

    def __str__(self):
        formato = '{:<18} {:<13} {:<15} {:<10} {:<10}'
        return formato.format(self.nome, self.estilo_patinador, self.pais, str(self.data_nascimento), self.anos_competição)