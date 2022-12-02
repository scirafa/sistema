#ctrl v do henry
#ta ok

import os
import sqlite3


class SQLite(object):
   def __init__(self, file):
       self.file = file

   def __enter__(self):
       self.conn = sqlite3.connect(self.file)
       self.conn.row_factory = sqlite3.Row
       return self.conn.cursor()

   def __exit__(self, type, value, traceback):
       self.conn.commit()
       self.conn.close()


def create_table(cursor: sqlite3.Cursor, table: str, fields: dict, other_data: list = None) -> None:
   """
   Função para criar tabelas.

   :param cursor: um cursor para o banco de dados
   :param table: Nome da tabela
   :param fields: Um dicionário onde a chave é o nome da coluna, e o valor o tipo/modificadores (e.g. primary key)
   :param other_data: Para definir foreign keys, ou outras configurações.
   """
   command = "CREATE TABLE %s (%s)" % (
       table,
       ','.join([k + ' ' + v for k, v in fields.items()] + (
           other_data if other_data is not None else []))
   )
   cursor.execute(command)


def insert_rows(cursor: sqlite3.Cursor, table: str, tuples: list) -> None:
   """
   Função para inserir tuplas numa tabela.

   :param cursor: um cursor para o banco de dados
   :param table: Nome da tabela
   :param tuples: Uma lista de dicionários. Para cada dicionário, a chave é o nome da coluna, e o valor, o valor da
                  tupla
   para aquela coluna.
   """
   for some_tuple in tuples:
       tuple_values = []
       for v in some_tuple.values():
           if isinstance(v, str):
               tuple_values += ['\'' + v + '\'']
           else:
               tuple_values += [str(v)]

       command = "INSERT INTO %s(%s) VALUES (%s)" % (
           table, ','.join(map(str, some_tuple.keys())), ','.join(tuple_values)
       )
       cursor.execute(command)


def select_rows(cursor: sqlite3.Cursor, clause: str) -> list:
   """
   Método para fazer seleção de tuplas de uma tabela. Aceita qualquer comando SQLITE.

   :param cursor: um cursor para o banco de dados
   :param clause: A cláusula de seleção (e.g. SELECT * FROM table)
   :return: Uma lista de tuplas
   """
   res = cursor.execute(clause)
   rows = []
   for row in res:  # type: sqlite3.Row
       rows += [tuple([row[k] for k in row.keys()])]

   return rows


def raw_execute(cursor: sqlite3.Cursor, clause: str) -> sqlite3.Cursor:
   """
   Executa qualquer comando SQLITE. Retorna o resultado.

   :param cursor: um cursor para o banco de dados
   :param clause: Qualquer cláusula SQLITE.
   :return: O resultado da execução da cláusula (se ela retorna um valor), ou None.
   """
   return cursor.execute(clause)


def remove_db(file: str) -> None:
   """
   Deleta o arquivo .db contido em file.

   :param file: Caminho para o banco .db.
   """
   try:
       os.remove(file)
   except FileNotFoundError:
       pass
