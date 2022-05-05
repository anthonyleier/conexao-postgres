import unittest
from banco import Banco


class BancoTestes(unittest.TestCase):
    def setUp(self):
        ipAcesso = 'localhost'
        nomeBanco = 'sistema'
        self.banco = Banco(ipAcesso, nomeBanco)

    def selecionar(self):
        pass

    def selecionarParams(self):
        pass

    def selecionarUm(self):
        pass

    def selecionarUmParams(self):
        pass

    def executar(self):
        pass

    def executarParams(self):
        pass

    def fecharConexao(self):
        pass


if __name__ == '__main__':
    unittest.main()
