import sys
from typing import Optional

from PySide6.QtCore import *
from PySide6.QtCore import QObject
from PySide6.QtGui import *
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from datetime import datetime
from database import Data_base
import sqlite3

######## VARIAVEIS
cod_processamento = QCompleter(["1201 - Lot. 1 Entrega Carreta",
                                "1201 - Lot. 1 Entrega Truck",
                                "1202 - Fracionado Carreta",
                                "1202 - Fracionado Truck"])

class DateTimeLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setInputMask("99/99/9999 99:99")
        self.setPlaceholderText("dd/MM/yyyy HH:MM")

        self.textChanged.connect(self.custom_validation)

    def custom_validation(self):
        text = self.text()
        cursor_position = self.cursorPosition()

        cleaned_text = ''.join(c for c in text if c.isdigit() or c == '/')

        valid_lenght = min(len(cleaned_text), 14)
        cleaned_text = cleaned_text[:valid_lenght]

        if valid_lenght >= 2 and cleaned_text[2] != '/':
            cleaned_text = cleaned_text[:2] + '/' + cleaned_text[2:]
        if valid_lenght >= 2 and cleaned_text[5] != '/':
            cleaned_text = cleaned_text[:5] + '/' + cleaned_text[5:]
        if valid_lenght >= 2 and cleaned_text[10] != ' ':
            cleaned_text = cleaned_text[:10] + ' ' + cleaned_text[10:]
        if valid_lenght >= 2 and cleaned_text[13] != ':':
            cleaned_text = cleaned_text[:13] + ':' + cleaned_text[13:]
        if valid_lenght >= 2 and cleaned_text[16]:
            cleaned_text = cleaned_text[:16]

        self.setText(cleaned_text)
        self.setCursorPosition(cursor_position)

class CustomValidator(QValidator):
    def validate(self, input_text, pos):
        valid_chars = "0123456789.,"
        for char in input_text:
            if char not in valid_chars:
                return (QValidator.Invalid, pos)
        return (QValidator.Acceptable, pos)

class NumberLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        validator = CustomValidator()
        self.setValidator(validator)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in [16777219, 16777223]:
            super().keyPressEvent(event)
        else:
            if self.validator().validate(event.text(), 0)[0] == QValidator.Acceptable:
                super().keyPressEvent(event)

def obter_dados_cliente():
    conexao = sqlite3.connect('system.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT NOME_CLIENTE, CIDADE FROM Cliente')
    dados = cursor.fetchall()
    conexao.close()
    return dados

dados = obter_dados_cliente()
nomes = [f"{dado[0]} {dado[1]}" for dado in dados]
CompleteCliente = QCompleter(nomes)

def obter_dados_destino():
    conexao = sqlite3.connect('system.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT NOME_DESTINO, CIDADE FROM Destino')
    dados = cursor.fetchall()
    conexao.close()
    return dados

dados = obter_dados_destino()
nomes = [f"{dado[0]} {dado[1]}" for dado in dados]
CompleteDestino = QCompleter(nomes)

def obter_dados_cavalo():
    conexao = sqlite3.connect('system.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT PLACA_CAVALO FROM Veiculos')
    dados = cursor.fetchall()
    conexao.close()
    return dados

dados = obter_dados_cavalo()
nomes = [f"{dado[0]}" for dado in dados]
CompleteCavalo = QCompleter(nomes)

def obter_dados_carreta():
    conexao = sqlite3.connect('system.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT PLACA_CARRETA FROM Carreta')
    dados = cursor.fetchall()
    conexao.close()
    return dados

dados = obter_dados_carreta()
nomes = [f"{dado[0]}" for dado in dados]
CompleteCarreta = QCompleter(nomes)

def obter_dados_motorista():
    conexao = sqlite3.connect('system.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT NOME_MOTORISTA FROM Motorista')
    dados = cursor.fetchall()
    conexao.close()
    return dados

dados = obter_dados_motorista()
nomes = [f"{dado[0]}" for dado in dados]
CompleteMotorista = QCompleter(nomes)
