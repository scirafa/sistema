# ctrl v henry

from app.static.database import insert_rows, SQLite
import os


def main(path: str = '.', db_name: str = 'test.db') -> None:
   with SQLite(os.path.join(path, db_name)) as cursor:
       # TODO desenvolva seu código aqui
       print('Inserindo tuplas nas tabelas do banco de dados...')

       insert_rows(
           cursor,
           'infos_animais_a',
           [{'id_animal_a': '1',
             'nome_animal_a': 'Luna',
             'raca_animal_a': 'srd',
             'sexo_animal_a': 'fêmea',
             'idade_animal_a': '3',
             'castrado_a': 's',
             'comport_animal_a': 'agitada, adora brincar',
             'gatilhos_animal_a': 'gatos',
             'nome_dono_a': 'Nicole Grazzioli',
             'end_dono_a': 'rua 10, num 200',
             'fone_dono_a': '01555999570938',
             },
            {'id_animal_a': '2',
             'nome_animal_a': 'Bob',
             'raca_animal_a': 'spitz alemão',
             'sexo_animal_a': 'macho',
             'idade_animal_a': '6',
             'castrado_a': 's',
             'comport_animal_a': 'calmo, pouca energia',
             'gatilhos_animal_a': 'nenhum',
             'nome_dono_a': 'Carlos Silva',
             'end_dono_a': 'rua Flor de Liz, num 569',
             'fone_dono_a': '01555999648257',
            ])

       # RELAÇÕES


       print('Tuplas inseridas com sucesso!')
       # TODO desenvolva seu código aqui


if __name__ == '__main__':
   main()
