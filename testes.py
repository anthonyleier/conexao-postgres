import unittest
from banco import Banco


class BancoTestes(unittest.TestCase):
    def setUp(self):
        ipAcesso = 'localhost'
        nomeBanco = 'sistema'
        self.banco = Banco(ipAcesso, nomeBanco)
        with open('estrutura.sql', 'r', encoding='utf-8') as arquivo:
            self.banco.executar(arquivo.read())

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
        query = "SELECT * FROM usuario WHERE nome = %s AND email = %s;"
        nome1 = 'Tânia Castro'
        email1 = 'tania.castro@hotmail.com'
        senha1 = 'tania123'
        parametros = [nome1, email1]
        dados1 = self.banco.selecionar(query, parametros)
        self.assertEqual(senha1, dados1[0]['senha'])

        nome2 = 'Erick Gonçalves'
        email2 = 'erick.goncalves@hotmail.com'
        senha2 = 'erick123'
        parametros = [nome2, email2]
        dados2 = self.banco.selecionar(query, parametros)
        self.assertEqual(senha2, dados2[0]['senha'])

    def test_selecionarUm(self):
        query = "SELECT * FROM usuario WHERE email LIKE '%@gmail.com' ORDER BY id;"
        senha = 'eduarda123'
        dados = self.banco.selecionarUm(query)
        self.assertEqual(senha, dados['senha'])

    def test_selecionarUmParams(self):
        query = "SELECT * FROM usuario WHERE email = %s;"
        nome = 'Matilde Oliveira'
        email = 'matilde.oliveira@hotmail.com'
        parametros = [email]
        dados = self.banco.selecionarUm(query, parametros)
        self.assertEqual(nome, dados['nome'])

    def test_executar(self):
        query = "INSERT INTO usuario (nome, email, senha) VALUES ('Evelyn Cruz', 'evelyn.cruz@gmail.com', 'evelyn123');"
        self.banco.executar(query)

        query2 = "SELECT * FROM usuario WHERE nome = 'Evelyn Cruz';"
        dados = self.banco.selecionarUm(query2)
        email = 'evelyn.cruz@gmail.com'
        self.assertEqual(email, dados['email'])

    def test_executarParams(self):
        query = "DELETE FROM usuario WHERE email = %s;"
        email = 'evelyn.cruz@gmail.com'
        parametros = [email]
        self.banco.executar(query, parametros)

        query2 = "SELECT * FROM usuario WHERE senha = 'evelyn123';"
        dados = self.banco.selecionarUm(query2)
        self.assertEqual(None, dados)

    def test_fecharConexao(self):
        self.assertEqual(self.banco.conexao.closed, 0)
        self.banco.fecharConexao()
        self.assertEqual(self.banco.conexao.closed, 1)


if __name__ == '__main__':
    unittest.main()
