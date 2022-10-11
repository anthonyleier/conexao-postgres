import psycopg2
import psycopg2.extras


class Banco:
    def __init__(self, host=None, database=None, encoding=None):
        if host and database:
            self.abrirConexao(host, database, encoding)

    def abrirConexao(self, host=None, database=None, encoding=None):
        try:
            if host and database:
                self.host = host
                self.database = database

            self.encoding = 'UTF8' if not encoding else encoding

            self.conexao = psycopg2.connect(
                host=self.host,
                database=self.database,
                user="postgres",
                password="postgres")

            self.conexao.set_client_encoding(self.encoding)
            self.cursor = self.conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        except Exception as erro:
            print(f"Não foi possivel conectar ao banco de dados: {erro}")

    def selecionarSafe(self, query, parametros=None):
        self.cursor.execute(query, parametros)
        resultado = self.cursor.fetchall()
        return resultado

    def selecionar(self, query, parametros=None):
        try:
            return self.selecionarSafe(query, parametros)

        except psycopg2.InterfaceError as erro:
            print(f"A conexão foi fechada inexperadamente, tentando reabrir: {erro}")
            self.reconectar()
            return self.selecionarSafe(query, parametros)

        except Exception as erro:
            print(f"Erro inesperado no selecionar: {erro} - {self.database} - {query}")

    def selecionarUmSafe(self, query, parametros=None):
        self.cursor.execute(query, parametros)
        resultado = self.cursor.fetchone()
        return resultado

    def selecionarUm(self, query, parametros=None):
        try:
            return self.selecionarUmSafe(query, parametros)

        except psycopg2.InterfaceError as erro:
            print(f"A conexão foi fechada inexperadamente, tentando reabrir: {erro}")
            self.reconectar()
            return self.selecionarUmSafe(query, parametros)

        except Exception as erro:
            print(f"Erro inesperado no selecionarUm: {erro} - {self.database} - {query}")

    def executarSafe(self, query, parametros=None):
        self.cursor.execute(query, parametros)
        self.conexao.commit()
        retorno = "RETURNING"

        if retorno in query:
            return self.cursor.fetchone()

    def executar(self, query, parametros=None):
        try:
            return self.executarSafe(query, parametros)

        except psycopg2.InterfaceError as erro:
            print(f"A conexão foi fechada inexperadamente, tentando reabrir: {erro}")
            self.reconectar()
            return self.executarSafe(query, parametros)

        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro inesperado no executar: {erro} - {self.database} - {query}")

    def fecharConexao(self):
        try:
            self.cursor.close()
            self.conexao.close()

        except Exception as erro:
            print(f"Não foi possível fechar a conexão: {erro}")

    def reconectar(self):
        self.fecharConexao()
        self.abrirConexao()
