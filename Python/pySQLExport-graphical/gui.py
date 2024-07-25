from PyQt6 import QtWidgets, QtCore, QtGui

from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QLineEdit, QPushButton, QFormLayout, 
    QVBoxLayout, QLabel, QFrame,
    QHBoxLayout, QSpacerItem, QSizePolicy
)
from pySQLExport import PySQLExport

class LoginWindow(QMainWindow):
    def __init__(self):
        self.main_app = PySQLExport()
        super(LoginWindow, self).__init__()
       
        # Set window geometry and title        
        self.setGeometry(200, 200, 400, 200)  
        self.setWindowTitle("pySQLExport")

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(self.central_widget)  # Set the central widget

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(40, 20, 40, 20)  # Set margins (left, top, right, bottom)
        self.central_widget.setLayout(self.main_layout)

        self.renderHeader()
        self.main_layout.addSpacing(0)
        self.renderHLine()
        self.renderInfoText()
        self.renderErrorText()
        self.renderForm() # Render form layout

    def renderHLine(self):
        # Add a horizontal line separator
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(line)

    def renderHeader(self):
      # Create and add header text
        self.header_label = QLabel("pySQLExport")
        self.header_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.TitleFont)
        self.header_font.setPointSize(48)  # Ensure the font size is set
        self.header_font.setBold(True)  # Ensure the font weight is set to bold
        self.header_label.setFont(self.header_font)
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Center the text
        self.main_layout.addWidget(self.header_label)

        self.version_label = QLabel('version 0.1.4')
        self.version_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.SmallestReadableFont)
        self.version_font.setPointSize(14)  # Ensure the font size is set
        self.version_label.setFont(self.version_font)
        self.version_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Center the text        
        self.main_layout.addWidget(self.version_label)

    def renderInfoText(self):
        # Add informative text
        self.info_label = QLabel("Please enter database server details in order to connect to a database.")
        self.info_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.GeneralFont)
        self.info_font.setPointSize(12)  # Ensure the font size is set
        self.info_label.setFont(self.info_font)
        self.info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Center the text
        self.info_label.setContentsMargins(0, 20, 0, 0)        
        self.main_layout.addWidget(self.info_label)

    def renderForm(self):
        self.form_layout = QFormLayout()
        self.form_layout.setContentsMargins(0, 0, 0, 0)  # Set margins (left, top, right, bottom)
        self.form_layout.setSpacing(10)  # Set spacing between form elements
        self.central_widget.setLayout(self.form_layout)  # Set the layout on the central widget

        # Create and add form elements
        self.server_input = QLineEdit()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.database_input = QLineEdit()
        self.port_input = QLineEdit()
        self.port_input.setText("3306")
        self.port_input.setMaxLength(5)  # Limit input to 8 characters
        self.port_input.setFixedWidth(50)  # Set a fixed width appropriate for 5 characters
        self.server_input.setText("localhost")
        self.username_input.setText("aaron")
        self.password_input.setText("")
        self.database_input.setText("classicmodels")

        self.form_layout.addRow("Server:", self.server_input)
        self.form_layout.addRow("Username:", self.username_input)
        self.form_layout.addRow("Password:", self.password_input)
        self.form_layout.addRow("Database:", self.database_input)
        self.form_layout.addRow("Port:", self.port_input)

        #Add form to main layout
        self.main_layout.addLayout(self.form_layout)

        # Create and add a submit button
        # Create and configure the establish connection button
        self.submit_button = QPushButton("Establish Connection")
        self.submit_button.clicked.connect(self.handle_login) # Connect to function when pressed
        self.submit_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        # Create a horizontal layout to center the button
        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.submit_button)
        self.main_layout.addLayout(self.button_layout)        
        # Apply styles
        self.setStyleSheet("""

            QLineEdit { padding: 5px;border: 1px solid #ccc;border-radius: 5px;}
            QPushButton {  padding: 5px 10px;background-color: #007bff;color: white;border: none;border-radius: 5px;}
            QPushButton:hover {background-color: #0056b3;}
            QLabel#errorLabel { color: red; }
        """)            

    def renderErrorText(self):
        self.error_label = QLabel("")
        self.error_label.setObjectName("errorLabel")
        self.error_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.SmallestReadableFont)
        self.error_font.setPointSize(12)  # Ensure the font size is set
        self.error_label.setFont(self.error_font)
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # Center the text
        self.main_layout.addWidget(self.error_label)        

    def handle_login(self):
        # Handle login logic here
        username = self.username_input.text()
        password = self.password_input.text()
        database = self.database_input.text()
        port = self.port_input.text()
        server = self.server_input.text()

        if self.main_app.connect_db(server, username, password, database, port):
            # Assuming the login is successful
            self.main_window = MainWindow(self.main_app)
            self.main_window.show()
            self.close()
        else:
            self.error_label.setText("Error: Could not connect to the database. Please try again.")

