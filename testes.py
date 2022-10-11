import unittest
from banco import Banco


class BancoTestes(unittest.TestCase):
    def setUp(self):
        ipAcesso = 'localhost'
        base = 'sistema'
        self.base = Banco(ipAcesso, base)
        with open('estrutura.sql', 'r', encoding='utf-8') as arquivo:
            self.base.executar(arquivo.read())

    def test_selecionar(self):
        query = "SELECT nome, email, senha FROM usuario;"
        usuario1 = {'nome': 'Gustavo Dias', 'email': 'gustavo.dias@hotmail.com', 'senha': 'gustavo123'}
        usuario2 = {'nome': 'Rafaela Barros', 'email': 'rafaela.barros@gmail.com', 'senha': 'rafaela123'}
        usuario3 = {'nome': 'Victoria Alves', 'email': 'victoria.alves@hotmail.com', 'senha': 'victoria123'}
        dados = self.base.selecionar(query)
        self.assertIn(usuario1, dados)
        self.assertIn(usuario2, dados)
        self.assertIn(usuario3, dados)

    def test_selecionar_params(self):
        query = "SELECT * FROM usuario WHERE nome = %s AND email = %s;"
        nome1 = 'Tânia Castro'
        email1 = 'tania.castro@hotmail.com'
        senha1 = 'tania123'
        parametros = [nome1, email1]
        dados1 = self.base.selecionar(query, parametros)
        self.assertEqual(senha1, dados1[0]['senha'])

        nome2 = 'Erick Gonçalves'
        email2 = 'erick.goncalves@hotmail.com'
        senha2 = 'erick123'
        parametros = [nome2, email2]
        dados2 = self.base.selecionar(query, parametros)
        self.assertEqual(senha2, dados2[0]['senha'])

    def test_selecionarUm(self):
        query = "SELECT * FROM usuario WHERE email LIKE '%@gmail.com' ORDER BY id;"
        senha = 'eduarda123'
        dados = self.base.selecionarUm(query)
        self.assertEqual(senha, dados['senha'])

    def test_selecionarUm_params(self):
        query = "SELECT * FROM usuario WHERE email = %s;"
        nome = 'Matilde Oliveira'
        email = 'matilde.oliveira@hotmail.com'
        parametros = [email]
        dados = self.base.selecionarUm(query, parametros)
        self.assertEqual(nome, dados['nome'])

    def test_executar(self):
        query = "INSERT INTO usuario (nome, email, senha) VALUES ('Evelyn Cruz', 'evelyn.cruz@gmail.com', 'evelyn123');"
        self.base.executar(query)

        query2 = "SELECT * FROM usuario WHERE nome = 'Evelyn Cruz';"
        dados = self.base.selecionarUm(query2)
        email = 'evelyn.cruz@gmail.com'
        self.assertEqual(email, dados['email'])

    def test_executar_params(self):
        query = "DELETE FROM usuario WHERE email = %s;"
        email = 'evelyn.cruz@gmail.com'
        parametros = [email]
        self.base.executar(query, parametros)

        query2 = "SELECT * FROM usuario WHERE senha = 'evelyn123';"
        dados = self.base.selecionarUm(query2)
        self.assertEqual(None, dados)

    def test_executar_returning(self):
        query = "INSERT INTO usuario (nome, email, senha) VALUES ('Carolina Dias', 'carolina.dias@gmail.com', 'carolina123') RETURNING id;"
        dados = self.base.executar(query)
        self.assertEqual(21, dados['id'])

    def test_fecharConexao(self):
        self.assertEqual(self.base.conexao.closed, 0)
        self.base.fecharConexao()
        self.assertEqual(self.base.conexao.closed, 1)

    def test_selecionar_reconectar(self):
        self.base.fecharConexao()
        dados = self.base.selecionar('SELECT 1 as resultado')[0]
        self.assertEqual(dados['resultado'], 1)

    def test_selecionarUm_reconectar(self):
        self.base.fecharConexao()
        dados = self.base.selecionarUm('SELECT 1 as resultado')
        self.assertEqual(dados['resultado'], 1)

    def test_executar_reconectar(self):
        self.base.fecharConexao()
        query = "INSERT INTO usuario (nome, email, senha) VALUES ('Giovanna Melo ', 'giovanna.melo@gmail.com', 'giovanna123') RETURNING id;"
        dados = self.base.executar(query)
        self.assertEqual(21, dados['id'])

    def test_reconectar_automaticamente_mesma_conexao(self):
        self.base.fecharConexao()
        query = """
        CREATE TEMPORARY TABLE setor (
            id INT GENERATED ALWAYS AS IDENTITY,
            nome VARCHAR(50) NOT NULL
        );
        """
        self.base.executar(query)
        query = "INSERT INTO setor (nome) VALUES ('TI');"
        self.base.executar(query)

        query = "SELECT * FROM setor;"
        dados = self.base.selecionarUm(query)

        self.assertEqual(dados['nome'], 'TI')

    def test_limit_automatico(self):
        query = "SELECT * FROM usuario ORDER BY 1 DESC;"
        dados = self.base.selecionarUm(query)
        self.assertEqual(dados['senha'], 'erick123')


if __name__ == '__main__':
    unittest.main()
