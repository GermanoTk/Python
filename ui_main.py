from qt_core import *

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(1097, 760)
        font = QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        StackedWidget.setFont(font)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.page_login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #1f295b, stop:1 #fff);")
        self.verticalLayout = QVBoxLayout(self.page_login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_login = QFrame(self.page_login)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMaximumSize(QSize(300, 16777215))
        self.frame_login.setStyleSheet(u"background-color: transparent;")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_login)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_user = QLineEdit(self.frame_login)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_user.sizePolicy().hasHeightForWidth())
        self.lineEdit_user.setSizePolicy(sizePolicy)
        self.lineEdit_user.setMinimumSize(QSize(250, 30))
        self.lineEdit_user.setMaximumSize(QSize(0, 0))
        self.lineEdit_user.setFont(font1)
        self.lineEdit_user.setStyleSheet(u"QLineEdit {\n"
"\n"
"	border: 2px solid #1f295b;\n"
"	background-color: transparent;\n"
"	border-radius: 10px;\n"
"\n"
"}")
        self.lineEdit_user.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_user, 1, 3, 1, 1, Qt.AlignHCenter)

        self.lineEdit_password = QLineEdit(self.frame_login)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(250, 30))
        self.lineEdit_password.setMaximumSize(QSize(0, 0))
        self.lineEdit_password.setFont(font1)
        self.lineEdit_password.setStyleSheet(u"QLineEdit {\n"
"\n"
"	border: 2px solid #1f295b;\n"
"	background-color: transparent;\n"
"	border-radius: 10px;\n"
"\n"
"}")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_password, 2, 3, 1, 1, Qt.AlignHCenter)

        self.radioButton_lembrar = QRadioButton(self.frame_login)
        self.radioButton_lembrar.setObjectName(u"radioButton_lembrar")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(True)
        self.radioButton_lembrar.setFont(font2)

        self.gridLayout_3.addWidget(self.radioButton_lembrar, 3, 3, 1, 1, Qt.AlignHCenter)

        self.btn_login = QPushButton(self.frame_login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(100, 0))
        self.btn_login.setMaximumSize(QSize(100, 30))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"\n"
