#ctrl v henry

#CRIAR AS TABELAS DO BANCO DE DADOS
#E CRIAR OS RELACIONAMENTOS (chave primária, chave estrangeira, etc)

import os
from app.static.database import remove_db, SQLite, create_table

def main(path: str = '.', db_name: str = 'test.db') -> None:
print('Removendo antigo banco de dados (se ele existir)')
remove_db(os.path.join(path, db_name))
print('Banco de dados antigo removido com sucesso!')

with SQLite(os.path.join(path, db_name)) as cursor:
    print('Criando tabelas do banco de dados...')

    # TODO desenvolva seu código aqui

    create_table(
        cursor,
        'masterchefs',
        {'id_masterchef': 'INTEGER AUTO_INCREMENT PRIMARY KEY',
         'nome': 'text NOT NULL',
         'email': 'text NOT NULL',}
    )

            #RELAÇÕES

    create_table(
        cursor,
        # 'um_para_dois',
        # {'id_dois': 'INTEGER NOT NULL', 'id_um': 'INTEGER NOT NULL'},
        # ['PRIMARY KEY(id_dois, id_um)', 'FOREIGN KEY(id_dois) REFERENCES dois(id)',
        # 'FOREIGN KEY(id_um) REFERENCES um(id)']
        'receitas_para_ingredientes',
        {'id_ingredientes': 'INTEGER NOT NULL', 'id_receita': 'INTEGER NOT NULL'},
        ['PRIMARY KEY(id_receita, id_ingredientes)', 'FOREIGN KEY(id_ingredientes) REFERENCES ingredientes(id_ingredientes)',
        'FOREIGN KEY(id_receita) REFERENCES receitas(id_receita)']
    )


    print('Tabelas do banco de dados criadas com sucesso!')
    # TODO desenvolva seu código aqui

if __name__ == '__main__':
main()
#O conteúdo dentro da estrutura if__name__==”main” só vai ser executado quando você rodar o código do arquivo, caso contrário o que tem dentro dessa estrutura não será executado
