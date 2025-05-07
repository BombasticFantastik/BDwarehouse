import sys

from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit,QTableWidget
from sqlalchemy import create_engine,Column,Integer,String,Float,Table,MetaData,insert,delete,update,text

class Warehouse_window(QWidget):
    def __init__(self,connection):
        super().__init__()
        self.connection=connection
        self.setWindowTitle("Warehouse")
        #self.setGeometry(256, 256, 512, 256)
        self.setFixedSize(1280,500)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(1050,387)
        self.table.setRowCount(50)
        self.table.setColumnCount(10)

        #id/name

        self.p_label=QLabel('id:')
        self.g_label=QLabel('name:')
        self.id_input=QLineEdit()
        self.g_input=QLineEdit()


        #sup/cat_id
        self.a_label=QLabel('sup_id:')
        self.b_label=QLabel('cat_id:')
        self.a_input=QLineEdit()
        self.b_input=QLineEdit()

        #quant/unit_price
        self.A_label=QLabel('quant_per_unit:')
        self.B_label=QLabel('unit_price:')
        self.A_input=QLineEdit()
        self.B_input=QLineEdit()

        #units_in_stock/order
        self.K_label_left=QLabel('units_in_stock:')
        self.K_label_right=QLabel('units_in_order:')
        self.K_input_left=QLineEdit()
        self.K_input_right=QLineEdit()

        #reor/disc
        self.reor_label_left=QLabel('reorder_level:')
        self.disc_label_right=QLabel('discounted:')
        self.reor_input_left=QLineEdit()
        self.disc_input_right=QLineEdit()

        #Добавить/Удалить/Найти
        self.button_Add = QPushButton("Добавить", self)
        self.button_Remove = QPushButton("Удалить", self)
        self.button_Select=QPushButton('Выбрать',self)

        #задаём размеры


        self.p_label.setFixedSize(50,20)
        self.g_label.setFixedSize(50,20)
        self.a_label.setFixedSize(50,20)
        self.b_label.setFixedSize(50,20)
        self.A_label.setFixedSize(50,20)
        self.B_label.setFixedSize(50,20)
        self.K_label_left.setFixedSize(50,20)
        self.K_label_right.setFixedSize(50,20)
        self.reor_label_left.setFixedSize(50,20)
        self.disc_label_right.setFixedSize(50,20)
        

        self.id_input.setFixedSize(100,35)
        self.g_input.setFixedSize(100,35)
        self.a_input.setFixedSize(100,35)
        self.b_input.setFixedSize(100,35)
        self.A_input.setFixedSize(100,35)
        self.B_input.setFixedSize(100,35)
        self.K_input_left.setFixedSize(100,35)
        self.K_input_right.setFixedSize(100,35)
        self.reor_input_left.setFixedSize(100,35)
        self.disc_input_right.setFixedSize(100,35)


        #левый
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.p_label)
        left_layout.addWidget(self.id_input)

        left_layout.addWidget(self.a_label)
        left_layout.addWidget(self.a_input)

        left_layout.addWidget(self.A_label)
        left_layout.addWidget(self.A_input)
        
        left_layout.addWidget(self.K_label_left)
        left_layout.addWidget(self.K_input_left)

        left_layout.addWidget(self.reor_label_left)
        left_layout.addWidget(self.reor_input_left)

        left_layout.addWidget(self.button_Add)
        

        #правый
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.g_label)
        right_layout.addWidget(self.g_input)

        right_layout.addWidget(self.b_label)
        right_layout.addWidget(self.b_input)

        right_layout.addWidget(self.B_label)
        right_layout.addWidget(self.B_input)
        
        right_layout.addWidget(self.K_label_right)
        right_layout.addWidget(self.K_input_right)
        
        right_layout.addWidget(self.disc_label_right)
        right_layout.addWidget(self.disc_input_right)

        right_layout.addWidget(self.button_Remove)

        #table
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)

        table_layout.addWidget(self.button_Select)

        #кнопки
        self.button_Add.clicked.connect(self.add)
        self.button_Remove.clicked.connect(self.remove)
        self.button_Select.clicked.connect(self.select)


        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        main_layout.addLayout(table_layout)
        self.setLayout(main_layout)

    def add(self):
        self.connection.execute(f"INSERT INTO products VALUES ({self.id_input.text},{self.g_input.text},{self.a_input.text},{self.b_input.text},{self.A_input.text},{self.B_input.text},{self.K_input_left.text},{self.K_input_right.text})")
    def remove(self):
        self.connection.execute(f"DELETE FROM products WHERE product_id={self.id_input.text}")
    def select(self):
        a=self.connection.execute(text('SELECT * FROM products'))
        print(1)
