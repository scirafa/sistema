# ctrl v henry

from app.static.database import insert_rows, SQLite
import os


def main(path: str = '.', db_name: str = 'test.db') -> None:
   with SQLite(os.path.join(path, db_name)) as cursor:
       # TODO desenvolva seu código aqui
       print('Inserindo tuplas nas tabelas do banco de dados...')

       insert_rows(
           cursor,
           'ingredientes',
           [{'id_ingredientes': '1',
             'nome': 'Feijão Preto',
             'quantidades': '1kg',
             },
            {'id_ingredientes': '2',
             'nome': 'Água',
             'quantidades': 'até cobrir o feijão',
             },
            ])

       # RELAÇÕES

       insert_rows(
           cursor,
           'receitas_para_preparo',  # OK
           [{'id_preparo': 1, 'id_receita': 1},
            {'id_preparo': 2, 'id_receita': 1},
            {'id_preparo': 3, 'id_receita': 1},
            {'id_preparo': 4, 'id_receita': 1},
            {'id_preparo': 5, 'id_receita': 1},
            {'id_preparo': 6, 'id_receita': 1},
            {'id_preparo': 7, 'id_receita': 1},
            {'id_preparo': 8, 'id_receita': 1},
            # Nega Maluca
            {'id_preparo': 9, 'id_receita': 2},
            {'id_preparo': 10, 'id_receita': 2},
            {'id_preparo': 11, 'id_receita': 2},
            {'id_preparo': 12, 'id_receita': 2},
            {'id_preparo': 13, 'id_receita': 2},
            {'id_preparo': 14, 'id_receita': 2},
            {'id_preparo': 15, 'id_receita': 2},
            {'id_preparo': 16, 'id_receita': 2},
            {'id_preparo': 17, 'id_receita': 2},
            ])

       print('Tuplas inseridas com sucesso!')
       # TODO desenvolva seu código aqui


if __name__ == '__main__':
   main()
