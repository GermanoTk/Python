from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6 import *
from PySide6.QtWidgets import *
from ui_main import Ui_StackedWidget
from icons_rc import *
from database import Data_base
from datetime import datetime, timedelta
import sys
import pandas as pd
import sqlite3

class StackedWidget(QStackedWidget, Ui_StackedWidget):
    def __init__(self):
        super(StackedWidget, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("APP Teste Lançamento")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        #toggle_button
        self.btn_toggle.clicked.connect(self.LeftMenu)
        self.btn_login.clicked.connect(self.login)

        #Buttons
        self.btn_salvar_carreg.clicked.connect(self.cadastrar_demarchi)
        self.btn_cancelar_carreg.clicked.connect(self.cancelar_demarchi)
        self.btn_editar_vincular_demarchi.clicked.connect(self.update_demarchi)
        self.btn_cancelar_vincular_demarchi.clicked.connect(self.deletar_demarchi)
        self.btn_gerarexcel_vincular_demarchi.clicked.connect(self.gerar_excel_demarchi)

        self.btn_salvar_carreg_2.clicked.connect(self.cadastrar_selafort)
        self.btn_editar_vincular_selafort.clicked.connect(self.update_selafort)
        self.btn_cancelar_vincular_selafort.clicked.connect(self.deletar_selafort)
        self.btn_gerarexcel_vincular_selafort.clicked.connect(self.gerar_excel_selafort)

        self.btn_cancelar_carregento.clicked.connect(self.deletar_demarchi2)
        self.btn_editar_carregamento.clicked.connect(self.update_demarchi2)
        self.btn_gerar_excel_carregamento.clicked.connect(self.gerar_excel_carreg_demarchi)

        self.btn_cancelar_carregento_2.clicked.connect(self.deletar_selafort2)
        self.btn_editar_carregamento_2.clicked.connect(self.update_selafort2)
        self.btn_gerar_excel_carregamento_2.clicked.connect(self.gerar_excel_carreg_selafort)

        self.btn_salvar_cliente.clicked.connect(self.cadastrar_cliente)
        self.btn_editar_cliente.clicked.connect(self.update_cliente)
        self.btn_excluir_cliente.clicked.connect(self.deletar_cliente)

        self.btn_salvar_destino.clicked.connect(self.cadastrar_destino)
        self.btn_editar_destino.clicked.connect(self.update_destino)
        self.btn_excluir_destino.clicked.connect(self.deletar_destino)

        self.btn_salvar_veiculo.clicked.connect(self.cadastrar_cavalo)
        self.btn_editar_veiculo.clicked.connect(self.update_cavalo)
        self.btn_excluir_veiculo.clicked.connect(self.deletar_cavalo)

        self.btn_salvar_veiculo_2.clicked.connect(self.cadastrar_carreta)
        self.btn_editar_veiculo_2.clicked.connect(self.update_carreta)
        self.btn_excluir_veiculo_2.clicked.connect(self.deletar_carreta)

        self.btn_salvar_motorista.clicked.connect(self.cadastrar_motorista)
        self.btn_editar_motorista.clicked.connect(self.update_motorista)
        self.btn_excluir_motorista.clicked.connect(self.deletar_motorista)

        self.buscar_demarchi()
        self.atualizar_tabela()
        self.buscar_selafort()
        self.atualizar_tabela2()
        self.buscar_cliente()
        self.buscar_destino()
        self.buscar_cavalo()
        self.buscar_carreta()
        self.buscar_motorista()

        #ConnectionPages
        self.btn_lancamento.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_carregamento))
        self.btn_vincular_demarchi.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_vincular_demarchi))
        self.btn_vincular_selafort.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_vincular_selafort))
        self.btn_cliente.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_cliente))
        self.btn_veiculos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_veiculo))
        self.btn_motorista.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_motorista))
        self.btn_carregamentos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_carregamentos))


        self.lineEdit_motorista_demarchi.textChanged.connect(self.atualizar_cpf)

        self.dateEdit_demarchi.dateChanged.connect(self.atualizar_tabela)
        self.dateEdit_selafort.dateChanged.connect(self.atualizar_tabela2)

        self.search_box_cavalo.textChanged.connect(self.on_search_cavalo)
        self.search_box_carreta.textChanged.connect(self.on_search_carreta)

    def login(self):
        user = self.lineEdit_user.text()
        password = self.lineEdit_password.text()

        if self.check_login(user, password):
            self.setCurrentWidget(self.page_inicial)
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def check_login(self, user, password):
        conn = sqlite3.connect("system.db")
        cursor = conn.cursor()

        query = f"SELECT * FROM Login WHERE User = ? AND Password = ?"
        cursor.execute(query, (user, password))

        result = cursor.fetchone()

        conn.close()

        return result is not None

    def LeftMenu(self):
        width = self.left_menu.width()
        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

