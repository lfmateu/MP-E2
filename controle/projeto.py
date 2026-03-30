from src.util.gerais import imprimir_objetos
from src.entidades.patinador import Patinador, inserir_patinador, get_patinadores
from src.entidades.olimpiada import Olimpiada, inserir_olimpiada, get_olimpiadas


def cadastrar_patinador():
    inserir_patinador(Patinador('Ilia Malinin', 'Acrobático', 'Estados Unidos'))
    inserir_patinador(Patinador('Isabeau Levito', 'Expressivo', 'Estados Unidos'))
    inserir_patinador(Patinador('Alysa Liu', 'Acrobático', 'Estados Unidos'))
    inserir_patinador(Patinador('Riku Miura', 'Clássico', 'Japão'))
    inserir_patinador(Patinador('Ryuichi Kihara', 'Expressivo', 'Japão'))
    inserir_patinador(Patinador('Yuzuru Hanyu', 'Clássico', 'Japão'))
    inserir_patinador(Patinador('Jordan Stolz', 'Velocidade', 'Estados Unidos'))
    inserir_patinador(Patinador('Casey Dawson', 'Velocidade', 'Estados Unidos'))
    inserir_patinador(Patinador('Wataru Morishige', 'Velocidade', 'Japão'))
    inserir_patinador(Patinador('Tatsuya Shinhama', 'Velocidade', 'Japão'))


def cadastrar_olimpiada():
    inserir_olimpiada(Olimpiada(id=25, nome='Milão-Cortina', ano=2026, internacional=True))
    inserir_olimpiada(Olimpiada(id=24, nome='Beijing', ano=2022, internacional=True))
    inserir_olimpiada(Olimpiada(id=23, nome='PyeongChang', ano=2018, internacional=False))


if __name__ == '__main__':
    cadastrar_patinador()
    cadastrar_olimpiada()

    imprimir_objetos(cabeçalho='Patinador: nome, estilo, país', objetos=get_patinadores())
    imprimir_objetos(cabeçalho='Olimpíada: ID, nome, ano, internacional', objetos=get_olimpiadas())
