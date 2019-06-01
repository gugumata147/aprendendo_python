class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao
        self.__like = 0

    @property
    def duracao(self):
        return self.duracao

    @duracao.setter
    def duracao(self, duracao):
        self.duracao = duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)
atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')