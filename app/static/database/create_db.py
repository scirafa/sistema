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
        'login',
        {'cpf_us': 'INTEGER PRIMARY KEY',
         'email_us': 'text NOT NULL',
         'nome_us': 'text NOT NULL',
         'fone_us': 'bigint NOT NULL',
         'cnpj_us': 'bigint NOT NULL',
         'end_us': 'text NOT NULL',}
    )

    create_table(
        cursor,
        'receita_f',
        {'id_mes_r': 'INTEGER AUTO_INCREMENT PRIMARY KEY',
         'entrada_r': 'float NOT NULL',
         'saida_r': 'float NOT NULL',
         'nome_animal_r': 'text NOT NULL',
         'nome_servico_r': 'text NOT NULL',
         'valor_r': 'float NOT NULL',
         'valor_pg_r': 'float NOT NULL',
         'forma_pg_r': 'text NOT NULL',}
    )

    create_table(
        cursor,
        'despesa_f',
        {'id_mes_d': 'INTEGER AUTO_INCREMENT PRIMARY KEY',
         'nome_despesa_d': 'text NOT NULL',
         'tipo_despesa_d': 'text NOT NULL',
         'valor_d': 'float NOT NULL',
         'forma_pg_d': 'text NOT NULL', }
    )

    create_table(
        cursor,
        'lucro_f',
        {'id_mes_l': 'INTEGER AUTO_INCREMENT PRIMARY KEY',
         'receita_l': 'float NOT NULL',
         'despesa_l': 'float NOT NULL',
         'saida_l': 'float NOT NULL',
         'lucro_l': 'float NOT NULL',}
    )

    create_table(
        cursor,
        'infos_animais_a',
        {'id_animal_a': 'INTEGER AUTO_INCREMENT PRIMARY KEY',
         'nome_animal_a': 'text NOT NULL',
         'raca_animal_a': 'text NOT NULL',
         'sexo_animal_a': 'text NOT NULL',
         'idade_animal_a': 'text NOT NULL',
         'castrado_a': 'boolean NOT NULL',
         'comport_animal_a': 'text NOT NULL',
         'gatilhos_animal_a': 'text',
         'nome_dono_a': 'text NOT NULL',
         'end_dono_a': 'text NOT NULL',
         'fone_dono_a': 'bigint NOT NULL',}
    )

    create_table(
        cursor,
        'infos_animais_s',
        {'id_animal_s': 'INTEGER AUTO_INCREMENT PRIMARY KEY',
         'nome_animal_s': 'text NOT NULL',
         'prob_s_psico': 'text',
         'vet_nome': 'text',
         'vet_clinica': 'text',
         'vet_fone': 'bigint',
         'alimentacao_s': 'text NOT NULL',
         'medicacao_s': 'text',
         'aviso_vacinas': 'text NOT NULL',}
    )


            #RELAÇÕES

    create_table(
        cursor,
        # 'um_para_dois',
        # {'id_dois': 'INTEGER NOT NULL', 'id_um': 'INTEGER NOT NULL'},
        # ['PRIMARY KEY(id_dois, id_um)', 'FOREIGN KEY(id_dois) REFERENCES dois(id)',
        # 'FOREIGN KEY(id_um) REFERENCES um(id)']
        'receita_f_para_lucro_f',
        {'id_mes_l': 'INTEGER NOT NULL', 'id_mes_r': 'INTEGER NOT NULL'},
        ['PRIMARY KEY(id_mes_l, id_mes_r)', 'FOREIGN KEY(id_mes_l) REFERENCES lucro_f(id_mes_l)',
        'FOREIGN KEY(id_mes_r) REFERENCES receita_f(id_mes_r)']
    )

    create_table(
        cursor,
        # 'um_para_dois',
        # {'id_dois': 'INTEGER NOT NULL', 'id_um': 'INTEGER NOT NULL'},
        # ['PRIMARY KEY(id_dois, id_um)', 'FOREIGN KEY(id_dois) REFERENCES dois(id)',
        # 'FOREIGN KEY(id_um) REFERENCES um(id)']
        'despesa_f_para_lucro_f',
        {'id_mes_l': 'INTEGER NOT NULL', 'id_mes_d': 'INTEGER NOT NULL'},
        ['PRIMARY KEY(id_mes_l, id_mes_d)', 'FOREIGN KEY(id_mes_l) REFERENCES lucro_f(id_mes_l)',
         'FOREIGN KEY(id_mes_d) REFERENCES despesa_f(id_mes_d)']
    )

    create_table(
        cursor,
        # 'um_para_dois',
        # {'id_dois': 'INTEGER NOT NULL', 'id_um': 'INTEGER NOT NULL'},
        # ['PRIMARY KEY(id_dois, id_um)', 'FOREIGN KEY(id_dois) REFERENCES dois(id)',
        # 'FOREIGN KEY(id_um) REFERENCES um(id)']
        'infos_animais_a_para_infos_animais_s',
        {'id_animal_s': 'INTEGER NOT NULL', 'id_animal_a': 'INTEGER NOT NULL'},
        ['PRIMARY KEY(id_animal_s, id_animal_a)', 'FOREIGN KEY(id_animal_s) REFERENCES infos_animais_s(id_animal_s)',
         'FOREIGN KEY(id_animal_a) REFERENCES infos_animais_a(id_animal_a)']
    )


    print('Tabelas do banco de dados criadas com sucesso!')
    # TODO desenvolva seu código aqui

if __name__ == '__main__':
main()
#O conteúdo dentro da estrutura if__name__==”main” só vai ser executado quando você rodar o código do arquivo, caso contrário o que tem dentro dessa estrutura não será executado
