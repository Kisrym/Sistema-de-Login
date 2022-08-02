from PyQt5 import uic, QtWidgets
import mysql.connector as mysql

db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'SENHA',
    database = 'login'
)

cursor = db.cursor()

class login_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(login_window, self).__init__()
        uic.loadUi(r'janelas\login.ui', self)
        widget.setWindowTitle("Login com MySQL")
        
        self.button_registrar.clicked.connect(self.mudar_janela)
        self.button_entrar.clicked.connect(self.entrar)
        
    def entrar(self):
        nome = self.Nome.text()
        senha = self.Senha.text()
        # Criando a janela de confirmação
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Login")
        
        if self.Nome.text() == '' or self.Senha.text() == '':             
            msg.setText("Preencha todos os campos.")
        
        #! Comando SQL
        else:
            cursor.execute(f'SELECT `LOGIN`, `PASSWORD` FROM dados WHERE `LOGIN` = "{nome}" AND `PASSWORD` = "{senha}";')

            # Se o SELECT não retornar nada, o usuário não existe
            if len(cursor.fetchall()) == 0:
                msg.setText("Usuário ou senha incorretos.")
            
            else:
                msg.setText("Bem vindo de volta!")
                
        msg.exec()
    def mudar_janela(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
        
class register_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(register_window, self).__init__()
        uic.loadUi(r'janelas\register.ui', self)
        widget.setWindowTitle("Register com MySQL")
        
        self.button_criar.clicked.connect(self.criar_usuario)
        
    def criar_usuario(self):
        # Criando a janela de confirmação
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Registro")
        
        if self.Nome.text() == '' or self.Senha.text() == '':
            msg.setText("Preencha todos os campos.") 
        
        else:
            msg.setText("Registrado com sucesso!")
            
            #! Comando SQL
            cursor.execute(f'INSERT INTO dados (`LOGIN`, `PASSWORD`) VALUES ("{self.Nome.text()}", "{self.Senha.text()}");')
            db.commit()
            
            msg.buttonClicked.connect(self.mudar_janela)
        
        msg.exec()
        
    def mudar_janela(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


app = QtWidgets.QApplication([])
widget = QtWidgets.QStackedWidget()

login = login_window()
register = register_window()

# Adicionando as janelas ao stackedWidget
widget.addWidget(login)
widget.addWidget(register)
widget.setFixedSize(444, 358)

widget.show()
app.exec()