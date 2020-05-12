from atleta import Atleta
class LutadorMMA(Atleta):
    def __init__(self,nome,idade,cat,cint):
      self.cat=cat
      self.cint=cint
      super().__init__(nome,idade)

    def Faz_o_que(self,nome,cat,cint):
        return ("O lutador "+nome+" da categoria "+cat+" e disputou "+cint+" cinturão.")