######## DEMARCHI

    def cadastrar_demarchi(self):
        db = Data_base()
        db.connect()

        datahora_1_text = self.lineEdit_1_datahora.text()
        datahora_1_text = '' if datahora_1_text == '// :' else datahora_1_text
        datahora_2_text = self.lineEdit_2_datahora.text()
        datahora_2_text = '' if datahora_2_text == '// :' else datahora_1_text
        datahora_3_text = self.lineEdit_3_datahora.text()
        datahora_3_text = '' if datahora_3_text == '// :' else datahora_1_text
        datahora_4_text = self.lineEdit_4_datahora.text()
        datahora_4_text = '' if datahora_4_text == '// :' else datahora_1_text
        datahora_5_text = self.lineEdit_5_datahora.text()
        datahora_5_text = '' if datahora_5_text == '// :' else datahora_1_text

        fullDataSet = (
            self.lineEdit_1_transporte.text(), self.lineEdit_2_transporte.text(), self.lineEdit_3_transporte.text(),
            self.lineEdit_4_transporte.text(), self.lineEdit_5_transporte.text(), datahora_1_text, datahora_2_text, datahora_3_text, 
            datahora_4_text, datahora_5_text, self.lineEdit_1_pesobruto.text(), self.lineEdit_2_pesobruto.text(),
            self.lineEdit_3_pesobruto.text(), self.lineEdit_4_pesobruto.text(), self.lineEdit_5_pesobruto.text(),
            self.lineEdit_1_denominacao.text(), self.lineEdit_2_denominacao.text(), self.lineEdit_3_denominacao.text(),
            self.lineEdit_4_denominacao.text(), self.lineEdit_5_denominacao.text(), self.lineEdit_1_cliente.text(),
            self.lineEdit_2_cliente.text(), self.lineEdit_3_cliente.text(), self.lineEdit_4_cliente.text(), self.lineEdit_5_cliente.text(),
            self.lineEdit_1_destino.text(), self.lineEdit_2_destino.text(), self.lineEdit_3_destino.text(), self.lineEdit_4_destino.text(),
            self.lineEdit_5_destino.text(), self.lineEdit_1_codproces.text(), self.lineEdit_2_codproces.text(), self.lineEdit_3_codproces.text(),
            self.lineEdit_4_codproces.text(), self.lineEdit_5_codproces.text(), self.lineEdit_cavalo_demarchi.text(),
            self.lineEdit_carreta_demarchi.text(), self.lineEdit_motorista_demarchi.text(), self.lineEdit_cpf_demarchi.text()
        )

        reset_dados = (
            self.lineEdit_1_transporte.clear(), self.lineEdit_2_transporte.clear(), self.lineEdit_3_transporte.clear(),
            self.lineEdit_4_transporte.clear(), self.lineEdit_5_transporte.clear(), self.lineEdit_1_datahora.clear(),
            self.lineEdit_2_datahora.clear(), self.lineEdit_3_datahora.clear(), self.lineEdit_4_datahora.clear(),
            self.lineEdit_5_datahora.clear(), self.lineEdit_1_pesobruto.clear(), self.lineEdit_2_pesobruto.clear(),
            self.lineEdit_3_pesobruto.clear(), self.lineEdit_4_pesobruto.clear(), self.lineEdit_5_pesobruto.clear(),
            self.lineEdit_1_denominacao.clear(), self.lineEdit_2_denominacao.clear(), self.lineEdit_3_denominacao.clear(),
            self.lineEdit_4_denominacao.clear(), self.lineEdit_5_denominacao.clear(), self.lineEdit_1_cliente.clear(),
            self.lineEdit_2_cliente.clear(), self.lineEdit_3_cliente.clear(), self.lineEdit_4_cliente.clear(), self.lineEdit_5_cliente.clear(),
            self.lineEdit_1_destino.clear(), self.lineEdit_2_destino.clear(), self.lineEdit_3_destino.clear(), self.lineEdit_4_destino.clear(),
            self.lineEdit_5_destino.clear(), self.lineEdit_1_codproces.clear(), self.lineEdit_2_codproces.clear(), self.lineEdit_3_codproces.clear(),
            self.lineEdit_4_codproces.clear(), self.lineEdit_5_codproces.clear(), self.lineEdit_cavalo_demarchi.clear(),
            self.lineEdit_carreta_demarchi.clear(), self.lineEdit_motorista_demarchi.clear(), self.lineEdit_cpf_demarchi.clear()
        )

        resp = db.register_demarchi(fullDataSet)
        db.register_demarchi(reset_dados)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Dados Inseridos")
            msg.setText("Dados Inseridos com Sucesso!")
            msg.exec()
            db.close_connection()
        elif resp.startswith("Error: ") and "não pode ser vazio!" in resp:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Dados não Inseridos")
            msg.setText(resp)
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Erro ao inserir dados!")
            msg.exec()
            db.close_connection()
            return
        
    def buscar_demarchi(self):
        db = Data_base()
        db.connect()
        result = db.select_all_demarchi()
        self.tableWidget_vincular_demarchi.clearContents()
        self.tableWidget_vincular_demarchi.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget_vincular_demarchi.setItem(row, column, QTableWidgetItem(str(data)))
            
    def update_demarchi(self):
        dados = []
        update_dados = []
        for row in range(self.tableWidget_vincular_demarchi.rowCount()):
            for column in range(self.tableWidget_vincular_demarchi.columnCount()):
                dados.append(self.tableWidget_vincular_demarchi.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Data_base()
        db.connect()
        for demar in update_dados:
            db.update_demarchi(tuple(demar))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tableWidget_vincular_demarchi.reset()
        self.buscar_demarchi()
            
    def deletar_demarchi(self):
        db = Data_base()
        db.connect()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            demar = self.tableWidget_vincular_demarchi.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_demarchi(demar)
            self.buscar_demarchi()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Demarchi")
            msg.setText(resultado)
            msg.exec()

        db.close_connection()

    def gerar_excel_demarchi(self):
        cnx = sqlite3.connect("system.db")
        demarchi = pd.read_sql_query("""SELECT * FROM Demarchi""", cnx)
        demarchi.to_excel("Demarchi.xlsx", sheet_name= 'Demarchi', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com Sucesso!")
        msg.exec()

    def cancelar_demarchi(self):
        msg = QMessageBox()
        msg.setWindowTitle("Cancelar")
        msg.setText("Deseja Cancelar o carregamento")
        msg.setInformativeText("Você tem certeza que deseja cancelar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            resultado = (
                self.lineEdit_1_transporte.clear(), self.lineEdit_2_transporte.clear(), self.lineEdit_3_transporte.clear(),
                self.lineEdit_4_transporte.clear(), self.lineEdit_5_transporte.clear(), self.lineEdit_1_datahora.clear(),
                self.lineEdit_2_datahora.clear(), self.lineEdit_3_datahora.clear(), self.lineEdit_4_datahora.clear(),
                self.lineEdit_5_datahora.clear(), self.lineEdit_1_pesobruto.clear(), self.lineEdit_2_pesobruto.clear(),
                self.lineEdit_3_pesobruto.clear(), self.lineEdit_4_pesobruto.clear(), self.lineEdit_5_pesobruto.clear(),
                self.lineEdit_1_denominacao.clear(), self.lineEdit_2_denominacao.clear(), self.lineEdit_3_denominacao.clear(),
                self.lineEdit_4_denominacao.clear(), self.lineEdit_5_denominacao.clear(), self.lineEdit_1_cliente.clear(),
                self.lineEdit_2_cliente.clear(), self.lineEdit_3_cliente.clear(), self.lineEdit_4_cliente.clear(), self.lineEdit_5_cliente.clear(),
                self.lineEdit_1_destino.clear(), self.lineEdit_2_destino.clear(), self.lineEdit_3_destino.clear(), self.lineEdit_4_destino.clear(),
                self.lineEdit_5_destino.clear(), self.lineEdit_1_codproces.clear(), self.lineEdit_2_codproces.clear(), self.lineEdit_3_codproces.clear(),
                self.lineEdit_4_codproces.clear(), self.lineEdit_5_codproces.clear(), self.lineEdit_cavalo_demarchi.clear(),
                self.lineEdit_carreta_demarchi.clear(), self.lineEdit_motorista_demarchi.clear(), self.lineEdit_cpf_demarchi.clear()
            )

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Carregamento")
            msg.setText("Carregamento Cancelado com Sucesso!")
            msg.exec()

######### SELAFORT

    def cadastrar_selafort(self):
        db = Data_base()
        db.connect()

        datahora_1_text = self.lineEdit_1_datahora_2.text()
        datahora_1_text = '' if datahora_1_text == '// :' else datahora_1_text
        datahora_2_text = self.lineEdit_2_datahora_2.text()
        datahora_2_text = '' if datahora_2_text == '// :' else datahora_1_text
        datahora_3_text = self.lineEdit_3_datahora_2.text()
        datahora_3_text = '' if datahora_3_text == '// :' else datahora_1_text
        datahora_4_text = self.lineEdit_4_datahora_2.text()
        datahora_4_text = '' if datahora_4_text == '// :' else datahora_1_text
        datahora_5_text = self.lineEdit_5_datahora_2.text()
        datahora_5_text = '' if datahora_5_text == '// :' else datahora_1_text

        fullDataSet = (
            self.lineEdit_1_transporte_2.text(), self.lineEdit_2_transporte_2.text(), self.lineEdit_3_transporte_2.text(),
            self.lineEdit_4_transporte_2.text(), self.lineEdit_5_transporte_2.text(), datahora_1_text, datahora_2_text, datahora_3_text, 
            datahora_4_text, datahora_5_text, self.lineEdit_1_pesobruto_2.text(), self.lineEdit_2_pesobruto_2.text(),
            self.lineEdit_3_pesobruto_2.text(), self.lineEdit_4_pesobruto_2.text(), self.lineEdit_5_pesobruto_2.text(),
            self.lineEdit_1_denominacao_2.text(), self.lineEdit_2_denominacao_2.text(), self.lineEdit_3_denominacao_2.text(),
            self.lineEdit_4_denominacao_2.text(), self.lineEdit_5_denominacao_2.text(), self.lineEdit_1_cliente_2.text(),
            self.lineEdit_2_cliente_2.text(), self.lineEdit_3_cliente_2.text(), self.lineEdit_4_cliente_2.text(), self.lineEdit_5_cliente_2.text(),
            self.lineEdit_1_destino_2.text(), self.lineEdit_2_destino_2.text(), self.lineEdit_3_destino_2.text(), self.lineEdit_4_destino_2.text(),
            self.lineEdit_5_destino_2.text(), self.lineEdit_1_codproces_2.text(), self.lineEdit_2_codproces_2.text(), self.lineEdit_3_codproces_2.text(),
            self.lineEdit_4_codproces_2.text(), self.lineEdit_5_codproces_2.text(), self.lineEdit_cavalo_selafort.text(),
            self.lineEdit_carreta_selafort.text(), self.lineEdit_motorista_selafort.text(), self.lineEdit_cpf_selafort.text()
        )

        reset_dados = (
            self.lineEdit_1_transporte_2.clear(), self.lineEdit_2_transporte_2.clear(), self.lineEdit_3_transporte_2.clear(),
            self.lineEdit_4_transporte_2.clear(), self.lineEdit_5_transporte_2.clear(), self.lineEdit_1_datahora_2.clear(),
            self.lineEdit_2_datahora_2.clear(), self.lineEdit_3_datahora_2.clear(), self.lineEdit_4_datahora_2.clear(),
            self.lineEdit_5_datahora_2.clear(), self.lineEdit_1_pesobruto_2.clear(), self.lineEdit_2_pesobruto_2.clear(),
            self.lineEdit_3_pesobruto_2.clear(), self.lineEdit_4_pesobruto_2.clear(), self.lineEdit_5_pesobruto_2.clear(),
            self.lineEdit_1_denominacao_2.clear(), self.lineEdit_2_denominacao_2.clear(), self.lineEdit_3_denominacao_2.clear(),
            self.lineEdit_4_denominacao_2.clear(), self.lineEdit_5_denominacao_2.clear(), self.lineEdit_1_cliente_2.clear(),
            self.lineEdit_2_cliente_2.clear(), self.lineEdit_3_cliente_2.clear(), self.lineEdit_4_cliente_2.clear(), self.lineEdit_5_cliente_2.clear(),
            self.lineEdit_1_destino_2.clear(), self.lineEdit_2_destino_2.clear(), self.lineEdit_3_destino_2.clear(), self.lineEdit_4_destino_2.clear(),
            self.lineEdit_5_destino_2.clear(), self.lineEdit_1_codproces_2.clear(), self.lineEdit_2_codproces_2.clear(), self.lineEdit_3_codproces_2.clear(),
            self.lineEdit_4_codproces_2.clear(), self.lineEdit_5_codproces_2.clear(), self.lineEdit_cavalo_selafort.clear(),
            self.lineEdit_carreta_selafort.clear(), self.lineEdit_motorista_selafort.clear(), self.lineEdit_cpf_selafort.clear()
        )

        resp = db.register_selafort(fullDataSet)
        db.register_selafort(reset_dados)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Dados Inseridos")
            msg.setText("Dados Inseridos com Sucesso!")
            msg.exec()
            db.close_connection()
        elif resp.startswith("Error: ") and "não pode ser vazio!" in resp:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Dados não Inseridos")
            msg.setText(resp)
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Erro ao inserir dados!")
            msg.exec()
            db.close_connection()
            return

    def buscar_selafort(self):
        db = Data_base()
        db.connect()
        result = db.select_all_selafort()
        self.tableWidget_vincular_selafort.clearContents()
        self.tableWidget_vincular_selafort.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget_vincular_selafort.setItem(row, column, QTableWidgetItem(str(data)))

    def update_selafort(self):
        dados = []
        update_dados = []
        for row in range(self.tableWidget_vincular_selafort.rowCount()):
            for column in range(self.tableWidget_vincular_selafort.columnCount()):
                dados.append(self.tableWidget_vincular_selafort.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Data_base()
        db.connect()
        for demar in update_dados:
            db.update_selafort(tuple(demar))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tableWidget_vincular_selafort.reset()
        self.buscar_selafort()

    def deletar_selafort(self):
        db = Data_base()
        db.connect()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            demar = self.tableWidget_vincular_selafort.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_selafort(demar)
            self.buscar_selafort()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Selafort")
            msg.setText(resultado)
            msg.exec()

        db.close_connection()

    def gerar_excel_selafort(self):
        cnx = sqlite3.connect("system.db")
        selafort = pd.read_sql_query("""SELECT * FROM Selafort""", cnx)
        selafort.to_excel("Selafort.xlsx", sheet_name= 'Selafort', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com Sucesso!")
        msg.exec()

######### CARREGAMENTOS

    def buscar_demarchi2(self, selected_date):
        db = Data_base()
        db.connect()
        result = db.select_all_demarchi2()

        index_data_de_lancamento = 5

        filtered_result = [row for row in result if datetime.strptime(row[index_data_de_lancamento], '%d/%m/%Y %H:%M').date() == selected_date]

        self.tableWidget_carregamento.clearContents()
        self.tableWidget_carregamento.setRowCount(len(filtered_result))

        for row, data_tuple in enumerate(filtered_result):
            for column, data in enumerate(data_tuple):
                self.tableWidget_carregamento.setItem(row, column, QTableWidgetItem(str(data)))

    def update_demarchi2(self):
        dados = []
        update_dados = []
        for row in range(self.tableWidget_carregamento.rowCount()):
            for column in range(self.tableWidget_carregamento.columnCount()):
                dados.append(self.tableWidget_carregamento.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Data_base()
        db.connect()
        for demar in update_dados:
            db.update_demarchi(tuple(demar))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tableWidget_carregamento.reset()
        self.atualizar_tabela()

    def deletar_demarchi2(self):
        db = Data_base()
        db.connect()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            demar = self.tableWidget_carregamento.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_demarchi(demar)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Demarchi")
            msg.setText(resultado)
            msg.exec()
        self.atualizar_tabela()
        db.close_connection()

    def atualizar_tabela(self):
        qdateedit = self.dateEdit_demarchi
        selected_date = qdateedit.date().toPython()

        self.buscar_demarchi2(selected_date)

    def gerar_excel_carreg_demarchi(self):
        dados = []
        all_dados = []

        for row in range(self.tableWidget_carregamento.rowCount()):
            for column in range(self.tableWidget_carregamento.columnCount()):
                dados.append(self.tableWidget_carregamento.item(row, column).text())
            all_dados.append(dados)
            dados = [0]
        columns = ['DATA_HORA_LANCAMENTO', 'NUMERO_TRANSPORTE', 'NUMERO_TRANSPORTE2', 'NUMERO_TRANSPORTE3', 'NUMERO_TRANSPORTE4', 'NUMERO_TRANSPORTE5',
                    'DATA_HORA_PLANEJAMENTO', 'DATA_HORA_PLANEJAMENTO2', 'DATA_HORA_PLANEJAMENTO3', 'DATA_HORA_PLANEJAMENTO4',
                    'DATA_HORA_PLANEJAMENTO5', 'PESO_BRUTO', 'PESO_BRUTO2', 'PESO_BRUTO3', 'PESO_BRUTO4', 'PESO_BRUTO5',
                    'DENOMINACAO', 'DENOMINACAO2', 'DENOMINACAO3', 'DENOMINACAO4', 'DENOMINACAO5', 'CLIENTE', 'CLIENTE2', 'CLIENTE3',
                    'CLIENTE4', 'CLIENTE5', 'DESTINO', 'DESTINO2', 'DESTINO3', 'DESTINO4', 'DESTINO5', 'COD_PROCES', 'COD_PROCES2',
                    'COD_PROCES3', 'COD_PROCES4', 'COD_PROCES5', 'CAVALO', 'CARRETA', 'MOTORISTA', 'CPF']
        demarchi = pd.DataFrame(all_dados, columns = columns)
        demarchi.to_excel("Carregamento_Demarchi.xlsx", sheet_name= 'Demarchi', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com Sucesso!")
        msg.exec()

####
        
    def buscar_selafort2(self, selected_date):
        db = Data_base()
        db.connect()
        result = db.select_all_selafort2()

        index_data_de_lancamento = 5

        filtered_result = [row for row in result if datetime.strptime(row[index_data_de_lancamento], '%d/%m/%Y %H:%M').date() == selected_date]

        self.tableWidget_carregamento_2.clearContents()
        self.tableWidget_carregamento_2.setRowCount(len(filtered_result))

        for row, data_tuple in enumerate(filtered_result):
            for column, data in enumerate(data_tuple):
                self.tableWidget_carregamento_2.setItem(row, column, QTableWidgetItem(str(data)))

    def update_selafort2(self):
        dados = []
        update_dados = []
        for row in range(self.tableWidget_carregamento_2.rowCount()):
            for column in range(self.tableWidget_carregamento_2.columnCount()):
                dados.append(self.tableWidget_carregamento_2.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Data_base()
        db.connect()
        for demar in update_dados:
            db.update_selafort(tuple(demar))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tableWidget_carregamento_2.reset()
        self.atualizar_tabela2()

    def deletar_selafort2(self):
        db = Data_base()
        db.connect()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            demar = self.tableWidget_carregamento_2.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_selafort(demar)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Selafort")
            msg.setText(resultado)
            msg.exec()
        self.atualizar_tabela2()
        db.close_connection()

    def atualizar_tabela2(self):
        qdateedit = self.dateEdit_selafort
        selected_date = qdateedit.date().toPython()

        self.buscar_selafort2(selected_date)

    def gerar_excel_carreg_selafort(self):
        dados = []
        all_dados = []

        for row in range(self.tableWidget_carregamento_2.rowCount()):
            for column in range(self.tableWidget_carregamento_2.columnCount()):
                dados.append(self.tableWidget_carregamento_2.item(row, column).text())
            all_dados.append(dados)
            dados = [0]
        columns = ['DATA_HORA_LANCAMENTO', 'NUMERO_TRANSPORTE', 'NUMERO_TRANSPORTE2', 'NUMERO_TRANSPORTE3', 'NUMERO_TRANSPORTE4', 'NUMERO_TRANSPORTE5',
                    'DATA_HORA_PLANEJAMENTO', 'DATA_HORA_PLANEJAMENTO2', 'DATA_HORA_PLANEJAMENTO3', 'DATA_HORA_PLANEJAMENTO4',
                    'DATA_HORA_PLANEJAMENTO5', 'PESO_BRUTO', 'PESO_BRUTO2', 'PESO_BRUTO3', 'PESO_BRUTO4', 'PESO_BRUTO5',
                    'DENOMINACAO', 'DENOMINACAO2', 'DENOMINACAO3', 'DENOMINACAO4', 'DENOMINACAO5', 'CLIENTE', 'CLIENTE2', 'CLIENTE3',
                    'CLIENTE4', 'CLIENTE5', 'DESTINO', 'DESTINO2', 'DESTINO3', 'DESTINO4', 'DESTINO5', 'COD_PROCES', 'COD_PROCES2',
                    'COD_PROCES3', 'COD_PROCES4', 'COD_PROCES5', 'CAVALO', 'CARRETA', 'MOTORISTA', 'CPF']
        selafort = pd.DataFrame(all_dados, columns = columns)
        selafort.to_excel("Carregamento_Selafort.xlsx", sheet_name= 'Selafort', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com Sucesso!")
        msg.exec()

######### CLIENTE
        
    def cadastrar_cliente(self):
        db = Data_base()
        db.connect()

        fullDataSet = (self.lineEdit_nome_cliente.text(), self.lineEdit_cidade_cliente.text(), self.lineEdit_uf_cliente.text())

        reset_dados = (self.lineEdit_nome_cliente.clear(), self.lineEdit_cidade_cliente.clear(), self.lineEdit_uf_cliente.clear())

        resp = db.register_cliente(fullDataSet)
        db.register_cliente(reset_dados)
        self.buscar_cliente()

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Dados Inseridos")
            msg.setText("Dados Inseridos com Sucesso!")
            msg.exec()
            db.close_connection()
        elif resp.startswith("Error: ") and "não pode ser vazio!" in resp:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Dados não Inseridos")
            msg.setText(resp)
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Erro ao inserir dados!")
            msg.exec()
            db.close_connection()
            return

    def buscar_cliente(self):
        db = Data_base()
        db.connect()
        result = db.select_all_cliente()
        self.tableWidget_clientes.clearContents()
        self.tableWidget_clientes.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget_clientes.setItem(row, column, QTableWidgetItem(str(data)))

    def deletar_cliente(self):
        db = Data_base()
        db.connect()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            client = self.tableWidget_clientes.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_cliente(client)
            self.buscar_cliente()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cliente")
            msg.setText(resultado)
            msg.exec()

        db.close_connection()

    def update_cliente(self):
        dados = []
        update_dados = []
        for row in range(self.tableWidget_clientes.rowCount()):
            for column in range(self.tableWidget_clientes.columnCount()):
                dados.append(self.tableWidget_clientes.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Data_base()
        db.connect()
        for client in update_dados:
            db.update_cliente(tuple(client))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tableWidget_clientes.reset()
        self.buscar_cliente()

########## DESTINO
        
    def cadastrar_destino(self):
        db = Data_base()
        db.connect()

        fullDataSet = (self.lineEdit_nome_destino.text(), self.lineEdit_cidade_destino.text(), self.lineEdit_uf_destino.text())

        reset_dados = (self.lineEdit_nome_destino.clear(), self.lineEdit_cidade_destino.clear(), self.lineEdit_uf_destino.clear())

        resp = db.register_destino(fullDataSet)
        db.register_destino(reset_dados)
        self.buscar_destino()

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Dados Inseridos")
            msg.setText("Dados Inseridos com Sucesso!")
            msg.exec()
            db.close_connection()
        elif resp.startswith("Error: ") and "não pode ser vazio!" in resp:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Dados não Inseridos")
            msg.setText(resp)
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Erro ao inserir dados!")
            msg.exec()
            db.close_connection()
            return

    def buscar_destino(self):
        db = Data_base()
        db.connect()
        result = db.select_all_destino()
        self.tableWidget_destino.clearContents()
        self.tableWidget_destino.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget_destino.setItem(row, column, QTableWidgetItem(str(data)))

    def deletar_destino(self):
        db = Data_base()
        db.connect()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            dest = self.tableWidget_destino.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_destino(dest)
            self.buscar_destino()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Destino")
            msg.setText(resultado)
            msg.exec()

        db.close_connection()

    def update_destino(self):
        dados = []
        update_dados = []
        for row in range(self.tableWidget_destino.rowCount()):
            for column in range(self.tableWidget_destino.columnCount()):
                dados.append(self.tableWidget_destino.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Data_base()
        db.connect()
        for client in update_dados:
            db.update_destino(tuple(client))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tableWidget_destino.reset()
        self.buscar_destino()

########## PLACA CAVALO
        
    def cadastrar_cavalo(self):
        try:
            db = Data_base()
            db.connect()

            placa_veiculo = self.lineEdit_placa_veiculo.text()

            if not placa_veiculo:
                raise ValueError("Error: PLACA_CAVALO não pode ser vazia!")

            resp = db.register_cavalo([None, placa_veiculo])

            self.lineEdit_placa_veiculo.clear()

            self.buscar_cavalo()

            if resp == "OK":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Dados Inseridos")
                msg.setText("Dados Inseridos com Sucesso!")
                msg.exec()
            else:
                raise ValueError(f"Erro ao inserir dados: {resp}")

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText(f"Erro ao cadastrar cavalo: {str(e)}")
            msg.exec()

        finally:
            db.close_connection()

    def buscar_cavalo(self):
        db = Data_base()
        db.connect()
        result = db.select_all_cavalo()
        self.load_data_to_table_cavalo(result)

    def load_data_to_table_cavalo(self, data):
        self.tableWidget_cavalo_veiculo.clearContents()
        self.tableWidget_cavalo_veiculo.setRowCount(len(data))

        for row, text in enumerate(data):
            for column, data in enumerate(text):
                self.tableWidget_cavalo_veiculo.setItem(row, column, QTableWidgetItem(str(data)))

    def on_search_cavalo(self):
        db = Data_base()
        db.connect()
        result = db.select_all_cavalo()

        search_text = self.search_box_cavalo.text().lower()

        filtered_result = [row for row in result if len(row) > 0 and search_text in str(row[0]).lower()]

        self.load_data_to_table_cavalo(filtered_result)

    def deletar_cavalo(self):
        db = Data_base()
        db.connect()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            dest = self.tableWidget_cavalo_veiculo.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_cavalo(dest)
            self.buscar_cavalo()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cavalo")
            msg.setText(resultado)
            msg.exec()

        db.close_connection()

    def update_cavalo(self):
        dados = []
        update_dados = []
        for row in range(self.tableWidget_cavalo_veiculo.rowCount()):
            for column in range(self.tableWidget_cavalo_veiculo.columnCount()):
                dados.append(self.tableWidget_cavalo_veiculo.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Data_base()
        db.connect()
        for client in update_dados:
            db.update_cavalo(tuple(client))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tableWidget_cavalo_veiculo.reset()
        self.buscar_cavalo()

########## PLACA CARRETA
        
    def cadastrar_carreta(self):
        try:
            db = Data_base()
            db.connect()

            placa_veiculo = self.lineEdit_placa_veiculo_2.text()

            if not placa_veiculo:
                raise ValueError("Error: PLACA_CARRETA não pode ser vazia!")

            resp = db.register_carreta([None, placa_veiculo])

            self.lineEdit_placa_veiculo_2.clear()

            self.buscar_carreta()

            if resp == "OK":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Dados Inseridos")
                msg.setText("Dados Inseridos com Sucesso!")
                msg.exec()
            else:
                raise ValueError(f"Erro ao inserir dados: {resp}")

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText(f"Erro ao cadastrar Carreta: {str(e)}")
            msg.exec()

        finally:
            db.close_connection()
            
    def buscar_carreta(self):
        db = Data_base()
        db.connect()
        result = db.select_all_carreta()
        self.load_data_to_table_carreta(result)

    def load_data_to_table_carreta(self, data):
        self.tableWidget_carreta_veiculo.clearContents()
        self.tableWidget_carreta_veiculo.setRowCount(len(data))

        for row, text in enumerate(data):
            for column, data in enumerate(text):
                self.tableWidget_carreta_veiculo.setItem(row, column, QTableWidgetItem(str(data)))

    def on_search_carreta(self):
        db = Data_base()
        db.connect()
        result = db.select_all_carreta()

        search_text = self.search_box_carreta.text().lower()

        filtered_result = [row for row in result if len(row) > 0 and search_text in str(row[0]).lower()]

        self.load_data_to_table_carreta(filtered_result)

    def deletar_carreta(self):
        db = Data_base()
        db.connect()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            dest = self.tableWidget_carreta_veiculo.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_carreta(dest)
            self.buscar_carreta()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Carreta")
            msg.setText(resultado)
            msg.exec()

        db.close_connection()

    def update_carreta(self):
        dados = []
        update_dados = []
        for row in range(self.tableWidget_carreta_veiculo.rowCount()):
            for column in range(self.tableWidget_carreta_veiculo.columnCount()):
                dados.append(self.tableWidget_carreta_veiculo.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Data_base()
        db.connect()
        for client in update_dados:
            db.update_carreta(tuple(client))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tableWidget_carreta_veiculo.reset()
        self.buscar_carreta()

########## MOTORISTA

    def cadastrar_motorista(self):
        db = Data_base()
        db.connect()

        fullDataSet = (self.lineEdit_nome_motorista.text(), self.lineEdit_cpf_motorista.text(), self.lineEdit_telefone_motorista.text())

        reset_dados = (self.lineEdit_nome_motorista.clear(), self.lineEdit_cpf_motorista.clear(), self.lineEdit_telefone_motorista.clear())

        resp = db.register_motorista(fullDataSet)
        db.register_motorista(reset_dados)
        self.buscar_motorista()

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Dados Inseridos")
            msg.setText("Dados Inseridos com Sucesso!")
            msg.exec()
            db.close_connection()
        elif resp.startswith("Error: ") and "não pode ser vazio!" in resp:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Dados não Inseridos")
            msg.setText(resp)
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Erro ao inserir dados!")
            msg.exec()
            db.close_connection()
            return
        
    def buscar_motorista(self):
        db = Data_base()
        db.connect()
        result = db.select_all_motorista()
        result.sort(key=lambda motorista: motorista[0])
        self.tableWidget_motorista.clearContents()
        self.tableWidget_motorista.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget_motorista.setItem(row, column, QTableWidgetItem(str(data)))

    def deletar_motorista(self):
        db = Data_base()
        db.connect()
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            dest = self.tableWidget_motorista.selectionModel().currentIndex().siblingAtColumn(0).data()
            resultado = db.delete_motorista(dest)
            self.buscar_motorista()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Motorista")
            msg.setText(resultado)
            msg.exec()

        db.close_connection()

    def update_motorista(self):
        dados = []
        update_dados = []
        for row in range(self.tableWidget_motorista.rowCount()):
            for column in range(self.tableWidget_motorista.columnCount()):
                dados.append(self.tableWidget_motorista.item(row, column).text())
            update_dados.append(dados)
            dados = []

        db = Data_base()
        db.connect()
        for client in update_dados:
            db.update_motorista(tuple(client))
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados Atualizados com Sucesso!")
        msg.exec()

        self.tableWidget_motorista.reset()
        self.buscar_motorista()

    def atualizar_cpf(self):
        db = Data_base()
        db.connect()
        nome_motorista = self.lineEdit_motorista_demarchi.text()
        cpf_motorista = db.obter_cpf_pelo_nome(nome_motorista)
        self.lineEdit_cpf_demarchi.setText(cpf_motorista)


if __name__ == "__main__":
    db = Data_base()
    db.connect()
    db.close_connection()
    app = QApplication(sys.argv)
    window = StackedWidget()
    window.show()
    app.exec()