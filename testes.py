import unittest
from banco import Banco


class BancoTestes(unittest.TestCase):
    def setUp(self):
        ipAcesso = 'localhost'
        nomeBanco = 'sistema'
        self.banco = Banco(ipAcesso, nomeBanco)

    def test_selecionar(self):
        query = "SELECT nome, email, senha FROM usuario;"
        usuario1 = {'nome': 'Gustavo Dias', 'email': 'gustavo.dias@hotmail.com', 'senha': 'gustavo123'}
        usuario2 = {'nome': 'Rafaela Barros', 'email': 'rafaela.barros@gmail.com', 'senha': 'rafaela123'}
        usuario3 = {'nome': 'Victoria Alves', 'email': 'victoria.alves@hotmail.com', 'senha': 'victoria123'}
        dados = self.banco.selecionar(query)
        self.assertIn(usuario1, dados)
        self.assertIn(usuario2, dados)
        self.assertIn(usuario3, dados)

    def test_selecionarParams(self):
        query = "SELECT senha FROM usuario WHERE nome = %s AND email = %s;"
        nome = 'Tânia Castro'
        email = 'tania.castro@hotmail.com'
        senha = 'tania123'
        parametros = [nome, email]
        dados = self.banco.selecionar(query, parametros)
        print(dados)
        self.assertEqual(senha, dados[0]['senha'])

    # def test_selecionarUm(self):
    #     query = "SELECT email FROM usuario WHERE email LIKE '%@gmail.com' ORDER BY id;"
    #     email = 'eduarda.azevedo@gmail.com'
    #     self.banco.selecionar(query)
    #     self.assertIn(email, self.banco.selecionar(query))

    # def test_selecionarUmParams(self):
    #     query = "SELECT email FROM usuario WHERE email LIKE '%@gmail.com' ORDER BY id;"
    #     email = 'eduarda.azevedo@gmail.com'
    #     parametros = [email]
    #     self.banco.selecionar(query, parametros)
    #     self.assertIn(email, self.banco.selecionar(query))

    # def test_executar(self):
    #     query = "INSERT INTO usuario (nome, email, senha) VALUES ('Evelyn', 'evelyn@gmail.com', 'evelyn123';"
    #     self.banco.executar(query)
    #     query2 = "SELECT email FROM usuario WHERE email = 'evelyn@gmail.com';"
    #     email = self.banco.selecionarUm(query2)
    #     self.assertEqual(email, 'evelyn@gmail.com')

    # def test_executarParams(self):
    #     query = "INSERT INTO usuario (nome, email, senha) VALUES ('Martim', 'martim@gmail.com', 'martim123';"
    #     self.banco.executar(query)
    #     query2 = "SELECT email FROM usuario WHERE email = 'martim@gmail.com';"
    #     email = self.banco.selecionarUm(query2)
    #     self.assertEqual(email, 'martim@gmail.com')

    # def test_fecharConexao(self):
    #     self.assertEqual(self.banco.conexao.closed, 0)
    #     self.banco.fecharConexao()
    #     self.assertEqual(self.banco.conexao.closed, 1)


if __name__ == '__main__':
    unittest.main()
