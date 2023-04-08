"""
Dao - Data access object
Implementa a conexao com o
banco de dados.

"""
from database import Database
from entidades import Cliente, Produto

import csv;

class ClienteDao:

    def save(self, cliente):
        """
        Realiza o INSERT na tabela cliente
        """
        # obtem uma conexao com o banco:
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO cliente (
                nome, cpf, cep, email
            ) VALUES (?, ?, ?, ?)
            """,
            (
                cliente.nome,
                cliente.cpf,
                cliente.cep,
                cliente.email,
            )
        )
        conn.commit()
        conn.close()


    def update(self, cliente):
        """
        Realiza UPDATE do cliente
        """
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE cliente SET nome = ?, cpf = ?, cep = ?, email = ?
            WHERE id = ?
            """,
            (
                cliente.nome,
                cliente.cpf,
                cliente.cep,
                cliente.email,
                cliente.id
            )
        )
        conn.commit()
        conn.close()

    def delete(self, id):
        """
        Remove um cliente de acordo com o id fornecido
        """
        conn = Database.get_connection()
        conn.execute(
            # Query
            # Hard Delete (cuidado!)
            f"""
            DELETE FROM cliente WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()


    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute("""
        SELECT id, nome, cpf, cep, email, data_cadastro FROM cliente
        """
        )
        # executa o SELECT
        results = res.fetchall()
        # results eh um vetor

        # versao 1
        results = [
            {
                "id": cliente[0],
                "nome": cliente[1],
                "cpf": cliente[2],
                "cep": cliente[3],
                "email": cliente[4],
                "data_cadastro": cliente[5],
            } for cliente in results]

        conn.close()
        return results


    def get_cliente(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, email, cpf, cep, data_cadastro  FROM cliente WHERE id = {id}
        """
        )
        row = res.fetchone()

        # cria um objeto cliente para armazenar resultado do SELECT:
        cliente = Cliente(
            row[1],
            row[2],
            id = row[0],
            cpf = row[3],
            cep = row[4],
            data_cadastro = row[5]
        )
        conn.close()
        return cliente

        #Buscando cliente de acordo com o que é inserido na input
    def get_busca(self, nome):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT * FROM cliente WHERE nome LIKE '%{nome}%'
        """
        )
        resultado = res.fetchall()
        # resultado --> vetor que vai mostrar todas as informações em ordem.
        resultado = [
            {
            "id": cliente[0],
            "nome": cliente[1],
            "email": cliente[2],
            "cep": cliente[3],
            "cpf": cliente [4]
            } for cliente in resultado]        
        conn.close()
        return resultado


#PRODUTO

class ProdutoDao:
    # define cada funcionalidade do CRUD
    # CREATE

    def save(self, produto):
        """
        Realiza o INSERT na tabela produto
        """
        # obtem uma conexao com o banco:
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO produto (
                nome, preco, marca
            ) VALUES (?, ?, ?)
            """,
            (
                produto.nome,
                produto.preco,
                produto.marca,
            )
        )
        conn.commit()
        conn.close()


    def update(self, produto):
        """
        Realiza UPDATE do produto
        """
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE produto SET nome = ?, preco = ?, marca = ?
            WHERE id = ?
            """,
            (
                produto.nome,
                produto.preco,
                produto.marca,
                produto.id
            )
        )
        conn.commit()
        conn.close()

    def delete(self, id):
        """
        Remove um produto de acordo com o id fornecido
        """
        conn = Database.get_connection()
        conn.execute(
            # Query
            # Hard Delete (cuidado!)
            f"""
            DELETE FROM produto WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()


    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute("""
        SELECT id, nome, preco, marca, added FROM produto
        """
        )
        # executa o SELECT
        results = res.fetchall()
        # results eh um vetor

        # versao 1
        results = [
            {
                "id": produto[0],
                "nome": produto[1],
                "preco": produto[2],
                "marca": produto[3],
                "added": produto[4],
            } for produto in results]

        conn.close()
        return results


    def get_produto(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, preco, marca, added  FROM produto WHERE id = {id}
        """
        )
        row = res.fetchone()

        # cria um objeto produto para armazenar resultado do SELECT:
        produto = Produto(
            row[1],
            row[2],
            id = row[0],
            marca = row[3],
            added = row[4]

        )
        conn.close()
        return produto

    # Pegando produtos
    def get_produto_lista(self):

        # 1. abrir o arquivo
        with open('lista-500.csv', encoding='utf8') as arquivo_referencia:
            # 2. ler a tabela
            tabela = csv.reader(arquivo_referencia, delimiter = ',')
            tabela.__next__()
            conn = Database.get_connection()
            # 3. navegar pela tabela
            for index,l in enumerate(tabela):
                    conn.execute(
                        f"""
                        INSERT INTO produto (
                            nome,marca,preco
                        ) VALUES (?, ?, ?)
                        """,
                        (
                            l[1],
                            l[2],
                            l[3]
                        )
                    )
            conn.commit()
            conn.close()
        return  1


#Buscando produto de acordo com o que é inserido na input
    def get_busca(self, nome):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT * FROM produto WHERE nome or marca LIKE '%{nome}%'
        """
        )
        results = res.fetchall()
        # results --> vetor que vai mostrar todas as informações em ordem.
        results = [
            {
            "id": produto[0],
            "nome": produto[1],
            "preco": produto[2],
            "marca": produto[3]
            } for produto in results]        
        conn.close()
        return results



