import psycopg2
import psycopg2.extras


class Banco:
    def __init__(self, host=None, database=None, encoding=None):
        if host and database:
            self.abrirConexao(host, database, encoding)

    def tentarReconectar(funcao):
        def decorator(*args, **kwargs):
            try:
                resultado = funcao(*args, **kwargs)
                return resultado

            except psycopg2.InterfaceError as erro:
                print(f"A conexão foi fechada inexperadamente, tentando reabrir: {erro}")
                args[0].reconectar()
                resultado = funcao(*args, **kwargs)
                return resultado

        return decorator

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

    @tentarReconectar
    def selecionar(self, query, parametros=None):
        try:
            self.cursor.execute(query, parametros)
            resultado = self.cursor.fetchall()
            return resultado

        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro inesperado no selecionar: {erro} - {self.database} - {query}")

    @tentarReconectar
    def selecionarUm(self, query, parametros=None):
        try:
            self.cursor.execute(query, parametros)
            resultado = self.cursor.fetchone()
            return resultado

        except Exception as erro:
            self.conexao.rollback()
            print(f"Erro inesperado no selecionarUm: {erro} - {self.database} - {query}")

    @tentarReconectar
    def executar(self, query, parametros=None):
        try:
            self.cursor.execute(query, parametros)
            self.conexao.commit()
            retorno = "RETURNING"

            if retorno in query:
                return self.cursor.fetchone()

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
