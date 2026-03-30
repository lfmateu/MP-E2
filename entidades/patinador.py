patinadores = []


def get_patinadores():
    return patinadores


def inserir_patinador(patinador):
    patinadores.append(patinador)


class Patinador:
    def __init__(self, nome, estilo_patinador, pais):
        self.nome = nome
        self.estilo_patinador = estilo_patinador
        self.pais = pais if pais in ("Estados Unidos", "Japão") else ("Indefinida")

    def __str__(self):
        formato = '{:<20} {:<15} {:<15}'
        return formato.format(self.nome, self.estilo_patinador, self.pais)
