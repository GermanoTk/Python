import sqlite3
from datetime import datetime

class Data_base:
    def __init__(self, name = 'system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

####################################### TABLE CARREGAMENTO DEMARCHI

    def create_table_demarchi(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Demarchi(
                       
            DATA_HORA_LANCAMENTO TEXT,
            NUMERO_TRANSPORTE TEXT NOT NULL,
            NUMERO_TRANSPORTE2 TEXT,
            NUMERO_TRANSPORTE3 TEXT,
            NUMERO_TRANSPORTE4 TEXT,
            NUMERO_TRANSPORTE5 TEXT,
            DATA_HORA_PLANEJAMENTO TEXT,
            DATA_HORA_PLANEJAMENTO2 TEXT,
            DATA_HORA_PLANEJAMENTO3 TEXT,
            DATA_HORA_PLANEJAMENTO4 TEXT,
            DATA_HORA_PLANEJAMENTO5 TEXT,
            PESO_BRUTO TEXT,
            PESO_BRUTO2 TEXT,
            PESO_BRUTO3 TEXT,
            PESO_BRUTO4 TEXT,
            PESO_BRUTO5 TEXT,
            DENOMINACAO TEXT,
            DENOMINACAO2 TEXT,
            DENOMINACAO3 TEXT,
            DENOMINACAO4 TEXT,
            DENOMINACAO5 TEXT,
            CLIENTE TEXT,
            CLIENTE2 TEXT,
            CLIENTE3 TEXT,
            CLIENTE4 TEXT,
            CLIENTE5 TEXT,
            DESTINO TEXT,
            DESTINO2 TEXT,
            DESTINO3 TEXT,
            DESTINO4 TEXT,
            DESTINO5 TEXT,
            COD_PROCES TEXT,
            COD_PROCES2 TEXT,
            COD_PROCES3 TEXT,
            COD_PROCES4 TEXT,
            COD_PROCES5 TEXT,
            CAVALO TEXT,
            CARRETA TEXT,
            MOTORISTA TEXT,
            CPF TEXT,
                       
            PRIMARY KEY(NUMERO_TRANSPORTE)
            );

        """)

    def register_demarchi(self, fullDataSet):
        campos_tabela = ('DATA_HORA_LANCAMENTO', 'NUMERO_TRANSPORTE', 'NUMERO_TRANSPORTE2', 'NUMERO_TRANSPORTE3', 'NUMERO_TRANSPORTE4', 'NUMERO_TRANSPORTE5',
                         'DATA_HORA_PLANEJAMENTO', 'DATA_HORA_PLANEJAMENTO2', 'DATA_HORA_PLANEJAMENTO3', 'DATA_HORA_PLANEJAMENTO4',
                         'DATA_HORA_PLANEJAMENTO5', 'PESO_BRUTO', 'PESO_BRUTO2', 'PESO_BRUTO3', 'PESO_BRUTO4', 'PESO_BRUTO5',
                         'DENOMINACAO', 'DENOMINACAO2', 'DENOMINACAO3', 'DENOMINACAO4', 'DENOMINACAO5', 'CLIENTE', 'CLIENTE2', 'CLIENTE3',
                         'CLIENTE4', 'CLIENTE5', 'DESTINO', 'DESTINO2', 'DESTINO3', 'DESTINO4', 'DESTINO5', 'COD_PROCES', 'COD_PROCES2',
                         'COD_PROCES3', 'COD_PROCES4', 'COD_PROCES5', 'CAVALO', 'CARRETA', 'MOTORISTA', 'CPF')

        qntd = ",".join(["?" for _ in range(len(campos_tabela))])
        cursor = self.connection.cursor()

        try:
            data_hora_lancamento = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            fullDataSet = [data_hora_lancamento] + list(fullDataSet)

            for campo in ['NUMERO_TRANSPORTE', 'DATA_HORA_PLANEJAMENTO', 'PESO_BRUTO', 'DENOMINACAO', 'CLIENTE', 'DESTINO', 'COD_PROCES']:
                if not fullDataSet[campos_tabela.index(campo)]:
                    return f"Error: {campo} não pode ser vazio!"

            cursor.execute(f"""INSERT INTO Demarchi {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            
            self.connection.commit()
            return "OK"
        except:
            return "Error"
   
    def select_all_demarchi(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT NUMERO_TRANSPORTE, NUMERO_TRANSPORTE2, NUMERO_TRANSPORTE3, NUMERO_TRANSPORTE4, NUMERO_TRANSPORTE5, "
                        "DATA_HORA_PLANEJAMENTO, DATA_HORA_PLANEJAMENTO2, DATA_HORA_PLANEJAMENTO3, DATA_HORA_PLANEJAMENTO4, DATA_HORA_PLANEJAMENTO5, "
                        "PESO_BRUTO, PESO_BRUTO2, PESO_BRUTO3, PESO_BRUTO4, PESO_BRUTO5, "
                        "DENOMINACAO, DENOMINACAO2, DENOMINACAO3, DENOMINACAO4, DENOMINACAO5, "
                        "CLIENTE, CLIENTE2, CLIENTE3, CLIENTE4, CLIENTE5, "
                        "DESTINO, DESTINO2, DESTINO3, DESTINO4, DESTINO5, "
                        "COD_PROCES, COD_PROCES2, COD_PROCES3, COD_PROCES4, COD_PROCES5, "
                        "CAVALO, CARRETA, MOTORISTA, CPF FROM Demarchi "
                        "WHERE (CAVALO IS NULL OR CAVALO = '') AND "
                        "(CARRETA IS NULL OR CARRETA = '') AND "
                        "(MOTORISTA IS NULL OR MOTORISTA = '') AND "
                        "(CPF IS NULL OR CPF = '')")
            dadosdemarchi = cursor.fetchall()
            return dadosdemarchi
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
        
    def select_all_demarchi2(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT NUMERO_TRANSPORTE, NUMERO_TRANSPORTE2, NUMERO_TRANSPORTE3, NUMERO_TRANSPORTE4, NUMERO_TRANSPORTE5, "
                        "DATA_HORA_PLANEJAMENTO, DATA_HORA_PLANEJAMENTO2, DATA_HORA_PLANEJAMENTO3, DATA_HORA_PLANEJAMENTO4, DATA_HORA_PLANEJAMENTO5, "
                        "PESO_BRUTO, PESO_BRUTO2, PESO_BRUTO3, PESO_BRUTO4, PESO_BRUTO5, "
                        "DENOMINACAO, DENOMINACAO2, DENOMINACAO3, DENOMINACAO4, DENOMINACAO5, "
                        "CLIENTE, CLIENTE2, CLIENTE3, CLIENTE4, CLIENTE5, "
                        "DESTINO, DESTINO2, DESTINO3, DESTINO4, DESTINO5, "
                        "COD_PROCES, COD_PROCES2, COD_PROCES3, COD_PROCES4, COD_PROCES5, "
                        "CAVALO, CARRETA, MOTORISTA, CPF FROM Demarchi "
                        )
            dadosdemarchi = cursor.fetchall()
            return dadosdemarchi
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

    def delete_demarchi(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Demarchi WHERE NUMERO_TRANSPORTE = '{id}' ")
            self.connection.commit()
            return "Dados Excluídos com Sucesso!"
        except:
            return "Erro ao excluir os Dados!"

    def update_demarchi(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Demarchi set
           
            NUMERO_TRANSPORTE = '{fullDataSet[0]}',
            NUMERO_TRANSPORTE2 = '{fullDataSet[1]}',
            NUMERO_TRANSPORTE3 = '{fullDataSet[2]}',
            NUMERO_TRANSPORTE4 = '{fullDataSet[3]}',
            NUMERO_TRANSPORTE5 = '{fullDataSet[4]}',
            DATA_HORA_PLANEJAMENTO = '{fullDataSet[5]}',
            DATA_HORA_PLANEJAMENTO2 = '{fullDataSet[6]}',
            DATA_HORA_PLANEJAMENTO3 = '{fullDataSet[7]}',
            DATA_HORA_PLANEJAMENTO4 = '{fullDataSet[8]}',
            DATA_HORA_PLANEJAMENTO5 = '{fullDataSet[9]}',
            PESO_BRUTO = '{fullDataSet[10]}',
            PESO_BRUTO2 = '{fullDataSet[11]}',
            PESO_BRUTO3 = '{fullDataSet[12]}',
            PESO_BRUTO4 = '{fullDataSet[13]}',
            PESO_BRUTO5 = '{fullDataSet[14]}',
            DENOMINACAO = '{fullDataSet[15]}',
            DENOMINACAO2 = '{fullDataSet[16]}',
            DENOMINACAO3 = '{fullDataSet[17]}',
            DENOMINACAO4 = '{fullDataSet[18]}',
            DENOMINACAO5 = '{fullDataSet[19]}',
            CLIENTE = '{fullDataSet[20]}',
            CLIENTE2 = '{fullDataSet[21]}',
            CLIENTE3 = '{fullDataSet[22]}',
            CLIENTE4 = '{fullDataSet[23]}',
            CLIENTE5 = '{fullDataSet[24]}',
            DESTINO = '{fullDataSet[25]}',
            DESTINO2 = '{fullDataSet[26]}',
            DESTINO3 = '{fullDataSet[27]}',
            DESTINO4 = '{fullDataSet[28]}',
            DESTINO5 = '{fullDataSet[29]}',
            COD_PROCES = '{fullDataSet[30]}',
            COD_PROCES2 = '{fullDataSet[31]}',
            COD_PROCES3 = '{fullDataSet[32]}',
            COD_PROCES4 = '{fullDataSet[33]}',
            COD_PROCES5 = '{fullDataSet[34]}',
            CAVALO = '{fullDataSet[35]}',
            CARRETA = '{fullDataSet[36]}',
            MOTORISTA = '{fullDataSet[37]}',
            CPF = '{fullDataSet[38]}'
            
            WHERE NUMERO_TRANSPORTE = '{fullDataSet[0]}'""")
        
        self.connection.commit()

####################################### TABLE CARREGAMENTO SELAFORT
    
    def create_table_selafort(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Selafort(
            
            DATA_HORA_LANCAMENTO TEXT,
            NUMERO_TRANSPORTE TEXT NOT NULL,
            NUMERO_TRANSPORTE2 TEXT,
            NUMERO_TRANSPORTE3 TEXT,
            NUMERO_TRANSPORTE4 TEXT,
            NUMERO_TRANSPORTE5 TEXT,
            DATA_HORA_PLANEJAMENTO TEXT,
            DATA_HORA_PLANEJAMENTO2 TEXT,
            DATA_HORA_PLANEJAMENTO3 TEXT,
            DATA_HORA_PLANEJAMENTO4 TEXT,
            DATA_HORA_PLANEJAMENTO5 TEXT,
            PESO_BRUTO TEXT,
            PESO_BRUTO2 TEXT,
            PESO_BRUTO3 TEXT,
            PESO_BRUTO4 TEXT,
            PESO_BRUTO5 TEXT,
            DENOMINACAO TEXT,
            DENOMINACAO2 TEXT,
            DENOMINACAO3 TEXT,
            DENOMINACAO4 TEXT,
            DENOMINACAO5 TEXT,
            CLIENTE TEXT,
            CLIENTE2 TEXT,
            CLIENTE3 TEXT,
            CLIENTE4 TEXT,
            CLIENTE5 TEXT,
            DESTINO TEXT,
            DESTINO2 TEXT,
            DESTINO3 TEXT,
            DESTINO4 TEXT,
            DESTINO5 TEXT,
            COD_PROCES TEXT,
            COD_PROCES2 TEXT,
            COD_PROCES3 TEXT,
            COD_PROCES4 TEXT,
            COD_PROCES5 TEXT,
            CAVALO TEXT,
            CARRETA TEXT,
            MOTORISTA TEXT,
            CPF TEXT,
                       
            PRIMARY KEY(NUMERO_TRANSPORTE)
            );

        """)

    def register_selafort(self, fullDataSet):
        campos_tabela = ('DATA_HORA_LANCAMENTO', 'NUMERO_TRANSPORTE', 'NUMERO_TRANSPORTE2', 'NUMERO_TRANSPORTE3', 'NUMERO_TRANSPORTE4', 'NUMERO_TRANSPORTE5',
                         'DATA_HORA_PLANEJAMENTO', 'DATA_HORA_PLANEJAMENTO2', 'DATA_HORA_PLANEJAMENTO3', 'DATA_HORA_PLANEJAMENTO4',
                         'DATA_HORA_PLANEJAMENTO5', 'PESO_BRUTO', 'PESO_BRUTO2', 'PESO_BRUTO3', 'PESO_BRUTO4', 'PESO_BRUTO5',
                         'DENOMINACAO', 'DENOMINACAO2', 'DENOMINACAO3', 'DENOMINACAO4', 'DENOMINACAO5', 'CLIENTE', 'CLIENTE2', 'CLIENTE3',
                         'CLIENTE4', 'CLIENTE5', 'DESTINO', 'DESTINO2', 'DESTINO3', 'DESTINO4', 'DESTINO5', 'COD_PROCES', 'COD_PROCES2',
                         'COD_PROCES3', 'COD_PROCES4', 'COD_PROCES5', 'CAVALO', 'CARRETA', 'MOTORISTA', 'CPF')

        qntd = ",".join(["?" for _ in range(len(campos_tabela))])
        cursor = self.connection.cursor()

        try:
            data_hora_lancamento = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            fullDataSet = [data_hora_lancamento] + list(fullDataSet)

            for campo in ['NUMERO_TRANSPORTE', 'DATA_HORA_PLANEJAMENTO', 'PESO_BRUTO', 'DENOMINACAO', 'CLIENTE', 'DESTINO', 'COD_PROCES']:
                if not fullDataSet[campos_tabela.index(campo)]:
                    return f"Error: {campo} não pode ser vazio!"

            cursor.execute(f"""INSERT INTO Selafort {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            
            self.connection.commit()
            return "OK"
        except:
            return "Error"

    def select_all_selafort(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT NUMERO_TRANSPORTE, NUMERO_TRANSPORTE2, NUMERO_TRANSPORTE3, NUMERO_TRANSPORTE4, NUMERO_TRANSPORTE5, "
                        "DATA_HORA_PLANEJAMENTO, DATA_HORA_PLANEJAMENTO2, DATA_HORA_PLANEJAMENTO3, DATA_HORA_PLANEJAMENTO4, DATA_HORA_PLANEJAMENTO5, "
                        "PESO_BRUTO, PESO_BRUTO2, PESO_BRUTO3, PESO_BRUTO4, PESO_BRUTO5, "
                        "DENOMINACAO, DENOMINACAO2, DENOMINACAO3, DENOMINACAO4, DENOMINACAO5, "
                        "CLIENTE, CLIENTE2, CLIENTE3, CLIENTE4, CLIENTE5, "
                        "DESTINO, DESTINO2, DESTINO3, DESTINO4, DESTINO5, "
                        "COD_PROCES, COD_PROCES2, COD_PROCES3, COD_PROCES4, COD_PROCES5, "
                        "CAVALO, CARRETA, MOTORISTA, CPF FROM Selafort "
                        "WHERE (CAVALO IS NULL OR CAVALO = '') AND "
                        "(CARRETA IS NULL OR CARRETA = '') AND "
                        "(MOTORISTA IS NULL OR MOTORISTA = '') AND "
                        "(CPF IS NULL OR CPF = '')")
            dadosselafort = cursor.fetchall()
            return dadosselafort
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

    def select_all_selafort2(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT NUMERO_TRANSPORTE, NUMERO_TRANSPORTE2, NUMERO_TRANSPORTE3, NUMERO_TRANSPORTE4, NUMERO_TRANSPORTE5, "
                        "DATA_HORA_PLANEJAMENTO, DATA_HORA_PLANEJAMENTO2, DATA_HORA_PLANEJAMENTO3, DATA_HORA_PLANEJAMENTO4, DATA_HORA_PLANEJAMENTO5, "
                        "PESO_BRUTO, PESO_BRUTO2, PESO_BRUTO3, PESO_BRUTO4, PESO_BRUTO5, "
                        "DENOMINACAO, DENOMINACAO2, DENOMINACAO3, DENOMINACAO4, DENOMINACAO5, "
                        "CLIENTE, CLIENTE2, CLIENTE3, CLIENTE4, CLIENTE5, "
                        "DESTINO, DESTINO2, DESTINO3, DESTINO4, DESTINO5, "
                        "COD_PROCES, COD_PROCES2, COD_PROCES3, COD_PROCES4, COD_PROCES5, "
                        "CAVALO, CARRETA, MOTORISTA, CPF FROM Selafort "
                        )
            dadosselafort = cursor.fetchall()
            return dadosselafort
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

    def delete_selafort(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Selafort WHERE NUMERO_TRANSPORTE = '{id}' ")
            self.connection.commit()
            return "Dados Excluídos com Sucesso!"
        except:
            return "Erro ao excluir os Dados!"

    def update_selafort(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Selafort set
           
            NUMERO_TRANSPORTE = '{fullDataSet[0]}',
            NUMERO_TRANSPORTE2 = '{fullDataSet[1]}',
            NUMERO_TRANSPORTE3 = '{fullDataSet[2]}',
            NUMERO_TRANSPORTE4 = '{fullDataSet[3]}',
            NUMERO_TRANSPORTE5 = '{fullDataSet[4]}',
            DATA_HORA_PLANEJAMENTO = '{fullDataSet[5]}',
            DATA_HORA_PLANEJAMENTO2 = '{fullDataSet[6]}',
            DATA_HORA_PLANEJAMENTO3 = '{fullDataSet[7]}',
            DATA_HORA_PLANEJAMENTO4 = '{fullDataSet[8]}',
            DATA_HORA_PLANEJAMENTO5 = '{fullDataSet[9]}',
            PESO_BRUTO = '{fullDataSet[10]}',
            PESO_BRUTO2 = '{fullDataSet[11]}',
            PESO_BRUTO3 = '{fullDataSet[12]}',
            PESO_BRUTO4 = '{fullDataSet[13]}',
            PESO_BRUTO5 = '{fullDataSet[14]}',
            DENOMINACAO = '{fullDataSet[15]}',
            DENOMINACAO2 = '{fullDataSet[16]}',
            DENOMINACAO3 = '{fullDataSet[17]}',
            DENOMINACAO4 = '{fullDataSet[18]}',
            DENOMINACAO5 = '{fullDataSet[19]}',
            CLIENTE = '{fullDataSet[20]}',
            CLIENTE2 = '{fullDataSet[21]}',
            CLIENTE3 = '{fullDataSet[22]}',
            CLIENTE4 = '{fullDataSet[23]}',
            CLIENTE5 = '{fullDataSet[24]}',
            DESTINO = '{fullDataSet[25]}',
            DESTINO2 = '{fullDataSet[26]}',
            DESTINO3 = '{fullDataSet[27]}',
            DESTINO4 = '{fullDataSet[28]}',
            DESTINO5 = '{fullDataSet[29]}',
            COD_PROCES = '{fullDataSet[30]}',
            COD_PROCES2 = '{fullDataSet[31]}',
            COD_PROCES3 = '{fullDataSet[32]}',
            COD_PROCES4 = '{fullDataSet[33]}',
            COD_PROCES5 = '{fullDataSet[34]}',
            CAVALO = '{fullDataSet[35]}',
            CARRETA = '{fullDataSet[36]}',
            MOTORISTA = '{fullDataSet[37]}',
            CPF = '{fullDataSet[38]}'
            
            WHERE NUMERO_TRANSPORTE = '{fullDataSet[0]}'""")
        
        self.connection.commit()

######################################### TABLE CLIENTE

    def create_table_cliente(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cliente(
            
            NOME_CLIENTE TEXT NOT NULL,
            CIDADE TEXT NOT NULL,
            UF TEXT NOT NULL,
                       
            PRIMARY KEY(NOME_CLIENTE)
            );

        """)

    def register_cliente(self, fullDataSet):
        campos_tabela = ('NOME_CLIENTE', 'CIDADE', 'UF')

        qntd = ",".join(["?" for _ in range(len(campos_tabela))])
        cursor = self.connection.cursor()

        try:
            fullDataSet = list(fullDataSet)

            for campo in ['NOME_CLIENTE', 'CIDADE', 'UF']:
                if not fullDataSet[campos_tabela.index(campo)]:
                    return f"Error: {campo} não pode ser vazio!"

            cursor.execute(f"""INSERT INTO Cliente {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            
            self.connection.commit()
            return "OK"
        except:
            return "Error"

    def select_all_cliente(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT NOME_CLIENTE, CIDADE, UF FROM Cliente ")
            dadosselafort = cursor.fetchall()
            return dadosselafort
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

    def delete_cliente(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Cliente WHERE NOME_CLIENTE = '{id}' ")
            self.connection.commit()
            return "Dados Excluídos com Sucesso!"
        except:
            return "Erro ao excluir os Dados!"

    def update_cliente(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Cliente set
           
            NOME_CLIENTE = '{fullDataSet[0]}',
            CIDADE = '{fullDataSet[1]}',
            UF = '{fullDataSet[2]}'
            
            WHERE NOME_CLIENTE = '{fullDataSet[0]}'""")
        
        self.connection.commit()

########################################## TABLE DESTINO

    def create_table_destino(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Destino(
                       
            NOME_DESTINO TEXT NOT NULL,
            CIDADE TEXT NOT NULL,
            UF TEXT NOT NULL,
                       
            PRIMARY KEY(NOME_DESTINO)
            );

        """)

    def register_destino(self, fullDataSet):
        campos_tabela = ('NOME_DESTINO', 'CIDADE', 'UF')

        qntd = ",".join(["?" for _ in range(len(campos_tabela))])
        cursor = self.connection.cursor()

        try:
            fullDataSet = list(fullDataSet)

            for campo in ['NOME_DESTINO', 'CIDADE', 'UF']:
                if not fullDataSet[campos_tabela.index(campo)]:
                    return f"Error: {campo} não pode ser vazio!"

            cursor.execute(f"""INSERT INTO Destino {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            
            self.connection.commit()
            return "OK"
        except:
            return "Error"

    def select_all_destino(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT NOME_DESTINO, CIDADE, UF FROM Destino ")
            dadosdestino = cursor.fetchall()
            return dadosdestino
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

    def delete_destino(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Destino WHERE NOME_DESTINO = '{id}' ")
            self.connection.commit()
            return "Dados Excluídos com Sucesso!"
        except:
            return "Erro ao excluir os Dados!"

    def update_destino(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Destino set
           
            NOME_DESTINO = '{fullDataSet[0]}',
            CIDADE = '{fullDataSet[1]}',
            UF = '{fullDataSet[2]}'
            
            WHERE NOME_DESTINO = '{fullDataSet[0]}'""")
        
        self.connection.commit()

########################################### TABLE CAVALO

    def create_table_veiculo(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Veiculos(
                       
            ID INTEGER NOT NULL,
            PLACA_CAVALO TEXT NOT NULL,
                       
            PRIMARY KEY(ID)
            );

        """)
        
    def register_cavalo(self, fullDataSet):
        campos_tabela = ('ID', 'PLACA_CAVALO')

        qntd = ",".join(["?" for _ in range(len(campos_tabela))])
        cursor = self.connection.cursor()

        try:
            if not fullDataSet[1]:
                return "Error: PLACA_CAVALO não pode ser vazia!"

            cursor.execute("SELECT ID FROM Veiculos WHERE PLACA_CAVALO=?", (fullDataSet[1],))
            existing_record = cursor.fetchone()

            if existing_record:
                return "Error: PLACA_CAVALO já existe na tabela!"

            cursor.execute(f"""INSERT INTO Veiculos ({campos_tabela[1]})
                            VALUES (?)""", (fullDataSet[1],))

            self.connection.commit()
            return "OK"
        except Exception as e:
            print(f"Erro ao inserir dados: {str(e)}")
            return "Error"

    def select_all_cavalo(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT PLACA_CAVALO FROM Veiculos ")
            dadoscavalo = cursor.fetchall()
            return dadoscavalo
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

    def delete_cavalo(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Veiculos WHERE PLACA_CAVALO = '{id}' ")
            self.connection.commit()
            return "Dados Excluídos com Sucesso!"
        except:
            return "Erro ao excluir os Dados!"

    def update_cavalo(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Veiculos set
           
            PLACA_CAVALO = '{fullDataSet[0]}'
            
            WHERE PLACA_CAVALO = '{fullDataSet[0]}'""")
        
        self.connection.commit()

############################################ TABLE CARRETA

    def create_table_carreta(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Carreta(

            ID INTEGER NOT NULL,
            PLACA_CARRETA TEXT NOT NULL,
                       
            PRIMARY KEY(ID)
            );

        """)

    def register_carreta(self, fullDataSet):
        campos_tabela = ('ID', 'PLACA_CARRETA')

        qntd = ",".join(["?" for _ in range(len(campos_tabela))])
        cursor = self.connection.cursor()

        try:
            if not fullDataSet[1]:
                return "Error: PLACA_CARRETA não pode ser vazia!"

            cursor.execute("SELECT ID FROM Carreta WHERE PLACA_CARRETA=?", (fullDataSet[1],))
            existing_record = cursor.fetchone()

            if existing_record:
                return "Error: PLACA_CARRETA já existe na tabela!"

            cursor.execute(f"""INSERT INTO Carreta ({campos_tabela[1]})
                            VALUES (?)""", (fullDataSet[1],))

            self.connection.commit()
            return "OK"
        except Exception as e:
            print(f"Erro ao inserir dados: {str(e)}")
            return "Error"

    def select_all_carreta(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT PLACA_CARRETA FROM Carreta ")
            dadoscarreta = cursor.fetchall()
            return dadoscarreta
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

    def delete_carreta(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Carreta WHERE PLACA_CARRETA = '{id}' ")
            self.connection.commit()
            return "Dados Excluídos com Sucesso!"
        except:
            return "Erro ao excluir os Dados!"

    def update_carreta(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Carreta set
           
            PLACA_CARRETA = '{fullDataSet[0]}'
            
            WHERE PLACA_CARRETA = '{fullDataSet[0]}'""")
        
        self.connection.commit()

############################################ TABLE MOTORISTA
        
    def create_table_motorista(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Motorista(
                       
            NOME_MOTORISTA TEXT NOT NULL,
            CPF TEXT NOT NULL,
            TELEFONE TEXT,
                       
            PRIMARY KEY(NOME_MOTORISTA)
            );

        """)

    def register_motorista(self, fullDataSet):
        campos_tabela = ('NOME_MOTORISTA', 'CPF', 'TELEFONE')

        qntd = ",".join(["?" for _ in range(len(campos_tabela))])
        cursor = self.connection.cursor()

        try:
            fullDataSet = list(fullDataSet)

            for campo in ['NOME_MOTORISTA', 'CPF']:
                if not fullDataSet[campos_tabela.index(campo)]:
                    return f"Error: {campo} não pode ser vazio!"

            cursor.execute(f"""INSERT INTO Motorista {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            
            self.connection.commit()
            return "OK"
        except:
            return "Error"

    def select_all_motorista(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT NOME_MOTORISTA, CPF, TELEFONE FROM Motorista ")
            dadosmotorista = cursor.fetchall()
            return dadosmotorista
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

    def delete_motorista(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Motorista WHERE NOME_MOTORISTA = '{id}' ")
            self.connection.commit()
            return "Dados Excluídos com Sucesso!"
        except:
            return "Erro ao excluir os Dados!"

    def update_motorista(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Motorista set
           
            NOME_MOTORISTA = '{fullDataSet[0]}',
            CPF = '{fullDataSet[1]}',
            TELEFONE = '{fullDataSet[2]}'
            
            WHERE NOME_MOTORISTA = '{fullDataSet[0]}'""")
        
        self.connection.commit()

    def obter_cpf_pelo_nome(self, nome_motorista):
        connection = sqlite3.connect("system.db")
        cursor = connection.cursor()
        cursor.execute('''
            SELECT CPF FROM Motorista WHERE NOME_MOTORISTA = ?
        ''', (nome_motorista,))
        resultado = cursor.fetchone()
        connection.close()

        return resultado[0] if resultado else ""