"	border: 2px solid #1F295B;\n"
"	border-radius: 10px;\n"
"	background-color: #1f295b;\n"
"	color: #ffffff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: transparent;\n"
"	color: #000000;\n"
"\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.btn_login, 4, 3, 1, 1, Qt.AlignHCenter)

        self.img_logo_login = QLabel(self.frame_login)
        self.img_logo_login.setObjectName(u"img_logo_login")
        self.img_logo_login.setMinimumSize(QSize(0, 0))
        self.img_logo_login.setMaximumSize(QSize(200, 150))
        self.img_logo_login.setPixmap(QPixmap(u":/icons/icons/wifi.svg"))
        self.img_logo_login.setScaledContents(True)

        self.gridLayout_3.addWidget(self.img_logo_login, 0, 3, 1, 1, Qt.AlignHCenter)

        self.img_senha_login = QLabel(self.frame_login)
        self.img_senha_login.setObjectName(u"img_senha_login")
        self.img_senha_login.setMinimumSize(QSize(30, 30))
        self.img_senha_login.setMaximumSize(QSize(0, 0))
        self.img_senha_login.setPixmap(QPixmap(u":/icons/icons/lock.svg"))
        self.img_senha_login.setScaledContents(True)

        self.gridLayout_3.addWidget(self.img_senha_login, 2, 0, 1, 1)

        self.img_user_login = QLabel(self.frame_login)
        self.img_user_login.setObjectName(u"img_user_login")
        self.img_user_login.setMinimumSize(QSize(30, 30))
        self.img_user_login.setMaximumSize(QSize(0, 0))
        self.img_user_login.setPixmap(QPixmap(u":/icons/icons/user.svg"))
        self.img_user_login.setScaledContents(True)

        self.gridLayout_3.addWidget(self.img_user_login, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_login, 0, Qt.AlignHCenter)

        StackedWidget.addWidget(self.page_login)
        self.page_inicial = QWidget()
        self.page_inicial.setObjectName(u"page_inicial")
        self.page_inicial.setStyleSheet(u"background-color: #ffffff;")
        self.horizontalLayout = QHBoxLayout(self.page_inicial)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_menu = QFrame(self.page_inicial)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setCursor(QCursor(Qt.ArrowCursor))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.left_menu)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 5, 0, 4)
        self.img_logo_en = QLabel(self.frame_logo)
        self.img_logo_en.setObjectName(u"img_logo_en")
        self.img_logo_en.setMaximumSize(QSize(40, 20))
        self.img_logo_en.setPixmap(QPixmap(u":/icons/icons/wifi.svg"))
        self.img_logo_en.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.img_logo_en)


        self.verticalLayout_3.addWidget(self.frame_logo)

        self.frame_left_menu = QFrame(self.left_menu)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setStyleSheet(u"QFrame{\n"
"\n"
"	border-radius: 10px;\n"
"	background-color: #dbdbdb\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"\n"
"	background-color: #c9c9c9\n"
"\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"\n"
"	border-radius: 5px;\n"
"	background-color: #fff;\n"
"\n"
"}")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, 9, 9)
        self.toolBox = QToolBox(self.frame_left_menu)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QWidget{\n"
"\n"
"	\n"
"	background-color: #dcdcdc;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"	border: 2px solid #1F295B;\n"
"	border-radius: 10px;\n"
"	background-color: #1f295b;\n"
"	color: #ffffff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: transparent;\n"
"	color: #000000;\n"
"\n"
"\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 217, 625))
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_lancamento = QPushButton(self.page)
        self.btn_lancamento.setObjectName(u"btn_lancamento")
        self.btn_lancamento.setMinimumSize(QSize(0, 0))
        self.btn_lancamento.setMaximumSize(QSize(200, 30))
        self.btn_lancamento.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setUnderline(False)
        self.btn_lancamento.setFont(font3)
        self.btn_lancamento.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lancamento.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/mais.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lancamento.setIcon(icon)

        self.verticalLayout_5.addWidget(self.btn_lancamento)

        self.btn_vincular_demarchi = QPushButton(self.page)
        self.btn_vincular_demarchi.setObjectName(u"btn_vincular_demarchi")
        self.btn_vincular_demarchi.setMaximumSize(QSize(200, 30))
        self.btn_vincular_demarchi.setFont(font1)
        self.btn_vincular_demarchi.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/tag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_vincular_demarchi.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.btn_vincular_demarchi)

        self.btn_vincular_selafort = QPushButton(self.page)
        self.btn_vincular_selafort.setObjectName(u"btn_vincular_selafort")
        self.btn_vincular_selafort.setMaximumSize(QSize(200, 30))
        self.btn_vincular_selafort.setFont(font1)
        self.btn_vincular_selafort.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_vincular_selafort.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.btn_vincular_selafort)

        self.btn_carregamentos = QPushButton(self.page)
        self.btn_carregamentos.setObjectName(u"btn_carregamentos")
        self.btn_carregamentos.setMaximumSize(QSize(16777215, 30))
        self.btn_carregamentos.setFont(font1)
        self.btn_carregamentos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_carregamentos.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.btn_carregamentos)

        self.btn_cliente = QPushButton(self.page)
        self.btn_cliente.setObjectName(u"btn_cliente")
        self.btn_cliente.setMinimumSize(QSize(0, 0))
        self.btn_cliente.setMaximumSize(QSize(200, 30))
        self.btn_cliente.setFont(font1)
        self.btn_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cliente.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/users_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cliente.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.btn_cliente)

        self.btn_veiculos = QPushButton(self.page)
        self.btn_veiculos.setObjectName(u"btn_veiculos")
        self.btn_veiculos.setMinimumSize(QSize(0, 0))
        self.btn_veiculos.setMaximumSize(QSize(200, 30))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setUnderline(False)
        self.btn_veiculos.setFont(font4)
        self.btn_veiculos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_veiculos.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/truck_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_veiculos.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.btn_veiculos)

        self.btn_motorista = QPushButton(self.page)
        self.btn_motorista.setObjectName(u"btn_motorista")
        self.btn_motorista.setMaximumSize(QSize(200, 30))
        self.btn_motorista.setFont(font1)
        self.btn_motorista.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/user_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_motorista.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.btn_motorista)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 217, 625))
        self.toolBox.addItem(self.page_2, u"Info")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_3.addWidget(self.frame_left_menu)


        self.horizontalLayout.addWidget(self.left_menu)

        self.frame_central = QFrame(self.page_inicial)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_central.setStyleSheet(u"*{\n"
"\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"	color: #000000;\n"
"\n"
"}")
        self.frame_central.setFrameShape(QFrame.StyledPanel)
        self.frame_central.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_central)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.frame_cima = QFrame(self.frame_central)
        self.frame_cima.setObjectName(u"frame_cima")
        self.frame_cima.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #dcdcdc")
        self.frame_cima.setFrameShape(QFrame.StyledPanel)
        self.frame_cima.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_cima)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.btn_toggle = QPushButton(self.frame_cima)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon5)
        self.btn_toggle.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label_nome_acima = QLabel(self.frame_cima)
        self.label_nome_acima.setObjectName(u"label_nome_acima")
        font5 = QFont()
        font5.setBold(True)
        font5.setUnderline(True)
        self.label_nome_acima.setFont(font5)

        self.horizontalLayout_2.addWidget(self.label_nome_acima, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_cima)

        self.central_frame = QFrame(self.frame_central)
        self.central_frame.setObjectName(u"central_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.central_frame.sizePolicy().hasHeightForWidth())
        self.central_frame.setSizePolicy(sizePolicy1)
        self.central_frame.setStyleSheet(u"")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.central_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.central_frame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_7 = QVBoxLayout(self.page_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.img_logo_expresso = QLabel(self.page_home)
        self.img_logo_expresso.setObjectName(u"img_logo_expresso")
        self.img_logo_expresso.setStyleSheet(u"background-color: transparent;")

        self.verticalLayout_7.addWidget(self.img_logo_expresso)

        self.Pages.addWidget(self.page_home)
        self.page_carregamento = QWidget()
        self.page_carregamento.setObjectName(u"page_carregamento")
        self.horizontalLayout_14 = QHBoxLayout(self.page_carregamento)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tabWidget_carregamento = QTabWidget(self.page_carregamento)
        self.tabWidget_carregamento.setObjectName(u"tabWidget_carregamento")
        self.tabWidget_carregamento.setMinimumSize(QSize(0, 0))
        self.tabWidget_carregamento.setStyleSheet(u"background-color: transparent;")
        self.tab_carreg_demarchi = QWidget()
        self.tab_carreg_demarchi.setObjectName(u"tab_carreg_demarchi")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_carreg_demarchi)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Layout_carreg_demarchi = QVBoxLayout()
        self.Layout_carreg_demarchi.setObjectName(u"Layout_carreg_demarchi")
        self.label_carreg_demarchi = QLabel(self.tab_carreg_demarchi)
        self.label_carreg_demarchi.setObjectName(u"label_carreg_demarchi")
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.label_carreg_demarchi.setFont(font6)

        self.Layout_carreg_demarchi.addWidget(self.label_carreg_demarchi, 0, Qt.AlignHCenter)

        self.frame_carreg = QFrame(self.tab_carreg_demarchi)
        self.frame_carreg.setObjectName(u"frame_carreg")
        self.frame_carreg.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"}")
        self.frame_carreg.setFrameShape(QFrame.StyledPanel)
        self.frame_carreg.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_carreg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_n_transporte = QLabel(self.frame_carreg)
        self.label_n_transporte.setObjectName(u"label_n_transporte")

        self.gridLayout.addWidget(self.label_n_transporte, 0, 0, 1, 1)

        self.lineEdit_1_transporte = NumberLineEdit(self.frame_carreg)
        self.lineEdit_1_transporte.setObjectName(u"lineEdit_1_transporte")
        self.lineEdit_1_transporte.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_transporte.setStyleSheet(u"")
        self.lineEdit_1_transporte.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_1_transporte, 1, 0, 1, 1)

        self.lineEdit_2_transporte = NumberLineEdit(self.frame_carreg)
        self.lineEdit_2_transporte.setObjectName(u"lineEdit_2_transporte")
        self.lineEdit_2_transporte.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_transporte.setStyleSheet(u"")
        self.lineEdit_2_transporte.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_2_transporte, 1, 1, 1, 1)

        self.lineEdit_3_transporte = NumberLineEdit(self.frame_carreg)
        self.lineEdit_3_transporte.setObjectName(u"lineEdit_3_transporte")
        self.lineEdit_3_transporte.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_transporte.setStyleSheet(u"")
        self.lineEdit_3_transporte.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3_transporte, 1, 2, 1, 1)

        self.lineEdit_4_transporte = NumberLineEdit(self.frame_carreg)
        self.lineEdit_4_transporte.setObjectName(u"lineEdit_4_transporte")
        self.lineEdit_4_transporte.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_transporte.setStyleSheet(u"")
        self.lineEdit_4_transporte.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4_transporte, 1, 3, 1, 1)

        self.lineEdit_5_transporte = NumberLineEdit(self.frame_carreg)
        self.lineEdit_5_transporte.setObjectName(u"lineEdit_5_transporte")
        self.lineEdit_5_transporte.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_transporte.setStyleSheet(u"")
        self.lineEdit_5_transporte.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_5_transporte, 1, 4, 1, 1)

        self.label_datahora = QLabel(self.frame_carreg)
        self.label_datahora.setObjectName(u"label_datahora")

        self.gridLayout.addWidget(self.label_datahora, 2, 0, 1, 2)

        self.lineEdit_1_datahora = DateTimeLineEdit(self.frame_carreg)
        self.lineEdit_1_datahora.setObjectName(u"lineEdit_1_datahora")
        self.lineEdit_1_datahora.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_datahora.setStyleSheet(u"")
        self.lineEdit_1_datahora.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_1_datahora, 3, 0, 1, 1)

        self.lineEdit_2_datahora = DateTimeLineEdit(self.frame_carreg)
        self.lineEdit_2_datahora.setObjectName(u"lineEdit_2_datahora")
        self.lineEdit_2_datahora.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_datahora.setStyleSheet(u"")
        self.lineEdit_2_datahora.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_2_datahora, 3, 1, 1, 1)

        self.lineEdit_3_datahora = DateTimeLineEdit(self.frame_carreg)
        self.lineEdit_3_datahora.setObjectName(u"lineEdit_3_datahora")
        self.lineEdit_3_datahora.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_datahora.setStyleSheet(u"")
        self.lineEdit_3_datahora.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3_datahora, 3, 2, 1, 1)

        self.lineEdit_4_datahora = DateTimeLineEdit(self.frame_carreg)
        self.lineEdit_4_datahora.setObjectName(u"lineEdit_4_datahora")
        self.lineEdit_4_datahora.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_datahora.setStyleSheet(u"")
        self.lineEdit_4_datahora.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4_datahora, 3, 3, 1, 1)

        self.lineEdit_5_datahora = DateTimeLineEdit(self.frame_carreg)
        self.lineEdit_5_datahora.setObjectName(u"lineEdit_5_datahora")
        self.lineEdit_5_datahora.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_datahora.setStyleSheet(u"")
        self.lineEdit_5_datahora.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_5_datahora, 3, 4, 1, 1)

        self.label_pesobruto = QLabel(self.frame_carreg)
        self.label_pesobruto.setObjectName(u"label_pesobruto")

        self.gridLayout.addWidget(self.label_pesobruto, 4, 0, 1, 1)

        self.lineEdit_1_pesobruto = NumberLineEdit(self.frame_carreg)
        self.lineEdit_1_pesobruto.setObjectName(u"lineEdit_1_pesobruto")
        self.lineEdit_1_pesobruto.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_pesobruto.setStyleSheet(u"")
        self.lineEdit_1_pesobruto.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_1_pesobruto, 5, 0, 1, 1)

        self.lineEdit_2_pesobruto = NumberLineEdit(self.frame_carreg)
        self.lineEdit_2_pesobruto.setObjectName(u"lineEdit_2_pesobruto")
        self.lineEdit_2_pesobruto.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_pesobruto.setStyleSheet(u"")
        self.lineEdit_2_pesobruto.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_2_pesobruto, 5, 1, 1, 1)

        self.lineEdit_3_pesobruto = NumberLineEdit(self.frame_carreg)
        self.lineEdit_3_pesobruto.setObjectName(u"lineEdit_3_pesobruto")
        self.lineEdit_3_pesobruto.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_pesobruto.setStyleSheet(u"")
        self.lineEdit_3_pesobruto.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3_pesobruto, 5, 2, 1, 1)

        self.lineEdit_4_pesobruto = NumberLineEdit(self.frame_carreg)
        self.lineEdit_4_pesobruto.setObjectName(u"lineEdit_4_pesobruto")
        self.lineEdit_4_pesobruto.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_pesobruto.setStyleSheet(u"")
        self.lineEdit_4_pesobruto.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4_pesobruto, 5, 3, 1, 1)

        self.lineEdit_5_pesobruto = NumberLineEdit(self.frame_carreg)
        self.lineEdit_5_pesobruto.setObjectName(u"lineEdit_5_pesobruto")
        self.lineEdit_5_pesobruto.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_pesobruto.setStyleSheet(u"")
        self.lineEdit_5_pesobruto.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_5_pesobruto, 5, 4, 1, 1)

        self.label_denominacao = QLabel(self.frame_carreg)
        self.label_denominacao.setObjectName(u"label_denominacao")

        self.gridLayout.addWidget(self.label_denominacao, 6, 0, 1, 1)

        self.lineEdit_1_denominacao = NumberLineEdit(self.frame_carreg)
        self.lineEdit_1_denominacao.setObjectName(u"lineEdit_1_denominacao")
        self.lineEdit_1_denominacao.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_denominacao.setStyleSheet(u"")
        self.lineEdit_1_denominacao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_1_denominacao, 7, 0, 1, 1)

        self.lineEdit_2_denominacao = NumberLineEdit(self.frame_carreg)
        self.lineEdit_2_denominacao.setObjectName(u"lineEdit_2_denominacao")
        self.lineEdit_2_denominacao.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_denominacao.setStyleSheet(u"")
        self.lineEdit_2_denominacao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_2_denominacao, 7, 1, 1, 1)

        self.lineEdit_3_denominacao = NumberLineEdit(self.frame_carreg)
        self.lineEdit_3_denominacao.setObjectName(u"lineEdit_3_denominacao")
        self.lineEdit_3_denominacao.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_denominacao.setStyleSheet(u"")
        self.lineEdit_3_denominacao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3_denominacao, 7, 2, 1, 1)

        self.lineEdit_4_denominacao = NumberLineEdit(self.frame_carreg)
        self.lineEdit_4_denominacao.setObjectName(u"lineEdit_4_denominacao")
        self.lineEdit_4_denominacao.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_denominacao.setStyleSheet(u"")
        self.lineEdit_4_denominacao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4_denominacao, 7, 3, 1, 1)

        self.lineEdit_5_denominacao = NumberLineEdit(self.frame_carreg)
        self.lineEdit_5_denominacao.setObjectName(u"lineEdit_5_denominacao")
        self.lineEdit_5_denominacao.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_denominacao.setStyleSheet(u"")
        self.lineEdit_5_denominacao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_5_denominacao, 7, 4, 1, 1)

        self.label_cliente = QLabel(self.frame_carreg)
        self.label_cliente.setObjectName(u"label_cliente")

        self.gridLayout.addWidget(self.label_cliente, 8, 0, 1, 1)

        self.lineEdit_1_cliente = QLineEdit(self.frame_carreg)
        self.lineEdit_1_cliente.setObjectName(u"lineEdit_1_cliente")
        self.lineEdit_1_cliente.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_cliente.setStyleSheet(u"")
        self.lineEdit_1_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_1_cliente.setCompleter(CompleteCliente)
        self.lineEdit_1_cliente.textChanged.connect(lambda text: self.lineEdit_1_cliente.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_1_cliente, 9, 0, 1, 1)

        self.lineEdit_2_cliente = QLineEdit(self.frame_carreg)
        self.lineEdit_2_cliente.setObjectName(u"lineEdit_2_cliente")
        self.lineEdit_2_cliente.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_cliente.setStyleSheet(u"")
        self.lineEdit_2_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_2_cliente.setCompleter(CompleteCliente)
        self.lineEdit_2_cliente.textChanged.connect(lambda text: self.lineEdit_2_cliente.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_2_cliente, 9, 1, 1, 1)

        self.lineEdit_3_cliente = QLineEdit(self.frame_carreg)
        self.lineEdit_3_cliente.setObjectName(u"lineEdit_3_cliente")
        self.lineEdit_3_cliente.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_cliente.setStyleSheet(u"")
        self.lineEdit_3_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_3_cliente.setCompleter(CompleteCliente)
        self.lineEdit_3_cliente.textChanged.connect(lambda text: self.lineEdit_3_cliente.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_3_cliente, 9, 2, 1, 1)

        self.lineEdit_4_cliente = QLineEdit(self.frame_carreg)
        self.lineEdit_4_cliente.setObjectName(u"lineEdit_4_cliente")
        self.lineEdit_4_cliente.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_cliente.setStyleSheet(u"")
        self.lineEdit_4_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_4_cliente.setCompleter(CompleteCliente)
        self.lineEdit_4_cliente.textChanged.connect(lambda text: self.lineEdit_4_cliente.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_4_cliente, 9, 3, 1, 1)

        self.lineEdit_5_cliente = QLineEdit(self.frame_carreg)
        self.lineEdit_5_cliente.setObjectName(u"lineEdit_5_cliente")
        self.lineEdit_5_cliente.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_cliente.setStyleSheet(u"")
        self.lineEdit_5_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_5_cliente.setCompleter(CompleteCliente)
        self.lineEdit_5_cliente.textChanged.connect(lambda text: self.lineEdit_5_cliente.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_5_cliente, 9, 4, 1, 1)

        self.label_destino = QLabel(self.frame_carreg)
        self.label_destino.setObjectName(u"label_destino")

        self.gridLayout.addWidget(self.label_destino, 10, 0, 1, 1)

        self.lineEdit_1_destino = QLineEdit(self.frame_carreg)
        self.lineEdit_1_destino.setObjectName(u"lineEdit_1_destino")
        self.lineEdit_1_destino.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_destino.setStyleSheet(u"")
        self.lineEdit_1_destino.setAlignment(Qt.AlignCenter)
        self.lineEdit_1_destino.setCompleter(CompleteDestino)
        self.lineEdit_1_destino.textChanged.connect(lambda text: self.lineEdit_1_destino.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_1_destino, 11, 0, 1, 1)

        self.lineEdit_2_destino = QLineEdit(self.frame_carreg)
        self.lineEdit_2_destino.setObjectName(u"lineEdit_2_destino")
        self.lineEdit_2_destino.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_destino.setStyleSheet(u"")
        self.lineEdit_2_destino.setAlignment(Qt.AlignCenter)
        self.lineEdit_2_destino.setCompleter(CompleteDestino)
        self.lineEdit_2_destino.textChanged.connect(lambda text: self.lineEdit_2_destino.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_2_destino, 11, 1, 1, 1)

        self.lineEdit_3_destino = QLineEdit(self.frame_carreg)
        self.lineEdit_3_destino.setObjectName(u"lineEdit_3_destino")
        self.lineEdit_3_destino.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_destino.setStyleSheet(u"")
        self.lineEdit_3_destino.setAlignment(Qt.AlignCenter)
        self.lineEdit_3_destino.setCompleter(CompleteDestino)
        self.lineEdit_3_destino.textChanged.connect(lambda text: self.lineEdit_3_destino.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_3_destino, 11, 2, 1, 1)

        self.lineEdit_4_destino = QLineEdit(self.frame_carreg)
        self.lineEdit_4_destino.setObjectName(u"lineEdit_4_destino")
        self.lineEdit_4_destino.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_destino.setStyleSheet(u"")
        self.lineEdit_4_destino.setAlignment(Qt.AlignCenter)
        self.lineEdit_4_destino.setCompleter(CompleteDestino)
        self.lineEdit_4_destino.textChanged.connect(lambda text: self.lineEdit_4_destino.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_4_destino, 11, 3, 1, 1)

        self.lineEdit_5_destino = QLineEdit(self.frame_carreg)
        self.lineEdit_5_destino.setObjectName(u"lineEdit_5_destino")
        self.lineEdit_5_destino.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_destino.setStyleSheet(u"")
        self.lineEdit_5_destino.setAlignment(Qt.AlignCenter)
        self.lineEdit_5_destino.setCompleter(CompleteDestino)
        self.lineEdit_5_destino.textChanged.connect(lambda text: self.lineEdit_5_destino.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_5_destino, 11, 4, 1, 1)

        self.label_cod_processamento = QLabel(self.frame_carreg)
        self.label_cod_processamento.setObjectName(u"label_cod_processamento")

        self.gridLayout.addWidget(self.label_cod_processamento, 12, 0, 1, 2)

        self.lineEdit_1_codproces = NumberLineEdit(self.frame_carreg)
        self.lineEdit_1_codproces.setObjectName(u"lineEdit_1_codproces")
        self.lineEdit_1_codproces.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_codproces.setStyleSheet(u"")
        self.lineEdit_1_codproces.setAlignment(Qt.AlignCenter)
        self.lineEdit_1_codproces.setCompleter(cod_processamento)

        self.gridLayout.addWidget(self.lineEdit_1_codproces, 13, 0, 1, 1)

        self.lineEdit_2_codproces = NumberLineEdit(self.frame_carreg)
        self.lineEdit_2_codproces.setObjectName(u"lineEdit_2_codproces")
        self.lineEdit_2_codproces.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_codproces.setStyleSheet(u"")
        self.lineEdit_2_codproces.setAlignment(Qt.AlignCenter)
        self.lineEdit_2_codproces.setCompleter(cod_processamento)

        self.gridLayout.addWidget(self.lineEdit_2_codproces, 13, 1, 1, 1)

        self.lineEdit_3_codproces = NumberLineEdit(self.frame_carreg)
        self.lineEdit_3_codproces.setObjectName(u"lineEdit_3_codproces")
        self.lineEdit_3_codproces.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_codproces.setStyleSheet(u"")
        self.lineEdit_3_codproces.setAlignment(Qt.AlignCenter)
        self.lineEdit_3_codproces.setCompleter(cod_processamento)

        self.gridLayout.addWidget(self.lineEdit_3_codproces, 13, 2, 1, 1)

        self.lineEdit_4_codproces = NumberLineEdit(self.frame_carreg)
        self.lineEdit_4_codproces.setObjectName(u"lineEdit_4_codproces")
        self.lineEdit_4_codproces.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_codproces.setStyleSheet(u"")
        self.lineEdit_4_codproces.setAlignment(Qt.AlignCenter)
        self.lineEdit_4_codproces.setCompleter(cod_processamento)

        self.gridLayout.addWidget(self.lineEdit_4_codproces, 13, 3, 1, 1)

        self.lineEdit_5_codproces = NumberLineEdit(self.frame_carreg)
        self.lineEdit_5_codproces.setObjectName(u"lineEdit_5_codproces")
        self.lineEdit_5_codproces.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_codproces.setStyleSheet(u"")
        self.lineEdit_5_codproces.setAlignment(Qt.AlignCenter)
        self.lineEdit_5_codproces.setCompleter(cod_processamento)

        self.gridLayout.addWidget(self.lineEdit_5_codproces, 13, 4, 1, 1)

        self.label_cavalo_demarchi = QLabel(self.frame_carreg)
        self.label_cavalo_demarchi.setObjectName(u"label_cavalo_demarchi")

        self.gridLayout.addWidget(self.label_cavalo_demarchi, 14, 0, 1, 1)

        self.label_carreta_demarchi = QLabel(self.frame_carreg)
        self.label_carreta_demarchi.setObjectName(u"label_carreta_demarchi")

        self.gridLayout.addWidget(self.label_carreta_demarchi, 14, 1, 1, 1)

        self.label_motorista_demarchi = QLabel(self.frame_carreg)
        self.label_motorista_demarchi.setObjectName(u"label_motorista_demarchi")

        self.gridLayout.addWidget(self.label_motorista_demarchi, 14, 2, 1, 1)

        self.label_cpf_demarchi = QLabel(self.frame_carreg)
        self.label_cpf_demarchi.setObjectName(u"label_cpf_demarchi")

        self.gridLayout.addWidget(self.label_cpf_demarchi, 14, 4, 1, 1)

        self.lineEdit_cavalo_demarchi = QLineEdit(self.frame_carreg)
        self.lineEdit_cavalo_demarchi.setObjectName(u"lineEdit_cavalo_demarchi")
        self.lineEdit_cavalo_demarchi.setMinimumSize(QSize(0, 30))
        self.lineEdit_cavalo_demarchi.setAlignment(Qt.AlignCenter)
        self.lineEdit_cavalo_demarchi.setMaxLength(7)
        self.lineEdit_cavalo_demarchi.setCompleter(CompleteCavalo)
        self.lineEdit_cavalo_demarchi.textChanged.connect(lambda text: self.lineEdit_cavalo_demarchi.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_cavalo_demarchi, 15, 0, 1, 1)

        self.lineEdit_carreta_demarchi = QLineEdit(self.frame_carreg)
        self.lineEdit_carreta_demarchi.setObjectName(u"lineEdit_carreta_demarchi")
        self.lineEdit_carreta_demarchi.setMinimumSize(QSize(0, 30))
        self.lineEdit_carreta_demarchi.setAlignment(Qt.AlignCenter)
        self.lineEdit_carreta_demarchi.setMaxLength(7)
        self.lineEdit_carreta_demarchi.setCompleter(CompleteCarreta)
        self.lineEdit_carreta_demarchi.textChanged.connect(lambda text: self.lineEdit_carreta_demarchi.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_carreta_demarchi, 15, 1, 1, 1)

        self.lineEdit_motorista_demarchi = QLineEdit(self.frame_carreg)
        self.lineEdit_motorista_demarchi.setObjectName(u"lineEdit_motorista_demarchi")
        self.lineEdit_motorista_demarchi.setMinimumSize(QSize(0, 30))
        self.lineEdit_motorista_demarchi.setAlignment(Qt.AlignCenter)
        self.lineEdit_motorista_demarchi.setCompleter(CompleteMotorista)
        self.lineEdit_motorista_demarchi.textChanged.connect(lambda text: self.lineEdit_motorista_demarchi.setText(text.upper()))

        self.gridLayout.addWidget(self.lineEdit_motorista_demarchi, 15, 2, 1, 2)

        self.lineEdit_cpf_demarchi = NumberLineEdit(self.frame_carreg)
        self.lineEdit_cpf_demarchi.setObjectName(u"lineEdit_cpf_demarchi")
        self.lineEdit_cpf_demarchi.setMinimumSize(QSize(0, 30))
        self.lineEdit_cpf_demarchi.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cpf_demarchi, 15, 4, 1, 1)


        self.Layout_carreg_demarchi.addWidget(self.frame_carreg)

        self.frame_btn_carreg = QFrame(self.tab_carreg_demarchi)
        self.frame_btn_carreg.setObjectName(u"frame_btn_carreg")
        self.frame_btn_carreg.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_btn_carreg.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_carreg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_btn_carreg)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_cancelar_carreg = QPushButton(self.frame_btn_carreg)
        self.btn_cancelar_carreg.setObjectName(u"btn_cancelar_carreg")
        self.btn_cancelar_carreg.setMinimumSize(QSize(0, 30))
        self.btn_cancelar_carreg.setMaximumSize(QSize(150, 16777215))
        self.btn_cancelar_carreg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_carreg.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.btn_cancelar_carreg)

        self.btn_salvar_carreg = QPushButton(self.frame_btn_carreg)
        self.btn_salvar_carreg.setObjectName(u"btn_salvar_carreg")
        self.btn_salvar_carreg.setMinimumSize(QSize(0, 30))
        self.btn_salvar_carreg.setMaximumSize(QSize(150, 16777215))
        self.btn_salvar_carreg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_carreg.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.btn_salvar_carreg)


        self.Layout_carreg_demarchi.addWidget(self.frame_btn_carreg)


        self.horizontalLayout_7.addLayout(self.Layout_carreg_demarchi)

        self.tabWidget_carregamento.addTab(self.tab_carreg_demarchi, "")
        self.tab_carreg_selafort = QWidget()
        self.tab_carreg_selafort.setObjectName(u"tab_carreg_selafort")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_carreg_selafort)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Layout_carreg_selafort = QVBoxLayout()
        self.Layout_carreg_selafort.setObjectName(u"Layout_carreg_selafort")
        self.label_carreg_selafort = QLabel(self.tab_carreg_selafort)
        self.label_carreg_selafort.setObjectName(u"label_carreg_selafort")
        self.label_carreg_selafort.setFont(font6)

        self.Layout_carreg_selafort.addWidget(self.label_carreg_selafort, 0, Qt.AlignHCenter)

        self.frame_carreg_2 = QFrame(self.tab_carreg_selafort)
        self.frame_carreg_2.setObjectName(u"frame_carreg_2")
        self.frame_carreg_2.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"}")
        self.frame_carreg_2.setFrameShape(QFrame.StyledPanel)
        self.frame_carreg_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_carreg_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_n_transporte_2 = QLabel(self.frame_carreg_2)
        self.label_n_transporte_2.setObjectName(u"label_n_transporte_2")

        self.gridLayout_2.addWidget(self.label_n_transporte_2, 0, 0, 1, 1)

        self.lineEdit_1_transporte_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_1_transporte_2.setObjectName(u"lineEdit_1_transporte_2")
        self.lineEdit_1_transporte_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_transporte_2.setStyleSheet(u"")
        self.lineEdit_1_transporte_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_1_transporte_2, 1, 0, 1, 1)

        self.lineEdit_2_transporte_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_2_transporte_2.setObjectName(u"lineEdit_2_transporte_2")
        self.lineEdit_2_transporte_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_transporte_2.setStyleSheet(u"")
        self.lineEdit_2_transporte_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_2_transporte_2, 1, 1, 1, 1)

        self.lineEdit_3_transporte_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_3_transporte_2.setObjectName(u"lineEdit_3_transporte_2")
        self.lineEdit_3_transporte_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_transporte_2.setStyleSheet(u"")
        self.lineEdit_3_transporte_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_3_transporte_2, 1, 2, 1, 1)

        self.lineEdit_4_transporte_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_4_transporte_2.setObjectName(u"lineEdit_4_transporte_2")
        self.lineEdit_4_transporte_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_transporte_2.setStyleSheet(u"")
        self.lineEdit_4_transporte_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_4_transporte_2, 1, 3, 1, 1)

        self.lineEdit_5_transporte_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_5_transporte_2.setObjectName(u"lineEdit_5_transporte_2")
        self.lineEdit_5_transporte_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_transporte_2.setStyleSheet(u"")
        self.lineEdit_5_transporte_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_5_transporte_2, 1, 4, 1, 1)

        self.label_datahora_2 = QLabel(self.frame_carreg_2)
        self.label_datahora_2.setObjectName(u"label_datahora_2")

        self.gridLayout_2.addWidget(self.label_datahora_2, 2, 0, 1, 2)

        self.lineEdit_1_datahora_2 = DateTimeLineEdit(self.frame_carreg_2)
        self.lineEdit_1_datahora_2.setObjectName(u"lineEdit_1_datahora_2")
        self.lineEdit_1_datahora_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_datahora_2.setStyleSheet(u"")
        self.lineEdit_1_datahora_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_1_datahora_2, 3, 0, 1, 1)

        self.lineEdit_2_datahora_2 = DateTimeLineEdit(self.frame_carreg_2)
        self.lineEdit_2_datahora_2.setObjectName(u"lineEdit_2_datahora_2")
        self.lineEdit_2_datahora_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_datahora_2.setStyleSheet(u"")
        self.lineEdit_2_datahora_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_2_datahora_2, 3, 1, 1, 1)

        self.lineEdit_3_datahora_2 = DateTimeLineEdit(self.frame_carreg_2)
        self.lineEdit_3_datahora_2.setObjectName(u"lineEdit_3_datahora_2")
        self.lineEdit_3_datahora_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_datahora_2.setStyleSheet(u"")
        self.lineEdit_3_datahora_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_3_datahora_2, 3, 2, 1, 1)

        self.lineEdit_4_datahora_2 = DateTimeLineEdit(self.frame_carreg_2)
        self.lineEdit_4_datahora_2.setObjectName(u"lineEdit_4_datahora_2")
        self.lineEdit_4_datahora_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_datahora_2.setStyleSheet(u"")
        self.lineEdit_4_datahora_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_4_datahora_2, 3, 3, 1, 1)

        self.lineEdit_5_datahora_2 = DateTimeLineEdit(self.frame_carreg_2)
        self.lineEdit_5_datahora_2.setObjectName(u"lineEdit_5_datahora_2")
        self.lineEdit_5_datahora_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_datahora_2.setStyleSheet(u"")
        self.lineEdit_5_datahora_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_5_datahora_2, 3, 4, 1, 1)

        self.label_pesobruto_2 = QLabel(self.frame_carreg_2)
        self.label_pesobruto_2.setObjectName(u"label_pesobruto_2")

        self.gridLayout_2.addWidget(self.label_pesobruto_2, 4, 0, 1, 1)

        self.lineEdit_1_pesobruto_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_1_pesobruto_2.setObjectName(u"lineEdit_1_pesobruto_2")
        self.lineEdit_1_pesobruto_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_pesobruto_2.setStyleSheet(u"")
        self.lineEdit_1_pesobruto_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_1_pesobruto_2, 5, 0, 1, 1)

        self.lineEdit_2_pesobruto_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_2_pesobruto_2.setObjectName(u"lineEdit_2_pesobruto_2")
        self.lineEdit_2_pesobruto_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_pesobruto_2.setStyleSheet(u"")
        self.lineEdit_2_pesobruto_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_2_pesobruto_2, 5, 1, 1, 1)

        self.lineEdit_3_pesobruto_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_3_pesobruto_2.setObjectName(u"lineEdit_3_pesobruto_2")
        self.lineEdit_3_pesobruto_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_pesobruto_2.setStyleSheet(u"")
        self.lineEdit_3_pesobruto_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_3_pesobruto_2, 5, 2, 1, 1)

        self.lineEdit_4_pesobruto_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_4_pesobruto_2.setObjectName(u"lineEdit_4_pesobruto_2")
        self.lineEdit_4_pesobruto_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_pesobruto_2.setStyleSheet(u"")
        self.lineEdit_4_pesobruto_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_4_pesobruto_2, 5, 3, 1, 1)

        self.lineEdit_5_pesobruto_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_5_pesobruto_2.setObjectName(u"lineEdit_5_pesobruto_2")
        self.lineEdit_5_pesobruto_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_pesobruto_2.setStyleSheet(u"")
        self.lineEdit_5_pesobruto_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_5_pesobruto_2, 5, 4, 1, 1)

        self.label_denominacao_2 = QLabel(self.frame_carreg_2)
        self.label_denominacao_2.setObjectName(u"label_denominacao_2")

        self.gridLayout_2.addWidget(self.label_denominacao_2, 6, 0, 1, 1)

        self.lineEdit_1_denominacao_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_1_denominacao_2.setObjectName(u"lineEdit_1_denominacao_2")
        self.lineEdit_1_denominacao_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_denominacao_2.setStyleSheet(u"")
        self.lineEdit_1_denominacao_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_1_denominacao_2, 7, 0, 1, 1)

        self.lineEdit_2_denominacao_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_2_denominacao_2.setObjectName(u"lineEdit_2_denominacao_2")
        self.lineEdit_2_denominacao_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_denominacao_2.setStyleSheet(u"")
        self.lineEdit_2_denominacao_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_2_denominacao_2, 7, 1, 1, 1)

        self.lineEdit_3_denominacao_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_3_denominacao_2.setObjectName(u"lineEdit_3_denominacao_2")
        self.lineEdit_3_denominacao_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_denominacao_2.setStyleSheet(u"")
        self.lineEdit_3_denominacao_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_3_denominacao_2, 7, 2, 1, 1)

        self.lineEdit_4_denominacao_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_4_denominacao_2.setObjectName(u"lineEdit_4_denominacao_2")
        self.lineEdit_4_denominacao_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_denominacao_2.setStyleSheet(u"")
        self.lineEdit_4_denominacao_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_4_denominacao_2, 7, 3, 1, 1)

        self.lineEdit_5_denominacao_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_5_denominacao_2.setObjectName(u"lineEdit_5_denominacao_2")
        self.lineEdit_5_denominacao_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_denominacao_2.setStyleSheet(u"")
        self.lineEdit_5_denominacao_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_5_denominacao_2, 7, 4, 1, 1)

        self.label_cliente_2 = QLabel(self.frame_carreg_2)
        self.label_cliente_2.setObjectName(u"label_cliente_2")

        self.gridLayout_2.addWidget(self.label_cliente_2, 8, 0, 1, 1)

        self.lineEdit_1_cliente_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_1_cliente_2.setObjectName(u"lineEdit_1_cliente_2")
        self.lineEdit_1_cliente_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_cliente_2.setStyleSheet(u"")
        self.lineEdit_1_cliente_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_1_cliente_2.setCompleter(CompleteCliente)
        self.lineEdit_1_cliente_2.textChanged.connect(lambda text: self.lineEdit_1_cliente_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_1_cliente_2, 9, 0, 1, 1)

        self.lineEdit_2_cliente_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_2_cliente_2.setObjectName(u"lineEdit_2_cliente_2")
        self.lineEdit_2_cliente_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_cliente_2.setStyleSheet(u"")
        self.lineEdit_2_cliente_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2_cliente_2.setCompleter(CompleteCliente)
        self.lineEdit_2_cliente_2.textChanged.connect(lambda text: self.lineEdit_2_cliente_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_2_cliente_2, 9, 1, 1, 1)

        self.lineEdit_3_cliente_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_3_cliente_2.setObjectName(u"lineEdit_3_cliente_2")
        self.lineEdit_3_cliente_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_cliente_2.setStyleSheet(u"")
        self.lineEdit_3_cliente_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3_cliente_2.setCompleter(CompleteCliente)
        self.lineEdit_3_cliente_2.textChanged.connect(lambda text: self.lineEdit_3_cliente_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_3_cliente_2, 9, 2, 1, 1)

        self.lineEdit_4_cliente_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_4_cliente_2.setObjectName(u"lineEdit_4_cliente_2")
        self.lineEdit_4_cliente_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_cliente_2.setStyleSheet(u"")
        self.lineEdit_4_cliente_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_4_cliente_2.setCompleter(CompleteCliente)
        self.lineEdit_4_cliente_2.textChanged.connect(lambda text: self.lineEdit_4_cliente_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_4_cliente_2, 9, 3, 1, 1)

        self.lineEdit_5_cliente_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_5_cliente_2.setObjectName(u"lineEdit_5_cliente_2")
        self.lineEdit_5_cliente_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_cliente_2.setStyleSheet(u"")
        self.lineEdit_5_cliente_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_5_cliente_2.setCompleter(CompleteCliente)
        self.lineEdit_5_cliente_2.textChanged.connect(lambda text: self.lineEdit_5_cliente_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_5_cliente_2, 9, 4, 1, 1)

        self.label_destino_2 = QLabel(self.frame_carreg_2)
        self.label_destino_2.setObjectName(u"label_destino_2")

        self.gridLayout_2.addWidget(self.label_destino_2, 10, 0, 1, 1)

        self.lineEdit_1_destino_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_1_destino_2.setObjectName(u"lineEdit_1_destino_2")
        self.lineEdit_1_destino_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_destino_2.setStyleSheet(u"")
        self.lineEdit_1_destino_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_1_destino_2.setCompleter(CompleteDestino)
        self.lineEdit_1_destino_2.textChanged.connect(lambda text: self.lineEdit_1_destino_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_1_destino_2, 11, 0, 1, 1)

        self.lineEdit_2_destino_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_2_destino_2.setObjectName(u"lineEdit_2_destino_2")
        self.lineEdit_2_destino_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_destino_2.setStyleSheet(u"")
        self.lineEdit_2_destino_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2_destino_2.setCompleter(CompleteDestino)
        self.lineEdit_2_destino_2.textChanged.connect(lambda text: self.lineEdit_2_destino_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_2_destino_2, 11, 1, 1, 1)

        self.lineEdit_3_destino_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_3_destino_2.setObjectName(u"lineEdit_3_destino_2")
        self.lineEdit_3_destino_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_destino_2.setStyleSheet(u"")
        self.lineEdit_3_destino_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3_destino_2.setCompleter(CompleteDestino)
        self.lineEdit_3_destino_2.textChanged.connect(lambda text: self.lineEdit_3_destino_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_3_destino_2, 11, 2, 1, 1)

        self.lineEdit_4_destino_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_4_destino_2.setObjectName(u"lineEdit_4_destino_2")
        self.lineEdit_4_destino_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_destino_2.setStyleSheet(u"")
        self.lineEdit_4_destino_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_4_destino_2.setCompleter(CompleteDestino)
        self.lineEdit_4_destino_2.textChanged.connect(lambda text: self.lineEdit_4_destino_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_4_destino_2, 11, 3, 1, 1)

        self.lineEdit_5_destino_2 = QLineEdit(self.frame_carreg_2)
        self.lineEdit_5_destino_2.setObjectName(u"lineEdit_5_destino_2")
        self.lineEdit_5_destino_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_destino_2.setStyleSheet(u"")
        self.lineEdit_5_destino_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_5_destino_2.setCompleter(CompleteDestino)
        self.lineEdit_5_destino_2.textChanged.connect(lambda text: self.lineEdit_5_destino_2.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_5_destino_2, 11, 4, 1, 1)

        self.label_cod_processamento_2 = QLabel(self.frame_carreg_2)
        self.label_cod_processamento_2.setObjectName(u"label_cod_processamento_2")

        self.gridLayout_2.addWidget(self.label_cod_processamento_2, 12, 0, 1, 2)

        self.lineEdit_1_codproces_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_1_codproces_2.setObjectName(u"lineEdit_1_codproces_2")
        self.lineEdit_1_codproces_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_1_codproces_2.setStyleSheet(u"")
        self.lineEdit_1_codproces_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_1_codproces_2.setCompleter(cod_processamento)

        self.gridLayout_2.addWidget(self.lineEdit_1_codproces_2, 13, 0, 1, 1)

        self.lineEdit_2_codproces_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_2_codproces_2.setObjectName(u"lineEdit_2_codproces_2")
        self.lineEdit_2_codproces_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2_codproces_2.setStyleSheet(u"")
        self.lineEdit_2_codproces_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2_codproces_2.setCompleter(cod_processamento)

        self.gridLayout_2.addWidget(self.lineEdit_2_codproces_2, 13, 1, 1, 1)

        self.lineEdit_3_codproces_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_3_codproces_2.setObjectName(u"lineEdit_3_codproces_2")
        self.lineEdit_3_codproces_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_3_codproces_2.setStyleSheet(u"")
        self.lineEdit_3_codproces_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3_codproces_2.setCompleter(cod_processamento)

        self.gridLayout_2.addWidget(self.lineEdit_3_codproces_2, 13, 2, 1, 1)

        self.lineEdit_4_codproces_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_4_codproces_2.setObjectName(u"lineEdit_4_codproces_2")
        self.lineEdit_4_codproces_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_4_codproces_2.setStyleSheet(u"")
        self.lineEdit_4_codproces_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_4_codproces_2.setCompleter(cod_processamento)

        self.gridLayout_2.addWidget(self.lineEdit_4_codproces_2, 13, 3, 1, 1)

        self.lineEdit_5_codproces_2 = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_5_codproces_2.setObjectName(u"lineEdit_5_codproces_2")
        self.lineEdit_5_codproces_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_5_codproces_2.setStyleSheet(u"")
        self.lineEdit_5_codproces_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_5_codproces_2.setCompleter(cod_processamento)

        self.gridLayout_2.addWidget(self.lineEdit_5_codproces_2, 13, 4, 1, 1)

        self.label_cavalo_selafort = QLabel(self.frame_carreg_2)
        self.label_cavalo_selafort.setObjectName(u"label_cavalo_selafort")

        self.gridLayout_2.addWidget(self.label_cavalo_selafort, 14, 0, 1, 1)

        self.label_carreta_selafort = QLabel(self.frame_carreg_2)
        self.label_carreta_selafort.setObjectName(u"label_carreta_selafort")

        self.gridLayout_2.addWidget(self.label_carreta_selafort, 14, 1, 1, 1)

        self.label_motorista_selafort = QLabel(self.frame_carreg_2)
        self.label_motorista_selafort.setObjectName(u"label_motorista_selafort")

        self.gridLayout_2.addWidget(self.label_motorista_selafort, 14, 2, 1, 1)

        self.label_cpf_selafort = QLabel(self.frame_carreg_2)
        self.label_cpf_selafort.setObjectName(u"label_cpf_selafort")

        self.gridLayout_2.addWidget(self.label_cpf_selafort, 14, 4, 1, 1)

        self.lineEdit_cavalo_selafort = QLineEdit(self.frame_carreg_2)
        self.lineEdit_cavalo_selafort.setObjectName(u"lineEdit_cavalo_selafort")
        self.lineEdit_cavalo_selafort.setMinimumSize(QSize(0, 30))
        self.lineEdit_cavalo_selafort.setAlignment(Qt.AlignCenter)
        self.lineEdit_cavalo_selafort.setMaxLength(7)
        self.lineEdit_cavalo_selafort.setCompleter(CompleteCavalo)
        self.lineEdit_cavalo_selafort.textChanged.connect(lambda text: self.lineEdit_cavalo_selafort.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_cavalo_selafort, 15, 0, 1, 1)

        self.lineEdit_carreta_selafort = QLineEdit(self.frame_carreg_2)
        self.lineEdit_carreta_selafort.setObjectName(u"lineEdit_carreta_selafort")
        self.lineEdit_carreta_selafort.setMinimumSize(QSize(0, 30))
        self.lineEdit_carreta_selafort.setAlignment(Qt.AlignCenter)
        self.lineEdit_carreta_selafort.setMaxLength(7)
        self.lineEdit_carreta_selafort.setCompleter(CompleteCarreta)
        self.lineEdit_carreta_selafort.textChanged.connect(lambda text: self.lineEdit_carreta_selafort.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_carreta_selafort, 15, 1, 1, 1)

        self.lineEdit_motorista_selafort = QLineEdit(self.frame_carreg_2)
        self.lineEdit_motorista_selafort.setObjectName(u"lineEdit_motorista_selafort")
        self.lineEdit_motorista_selafort.setMinimumSize(QSize(0, 30))
        self.lineEdit_motorista_selafort.setAlignment(Qt.AlignCenter)
        self.lineEdit_motorista_selafort.setAlignment(Qt.AlignCenter)
        self.lineEdit_motorista_selafort.setCompleter(CompleteMotorista)
        self.lineEdit_motorista_selafort.textChanged.connect(lambda text: self.lineEdit_motorista_selafort.setText(text.upper()))

        self.gridLayout_2.addWidget(self.lineEdit_motorista_selafort, 15, 2, 1, 2)

        self.lineEdit_cpf_selafort = NumberLineEdit(self.frame_carreg_2)
        self.lineEdit_cpf_selafort.setObjectName(u"lineEdit_cpf_selafort")
        self.lineEdit_cpf_selafort.setMinimumSize(QSize(0, 30))
        self.lineEdit_cpf_selafort.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_cpf_selafort, 15, 4, 1, 1)


        self.Layout_carreg_selafort.addWidget(self.frame_carreg_2)

        self.frame_btn_carreg_2 = QFrame(self.tab_carreg_selafort)
        self.frame_btn_carreg_2.setObjectName(u"frame_btn_carreg_2")
        self.frame_btn_carreg_2.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_btn_carreg_2.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_carreg_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_btn_carreg_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_cancelar_carreg_2 = QPushButton(self.frame_btn_carreg_2)
        self.btn_cancelar_carreg_2.setObjectName(u"btn_cancelar_carreg_2")
        self.btn_cancelar_carreg_2.setMinimumSize(QSize(0, 30))
        self.btn_cancelar_carreg_2.setMaximumSize(QSize(150, 16777215))
        self.btn_cancelar_carreg_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_carreg_2.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.btn_cancelar_carreg_2)

        self.btn_salvar_carreg_2 = QPushButton(self.frame_btn_carreg_2)
        self.btn_salvar_carreg_2.setObjectName(u"btn_salvar_carreg_2")
        self.btn_salvar_carreg_2.setMinimumSize(QSize(0, 30))
        self.btn_salvar_carreg_2.setMaximumSize(QSize(150, 16777215))
        self.btn_salvar_carreg_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_carreg_2.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.btn_salvar_carreg_2)


        self.Layout_carreg_selafort.addWidget(self.frame_btn_carreg_2)


        self.horizontalLayout_11.addLayout(self.Layout_carreg_selafort)

        self.tabWidget_carregamento.addTab(self.tab_carreg_selafort, "")

        self.horizontalLayout_14.addWidget(self.tabWidget_carregamento)

        self.Pages.addWidget(self.page_carregamento)
        self.page_vincular_demarchi = QWidget()
        self.page_vincular_demarchi.setObjectName(u"page_vincular_demarchi")
        self.horizontalLayout_13 = QHBoxLayout(self.page_vincular_demarchi)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Layout_vincular_demarchi = QVBoxLayout()
        self.Layout_vincular_demarchi.setObjectName(u"Layout_vincular_demarchi")
        self.label_vincular_demarchi = QLabel(self.page_vincular_demarchi)
        self.label_vincular_demarchi.setObjectName(u"label_vincular_demarchi")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        self.label_vincular_demarchi.setFont(font7)

        self.Layout_vincular_demarchi.addWidget(self.label_vincular_demarchi, 0, Qt.AlignHCenter)

        self.tableWidget_vincular_demarchi = QTableWidget(self.page_vincular_demarchi)
        if (self.tableWidget_vincular_demarchi.columnCount() < 39):
            self.tableWidget_vincular_demarchi.setColumnCount(39)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(26, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(27, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(28, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(29, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(30, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(31, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(32, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(33, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(34, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(35, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(36, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(37, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_vincular_demarchi.setHorizontalHeaderItem(38, __qtablewidgetitem38)
        self.tableWidget_vincular_demarchi.setObjectName(u"tableWidget_vincular_demarchi")
        self.tableWidget_vincular_demarchi.setStyleSheet(u"QHeaderView::section{\n"
"border: 1px solid #ffffff;\n"
"background-color:#1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QTableWidget{border: 2px solid #1F295B; border-radius: 10px;}")

        self.Layout_vincular_demarchi.addWidget(self.tableWidget_vincular_demarchi)

        self.frame_vincular_demarchi = QFrame(self.page_vincular_demarchi)
        self.frame_vincular_demarchi.setObjectName(u"frame_vincular_demarchi")
        self.frame_vincular_demarchi.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_vincular_demarchi.setFrameShape(QFrame.StyledPanel)
        self.frame_vincular_demarchi.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_vincular_demarchi)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_cancelar_vincular_demarchi = QPushButton(self.frame_vincular_demarchi)
        self.btn_cancelar_vincular_demarchi.setObjectName(u"btn_cancelar_vincular_demarchi")
        self.btn_cancelar_vincular_demarchi.setMinimumSize(QSize(0, 30))
        self.btn_cancelar_vincular_demarchi.setMaximumSize(QSize(100, 16777215))
        self.btn_cancelar_vincular_demarchi.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.btn_cancelar_vincular_demarchi)

        self.btn_editar_vincular_demarchi = QPushButton(self.frame_vincular_demarchi)
        self.btn_editar_vincular_demarchi.setObjectName(u"btn_editar_vincular_demarchi")
        self.btn_editar_vincular_demarchi.setMinimumSize(QSize(0, 30))
        self.btn_editar_vincular_demarchi.setMaximumSize(QSize(100, 16777215))
        self.btn_editar_vincular_demarchi.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.btn_editar_vincular_demarchi)

        self.btn_gerarexcel_vincular_demarchi = QPushButton(self.frame_vincular_demarchi)
        self.btn_gerarexcel_vincular_demarchi.setObjectName(u"btn_gerarexcel_vincular_demarchi")
        self.btn_gerarexcel_vincular_demarchi.setMinimumSize(QSize(0, 30))
        self.btn_gerarexcel_vincular_demarchi.setMaximumSize(QSize(100, 16777215))
        self.btn_gerarexcel_vincular_demarchi.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.btn_gerarexcel_vincular_demarchi)


        self.Layout_vincular_demarchi.addWidget(self.frame_vincular_demarchi)


        self.horizontalLayout_13.addLayout(self.Layout_vincular_demarchi)

        self.Pages.addWidget(self.page_vincular_demarchi)
        self.page_vincular_selafort = QWidget()
        self.page_vincular_selafort.setObjectName(u"page_vincular_selafort")
        self.horizontalLayout_10 = QHBoxLayout(self.page_vincular_selafort)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Layout_vincular_selafort = QVBoxLayout()
        self.Layout_vincular_selafort.setObjectName(u"Layout_vincular_selafort")
        self.label_vincular_selafort = QLabel(self.page_vincular_selafort)
        self.label_vincular_selafort.setObjectName(u"label_vincular_selafort")
        self.label_vincular_selafort.setFont(font7)

        self.Layout_vincular_selafort.addWidget(self.label_vincular_selafort, 0, Qt.AlignHCenter)

        self.tableWidget_vincular_selafort = QTableWidget(self.page_vincular_selafort)
        if (self.tableWidget_vincular_selafort.columnCount() < 39):
            self.tableWidget_vincular_selafort.setColumnCount(39)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(6, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(7, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(8, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(9, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(10, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(11, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(12, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(13, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(14, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(15, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(16, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(17, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(18, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(19, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(20, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(21, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(22, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(23, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(24, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(25, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(26, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(27, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(28, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(29, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(30, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(31, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(32, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(33, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(34, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(35, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(36, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(37, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_vincular_selafort.setHorizontalHeaderItem(38, __qtablewidgetitem77)
        self.tableWidget_vincular_selafort.setObjectName(u"tableWidget_vincular_selafort")
        self.tableWidget_vincular_selafort.setStyleSheet(u"QHeaderView::section{\n"
"border: 1px solid #ffffff;\n"
"background-color:#1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QTableWidget{border: 2px solid #1F295B; border-radius: 10px;}")

        self.Layout_vincular_selafort.addWidget(self.tableWidget_vincular_selafort)

        self.frame_vincular_selafort = QFrame(self.page_vincular_selafort)
        self.frame_vincular_selafort.setObjectName(u"frame_vincular_selafort")
        self.frame_vincular_selafort.setMinimumSize(QSize(0, 0))
        self.frame_vincular_selafort.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_vincular_selafort.setFrameShape(QFrame.StyledPanel)
        self.frame_vincular_selafort.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_vincular_selafort)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_cancelar_vincular_selafort = QPushButton(self.frame_vincular_selafort)
        self.btn_cancelar_vincular_selafort.setObjectName(u"btn_cancelar_vincular_selafort")
        self.btn_cancelar_vincular_selafort.setMinimumSize(QSize(0, 30))
        self.btn_cancelar_vincular_selafort.setMaximumSize(QSize(100, 16777215))
        self.btn_cancelar_vincular_selafort.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_cancelar_vincular_selafort)

        self.btn_editar_vincular_selafort = QPushButton(self.frame_vincular_selafort)
        self.btn_editar_vincular_selafort.setObjectName(u"btn_editar_vincular_selafort")
        self.btn_editar_vincular_selafort.setMinimumSize(QSize(0, 30))
        self.btn_editar_vincular_selafort.setMaximumSize(QSize(100, 16777215))
        self.btn_editar_vincular_selafort.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_editar_vincular_selafort)

        self.btn_gerarexcel_vincular_selafort = QPushButton(self.frame_vincular_selafort)
        self.btn_gerarexcel_vincular_selafort.setObjectName(u"btn_gerarexcel_vincular_selafort")
        self.btn_gerarexcel_vincular_selafort.setMinimumSize(QSize(0, 30))
        self.btn_gerarexcel_vincular_selafort.setMaximumSize(QSize(100, 16777215))
        self.btn_gerarexcel_vincular_selafort.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_gerarexcel_vincular_selafort)


        self.Layout_vincular_selafort.addWidget(self.frame_vincular_selafort)


        self.horizontalLayout_10.addLayout(self.Layout_vincular_selafort)

        self.Pages.addWidget(self.page_vincular_selafort)
        self.page_carregamentos = QWidget()
        self.page_carregamentos.setObjectName(u"page_carregamentos")
        self.horizontalLayout_15 = QHBoxLayout(self.page_carregamentos)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tabWidget_carregamentos = QTabWidget(self.page_carregamentos)
        self.tabWidget_carregamentos.setObjectName(u"tabWidget_carregamentos")
        self.tab_demarchi = QWidget()
        self.tab_demarchi.setObjectName(u"tab_demarchi")
        self.horizontalLayout_17 = QHBoxLayout(self.tab_demarchi)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.Layout_carregamento = QVBoxLayout()
        self.Layout_carregamento.setObjectName(u"Layout_carregamento")
        self.dateEdit_demarchi = QDateEdit(self.tab_demarchi)
        self.dateEdit_demarchi.setObjectName(u"dateEdit_demarchi")
        self.dateEdit_demarchi.setDate(QDate.currentDate())
        self.Layout_carregamento.addWidget(self.dateEdit_demarchi, 0, Qt.AlignRight)

        self.tableWidget_carregamento = QTableWidget(self.tab_demarchi)
        if (self.tableWidget_carregamento.columnCount() < 39):
            self.tableWidget_carregamento.setColumnCount(39)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(2, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(3, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(4, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(5, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(6, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(7, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(8, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(9, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(10, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(11, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(12, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(13, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(14, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(15, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(16, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(17, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(18, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(19, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(20, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(21, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(22, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(23, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(24, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(25, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(26, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(27, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(28, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(29, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(30, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(31, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(32, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(33, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(34, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(35, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(36, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(37, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_carregamento.setHorizontalHeaderItem(38, __qtablewidgetitem116)
        self.tableWidget_carregamento.setObjectName(u"tableWidget_carregamento")
        self.tableWidget_carregamento.setStyleSheet(u"QHeaderView::section{\n"
"border: 1px solid #ffffff;\n"
"background-color:#1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QTableWidget{border: 2px solid #1F295B; border-radius: 10px;}")

        self.Layout_carregamento.addWidget(self.tableWidget_carregamento)

        self.frame_carregamento = QFrame(self.tab_demarchi)
        self.frame_carregamento.setObjectName(u"frame_carregamento")
        self.frame_carregamento.setMinimumSize(QSize(0, 0))
        self.frame_carregamento.setMaximumSize(QSize(16777215, 16777215))
        self.frame_carregamento.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_carregamento.setFrameShape(QFrame.StyledPanel)
        self.frame_carregamento.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_carregamento)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_cancelar_carregento = QPushButton(self.frame_carregamento)
        self.btn_cancelar_carregento.setObjectName(u"btn_cancelar_carregento")
        self.btn_cancelar_carregento.setMinimumSize(QSize(0, 30))
        self.btn_cancelar_carregento.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_16.addWidget(self.btn_cancelar_carregento)

        self.btn_editar_carregamento = QPushButton(self.frame_carregamento)
        self.btn_editar_carregamento.setObjectName(u"btn_editar_carregamento")
        self.btn_editar_carregamento.setMinimumSize(QSize(0, 30))
        self.btn_editar_carregamento.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_16.addWidget(self.btn_editar_carregamento)

        self.btn_gerar_excel_carregamento = QPushButton(self.frame_carregamento)
        self.btn_gerar_excel_carregamento.setObjectName(u"btn_gerar_excel_carregamento")
        self.btn_gerar_excel_carregamento.setMinimumSize(QSize(0, 30))
        self.btn_gerar_excel_carregamento.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_16.addWidget(self.btn_gerar_excel_carregamento)


        self.Layout_carregamento.addWidget(self.frame_carregamento)


        self.horizontalLayout_17.addLayout(self.Layout_carregamento)

        self.tabWidget_carregamentos.addTab(self.tab_demarchi, "")
        self.tab_selafort = QWidget()
        self.tab_selafort.setObjectName(u"tab_selafort")
        self.horizontalLayout_19 = QHBoxLayout(self.tab_selafort)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.Layout_carregamento2 = QVBoxLayout()
        self.Layout_carregamento2.setObjectName(u"Layout_carregamento2")
        self.dateEdit_selafort = QDateEdit(self.tab_selafort)
        self.dateEdit_selafort.setObjectName(u"dateEdit_selafort")
        self.dateEdit_selafort.setDate(QDate.currentDate())
        self.Layout_carregamento2.addWidget(self.dateEdit_selafort, 0, Qt.AlignRight)
        self.tableWidget_carregamento_2 = QTableWidget(self.tab_selafort)
        if (self.tableWidget_carregamento_2.columnCount() < 39):
            self.tableWidget_carregamento_2.setColumnCount(39)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(0, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(1, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(2, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(3, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(4, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(5, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(6, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(7, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(8, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(9, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(10, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(11, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(12, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(13, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(14, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(15, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(16, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(17, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(18, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(19, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(20, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(21, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(22, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(23, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(24, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(25, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(26, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(27, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(28, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(29, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(30, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(31, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(32, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(33, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(34, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(35, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(36, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(37, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_carregamento_2.setHorizontalHeaderItem(38, __qtablewidgetitem155)
        self.tableWidget_carregamento_2.setObjectName(u"tableWidget_carregamento_2")
        self.tableWidget_carregamento_2.setStyleSheet(u"QHeaderView::section{\n"
"border: 1px solid #ffffff;\n"
"background-color:#1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QTableWidget{border: 2px solid #1F295B; border-radius: 10px;}")

        self.Layout_carregamento2.addWidget(self.tableWidget_carregamento_2)

        self.frame_carregamento2 = QFrame(self.tab_selafort)
        self.frame_carregamento2.setObjectName(u"frame_carregamento2")
        self.frame_carregamento2.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_carregamento2.setFrameShape(QFrame.StyledPanel)
        self.frame_carregamento2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_carregamento2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_cancelar_carregento_2 = QPushButton(self.frame_carregamento2)
        self.btn_cancelar_carregento_2.setObjectName(u"btn_cancelar_carregento_2")
        self.btn_cancelar_carregento_2.setMinimumSize(QSize(0, 30))
        self.btn_cancelar_carregento_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.btn_cancelar_carregento_2)

        self.btn_editar_carregamento_2 = QPushButton(self.frame_carregamento2)
        self.btn_editar_carregamento_2.setObjectName(u"btn_editar_carregamento_2")
        self.btn_editar_carregamento_2.setMinimumSize(QSize(0, 30))
        self.btn_editar_carregamento_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.btn_editar_carregamento_2)

        self.btn_gerar_excel_carregamento_2 = QPushButton(self.frame_carregamento2)
        self.btn_gerar_excel_carregamento_2.setObjectName(u"btn_gerar_excel_carregamento_2")
        self.btn_gerar_excel_carregamento_2.setMinimumSize(QSize(0, 30))
        self.btn_gerar_excel_carregamento_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.btn_gerar_excel_carregamento_2)

        self.Layout_carregamento2.addWidget(self.frame_carregamento2)

        self.horizontalLayout_19.addLayout(self.Layout_carregamento2)

        self.tabWidget_carregamentos.addTab(self.tab_selafort, "")

        self.horizontalLayout_15.addWidget(self.tabWidget_carregamentos)

        self.Pages.addWidget(self.page_carregamentos)
        self.page_cliente = QWidget()
        self.page_cliente.setObjectName(u"page_cliente")
        self.verticalLayout_10 = QVBoxLayout(self.page_cliente)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_cliente_destino = QLabel(self.page_cliente)
        self.label_cliente_destino.setObjectName(u"label_cliente_destino")
        self.label_cliente_destino.setFont(font7)

        self.verticalLayout_10.addWidget(self.label_cliente_destino, 0, Qt.AlignHCenter)

        self.Layout_cliente_destino_2 = QVBoxLayout()
        self.Layout_cliente_destino_2.setObjectName(u"Layout_cliente_destino_2")
        self.Layout_cliente_destino = QHBoxLayout()
        self.Layout_cliente_destino.setObjectName(u"Layout_cliente_destino")
        self.frame_cliente = QFrame(self.page_cliente)
        self.frame_cliente.setObjectName(u"frame_cliente")
        self.frame_cliente.setStyleSheet(u"QLineEdit{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QComboBox{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_cliente.setFrameShape(QFrame.StyledPanel)
        self.frame_cliente.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_cliente)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_salvar_cliente = QPushButton(self.frame_cliente)
        self.btn_salvar_cliente.setObjectName(u"btn_salvar_cliente")
        self.btn_salvar_cliente.setMinimumSize(QSize(100, 30))
        self.btn_salvar_cliente.setMaximumSize(QSize(100, 16777215))
        self.btn_salvar_cliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.btn_salvar_cliente, 2, 2, 1, 1)

        self.lineEdit_nome_cliente = QLineEdit(self.frame_cliente)
        self.lineEdit_nome_cliente.setObjectName(u"lineEdit_nome_cliente")
        self.lineEdit_nome_cliente.setMinimumSize(QSize(0, 30))
        self.lineEdit_nome_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_nome_cliente.textChanged.connect(lambda text: self.lineEdit_nome_cliente.setText(text.upper()))

        self.gridLayout_5.addWidget(self.lineEdit_nome_cliente, 1, 0, 1, 1)

        self.label_nome_cliente = QLabel(self.frame_cliente)
        self.label_nome_cliente.setObjectName(u"label_nome_cliente")

        self.gridLayout_5.addWidget(self.label_nome_cliente, 0, 0, 1, 1)

        self.btn_editar_cliente = QPushButton(self.frame_cliente)
        self.btn_editar_cliente.setObjectName(u"btn_editar_cliente")
        self.btn_editar_cliente.setMinimumSize(QSize(100, 30))
        self.btn_editar_cliente.setMaximumSize(QSize(100, 16777215))
        self.btn_editar_cliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.btn_editar_cliente, 2, 0, 1, 1)

        self.btn_excluir_cliente = QPushButton(self.frame_cliente)
        self.btn_excluir_cliente.setObjectName(u"btn_excluir_cliente")
        self.btn_excluir_cliente.setMinimumSize(QSize(100, 30))
        self.btn_excluir_cliente.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.btn_excluir_cliente, 2, 1, 1, 1)

        self.lineEdit_cidade_cliente = QLineEdit(self.frame_cliente)
        self.lineEdit_cidade_cliente.setObjectName(u"lineEdit_cidade_cliente")
        self.lineEdit_cidade_cliente.setMinimumSize(QSize(0, 30))
        self.lineEdit_cidade_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_cidade_cliente.textChanged.connect(lambda text: self.lineEdit_cidade_cliente.setText(text.upper()))

        self.gridLayout_5.addWidget(self.lineEdit_cidade_cliente, 1, 1, 1, 1)

        self.lineEdit_uf_cliente = QLineEdit(self.frame_cliente)
        self.lineEdit_uf_cliente.setObjectName(u"lineEdit_uf_cliente")
        self.lineEdit_uf_cliente.setMinimumSize(QSize(0, 30))
        self.lineEdit_uf_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_uf_cliente.textChanged.connect(lambda text: self.lineEdit_uf_cliente.setText(text.upper()))

        self.gridLayout_5.addWidget(self.lineEdit_uf_cliente, 1, 2, 1, 1)

        self.label_cidade_cliente = QLabel(self.frame_cliente)
        self.label_cidade_cliente.setObjectName(u"label_cidade_cliente")

        self.gridLayout_5.addWidget(self.label_cidade_cliente, 0, 1, 1, 1)

        self.label_uf_cliente = QLabel(self.frame_cliente)
        self.label_uf_cliente.setObjectName(u"label_uf_cliente")

        self.gridLayout_5.addWidget(self.label_uf_cliente, 0, 2, 1, 1)

        self.Layout_cliente_destino.addWidget(self.frame_cliente)

        self.frame_destino = QFrame(self.page_cliente)
        self.frame_destino.setObjectName(u"frame_destino")
        self.frame_destino.setStyleSheet(u"QLineEdit{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QComboBox{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_destino.setFrameShape(QFrame.StyledPanel)
        self.frame_destino.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_destino)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.btn_editar_destino = QPushButton(self.frame_destino)
        self.btn_editar_destino.setObjectName(u"btn_editar_destino")
        self.btn_editar_destino.setMinimumSize(QSize(100, 30))
        self.btn_editar_destino.setMaximumSize(QSize(100, 16777215))
        self.btn_editar_destino.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.btn_editar_destino, 2, 0, 1, 1)

        self.btn_salvar_destino = QPushButton(self.frame_destino)
        self.btn_salvar_destino.setObjectName(u"btn_salvar_destino")
        self.btn_salvar_destino.setMinimumSize(QSize(100, 30))
        self.btn_salvar_destino.setMaximumSize(QSize(100, 16777215))
        self.btn_salvar_destino.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.btn_salvar_destino, 2, 2, 1, 1)

        self.btn_excluir_destino = QPushButton(self.frame_destino)
        self.btn_excluir_destino.setObjectName(u"btn_excluir_destino")
        self.btn_excluir_destino.setMinimumSize(QSize(100, 30))
        self.btn_excluir_destino.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_10.addWidget(self.btn_excluir_destino, 2, 1, 1, 1)

        self.lineEdit_nome_destino = QLineEdit(self.frame_destino)
        self.lineEdit_nome_destino.setObjectName(u"lineEdit_nome_destino")
        self.lineEdit_nome_destino.setMinimumSize(QSize(0, 30))
        self.lineEdit_nome_destino.setAlignment(Qt.AlignCenter)
        self.lineEdit_nome_destino.textChanged.connect(lambda text: self.lineEdit_nome_destino.setText(text.upper()))

        self.gridLayout_10.addWidget(self.lineEdit_nome_destino, 1, 0, 1, 1)

        self.label_nome_destino = QLabel(self.frame_destino)
        self.label_nome_destino.setObjectName(u"label_nome_destino")

        self.gridLayout_10.addWidget(self.label_nome_destino, 0, 0, 1, 1)

        self.lineEdit_cidade_destino = QLineEdit(self.frame_destino)
        self.lineEdit_cidade_destino.setObjectName(u"lineEdit_cidade_destino")
        self.lineEdit_cidade_destino.setMinimumSize(QSize(0, 30))
        self.lineEdit_cidade_destino.setAlignment(Qt.AlignCenter)
        self.lineEdit_cidade_destino.textChanged.connect(lambda text: self.lineEdit_cidade_destino.setText(text.upper()))

        self.gridLayout_10.addWidget(self.lineEdit_cidade_destino, 1, 1, 1, 1)

        self.lineEdit_uf_destino = QLineEdit(self.frame_destino)
        self.lineEdit_uf_destino.setObjectName(u"lineEdit_uf_destino")
        self.lineEdit_uf_destino.setMinimumSize(QSize(0, 30))
        self.lineEdit_uf_destino.setAlignment(Qt.AlignCenter)
        self.lineEdit_uf_destino.textChanged.connect(lambda text: self.lineEdit_uf_destino.setText(text.upper()))

        self.gridLayout_10.addWidget(self.lineEdit_uf_destino, 1, 2, 1, 1)

        self.label_cidade_destino = QLabel(self.frame_destino)
        self.label_cidade_destino.setObjectName(u"label_cidade_destino")

        self.gridLayout_10.addWidget(self.label_cidade_destino, 0, 1, 1, 1)

        self.label_uf_destino = QLabel(self.frame_destino)
        self.label_uf_destino.setObjectName(u"label_uf_destino")

        self.gridLayout_10.addWidget(self.label_uf_destino, 0, 2, 1, 1)

        self.Layout_cliente_destino.addWidget(self.frame_destino)

        self.Layout_cliente_destino_2.addLayout(self.Layout_cliente_destino)

        self.frame_cliente2 = QFrame(self.page_cliente)
        self.frame_cliente2.setObjectName(u"frame_cliente2")
        self.frame_cliente2.setFrameShape(QFrame.StyledPanel)
        self.frame_cliente2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_cliente2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_cliente_3 = QLabel(self.frame_cliente2)
        self.label_cliente_3.setObjectName(u"label_cliente_3")
        font8 = QFont()
        font8.setBold(True)
        self.label_cliente_3.setFont(font8)

        self.gridLayout_6.addWidget(self.label_cliente_3, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_destino_3 = QLabel(self.frame_cliente2)
        self.label_destino_3.setObjectName(u"label_destino_3")
        self.label_destino_3.setFont(font8)

        self.gridLayout_6.addWidget(self.label_destino_3, 0, 1, 1, 1, Qt.AlignHCenter)

        self.tableWidget_clientes = QTableWidget(self.frame_cliente2)
        if (self.tableWidget_clientes.columnCount() < 3):
            self.tableWidget_clientes.setColumnCount(3)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem158)
        self.tableWidget_clientes.setObjectName(u"tableWidget_clientes")
        self.tableWidget_clientes.setStyleSheet(u"QHeaderView::section{\n"
"border: 1px solid #ffffff;\n"
"background-color:#1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QTableWidget{border: 2px solid #1F295B; border-radius: 10px;}")

        self.gridLayout_6.addWidget(self.tableWidget_clientes, 1, 0, 1, 1)

        self.tableWidget_destino = QTableWidget(self.frame_cliente2)
        if (self.tableWidget_destino.columnCount() < 3):
            self.tableWidget_destino.setColumnCount(3)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_destino.setHorizontalHeaderItem(0, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_destino.setHorizontalHeaderItem(1, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_destino.setHorizontalHeaderItem(2, __qtablewidgetitem161)
        self.tableWidget_destino.setObjectName(u"tableWidget_destino")
        self.tableWidget_destino.setStyleSheet(u"QHeaderView::section{\n"
"border: 1px solid #ffffff;\n"
"background-color:#1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QTableWidget{border: 2px solid #1F295B; border-radius: 10px;}")

        self.gridLayout_6.addWidget(self.tableWidget_destino, 1, 1, 1, 1)


        self.Layout_cliente_destino_2.addWidget(self.frame_cliente2)


        self.verticalLayout_10.addLayout(self.Layout_cliente_destino_2)

        self.Pages.addWidget(self.page_cliente)
        self.page_veiculo = QWidget()
        self.page_veiculo.setObjectName(u"page_veiculo")
        self.verticalLayout_9 = QVBoxLayout(self.page_veiculo)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_veiculos = QLabel(self.page_veiculo)
        self.label_veiculos.setObjectName(u"label_veiculos")
        self.label_veiculos.setFont(font7)

        self.verticalLayout_9.addWidget(self.label_veiculos, 0, Qt.AlignHCenter)

        self.Layout_veiculos = QVBoxLayout()
        self.Layout_veiculos.setObjectName(u"Layout_veiculos")
        self.Layout_veiculos2 = QHBoxLayout()
        self.Layout_veiculos2.setObjectName(u"Layout_veiculos2")
        self.frame_veiculo = QFrame(self.page_veiculo)
        self.frame_veiculo.setObjectName(u"frame_veiculo")
        self.frame_veiculo.setStyleSheet(u"QLineEdit{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QComboBox{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_veiculo.setFrameShape(QFrame.StyledPanel)
        self.frame_veiculo.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_veiculo)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_placa_veiculo = QLabel(self.frame_veiculo)
        self.label_placa_veiculo.setObjectName(u"label_placa_veiculo")

        self.gridLayout_7.addWidget(self.label_placa_veiculo, 0, 0, 1, 1)

        self.lineEdit_placa_veiculo = QLineEdit(self.frame_veiculo)
        self.lineEdit_placa_veiculo.setObjectName(u"lineEdit_placa_veiculo")
        self.lineEdit_placa_veiculo.setMinimumSize(QSize(0, 30))
        self.lineEdit_placa_veiculo.setAlignment(Qt.AlignCenter)
        self.lineEdit_placa_veiculo.setMaxLength(7)
        self.lineEdit_placa_veiculo.textChanged.connect(lambda text: self.lineEdit_placa_veiculo.setText(text.upper()))

        self.gridLayout_7.addWidget(self.lineEdit_placa_veiculo, 1, 0, 1, 2)

        self.search_box_cavalo = QLineEdit(self)
        self.search_box_cavalo.setPlaceholderText("Search...")
        self.search_box_cavalo.setMinimumSize(QSize(0, 30))
        self.search_box_cavalo.setMaximumSize(QSize(100, 16777215))
        self.search_box_cavalo.setAlignment(Qt.AlignCenter)
        self.search_box_cavalo.setMaxLength(7)
        self.gridLayout_7.addWidget(self.search_box_cavalo, 1, 2, 1, 1)

        self.btn_editar_veiculo = QPushButton(self.frame_veiculo)
        self.btn_editar_veiculo.setObjectName(u"btn_editar_veiculo")
        self.btn_editar_veiculo.setMinimumSize(QSize(100, 30))
        self.btn_editar_veiculo.setMaximumSize(QSize(100, 16777215))
        self.btn_editar_veiculo.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_7.addWidget(self.btn_editar_veiculo, 2, 0, 1, 1)

        self.btn_salvar_veiculo = QPushButton(self.frame_veiculo)
        self.btn_salvar_veiculo.setObjectName(u"btn_salvar_veiculo")
        self.btn_salvar_veiculo.setMinimumSize(QSize(100, 30))
        self.btn_salvar_veiculo.setMaximumSize(QSize(100, 16777215))
        self.btn_salvar_veiculo.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_7.addWidget(self.btn_salvar_veiculo, 2, 2, 1, 1)

        self.btn_excluir_veiculo = QPushButton(self.frame_veiculo)
        self.btn_excluir_veiculo.setObjectName(u"btn_excluir_veiculo")
        self.btn_excluir_veiculo.setMinimumSize(QSize(100, 30))
        self.btn_excluir_veiculo.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.btn_excluir_veiculo, 2, 1, 1, 1)


        self.Layout_veiculos2.addWidget(self.frame_veiculo)

        self.frame_veiculo_2 = QFrame(self.page_veiculo)
        self.frame_veiculo_2.setObjectName(u"frame_veiculo_2")
        self.frame_veiculo_2.setStyleSheet(u"QLineEdit{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QComboBox{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_veiculo_2.setFrameShape(QFrame.StyledPanel)
        self.frame_veiculo_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_veiculo_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_editar_veiculo_2 = QPushButton(self.frame_veiculo_2)
        self.btn_editar_veiculo_2.setObjectName(u"btn_editar_veiculo_2")
        self.btn_editar_veiculo_2.setMinimumSize(QSize(100, 30))
        self.btn_editar_veiculo_2.setMaximumSize(QSize(100, 16777215))
        self.btn_editar_veiculo_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_editar_veiculo_2, 2, 0, 1, 1)

        self.btn_salvar_veiculo_2 = QPushButton(self.frame_veiculo_2)
        self.btn_salvar_veiculo_2.setObjectName(u"btn_salvar_veiculo_2")
        self.btn_salvar_veiculo_2.setMinimumSize(QSize(100, 30))
        self.btn_salvar_veiculo_2.setMaximumSize(QSize(100, 16777215))
        self.btn_salvar_veiculo_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_salvar_veiculo_2, 2, 2, 1, 1)

        self.lineEdit_placa_veiculo_2 = QLineEdit(self.frame_veiculo_2)
        self.lineEdit_placa_veiculo_2.setObjectName(u"lineEdit_placa_veiculo_2")
        self.lineEdit_placa_veiculo_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_placa_veiculo_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_placa_veiculo_2.setMaxLength(7)
        self.lineEdit_placa_veiculo_2.textChanged.connect(lambda text: self.lineEdit_placa_veiculo_2.setText(text.upper()))

        self.gridLayout_4.addWidget(self.lineEdit_placa_veiculo_2, 1, 0, 1, 2)

        self.search_box_carreta = QLineEdit(self)
        self.search_box_carreta.setPlaceholderText("Search...")
        self.search_box_carreta.setMinimumSize(QSize(0, 30))
        self.search_box_carreta.setMaximumSize(QSize(100, 16777215))
        self.search_box_carreta.setAlignment(Qt.AlignCenter)
        self.search_box_carreta.setMaxLength(7)
        self.gridLayout_4.addWidget(self.search_box_carreta, 1, 2, 1, 1)

        self.label_placa_veiculo_2 = QLabel(self.frame_veiculo_2)
        self.label_placa_veiculo_2.setObjectName(u"label_placa_veiculo_2")

        self.gridLayout_4.addWidget(self.label_placa_veiculo_2, 0, 0, 1, 1)

        self.btn_excluir_veiculo_2 = QPushButton(self.frame_veiculo_2)
        self.btn_excluir_veiculo_2.setObjectName(u"btn_excluir_veiculo_2")
        self.btn_excluir_veiculo_2.setMinimumSize(QSize(100, 30))
        self.btn_excluir_veiculo_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.btn_excluir_veiculo_2, 2, 1, 1, 1)

        self.Layout_veiculos2.addWidget(self.frame_veiculo_2)

        self.Layout_veiculos.addLayout(self.Layout_veiculos2)

        self.frame_table_veiculo = QFrame(self.page_veiculo)
        self.frame_table_veiculo.setObjectName(u"frame_table_veiculo")
        self.frame_table_veiculo.setStyleSheet(u"QHeaderView::section{\n"
"border: 1px solid #ffffff;\n"
"background-color:#1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QTableWidget{border: 2px solid #1F295B; border-radius: 10px;}")
        self.frame_table_veiculo.setFrameShape(QFrame.StyledPanel)
        self.frame_table_veiculo.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_table_veiculo)
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.label_cavalo_veiculo = QLabel(self.frame_table_veiculo)
        self.label_cavalo_veiculo.setObjectName(u"label_cavalo_veiculo")
        self.label_cavalo_veiculo.setFont(font8)

        self.gridLayout_8.addWidget(self.label_cavalo_veiculo, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_carreta_veiculo = QLabel(self.frame_table_veiculo)
        self.label_carreta_veiculo.setObjectName(u"label_carreta_veiculo")
        self.label_carreta_veiculo.setFont(font8)

        self.gridLayout_8.addWidget(self.label_carreta_veiculo, 0, 1, 1, 1, Qt.AlignHCenter)

        self.tableWidget_cavalo_veiculo = QTableWidget(self.frame_table_veiculo)
        if (self.tableWidget_cavalo_veiculo.columnCount() < 1):
            self.tableWidget_cavalo_veiculo.setColumnCount(1)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_cavalo_veiculo.setHorizontalHeaderItem(0, __qtablewidgetitem162)
        self.tableWidget_cavalo_veiculo.setObjectName(u"tableWidget_cavalo_veiculo")

        self.gridLayout_8.addWidget(self.tableWidget_cavalo_veiculo, 1, 0, 1, 1)

        self.tableWidget_carreta_veiculo = QTableWidget(self.frame_table_veiculo)
        if (self.tableWidget_carreta_veiculo.columnCount() < 1):
            self.tableWidget_carreta_veiculo.setColumnCount(1)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_carreta_veiculo.setHorizontalHeaderItem(0, __qtablewidgetitem163)
        self.tableWidget_carreta_veiculo.setObjectName(u"tableWidget_carreta_veiculo")

        self.gridLayout_8.addWidget(self.tableWidget_carreta_veiculo, 1, 1, 1, 1)

        self.Layout_veiculos.addWidget(self.frame_table_veiculo)

        self.verticalLayout_9.addLayout(self.Layout_veiculos)

        self.Pages.addWidget(self.page_veiculo)
        self.page_motorista = QWidget()
        self.page_motorista.setObjectName(u"page_motorista")
        self.horizontalLayout_5 = QHBoxLayout(self.page_motorista)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Layout_motorista = QVBoxLayout()
        self.Layout_motorista.setObjectName(u"Layout_motorista")
        self.label_motorista = QLabel(self.page_motorista)
        self.label_motorista.setObjectName(u"label_motorista")
        self.label_motorista.setFont(font7)

        self.Layout_motorista.addWidget(self.label_motorista, 0, Qt.AlignHCenter)

        self.frame_motorista = QFrame(self.page_motorista)
        self.frame_motorista.setObjectName(u"frame_motorista")
        self.frame_motorista.setStyleSheet(u"QLineEdit{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QComboBox{border: 2px solid #1F295B;border-radius: 5px;}\n"
"QPushButton{\n"
"border: 2px solid #1F295B;\n"
"border-radius: 10px;\n"
"background-color: #1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}")
        self.frame_motorista.setFrameShape(QFrame.StyledPanel)
        self.frame_motorista.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_motorista)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.label_nome_motorista = QLabel(self.frame_motorista)
        self.label_nome_motorista.setObjectName(u"label_nome_motorista")

        self.gridLayout_9.addWidget(self.label_nome_motorista, 0, 0, 1, 1)

        self.lineEdit_nome_motorista = QLineEdit(self.frame_motorista)
        self.lineEdit_nome_motorista.setObjectName(u"lineEdit_nome_motorista")
        self.lineEdit_nome_motorista.setMinimumSize(QSize(150, 30))
        self.lineEdit_nome_motorista.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_nome_motorista.setAlignment(Qt.AlignCenter)
        self.lineEdit_nome_motorista.textChanged.connect(lambda text: self.lineEdit_nome_motorista.setText(text.upper()))

        self.gridLayout_9.addWidget(self.lineEdit_nome_motorista, 1, 0, 1, 1)

        self.label_cpf_motorista = QLabel(self.frame_motorista)
        self.label_cpf_motorista.setObjectName(u"label_cpf_motorista")

        self.gridLayout_9.addWidget(self.label_cpf_motorista, 0, 1, 1, 1)

        self.lineEdit_cpf_motorista = NumberLineEdit(self.frame_motorista)
        self.lineEdit_cpf_motorista.setObjectName(u"lineEdit_cpf_motorista")
        self.lineEdit_cpf_motorista.setMinimumSize(QSize(150, 30))
        self.lineEdit_cpf_motorista.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_cpf_motorista.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_cpf_motorista, 1, 1, 1, 1)

        self.label_telefone_motorista = QLabel(self.frame_motorista)
        self.label_telefone_motorista.setObjectName(u"label_telefone_motorista")

        self.gridLayout_9.addWidget(self.label_telefone_motorista, 0, 2, 1, 1)

        self.lineEdit_telefone_motorista = NumberLineEdit(self.frame_motorista)
        self.lineEdit_telefone_motorista.setObjectName(u"lineEdit_telefone_motorista")
        self.lineEdit_telefone_motorista.setMinimumSize(QSize(150, 30))
        self.lineEdit_telefone_motorista.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_telefone_motorista.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_telefone_motorista, 1, 2, 1, 1)

        self.btn_editar_motorista = QPushButton(self.frame_motorista)
        self.btn_editar_motorista.setObjectName(u"btn_editar_motorista")
        self.btn_editar_motorista.setMinimumSize(QSize(100, 30))
        self.btn_editar_motorista.setMaximumSize(QSize(100, 16777215))
        self.btn_editar_motorista.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.btn_editar_motorista, 1, 3, 1, 1)

        self.btn_salvar_motorista = QPushButton(self.frame_motorista)
        self.btn_salvar_motorista.setObjectName(u"btn_salvar_motorista")
        self.btn_salvar_motorista.setMinimumSize(QSize(100, 30))
        self.btn_salvar_motorista.setMaximumSize(QSize(100, 16777215))
        self.btn_salvar_motorista.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.btn_salvar_motorista, 1, 5, 1, 1)

        self.btn_excluir_motorista = QPushButton(self.frame_motorista)
        self.btn_excluir_motorista.setObjectName(u"btn_excluir_motorista")
        self.btn_excluir_motorista.setMinimumSize(QSize(100, 30))
        self.btn_excluir_motorista.setMaximumSize(QSize(100, 16777215))
        self.btn_excluir_motorista.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.btn_excluir_motorista, 1, 4, 1, 1)


        self.Layout_motorista.addWidget(self.frame_motorista)

        self.tableWidget_motorista = QTableWidget(self.page_motorista)
        if (self.tableWidget_motorista.columnCount() < 3):
            self.tableWidget_motorista.setColumnCount(3)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tableWidget_motorista.setHorizontalHeaderItem(0, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_motorista.setHorizontalHeaderItem(1, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tableWidget_motorista.setHorizontalHeaderItem(2, __qtablewidgetitem166)
        self.tableWidget_motorista.setObjectName(u"tableWidget_motorista")
        self.tableWidget_motorista.setStyleSheet(u"QHeaderView::section{\n"
"border: 1px solid #ffffff;\n"
"background-color:#1f295b;\n"
"color: #ffffff;\n"
"}\n"
"QTableWidget{border: 2px solid #1F295B; border-radius: 10px;}")

        self.Layout_motorista.addWidget(self.tableWidget_motorista)


        self.horizontalLayout_5.addLayout(self.Layout_motorista)

        self.Pages.addWidget(self.page_motorista)

        self.verticalLayout_6.addWidget(self.Pages)


        self.verticalLayout_2.addWidget(self.central_frame)

        self.frame_baixo = QFrame(self.frame_central)
        self.frame_baixo.setObjectName(u"frame_baixo")
        self.frame_baixo.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #dcdcdc;")
        self.frame_baixo.setFrameShape(QFrame.StyledPanel)
        self.frame_baixo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_baixo)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 0, 5)
        self.label_nome_abaixo = QLabel(self.frame_baixo)
        self.label_nome_abaixo.setObjectName(u"label_nome_abaixo")
        self.label_nome_abaixo.setMinimumSize(QSize(20, 20))
        self.label_nome_abaixo.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_nome_abaixo)

        self.verticalLayout_2.addWidget(self.frame_baixo)

        self.horizontalLayout.addWidget(self.frame_central)

        StackedWidget.addWidget(self.page_inicial)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)
        self.Pages.setCurrentIndex(0)
        self.tabWidget_carregamento.setCurrentIndex(0)
        self.tabWidget_carregamentos.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Password", None))
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"User", None))
        self.radioButton_lembrar.setText(QCoreApplication.translate("StackedWidget", u"Lembrar-me", None))
        self.btn_login.setText(QCoreApplication.translate("StackedWidget", u"Login", None))
        self.img_logo_login.setText("")
        self.img_senha_login.setText("")
        self.img_user_login.setText("")
        self.img_logo_en.setText("")
        self.btn_lancamento.setText(QCoreApplication.translate("StackedWidget", u"Carregamento", None))
        self.btn_vincular_demarchi.setText(QCoreApplication.translate("StackedWidget", u"Vincular Demarchi", None))
        self.btn_vincular_selafort.setText(QCoreApplication.translate("StackedWidget", u"Vincular Selafort", None))
        self.btn_carregamentos.setText(QCoreApplication.translate("StackedWidget", u"Carregamentos", None))
        self.btn_cliente.setText(QCoreApplication.translate("StackedWidget", u"Clientes / Destinos", None))
        self.btn_veiculos.setText(QCoreApplication.translate("StackedWidget", u"Ve\u00edculos", None))
        self.btn_motorista.setText(QCoreApplication.translate("StackedWidget", u"Motoristas", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("StackedWidget", u"Menu", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("StackedWidget", u"Info", None))
        self.btn_toggle.setText("")
        self.label_nome_acima.setText(QCoreApplication.translate("StackedWidget", u"Gest\u00e3o de Intelig\u00eancia Operacional", None))
        self.img_logo_expresso.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/wifi.svg\"/></p></body></html>", None))
        self.label_carreg_demarchi.setText(QCoreApplication.translate("StackedWidget", u"CARREGAMENTO DEMARCHI", None))
        self.label_n_transporte.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte", None))
        self.label_datahora.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej. do Registro ", None))
        self.label_pesobruto.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto", None))
        self.label_denominacao.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o", None))
        self.label_cliente.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None))
        self.label_destino.setText(QCoreApplication.translate("StackedWidget", u"Destino", None))
        self.label_cod_processamento.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processamento Especial", None))
        self.label_cavalo_demarchi.setText(QCoreApplication.translate("StackedWidget", u"Cavalo", None))
        self.label_carreta_demarchi.setText(QCoreApplication.translate("StackedWidget", u"Carreta", None))
        self.label_motorista_demarchi.setText(QCoreApplication.translate("StackedWidget", u"Motorista", None))
        self.label_cpf_demarchi.setText(QCoreApplication.translate("StackedWidget", u"CPF", None))
        self.btn_cancelar_carreg.setText(QCoreApplication.translate("StackedWidget", u"Cancelar", None))
        self.btn_salvar_carreg.setText(QCoreApplication.translate("StackedWidget", u"Salvar", None))
        self.tabWidget_carregamento.setTabText(self.tabWidget_carregamento.indexOf(self.tab_carreg_demarchi), QCoreApplication.translate("StackedWidget", u"DEMARCHI", None))
        self.label_carreg_selafort.setText(QCoreApplication.translate("StackedWidget", u"CARREGAMENTO SELAFORT", None))
        self.label_n_transporte_2.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte", None))
        self.label_datahora_2.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej. do Registro ", None))
        self.label_pesobruto_2.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto", None))
        self.label_denominacao_2.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o", None))
        self.label_cliente_2.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None))
        self.label_destino_2.setText(QCoreApplication.translate("StackedWidget", u"Destino", None))
        self.label_cod_processamento_2.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processamento Especial", None))
        self.label_cavalo_selafort.setText(QCoreApplication.translate("StackedWidget", u"Cavalo", None))
        self.label_carreta_selafort.setText(QCoreApplication.translate("StackedWidget", u"Carreta", None))
        self.label_motorista_selafort.setText(QCoreApplication.translate("StackedWidget", u"Motorista", None))
        self.label_cpf_selafort.setText(QCoreApplication.translate("StackedWidget", u"CPF", None))
        self.btn_cancelar_carreg_2.setText(QCoreApplication.translate("StackedWidget", u"Cancelar", None))
        self.btn_salvar_carreg_2.setText(QCoreApplication.translate("StackedWidget", u"Salvar", None))
        self.tabWidget_carregamento.setTabText(self.tabWidget_carregamento.indexOf(self.tab_carreg_selafort), QCoreApplication.translate("StackedWidget", u"SELAFORT", None))
        self.label_vincular_demarchi.setText(QCoreApplication.translate("StackedWidget", u"DEMARCHI", None))
        ___qtablewidgetitem = self.tableWidget_vincular_demarchi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte", None));
        ___qtablewidgetitem1 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte2", None));
        ___qtablewidgetitem2 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte3", None));
        ___qtablewidgetitem3 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte4", None));
        ___qtablewidgetitem4 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte5", None));
        ___qtablewidgetitem5 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.", None));
        ___qtablewidgetitem6 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.2", None));
        ___qtablewidgetitem7 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.3", None));
        ___qtablewidgetitem8 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.4", None));
        ___qtablewidgetitem9 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.5", None));
        ___qtablewidgetitem10 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto", None));
        ___qtablewidgetitem11 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto2", None));
        ___qtablewidgetitem12 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto3", None));
        ___qtablewidgetitem13 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto4", None));
        ___qtablewidgetitem14 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto5", None));
        ___qtablewidgetitem15 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o", None));
        ___qtablewidgetitem16 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o2", None));
        ___qtablewidgetitem17 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o3", None));
        ___qtablewidgetitem18 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o4", None));
        ___qtablewidgetitem19 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o5", None));
        ___qtablewidgetitem20 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None));
        ___qtablewidgetitem21 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("StackedWidget", u"Cliente2", None));
        ___qtablewidgetitem22 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("StackedWidget", u"Cliente3", None));
        ___qtablewidgetitem23 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("StackedWidget", u"Cliente4", None));
        ___qtablewidgetitem24 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("StackedWidget", u"Cliente5", None));
        ___qtablewidgetitem25 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("StackedWidget", u"Destino", None));
        ___qtablewidgetitem26 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("StackedWidget", u"Destino2", None));
        ___qtablewidgetitem27 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(27)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("StackedWidget", u"Destino3", None));
        ___qtablewidgetitem28 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(28)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("StackedWidget", u"Destino4", None));
        ___qtablewidgetitem29 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(29)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("StackedWidget", u"Destino5", None));
        ___qtablewidgetitem30 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(30)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.", None));
        ___qtablewidgetitem31 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(31)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.2", None));
        ___qtablewidgetitem32 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(32)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.3", None));
        ___qtablewidgetitem33 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(33)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.4", None));
        ___qtablewidgetitem34 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(34)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.5", None));
        ___qtablewidgetitem35 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(35)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("StackedWidget", u"Cavalo", None));
        ___qtablewidgetitem36 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(36)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("StackedWidget", u"Carreta", None));
        ___qtablewidgetitem37 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(37)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("StackedWidget", u"Motorista", None));
        ___qtablewidgetitem38 = self.tableWidget_vincular_demarchi.horizontalHeaderItem(38)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("StackedWidget", u"CPF", None));
        self.btn_cancelar_vincular_demarchi.setText(QCoreApplication.translate("StackedWidget", u"Cancelar", None))
        self.btn_editar_vincular_demarchi.setText(QCoreApplication.translate("StackedWidget", u"Editar", None))
        self.btn_gerarexcel_vincular_demarchi.setText(QCoreApplication.translate("StackedWidget", u"Gerar Excel", None))
        self.label_vincular_selafort.setText(QCoreApplication.translate("StackedWidget", u"SELAFORT", None))
        ___qtablewidgetitem39 = self.tableWidget_vincular_selafort.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte", None));
        ___qtablewidgetitem40 = self.tableWidget_vincular_selafort.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte2", None));
        ___qtablewidgetitem41 = self.tableWidget_vincular_selafort.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte3", None));
        ___qtablewidgetitem42 = self.tableWidget_vincular_selafort.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte4", None));
        ___qtablewidgetitem43 = self.tableWidget_vincular_selafort.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte5", None));
        ___qtablewidgetitem44 = self.tableWidget_vincular_selafort.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.", None));
        ___qtablewidgetitem45 = self.tableWidget_vincular_selafort.horizontalHeaderItem(6)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.2", None));
        ___qtablewidgetitem46 = self.tableWidget_vincular_selafort.horizontalHeaderItem(7)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.3", None));
        ___qtablewidgetitem47 = self.tableWidget_vincular_selafort.horizontalHeaderItem(8)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.4", None));
        ___qtablewidgetitem48 = self.tableWidget_vincular_selafort.horizontalHeaderItem(9)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.5", None));
        ___qtablewidgetitem49 = self.tableWidget_vincular_selafort.horizontalHeaderItem(10)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto", None));
        ___qtablewidgetitem50 = self.tableWidget_vincular_selafort.horizontalHeaderItem(11)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto2", None));
        ___qtablewidgetitem51 = self.tableWidget_vincular_selafort.horizontalHeaderItem(12)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto3", None));
        ___qtablewidgetitem52 = self.tableWidget_vincular_selafort.horizontalHeaderItem(13)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto4", None));
        ___qtablewidgetitem53 = self.tableWidget_vincular_selafort.horizontalHeaderItem(14)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto5", None));
        ___qtablewidgetitem54 = self.tableWidget_vincular_selafort.horizontalHeaderItem(15)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o", None));
        ___qtablewidgetitem55 = self.tableWidget_vincular_selafort.horizontalHeaderItem(16)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o2", None));
        ___qtablewidgetitem56 = self.tableWidget_vincular_selafort.horizontalHeaderItem(17)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o3", None));
        ___qtablewidgetitem57 = self.tableWidget_vincular_selafort.horizontalHeaderItem(18)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o4", None));
        ___qtablewidgetitem58 = self.tableWidget_vincular_selafort.horizontalHeaderItem(19)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o5", None));
        ___qtablewidgetitem59 = self.tableWidget_vincular_selafort.horizontalHeaderItem(20)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None));
        ___qtablewidgetitem60 = self.tableWidget_vincular_selafort.horizontalHeaderItem(21)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("StackedWidget", u"Cliente2", None));
        ___qtablewidgetitem61 = self.tableWidget_vincular_selafort.horizontalHeaderItem(22)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("StackedWidget", u"Cliente3", None));
        ___qtablewidgetitem62 = self.tableWidget_vincular_selafort.horizontalHeaderItem(23)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("StackedWidget", u"Cliente4", None));
        ___qtablewidgetitem63 = self.tableWidget_vincular_selafort.horizontalHeaderItem(24)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("StackedWidget", u"Cliente5", None));
        ___qtablewidgetitem64 = self.tableWidget_vincular_selafort.horizontalHeaderItem(25)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("StackedWidget", u"Destino", None));
        ___qtablewidgetitem65 = self.tableWidget_vincular_selafort.horizontalHeaderItem(26)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("StackedWidget", u"Destino2", None));
        ___qtablewidgetitem66 = self.tableWidget_vincular_selafort.horizontalHeaderItem(27)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("StackedWidget", u"Destino3", None));
        ___qtablewidgetitem67 = self.tableWidget_vincular_selafort.horizontalHeaderItem(28)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("StackedWidget", u"Destino4", None));
        ___qtablewidgetitem68 = self.tableWidget_vincular_selafort.horizontalHeaderItem(29)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("StackedWidget", u"Destino5", None));
        ___qtablewidgetitem69 = self.tableWidget_vincular_selafort.horizontalHeaderItem(30)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.", None));
        ___qtablewidgetitem70 = self.tableWidget_vincular_selafort.horizontalHeaderItem(31)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.2", None));
        ___qtablewidgetitem71 = self.tableWidget_vincular_selafort.horizontalHeaderItem(32)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.3", None));
        ___qtablewidgetitem72 = self.tableWidget_vincular_selafort.horizontalHeaderItem(33)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.4", None));
        ___qtablewidgetitem73 = self.tableWidget_vincular_selafort.horizontalHeaderItem(34)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.5", None));
        ___qtablewidgetitem74 = self.tableWidget_vincular_selafort.horizontalHeaderItem(35)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("StackedWidget", u"Cavalo", None));
        ___qtablewidgetitem75 = self.tableWidget_vincular_selafort.horizontalHeaderItem(36)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("StackedWidget", u"Carreta", None));
        ___qtablewidgetitem76 = self.tableWidget_vincular_selafort.horizontalHeaderItem(37)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("StackedWidget", u"Motorista", None));
        ___qtablewidgetitem77 = self.tableWidget_vincular_selafort.horizontalHeaderItem(38)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("StackedWidget", u"CPF", None));
        self.btn_cancelar_vincular_selafort.setText(QCoreApplication.translate("StackedWidget", u"Cancelar", None))
        self.btn_editar_vincular_selafort.setText(QCoreApplication.translate("StackedWidget", u"Editar", None))
        self.btn_gerarexcel_vincular_selafort.setText(QCoreApplication.translate("StackedWidget", u"Gerar Excel", None))
        ___qtablewidgetitem78 = self.tableWidget_carregamento.horizontalHeaderItem(0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte", None));
        ___qtablewidgetitem79 = self.tableWidget_carregamento.horizontalHeaderItem(1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte2", None));
        ___qtablewidgetitem80 = self.tableWidget_carregamento.horizontalHeaderItem(2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte3", None));
        ___qtablewidgetitem81 = self.tableWidget_carregamento.horizontalHeaderItem(3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte4", None));
        ___qtablewidgetitem82 = self.tableWidget_carregamento.horizontalHeaderItem(4)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte5", None));
        ___qtablewidgetitem83 = self.tableWidget_carregamento.horizontalHeaderItem(5)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.", None));
        ___qtablewidgetitem84 = self.tableWidget_carregamento.horizontalHeaderItem(6)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.2", None));
        ___qtablewidgetitem85 = self.tableWidget_carregamento.horizontalHeaderItem(7)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.3", None));
        ___qtablewidgetitem86 = self.tableWidget_carregamento.horizontalHeaderItem(8)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.4", None));
        ___qtablewidgetitem87 = self.tableWidget_carregamento.horizontalHeaderItem(9)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.5", None));
        ___qtablewidgetitem88 = self.tableWidget_carregamento.horizontalHeaderItem(10)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto", None));
        ___qtablewidgetitem89 = self.tableWidget_carregamento.horizontalHeaderItem(11)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto2", None));
        ___qtablewidgetitem90 = self.tableWidget_carregamento.horizontalHeaderItem(12)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto3", None));
        ___qtablewidgetitem91 = self.tableWidget_carregamento.horizontalHeaderItem(13)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto4", None));
        ___qtablewidgetitem92 = self.tableWidget_carregamento.horizontalHeaderItem(14)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto5", None));
        ___qtablewidgetitem93 = self.tableWidget_carregamento.horizontalHeaderItem(15)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o", None));
        ___qtablewidgetitem94 = self.tableWidget_carregamento.horizontalHeaderItem(16)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o2", None));
        ___qtablewidgetitem95 = self.tableWidget_carregamento.horizontalHeaderItem(17)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o3", None));
        ___qtablewidgetitem96 = self.tableWidget_carregamento.horizontalHeaderItem(18)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o4", None));
        ___qtablewidgetitem97 = self.tableWidget_carregamento.horizontalHeaderItem(19)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o5", None));
        ___qtablewidgetitem98 = self.tableWidget_carregamento.horizontalHeaderItem(20)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None));
        ___qtablewidgetitem99 = self.tableWidget_carregamento.horizontalHeaderItem(21)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("StackedWidget", u"Cliente2", None));
        ___qtablewidgetitem100 = self.tableWidget_carregamento.horizontalHeaderItem(22)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("StackedWidget", u"Cliente3", None));
        ___qtablewidgetitem101 = self.tableWidget_carregamento.horizontalHeaderItem(23)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("StackedWidget", u"Cliente4", None));
        ___qtablewidgetitem102 = self.tableWidget_carregamento.horizontalHeaderItem(24)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("StackedWidget", u"Cliente5", None));
        ___qtablewidgetitem103 = self.tableWidget_carregamento.horizontalHeaderItem(25)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("StackedWidget", u"Destino", None));
        ___qtablewidgetitem104 = self.tableWidget_carregamento.horizontalHeaderItem(26)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("StackedWidget", u"Destino2", None));
        ___qtablewidgetitem105 = self.tableWidget_carregamento.horizontalHeaderItem(27)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("StackedWidget", u"Destino3", None));
        ___qtablewidgetitem106 = self.tableWidget_carregamento.horizontalHeaderItem(28)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("StackedWidget", u"Destino4", None));
        ___qtablewidgetitem107 = self.tableWidget_carregamento.horizontalHeaderItem(29)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("StackedWidget", u"Destino5", None));
        ___qtablewidgetitem108 = self.tableWidget_carregamento.horizontalHeaderItem(30)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.", None));
        ___qtablewidgetitem109 = self.tableWidget_carregamento.horizontalHeaderItem(31)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.2", None));
        ___qtablewidgetitem110 = self.tableWidget_carregamento.horizontalHeaderItem(32)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.3", None));
        ___qtablewidgetitem111 = self.tableWidget_carregamento.horizontalHeaderItem(33)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.4", None));
        ___qtablewidgetitem112 = self.tableWidget_carregamento.horizontalHeaderItem(34)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.5", None));
        ___qtablewidgetitem113 = self.tableWidget_carregamento.horizontalHeaderItem(35)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("StackedWidget", u"Cavalo", None));
        ___qtablewidgetitem114 = self.tableWidget_carregamento.horizontalHeaderItem(36)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("StackedWidget", u"Carreta", None));
        ___qtablewidgetitem115 = self.tableWidget_carregamento.horizontalHeaderItem(37)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("StackedWidget", u"Motorista", None));
        ___qtablewidgetitem116 = self.tableWidget_carregamento.horizontalHeaderItem(38)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("StackedWidget", u"CPF", None));
        self.btn_cancelar_carregento.setText(QCoreApplication.translate("StackedWidget", u"Cancelar", None))
        self.btn_editar_carregamento.setText(QCoreApplication.translate("StackedWidget", u"Atualizar", None))
        self.btn_gerar_excel_carregamento.setText(QCoreApplication.translate("StackedWidget", u"Gerar Excel", None))
        self.tabWidget_carregamentos.setTabText(self.tabWidget_carregamentos.indexOf(self.tab_demarchi), QCoreApplication.translate("StackedWidget", u"DEMARCHI", None))
        ___qtablewidgetitem117 = self.tableWidget_carregamento_2.horizontalHeaderItem(0)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte", None));
        ___qtablewidgetitem118 = self.tableWidget_carregamento_2.horizontalHeaderItem(1)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte2", None));
        ___qtablewidgetitem119 = self.tableWidget_carregamento_2.horizontalHeaderItem(2)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte3", None));
        ___qtablewidgetitem120 = self.tableWidget_carregamento_2.horizontalHeaderItem(3)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte4", None));
        ___qtablewidgetitem121 = self.tableWidget_carregamento_2.horizontalHeaderItem(4)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("StackedWidget", u"N\u00ba Transporte5", None));
        ___qtablewidgetitem122 = self.tableWidget_carregamento_2.horizontalHeaderItem(5)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.", None));
        ___qtablewidgetitem123 = self.tableWidget_carregamento_2.horizontalHeaderItem(6)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.2", None));
        ___qtablewidgetitem124 = self.tableWidget_carregamento_2.horizontalHeaderItem(7)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.3", None));
        ___qtablewidgetitem125 = self.tableWidget_carregamento_2.horizontalHeaderItem(8)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.4", None));
        ___qtablewidgetitem126 = self.tableWidget_carregamento_2.horizontalHeaderItem(9)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("StackedWidget", u"Data/Hora Planej.5", None));
        ___qtablewidgetitem127 = self.tableWidget_carregamento_2.horizontalHeaderItem(10)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto", None));
        ___qtablewidgetitem128 = self.tableWidget_carregamento_2.horizontalHeaderItem(11)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto2", None));
        ___qtablewidgetitem129 = self.tableWidget_carregamento_2.horizontalHeaderItem(12)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto3", None));
        ___qtablewidgetitem130 = self.tableWidget_carregamento_2.horizontalHeaderItem(13)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto4", None));
        ___qtablewidgetitem131 = self.tableWidget_carregamento_2.horizontalHeaderItem(14)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("StackedWidget", u"Peso Bruto5", None));
        ___qtablewidgetitem132 = self.tableWidget_carregamento_2.horizontalHeaderItem(15)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o", None));
        ___qtablewidgetitem133 = self.tableWidget_carregamento_2.horizontalHeaderItem(16)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o2", None));
        ___qtablewidgetitem134 = self.tableWidget_carregamento_2.horizontalHeaderItem(17)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o3", None));
        ___qtablewidgetitem135 = self.tableWidget_carregamento_2.horizontalHeaderItem(18)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o4", None));
        ___qtablewidgetitem136 = self.tableWidget_carregamento_2.horizontalHeaderItem(19)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("StackedWidget", u"Denomina\u00e7\u00e3o5", None));
        ___qtablewidgetitem137 = self.tableWidget_carregamento_2.horizontalHeaderItem(20)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None));
        ___qtablewidgetitem138 = self.tableWidget_carregamento_2.horizontalHeaderItem(21)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("StackedWidget", u"Cliente2", None));
        ___qtablewidgetitem139 = self.tableWidget_carregamento_2.horizontalHeaderItem(22)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("StackedWidget", u"Cliente3", None));
        ___qtablewidgetitem140 = self.tableWidget_carregamento_2.horizontalHeaderItem(23)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("StackedWidget", u"Cliente4", None));
        ___qtablewidgetitem141 = self.tableWidget_carregamento_2.horizontalHeaderItem(24)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("StackedWidget", u"Cliente5", None));
        ___qtablewidgetitem142 = self.tableWidget_carregamento_2.horizontalHeaderItem(25)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("StackedWidget", u"Destino", None));
        ___qtablewidgetitem143 = self.tableWidget_carregamento_2.horizontalHeaderItem(26)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("StackedWidget", u"Destino2", None));
        ___qtablewidgetitem144 = self.tableWidget_carregamento_2.horizontalHeaderItem(27)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("StackedWidget", u"Destino3", None));
        ___qtablewidgetitem145 = self.tableWidget_carregamento_2.horizontalHeaderItem(28)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("StackedWidget", u"Destino4", None));
        ___qtablewidgetitem146 = self.tableWidget_carregamento_2.horizontalHeaderItem(29)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("StackedWidget", u"Destino5", None));
        ___qtablewidgetitem147 = self.tableWidget_carregamento_2.horizontalHeaderItem(30)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.", None));
        ___qtablewidgetitem148 = self.tableWidget_carregamento_2.horizontalHeaderItem(31)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.2", None));
        ___qtablewidgetitem149 = self.tableWidget_carregamento_2.horizontalHeaderItem(32)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.3", None));
        ___qtablewidgetitem150 = self.tableWidget_carregamento_2.horizontalHeaderItem(33)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.4", None));
        ___qtablewidgetitem151 = self.tableWidget_carregamento_2.horizontalHeaderItem(34)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("StackedWidget", u"C\u00f3d. Processam.5", None));
        ___qtablewidgetitem152 = self.tableWidget_carregamento_2.horizontalHeaderItem(35)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("StackedWidget", u"Cavalo", None));
        ___qtablewidgetitem153 = self.tableWidget_carregamento_2.horizontalHeaderItem(36)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("StackedWidget", u"Carreta", None));
        ___qtablewidgetitem154 = self.tableWidget_carregamento_2.horizontalHeaderItem(37)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("StackedWidget", u"Motorista", None));
        ___qtablewidgetitem155 = self.tableWidget_carregamento_2.horizontalHeaderItem(38)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("StackedWidget", u"CPF", None));
        self.btn_cancelar_carregento_2.setText(QCoreApplication.translate("StackedWidget", u"Cancelar", None))
        self.btn_editar_carregamento_2.setText(QCoreApplication.translate("StackedWidget", u"Atualizar", None))
        self.btn_gerar_excel_carregamento_2.setText(QCoreApplication.translate("StackedWidget", u"Gerar Excel", None))
        self.tabWidget_carregamentos.setTabText(self.tabWidget_carregamentos.indexOf(self.tab_selafort), QCoreApplication.translate("StackedWidget", u"SELAFORT", None))
        self.label_cliente_destino.setText(QCoreApplication.translate("StackedWidget", u"Clientes e Destinos", None))
        self.btn_salvar_cliente.setText(QCoreApplication.translate("StackedWidget", u"Salvar", None))
        self.label_nome_cliente.setText(QCoreApplication.translate("StackedWidget", u"Nome", None))
        self.btn_editar_cliente.setText(QCoreApplication.translate("StackedWidget", u"Editar", None))
        self.btn_excluir_cliente.setText(QCoreApplication.translate("StackedWidget", u"Excluir", None))
        self.label_cidade_cliente.setText(QCoreApplication.translate("StackedWidget", u"Cidade", None))
        self.label_uf_cliente.setText(QCoreApplication.translate("StackedWidget", u"UF", None))
        self.btn_editar_destino.setText(QCoreApplication.translate("StackedWidget", u"Editar", None))
        self.btn_salvar_destino.setText(QCoreApplication.translate("StackedWidget", u"Salvar", None))
        self.btn_excluir_destino.setText(QCoreApplication.translate("StackedWidget", u"Excluir", None))
        self.label_nome_destino.setText(QCoreApplication.translate("StackedWidget", u"Destino", None))
        self.label_cidade_destino.setText(QCoreApplication.translate("StackedWidget", u"Cidade", None))
        self.label_uf_destino.setText(QCoreApplication.translate("StackedWidget", u"UF", None))
        self.label_cliente_3.setText(QCoreApplication.translate("StackedWidget", u"Clientes", None))
        self.label_destino_3.setText(QCoreApplication.translate("StackedWidget", u"Destinos", None))
        ___qtablewidgetitem156 = self.tableWidget_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None));
        ___qtablewidgetitem157 = self.tableWidget_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("StackedWidget", u"Cidade", None));
        ___qtablewidgetitem158 = self.tableWidget_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("StackedWidget", u"UF", None));
        ___qtablewidgetitem159 = self.tableWidget_destino.horizontalHeaderItem(0)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("StackedWidget", u"Destino", None));
        ___qtablewidgetitem160 = self.tableWidget_destino.horizontalHeaderItem(1)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("StackedWidget", u"Cidade", None));
        ___qtablewidgetitem161 = self.tableWidget_destino.horizontalHeaderItem(2)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("StackedWidget", u"UF", None));
        self.label_veiculos.setText(QCoreApplication.translate("StackedWidget", u"Ve\u00edculos", None))
        self.label_placa_veiculo.setText(QCoreApplication.translate("StackedWidget", u"Placa", None))
        self.btn_editar_veiculo.setText(QCoreApplication.translate("StackedWidget", u"Editar", None))
        self.btn_salvar_veiculo.setText(QCoreApplication.translate("StackedWidget", u"Salvar", None))
        self.btn_excluir_veiculo.setText(QCoreApplication.translate("StackedWidget", u"Excluir", None))
        self.btn_editar_veiculo_2.setText(QCoreApplication.translate("StackedWidget", u"Editar", None))
        self.btn_salvar_veiculo_2.setText(QCoreApplication.translate("StackedWidget", u"Salvar", None))
        self.label_placa_veiculo_2.setText(QCoreApplication.translate("StackedWidget", u"Placa", None))
        self.btn_excluir_veiculo_2.setText(QCoreApplication.translate("StackedWidget", u"Excluir", None))
        self.label_cavalo_veiculo.setText(QCoreApplication.translate("StackedWidget", u"Cavalo", None))
        self.label_carreta_veiculo.setText(QCoreApplication.translate("StackedWidget", u"Carreta", None))
        ___qtablewidgetitem162 = self.tableWidget_cavalo_veiculo.horizontalHeaderItem(0)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("StackedWidget", u"Placa", None));
        ___qtablewidgetitem163 = self.tableWidget_carreta_veiculo.horizontalHeaderItem(0)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("StackedWidget", u"Placa", None));
        self.label_motorista.setText(QCoreApplication.translate("StackedWidget", u"Motoristas", None))
        self.label_telefone_motorista.setText(QCoreApplication.translate("StackedWidget", u"Telefone", None))
        self.label_cpf_motorista.setText(QCoreApplication.translate("StackedWidget", u"CPF", None))
        self.label_nome_motorista.setText(QCoreApplication.translate("StackedWidget", u"Nome", None))
        self.btn_editar_motorista.setText(QCoreApplication.translate("StackedWidget", u"Editar", None))
        self.btn_salvar_motorista.setText(QCoreApplication.translate("StackedWidget", u"Salvar", None))
        self.btn_excluir_motorista.setText(QCoreApplication.translate("StackedWidget", u"Excluir", None))
        ___qtablewidgetitem164 = self.tableWidget_motorista.horizontalHeaderItem(0)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("StackedWidget", u"Nome", None));
        ___qtablewidgetitem165 = self.tableWidget_motorista.horizontalHeaderItem(1)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("StackedWidget", u"CPF", None));
        ___qtablewidgetitem166 = self.tableWidget_motorista.horizontalHeaderItem(2)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("StackedWidget", u"Telefone", None));
        self.label_nome_abaixo.setText(QCoreApplication.translate("StackedWidget", u"Copyright: Felipe Germano", None))
    # retranslateUi
