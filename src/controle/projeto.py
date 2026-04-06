from src.util.gerais import imprimir_objetos, ordenar_objetos_por_um_atributo
from src.entidades.patinador import Patinador, inserir_patinador, get_patinadores
from src.entidades.olimpiada import Olimpiada, inserir_olimpiada, get_olimpiadas
from src.entidades.equipe import Equipe, inserir_equipe, get_equipes
from src.util.data import Data


def cadastrar_patinador():
    inserir_patinador(Patinador('Ilia Malinin', 'Acrobático', 'Estados Unidos', data_nascimento=Data(2, 12, 2004), anos_competição=5))
    inserir_patinador(Patinador('Isabeau Levito', 'Expressivo', 'Estados Unidos', data_nascimento=Data(3, 3, 2007), anos_competição=4))
    inserir_patinador(Patinador('Alysa Liu', 'Acrobático', 'Estados Unidos', data_nascimento=Data(8, 8, 2005), anos_competição=8))
    inserir_patinador(Patinador('Riku Miura', 'Clássico', 'Japão', data_nascimento=Data(17, 12, 2001), anos_competição=7))
    inserir_patinador(Patinador('Ryuichi Kihara', 'Expressivo', 'Japão', data_nascimento=Data(22, 8, 1992), anos_competição=13))
    inserir_patinador(Patinador('Yuzuru Hanyu', 'Clássico', 'Japão', data_nascimento=Data(7, 12, 2004), anos_competição=16))
    inserir_patinador(Patinador('Jordan Stolz', 'Velocidade', 'Estados Unidos', data_nascimento=Data(21, 5, 2001), anos_competição=6))
    inserir_patinador(Patinador('Casey Dawson', 'Velocidade', 'Estados Unidos', data_nascimento=Data(2, 8, 2000), anos_competição=5))
    inserir_patinador(Patinador('Wataru Morishige', 'Velocidade', 'Japão', data_nascimento=Data(17, 7, 2000), anos_competição=3))
    inserir_patinador(Patinador('Tatsuya Shinhama', 'Velocidade', 'Japão', data_nascimento=Data(11, 7, 1996), anos_competição=7))
def cadastrar_olimpiada():
    inserir_olimpiada(Olimpiada(id=25, nome='Milão-Cortina', ano=2026, internacional=True))
    inserir_olimpiada(Olimpiada(id=24, nome='Beijing', ano=2022, internacional=True))
    inserir_olimpiada(Olimpiada(id=23, nome='PyeongChang', ano=2018, internacional=False))


def cadastrar_equipes():
    equipe_euaa = Equipe(nome_equipe='EUA Artístico', país='Estados Unidos', estilo_equipe='Artística')
    equipe_euaa.inserir_patinadores(['Ilia Malinin', 'Isabeau Levito', 'Alysa Liu'])
    inserir_equipe(equipe_euaa)
    equipe_euav = Equipe(nome_equipe='EUA Velocidade', país='Estados Unidos', estilo_equipe='Velocidade')
    equipe_euav.inserir_patinadores(['Jordan Stolz', 'Casey Dawson'])
    inserir_equipe(equipe_euav)
    equipe_jpa = Equipe(nome_equipe='Japão Artística', país='Japão', estilo_equipe='Artística')
    equipe_jpa.inserir_patinadores(['Yuzuru Hanyu', 'Riku Miura', 'Ryuichi Kihara'])
    inserir_equipe(equipe_jpa)
    equipe_jpv = Equipe(nome_equipe='Japão Velocidade', país='Japão', estilo_equipe='Velocidade')
    equipe_jpv.inserir_patinadores(['Wataru Morishige', 'Tatsuya Shinhama'])
    inserir_equipe(equipe_jpv)


if __name__ == '__main__':
    cadastrar_patinador()
    cadastrar_olimpiada()
    cadastrar_equipes()

    imprimir_objetos(cabeçalho='Patinador: nome, estilo, país, data de nascimento, anos de competição', objetos=get_patinadores().values())
    imprimir_objetos(cabeçalho='Olimpíada: ID, nome, ano, internacional', objetos=get_olimpiadas().values())

    imprimir_objetos(cabeçalho='Equipe: nome, país, estilo', objetos=get_equipes().values())

    for equipe in get_equipes().values():
        print(f'\n\n=== Detalhes da Equipe: {equipe.nome_equipe} ===')
        patinadores_da_equipe = equipe.patinadores.values()
        imprimir_objetos('Patinadores da Equipe (Ordem de Cadastro):', patinadores_da_equipe)
        patinadores_ordenados = ordenar_objetos_por_um_atributo(
            objetos=patinadores_da_equipe,
            comparador=lambda p1, p2: p1.nome < p2.nome
        )
        imprimir_objetos('Patinadores (Ordem Alfabética):', patinadores_ordenados)