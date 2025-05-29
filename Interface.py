import sys

from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit,QTableWidget,QTableWidgetItem
from sqlalchemy import create_engine,Column,Integer,String,Float,Table,MetaData,insert,delete,update,text

class Warehouse_window(QWidget):
    def __init__(self,connection):
        super().__init__()
        self.connection=connection
        self.setWindowTitle("Warehouse")
        self.setFixedSize(1280,500)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(1060,387)
        self.table.setRowCount(100)
        self.table.setColumnCount(10)
        self.get_names()


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

    def get_names(self):
            self.table.setHorizontalHeaderLabels([
            'product_id',
            'product_name',
            'supplier_id',
            'category_id',
            'quantity_per_unit',
            'unit_price',
            'units_in_stock',
            'units_on_order',
            'reorder_level',
            'discontinued'
        ])

    def add(self):
        self.connection.execute(text(f"INSERT INTO products VALUES ({self.id_input.text()},'{self.g_input.text()}',{self.a_input.text()},{self.b_input.text()},'{self.A_input.text()}',{self.B_input.text()},{self.K_input_left.text()},{self.K_input_right.text()},{self.reor_input_left.text()},{self.disc_input_right.text()})"))
        self.connection.commit()
        self.select()
        
    def remove(self):
        self.connection.execute(text(f"DELETE FROM products WHERE product_id={self.id_input.text()}"))
        self.id_input.setText('')
        self.connection.commit()
        self.select()
    def select(self):
        command=f"SELECT * FROM products WHERE product_id= {self.id_input.text()} AND product_name LIKE '{self.g_input.text()}%' AND supplier_id= {self.a_input.text()} AND category_id= {self.b_input.text()} AND quantity_per_unit LIKE '{self.A_input.text()}%' AND unit_price= {self.B_input.text()} AND units_in_stock= {self.K_input_left.text()} AND units_on_order= {self.K_input_right.text()} AND reorder_level= {self.reor_input_left.text()} AND discontinued= {self.disc_input_right.text()} "

        command=command.replace('product_id=  ',' ').replace('supplier_id=  ',' ').replace('category_id=  ',' ').replace('unit_price=  ',' ').replace('units_in_stock=  ',' ').replace('units_on_order=  ',' ').replace('reorder_level=  ',' ').replace('discontinued=  ',' ')

        command=command.replace('  AND','').replace('AND  ','')
       
        data=self.connection.execute(text(command))
        self.show_table(data)
        
    def show_table(self,data):
        self.table.clear()
        data=[row for row in data]
        for i in range(len(data)):
            prod_id=QTableWidgetItem(str(data[i].product_id))
            prod_name=QTableWidgetItem(str(data[i].product_name))
            sup_id=QTableWidgetItem(str(data[i].supplier_id))
            cat_id=QTableWidgetItem(str(data[i].category_id))
            quant=QTableWidgetItem(str(data[i].quantity_per_unit))
            price=QTableWidgetItem(str(data[i].unit_price))
            in_stock=QTableWidgetItem(str(data[i].units_in_stock))
            on_order=QTableWidgetItem(str(data[i].units_on_order))
            level=QTableWidgetItem(str(data[i].reorder_level))
            disc=QTableWidgetItem(str(data[i].discontinued))

            self.table.setItem(i,0,prod_id)
            self.table.setItem(i,1,prod_name)
            self.table.setItem(i,2,sup_id)
            self.table.setItem(i,3,cat_id)
            self.table.setItem(i,4,quant)
            self.table.setItem(i,5,price)
            self.table.setItem(i,6,in_stock)
            self.table.setItem(i,7,on_order)
            self.table.setItem(i,8,level)
            self.table.setItem(i,9,disc)

        self.table.show()
        self.get_names()
            

