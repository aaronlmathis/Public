from PyQt6 import QtWidgets, QtCore, QtGui

from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QLineEdit, QPushButton, QFormLayout, 
    QVBoxLayout, QLabel, QFrame,
    QHBoxLayout, QSpacerItem, QSizePolicy,
    QMessageBox, QFileDialog
)
from pySQLExport import PySQLExport

class NewConnectionWindow(QMainWindow):
    def __init__(self):
        self.main_app = PySQLExport()
        super(NewConnectionWindow, self).__init__()
       
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
        self.main_layout.addSpacing(20)
        self.renderHLine()
        self.main_layout.addSpacing(20)
        self.renderInfoText()
        self.main_layout.addSpacing(40)

        self.renderForm() # Render form layout
        self.setWindowStyle()

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
        self.username_input.setText("root")
        self.password_input.setText("my-secret-pw")
        self.database_input.setText("employees")

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
         

    def setWindowStyle(self):
        self.setStyleSheet("""

            QLineEdit { padding: 5px;border: 1px solid #ccc;border-radius: 5px;}
            QPushButton {  padding: 5px 10px;background-color: #007bff;color: white;border: none;border-radius: 5px;}
            QPushButton:hover {background-color: #0056b3;}
            QLabel#errorLabel { color: red; }
            QHeaderView::section {
                background-color: #d3d3d3;  /* Gray background for headers */
            }
            QTableView {
                gridline-color: #d3d3d3;  /* Gray grid lines */
            }
            QTableView::item {
                border-left: 1px solid #d3d3d3;  /* Left border of each cell */
                border-right: 1px solid #d3d3d3; /* Right border of each cell */
            }                           
        """)     
    def renderErrorText(self, message):

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("pySQLExport - Error")
        msg_box.setText(message)
        msg_box.exec()            

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
            self.renderErrorText(f"Could not connect: {self.main_app.error}")

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
        self.results = None
        self.columns = None

    def initUI(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)  # Add margins
        self.verticalLayout.setObjectName("verticalLayout")
       
        self.renderTabTable()
        self.renderQueryForm()
        self.renderMenuBar()
        self.setWindowStyle()

    def renderErrorText(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("pySQLExport - Error")
        msg_box.setText(message)
        msg_box.exec()            

    def renderDetailedErrorText(self, e):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("pySQLExport - Error")
        msg.setText("An error occurred:                                            ")
        msg.setInformativeText("Please see the details below.")
        msg.setDetailedText(e)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def renderInfoText(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("pySQLExport - Info")
        msg_box.setText(message)
        msg_box.exec()           

    def renderQueryForm(self):
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setObjectName("formLayout")

        self.label_sql_query = QtWidgets.QLabel(self.centralwidget)
        self.label_sql_query.setObjectName("label_sql_query")

        """self.label_sql_query_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.GeneralFont)
        self.label_sql_query_font.setPointSize(12)  # Ensure the font size is set

        self.label_sql_query_2.setFont(self.label_sql_query_font)
        self.label_sql_query_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # Center the text"""
    
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_sql_query)

        self.text_sql_query = QtWidgets.QTextEdit(self.centralwidget)
        self.text_sql_query.setObjectName("text_sql_query")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.text_sql_query)
        self.verticalLayout.addLayout(self.formLayout, stretch=1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run_query) # Connect to function when pressed

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton)
        
        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.button_layout)    

        #self.verticalLayout.addLayout(self.formLayout_2, stretch=1)

    def renderTabTable(self):
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tab_1_layout = QtWidgets.QVBoxLayout(self.tab_1)  # Create a layout for the tab
        self.tab_1_layout.setContentsMargins(0, 0, 0, 0)  # Optional: set margins for the layout

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_1")
        self.tab_2_layout = QtWidgets.QVBoxLayout(self.tab_2)  # Create a layout for the tab
        self.tab_2_layout.setContentsMargins(0, 0, 0, 0)  # Optional: set margins for the layout

        self.tableViewResults = QtWidgets.QTableView(self.tab_1)
        self.tableViewResults.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.tableViewResults.setObjectName("tableViewResults")
        self.tab_1_layout.addWidget(self.tableViewResults)  # Add the tableView to the layout

        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget, stretch=9)  # Add the tabWidget with stretch factor
        
    def renderMenuBar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        # FILE Menu
        self.menuFile = QtWidgets.QMenu("File", self.menubar)
        self.menuFile.setObjectName("menuFile")

        #New Connection
        self.actionNewConnection = QtGui.QAction("New Connection", self)
        self.actionNewConnection.setObjectName("actionNewConnection")
        self.actionNewConnection.setShortcut(QtGui.QKeySequence('Ctrl+N'))
        self.actionNewConnection.setStatusTip("Create a new connection")
        self.actionNewConnection.triggered.connect(self.newConnection)
        self.menuFile.addAction(self.actionNewConnection)
        
        #Exit
        self.actionExit = QtGui.QAction("Exit", self)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut(QtGui.QKeySequence('Ctrl+Q'))
        self.actionExit.setStatusTip("Close database and exit pySQLExport")        
        self.actionExit.triggered.connect(lambda: self.exitApp())
        self.menuFile.addAction(self.actionExit)        

        #Export Menu
        self.menuExport = QtWidgets.QMenu("Export", self.menubar)
        self.menuExport.setObjectName("menuExport")
        #Export Selection
                
        # Export Selection submenu
        self.menuExportSelection = QtWidgets.QMenu("Export Selection", self.menuExport)
        self.menuExport.addMenu(self.menuExportSelection)

        self.actionExportSelectionToCSV = QtGui.QAction("To CSV", self)
        self.actionExportSelectionToCSV.setStatusTip("Export selected items to CSV format")
        self.actionExportSelectionToCSV.triggered.connect(lambda: self.export("selection", "csv"))
        self.menuExportSelection.addAction(self.actionExportSelectionToCSV)

        self.actionExportSelectionToJSON = QtGui.QAction("To JSON", self)
        self.actionExportSelectionToJSON.setStatusTip("Export selected items to JSON format")
        self.actionExportSelectionToJSON.triggered.connect(lambda: self.export("selection", "json"))
        self.menuExportSelection.addAction(self.actionExportSelectionToJSON)

        self.actionExportSelectionToHTML = QtGui.QAction("To HTML", self)
        self.actionExportSelectionToHTML.setStatusTip("Export selected items to HTML format")
        self.actionExportSelectionToHTML.triggered.connect(lambda: self.export("selection", "html"))
        self.menuExportSelection.addAction(self.actionExportSelectionToHTML)

        self.actionExportSelectionToXML = QtGui.QAction("To XML", self)
        self.actionExportSelectionToXML.setStatusTip("Export selected items to XML format")
        self.actionExportSelectionToXML.triggered.connect(lambda: self.export("selection", "xml"))
        self.menuExportSelection.addAction(self.actionExportSelectionToXML)

        self.actionExportSelectionToExcel = QtGui.QAction("To Excel", self)
        self.actionExportSelectionToExcel.setStatusTip("Export selected items to Excel format")
        self.actionExportSelectionToExcel.triggered.connect(lambda: self.export("selection", "excel"))
        self.menuExportSelection.addAction(self.actionExportSelectionToExcel)

        # Export All submenu
        self.menuExportAll = QtWidgets.QMenu("Export All", self.menuExport)
        self.menuExport.addMenu(self.menuExportAll)

        self.actionExportAllToCSV = QtGui.QAction("To CSV", self)
        self.actionExportAllToCSV.setStatusTip("Export all items to CSV format")
        self.actionExportAllToCSV.triggered.connect(lambda: self.export("all", "csv"))
        self.menuExportAll.addAction(self.actionExportAllToCSV)

        self.actionExportAllToJSON = QtGui.QAction("To JSON", self)
        self.actionExportAllToJSON.setStatusTip("Export all items to JSON format")
        self.actionExportAllToJSON.triggered.connect(lambda: self.export("all", "json"))
        self.menuExportAll.addAction(self.actionExportAllToJSON)

        self.actionExportAllToHTML = QtGui.QAction("To HTML", self)
        self.actionExportAllToHTML.setStatusTip("Export all items to HTML format")
        self.actionExportAllToHTML.triggered.connect(lambda: self.export("all", "html"))
        self.menuExportAll.addAction(self.actionExportAllToHTML)

        self.actionExportAllToXML = QtGui.QAction("To XML", self)
        self.actionExportAllToXML.setStatusTip("Export all items to XML format")
        self.actionExportAllToXML.triggered.connect(lambda: self.export("all", "xml"))
        self.menuExportAll.addAction(self.actionExportAllToXML)

        self.actionExportAllToExcel = QtGui.QAction("To Excel", self)
        self.actionExportAllToExcel.setStatusTip("Export all items to Excel format")
        self.actionExportAllToExcel.triggered.connect(lambda: self.export("all", "excel"))
        self.menuExportAll.addAction(self.actionExportAllToExcel)
       

        #Add MenuFile/MenuExport action to menubar            
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())       

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def export(self, scope, format):
        if self.results and self.columns:
            if format == 'csv':
                # Open a file dialog to choose the save location
                file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv);;All Files (*)")
                if file_path:
                    e = self.main_app.exportToCSV(self.results, self.columns, file_path)
            elif format == 'json':
                 # Open a file dialog to choose the save location
                file_path, _ = QFileDialog.getSaveFileName(self, "Save JSON", "", "JSON Files (*.json);;All Files (*)")
                if file_path:
                    e = self.main_app.exportToJSON(self.results, self.columns, file_path)
            elif format == 'html':
                 # Open a file dialog to choose the save location
                file_path, _ = QFileDialog.getSaveFileName(self, "Save HTML", "", "HTML Files (*.html);;All Files (*)")
                if file_path:
                    e = self.main_app.exportToHTML(self.results, self.columns, file_path)
            elif format == 'xml':
                 # Open a file dialog to choose the save location
                file_path, _ = QFileDialog.getSaveFileName(self, "Save XML", "", "XML Files (*.xml);;All Files (*)")
                if file_path:
                    e = self.main_app.exportToXML(self.results, self.columns, file_path)                                                                                                                      
            elif format == 'excel':
                # Open a file dialog to choose the save location
                file_path, _ = QFileDialog.getSaveFileName(self, "Save Excel", "", "Excel Files (*.xlsx);;All Files (*)")
                if file_path:
                    e = self.main_app.exportToEXCEL(self.results, self.columns, file_path)                  
            if e is True:
                QMessageBox.information(self, "Success", "File was exported successfully.")
            else:
                self.renderDetailedErrorText(f"{e}")
        else:
            self.renderInfoText("Please run a query first.                         ")


    def setWindowStyle(self):
        self.setStyleSheet("""

            QLineEdit { padding: 5px;}
            QPushButton {  padding: 5px 10px;background-color: #007bff;color: white;border: none;border-radius: 5px;}
            QPushButton:hover {background-color: #0056b3;}

            QHeaderView::section {

            }
            QTableView {
                border: 1px solid #fff;
            }
            QTableView::item {

            }                           
        """)     

    def newConnection(self):
        self.main_app.close_db()
        self.connection_window = NewConnectionWindow()
        self.connection_window.show()
        self.close()

    def exitApp(self):
        self.main_app.close_db()
        QApplication.quit()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "pySQLExport"))
        self.label_sql_query.setText(_translate("MainWindow", "Run Query:"))
        self.pushButton.setText(_translate("MainWindow", "Execute Query"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", self.main_app.config['database']))
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "(empty)"))

    def run_query(self):
        query = self.text_sql_query.toPlainText()
        self.results, self.columns = self.main_app.execute_query(query)
        
        self.displayResults(self.results, self.columns)

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