class MainWindow(QMainWindow):
    def __init__(self, main_app):
        super(MainWindow, self).__init__()
        self.main_app = main_app
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("pySQLExport")
        self.initUI()
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def initUI(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)  # Add margins
        self.verticalLayout.setObjectName("verticalLayout")

        self.renderQueryForm()
        self.renderTabTable()
        self.renderMenuBar()

    def renderQueryForm(self):
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label_sql_query_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sql_query_2.setObjectName("label_sql_query_2")

        self.label_sql_query_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.TitleFont)
        self.label_sql_query_font.setPointSize(16)  # Ensure the font size is set
        self.label_sql_query_font.setBold(True)  # Ensure the font weight is set to bold
        self.label_sql_query_2.setFont(self.label_sql_query_font)
        self.label_sql_query_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Center the text
    
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_sql_query_2)

        self.text_sql_query = QtWidgets.QTextEdit(self.centralwidget)
        self.text_sql_query.setObjectName("text_sql_query")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.text_sql_query)
        self.verticalLayout.addLayout(self.formLayout_2, stretch=1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run_query) # Connect to function when pressed

        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton)
        self.setStyleSheet("""

            QLineEdit { padding: 5px;border: 1px solid #ccc;border-radius: 5px;}
            QPushButton {  padding: 5px 10px;background-color: #007bff;color: white;border: none;border-radius: 5px;}
            QPushButton:hover {background-color: #0056b3;}
            QLabel#errorLabel { color: red; }
        """) 
        self.button_layout2 = QHBoxLayout()
        self.button_layout2.addStretch()
        self.button_layout2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.button_layout2)    

        #self.verticalLayout.addLayout(self.formLayout_2, stretch=1)

    def renderTabTable(self):
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab_3_layout = QtWidgets.QVBoxLayout(self.tab_3)  # Create a layout for the tab
        self.tab_3_layout.setContentsMargins(0, 0, 0, 0)  # Optional: set margins for the layout

        self.tableViewResults = QtWidgets.QTableView(self.tab_3)
        self.tableViewResults.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.tableViewResults.setObjectName("tableViewResults")
        self.tab_3_layout.addWidget(self.tableViewResults)  # Add the tableView to the layout

        self.tabWidget.addTab(self.tab_3, "")

       # self.tab_4 = QtWidgets.QWidget()
        #self.tab_4.setObjectName("tab_4")
        #self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget, stretch=9)  # Add the tabWidget with stretch factor
        
    def renderMenuBar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "pySQLExport"))
        self.label_sql_query_2.setText(_translate("MainWindow", "SQL Query"))
        self.pushButton.setText(_translate("MainWindow", "Execute Query"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Results"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))

    def run_query(self):
        query = self.text_sql_query.toPlainText()
        results, columns = self.main_app.execute_query(query)
        
        self.displayResults(results, columns)

    def displayResults(self, results, columns):
        model = QtGui.QStandardItemModel()
        
        model.setHorizontalHeaderLabels(columns)

        for row in results:
            items = [QtGui.QStandardItem(str(field)) for field in row]
            for item in items:
                
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)  # Make item non-editable
            model.appendRow(items)

        self.tableViewResults.setModel(model)
        header = self.tableViewResults.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)