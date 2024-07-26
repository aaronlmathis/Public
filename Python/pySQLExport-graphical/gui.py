from PyQt6 import QtWidgets, QtCore, QtGui

from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QLineEdit, QPushButton, QFormLayout, 
    QVBoxLayout, QLabel, QFrame,
    QHBoxLayout, QSpacerItem, QSizePolicy,
    QMessageBox, QFileDialog, QAbstractItemView
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
        self.submit_button.clicked.connect(self.handleConnect) # Connect to function when pressed
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

    def handleConnect(self):
 
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
        self.init_ui()
        self.setCentralWidget(self.centralwidget)
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.results = None
        self.columns = None
        self.clipboard = {"data": [], "columns": []}        

    def init_ui(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)  # Add margins
        self.verticalLayout.setObjectName("verticalLayout")
       
        self.render_tab_table()
        self.render_query_form()
        self.render_menu_bar()
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

    def render_info_text(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("pySQLExport - Info")
        msg_box.setText(message)
        msg_box.exec()           

    def render_query_form(self):
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.form_layout.setObjectName("form_layout")

        self.label_sql_query = QtWidgets.QLabel(self.centralwidget)
        self.label_sql_query.setObjectName("label_sql_query")

        self.form_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_sql_query)

        self.text_sql_query = QtWidgets.QTextEdit(self.centralwidget)
        self.text_sql_query.setObjectName("text_sql_query")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.text_sql_query)
        self.verticalLayout.addLayout(self.form_layout, stretch=1)
        self.query_button = QtWidgets.QPushButton(self.centralwidget)
        self.query_button.setObjectName("query_button")
        self.query_button.clicked.connect(lambda: self.run_query(self.text_sql_query.toPlainText())) # Connect to function when pressed

        self.form_layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.query_button)

        self.append_check_box = QtWidgets.QCheckBox("Append results of query to existing dataset", self.centralwidget)
        self.append_check_box.setObjectName("append_check_box")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.append_check_box)

        self.duplicates_check_box = QtWidgets.QCheckBox("Allow duplicate rows of data", self.centralwidget)
        self.duplicates_check_box.setObjectName("duplicate_check_box")
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.duplicates_check_box)
        
        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.query_button)
        self.verticalLayout.addLayout(self.button_layout)    

        #self.verticalLayout.addLayout(self.formLayout_2, stretch=1)

    def render_tab_table(self):
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tab_1_layout = QtWidgets.QVBoxLayout(self.tab_1)  # Create a layout for the tab
        self.tab_1_layout.setContentsMargins(0, 0, 0, 0)  # Optional: set margins for the layout

        self.tableView_1 = QtWidgets.QTableView(self.tab_1)
        self.tableView_1.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.tableView_1.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  # Set selection behavior to rows

        self.tableView_1.setObjectName("tableView_1")
        self.tab_1_layout.addWidget(self.tableView_1)  # Add the tableView to the layout

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_1")
        self.tab_2_layout = QtWidgets.QVBoxLayout(self.tab_2)  # Create a layout for the tab
        self.tab_2_layout.setContentsMargins(0, 0, 0, 0)  # Optional: set margins for the layout        
        
        self.tableView_2 = QtWidgets.QTableView(self.tab_1)
        self.tableView_2.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.tableView_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  # Set selection behavior to rows

        self.tableView_2.setObjectName("tableView_2")
        self.tab_2_layout.addWidget(self.tableView_2)  # Add the tableView to the layout

        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget, stretch=9)  # Add the tabWidget with stretch factor
    
    def add_new_tab(self):
        new_tab = QtWidgets.QWidget()
        new_tab.setObjectName(f"tab_{self.tabWidget.count() + 1}")
        new_tab_layout = QtWidgets.QVBoxLayout(new_tab)
        new_tab_layout.setContentsMargins(0, 0, 0, 0)

        new_table_view = QtWidgets.QTableView(new_tab)
        new_table_view.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        new_table_view.setObjectName(f"tableView_{self.tabWidget.count() + 1}")
        new_tab_layout.addWidget(new_table_view)

        self.tabWidget.addTab(new_tab, f"Tab {self.tabWidget.count() + 1}")

    def render_menu_bar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        # FILE Menu
        self.menu_file = QtWidgets.QMenu("File", self.menubar)
        self.menu_file.setObjectName("menu_file")

        #New Connection
        self.action_new_connection = QtGui.QAction("New Connection", self)
        self.action_new_connection.setObjectName("action_new_connection")
        self.action_new_connection.setShortcut(QtGui.QKeySequence('Ctrl+N'))
        self.action_new_connection.setStatusTip("Create a new connection")
        self.action_new_connection.triggered.connect(self.new_connection)
        self.menu_file.addAction(self.action_new_connection)

        #Copy
        self.action_copy = QtGui.QAction("Copy", self)
        self.action_copy.setObjectName("action_copy")
        self.action_copy.setShortcut(QtGui.QKeySequence('Ctrl+C'))
        self.action_copy.setStatusTip("Copy selected rows")
        self.action_copy.triggered.connect(self.copy_selected)
        self.menu_file.addAction(self.action_copy)

        #Paste
        self.action_paste = QtGui.QAction("Paste", self)
        self.action_paste.setObjectName("action_paste")
        self.action_paste.setShortcut(QtGui.QKeySequence('Ctrl+V'))
        self.action_paste.setStatusTip("Paste selection into current table")
        self.action_paste.triggered.connect(self.paste_selected)
        self.menu_file.addAction(self.action_paste)

        #Exit
        self.action_exit = QtGui.QAction("Exit", self)
        self.action_exit.setObjectName("action_exit")
        self.action_exit.setShortcut(QtGui.QKeySequence('Ctrl+Q'))
        self.action_exit.setStatusTip("Close database and exit pySQLExport")        
        self.action_exit.triggered.connect(lambda: self.exit_app())
        self.menu_file.addAction(self.action_exit)        

        #Export Menu
        self.menu_export = QtWidgets.QMenu("Export", self.menubar)
        self.menu_export.setObjectName("menu_export")
        #Export Selection
                
        # Export Selection submenu
        self.menu_export_selection = QtWidgets.QMenu("Export Selection", self.menu_export)
        self.menu_export.addMenu(self.menu_export_selection)

        self.action_export_selection_to_csv = QtGui.QAction("To CSV", self)
        self.action_export_selection_to_csv.setStatusTip("Export selected items to CSV format")
        self.action_export_selection_to_csv.triggered.connect(lambda: self.export("selection", "csv"))
        self.menu_export_selection.addAction(self.action_export_selection_to_csv)

        self.action_export_selection_to_json = QtGui.QAction("To JSON", self)
        self.action_export_selection_to_json.setStatusTip("Export selected items to JSON format")
        self.action_export_selection_to_json.triggered.connect(lambda: self.export("selection", "json"))
        self.menu_export_selection.addAction(self.action_export_selection_to_json)

        self.action_export_selection_to_html = QtGui.QAction("To HTML", self)
        self.action_export_selection_to_html.setStatusTip("Export selected items to HTML format")
        self.action_export_selection_to_html.triggered.connect(lambda: self.export("selection", "html"))
        self.menu_export_selection.addAction(self.action_export_selection_to_html)

        self.action_export_selection_to_xml = QtGui.QAction("To XML", self)
        self.action_export_selection_to_xml.setStatusTip("Export selected items to XML format")
        self.action_export_selection_to_xml.triggered.connect(lambda: self.export("selection", "xml"))
        self.menu_export_selection.addAction(self.action_export_selection_to_xml)

        self.actionExportSelectionToExcel = QtGui.QAction("To Excel", self)
        self.actionExportSelectionToExcel.setStatusTip("Export selected items to Excel format")
        self.actionExportSelectionToExcel.triggered.connect(lambda: self.export("selection", "excel"))
        self.menu_export_selection.addAction(self.actionExportSelectionToExcel)

        # Export All submenu
        self.menu_export_all = QtWidgets.QMenu("Export All", self.menu_export)
        self.menu_export.addMenu(self.menu_export_all)

        self.action_export_all_to_csv = QtGui.QAction("To CSV", self)
        self.action_export_all_to_csv.setStatusTip("Export all items to CSV format")
        self.action_export_all_to_csv.triggered.connect(lambda: self.export("all", "csv"))
        self.menu_export_all.addAction(self.action_export_all_to_csv)

        self.action_export_all_to_json = QtGui.QAction("To JSON", self)
        self.action_export_all_to_json.setStatusTip("Export all items to JSON format")
        self.action_export_all_to_json.triggered.connect(lambda: self.export("all", "json"))
        self.menu_export_all.addAction(self.action_export_all_to_json)

        self.action_export_all_to_html = QtGui.QAction("To HTML", self)
        self.action_export_all_to_html.setStatusTip("Export all items to HTML format")
        self.action_export_all_to_html.triggered.connect(lambda: self.export("all", "html"))
        self.menu_export_all.addAction(self.action_export_all_to_html)

        self.action_export_all_to_xml = QtGui.QAction("To XML", self)
        self.action_export_all_to_xml.setStatusTip("Export all items to XML format")
        self.action_export_all_to_xml.triggered.connect(lambda: self.export("all", "xml"))
        self.menu_export_all.addAction(self.action_export_all_to_xml)

        self.action_export_all_to_excel = QtGui.QAction("To Excel", self)
        self.action_export_all_to_excel.setStatusTip("Export all items to Excel format")
        self.action_export_all_to_excel.triggered.connect(lambda: self.export("all", "excel"))
        self.menu_export_all.addAction(self.action_export_all_to_excel)
       

        #Add MenuFile/MenuExport action to menubar            
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_export.menuAction())       

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def is_tableview_empty(self, table_view):
        model = table_view.model()
        if model is None:
            return True  # If there is no model, consider the table view empty
    
        return model.rowCount() == 0  

    def copy_selected(self):
        table_view = self.get_active_tableview()
        
        if self.is_tableview_empty(table_view):
            self.render_info_text("Please run a query first.                         ") 
            return

        results, columns = self.get_selected_rows(table_view)
            
        if not results or not columns:
            self.render_info_text("Please make a valid selection.                        ")
            return
        
        if results:
            self.clipboard["data"] = results
            self.clipboard["columns"] = columns
            self.render_info_text("Selection copied to clipboard.")    
          
    def paste_selected(self):
        active_table_view = self.get_active_tableview()
        if active_table_view and self.clipboard["data"]:
            model = active_table_view.model()
            
            if model is None:
                model = QtGui.QStandardItemModel()
                model.setHorizontalHeaderLabels(self.clipboard["columns"])
                active_table_view.setModel(model)
        
            # Check for selected rows and remove them
            selection_model = active_table_view.selectionModel()
            selected_indexes = selection_model.selectedRows()

            if selected_indexes:
                rows_to_remove = sorted([index.row() for index in selected_indexes], reverse=True)
                for row in rows_to_remove:
                    model.removeRow(row)                
            
            for row in self.clipboard["data"]:
                items = [QtGui.QStandardItem(str(field)) for field in row]
                for item in items:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                model.appendRow(items)
            
            header = active_table_view.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

            self.render_info_text("Clipboard pasted to the current table.")
        else:
            self.render_info_text("Clipboard is empty or no active table view.")


    def export(self, scope, format):
        active_table_view = self.get_active_tableview()
        
        if self.is_tableview_empty(active_table_view):
            self.render_info_text("Please run a query first.                         ")
            return

        if scope == 'all':
            results, columns = self.get_all_rows(active_table_view)
        elif scope == 'selection':
            results, columns = self.get_selected_rows(active_table_view)
            
            if not results or not columns:
                self.render_info_text("Please make a valid selection.                        ")
                return        
       

        if format == 'csv':
            # Open a file dialog to choose the save location
            file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv);;All Files (*)")
            if file_path:
                e = self.main_app.exportToCSV(results, columns, file_path)
        elif format == 'json':
            # Open a file dialog to choose the save location
            file_path, _ = QFileDialog.getSaveFileName(self, "Save JSON", "", "JSON Files (*.json);;All Files (*)")
            if file_path:
                e = self.main_app.exportToJSON(results, columns, file_path)
        elif format == 'html':
            # Open a file dialog to choose the save location
            file_path, _ = QFileDialog.getSaveFileName(self, "Save HTML", "", "HTML Files (*.html);;All Files (*)")
            if file_path:
                e = self.main_app.exportToHTML(results, columns, file_path)
        elif format == 'xml':
            # Open a file dialog to choose the save location
            file_path, _ = QFileDialog.getSaveFileName(self, "Save XML", "", "XML Files (*.xml);;All Files (*)")
            if file_path:
                e = self.main_app.exportToXML(results, columns, file_path)                                                                                                                      
        elif format == 'excel':
            # Open a file dialog to choose the save location
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Excel", "", "Excel Files (*.xlsx);;All Files (*)")
            if file_path:
                e = self.main_app.exportToEXCEL(results, columns, file_path)                  
        
        if e is True:
            QMessageBox.information(self, "Success", "File was exported successfully.")
        else:
            self.renderDetailedErrorText(f"{e}")
                      

    def get_selected_rows(self, table_view):

        selection_model = table_view.selectionModel()
        selected_rows = selection_model.selectedRows()

        # Get the model associated with the QTableView
        model = table_view.model()

        # Initialize results and columns
        selected_results = []
        selected_columns = [model.headerData(i, QtCore.Qt.Orientation.Horizontal) for i in range(model.columnCount())]

        # Extract data from selected rows
        for row_index in selected_rows:
            row_data = []
            for column_index in range(model.columnCount()):
                index = model.index(row_index.row(), column_index)
                row_data.append(model.data(index))
            selected_results.append(row_data)
        
        return selected_results, selected_columns
    
    def get_all_rows(self, table_view):
        model = table_view.model()
        if model is None:
            return [], []

        results = []
        columns = [model.headerData(i, QtCore.Qt.Orientation.Horizontal) for i in range(model.columnCount())]

        for row in range(model.rowCount()):
            row_data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                row_data.append(model.data(index))
            results.append(row_data)

        return results, columns        

    def get_active_tableview(self):
        current_index = self.tabWidget.currentIndex()
        current_tab = self.tabWidget.widget(current_index)
        table_view = current_tab.findChild(QtWidgets.QTableView, f"tableView_{current_index + 1}")
        return table_view        




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

    def new_connection(self):
        self.main_app.close_db()
        self.connection_window = NewConnectionWindow()
        self.connection_window.show()
        self.close()

    def exit_app(self):
        self.main_app.close_db()
        QApplication.quit()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "pySQLExport"))
        self.label_sql_query.setText(_translate("MainWindow", "Run Query:"))
        self.query_button.setText(_translate("MainWindow", "Execute Query"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Query 1"))
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "(empty)"))

    def run_query(self, query):
        if query:
            success, result_or_error, columns = self.main_app.execute_query(query)
            if success:
                results = result_or_error
                append = self.append_check_box.isChecked()
                self.display_results(results, columns, append)
                self.text_sql_query.setPlainText("")
            else:
                self.renderErrorText(f"Failed to execute query: {result_or_error}")
        else:
            self.render_info_text("Query cannot be empty.          ")

    def display_results(self, results, columns, append=False):
        table_view = self.get_active_tableview()  # Get the active table view
        model = table_view.model()

        if model is None or not append:
            model = QtGui.QStandardItemModel()
            model.setHorizontalHeaderLabels(columns)
            table_view.setModel(model)
        else:
            existing_columns = model.columnCount()
            for i, column in enumerate(columns):
                if i >= existing_columns:
                    model.setHorizontalHeaderItem(i, QtGui.QStandardItem(column))

        for row in results:
            items = [QtGui.QStandardItem(str(field)) for field in row]
            for item in items:
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)  # Make item non-editable
            model.appendRow(items)

        header = table_view.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)