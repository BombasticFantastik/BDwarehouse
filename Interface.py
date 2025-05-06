import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit


class Third_Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Warehouse")
        self.setGeometry(256, 256, 512, 256)

        #id/name

        self.p_label=QLabel('id:')
        self.g_label=QLabel('name:')
        self.p_input=QLineEdit()
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
        self.button_get_A = QPushButton("Добавить", self)
        self.button_get_B = QPushButton("Удалить", self)


        #левый
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.p_label)
        left_layout.addWidget(self.p_input)

        left_layout.addWidget(self.a_label)
        left_layout.addWidget(self.a_input)

        left_layout.addWidget(self.A_label)
        left_layout.addWidget(self.A_input)
        
        left_layout.addWidget(self.K_label_left)
        left_layout.addWidget(self.K_input_left)

        left_layout.addWidget(self.reor_label_left)
        left_layout.addWidget(self.reor_input_left)

        left_layout.addWidget(self.button_get_A)


        

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
        

        right_layout.addWidget(self.button_get_B)


        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)
app = QApplication(sys.argv)
window = Third_Window()
window.show()
sys.exit(app.exec())