from atleta import Atleta
class Nadador(Atleta):
    def __init__(self,nome,idade,nmeda,noli):
      self.nmeda=nmeda
      self.noli=noli
      super().__init__(nome,idade)

    def Faz_o_que(self,nome,nmeda,noli):
        return ("O nadador "+nome+" ganhou "+nmeda+" medalhas e partcipou de "+noli+" olimpiadas.")