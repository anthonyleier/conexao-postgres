# conexao-postgres

Este é um código em Python que cria uma classe Banco para se conectar a um banco de dados PostgreSQL usando a biblioteca psycopg2. A classe possui métodos para selecionar dados (selecionar e selecionarUm) e executar comandos (executar) no banco de dados, além de métodos para abrir e fechar a conexão com o banco (abrirConexao e fecharConexao, respectivamente). Também há um decorador tentarReconectar que trata erros de conexão e tenta reconectar automaticamente.

# Selecionar
Para usar esta classe, é preciso instalar a biblioteca psycopg2 e criar uma instância da classe passando os parâmetros de conexão com o banco de dados (host, nome do banco de dados, etc.). Exemplo:

```python
import psycopg2
from Banco import Banco

banco = Banco(host='localhost', database='meubanco')

resultado = banco.selecionar("SELECT * FROM minha_tabela")
print(resultado)

banco.fecharConexao()
```

Este código criaria uma instância da classe Banco conectada ao banco de dados meubanco no host localhost. Em seguida, executa uma consulta para selecionar todos os registros da tabela minha_tabela e imprime o resultado. Finalmente, fecha a conexão com o banco.

# Selecionar Um
A função selecionarUm é utilizada para executar uma query que espera um único resultado como resposta e retorna apenas uma única linha. Já a função selecionar é utilizada para executar uma query que retorna múltiplas linhas.

Um exemplo de uso da função selecionarUm seria para buscar os dados de um usuário a partir do seu ID. Suponha que temos uma tabela usuarios com os campos id, nome e email. Para buscar os dados de um usuário a partir de seu ID, poderíamos fazer:

```python
banco = Banco(host='localhost', database='meubanco')

usuario_id = 1
query = "SELECT * FROM usuarios WHERE id = %s"

usuario = banco.selecionarUm(query, (usuario_id,))
print(usuario)
```


# Executar
Nesse exemplo, estamos criando uma instância da classe Banco, passando os parâmetros necessários para conectar ao banco de dados. Depois, criamos a variável query com o comando SQL que queremos executar, que é uma inserção na tabela clientes. Como a query utiliza placeholders %s, também precisamos criar a variável parametros, que contém os valores que serão substituídos nesses placeholders.

Em seguida, chamamos a função executar do objeto banco, passando a query e os parâmetros como argumentos. Se a query contiver um RETURNING, o método irá retornar o resultado da query, que nesse caso é o id do novo cliente inserido na tabela.

Por fim, imprimimos o id do novo cliente para confirmar que a inserção ocorreu com sucesso.

```python
banco = Banco(host="localhost", database="meu_banco")
query = "INSERT INTO clientes (nome, idade) VALUES (%s, %s) RETURNING id;"
parametros = ("João da Silva", 35)

novo_cliente_id = banco.executar(query, parametros)

print(f"Novo cliente inserido com id: {novo_cliente_id}")
```

# Testes Automatizados
Para executar os testes automatizados com Python, podemos utilizar o seguinte comando no terminal: python testes.py. Este comando irá rodar o arquivo testes.py que contém os testes automatizados.

``` python testes.py ```

Os testes automatizados são uma parte fundamental do desenvolvimento de software. Eles são utilizados para garantir que o código esteja funcionando corretamente, evitando que erros sejam lançados em produção e que possam prejudicar a experiência do usuário.

Os testes foram escritos utilizando a biblioteca unittest. A biblioteca unittest é uma das bibliotecas padrão do Python e é utilizada para criar testes automatizados. Ela fornece uma série de funcionalidades para facilitar a criação e execução de testes. Com a biblioteca unittest, é possível criar testes de unidade, testes de integração e testes funcionais. Além disso, ela permite criar suítes de testes e relatórios de testes.