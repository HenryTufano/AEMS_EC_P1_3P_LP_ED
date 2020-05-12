from atleta import Atleta
class Futebolista(Atleta):
    def __init__(self,nome,idade,gol):
      self.gol=gol
      super().__init__(nome,idade)
    
    def Faz_o_que(self,nome,gol):
        return ("O jogador "+nome+" fez "+gol+" gols.")