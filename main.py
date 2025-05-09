from sqlalchemy import create_engine
import psycopg2
from PyQt6.QtWidgets import QApplication
from Interface import Warehouse_window
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import yaml

option_path='config.yaml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)


engine=create_engine(option['path'])
connection=engine.connect()


#metadata = MetaData()

app = QApplication(sys.argv)
window = Warehouse_window(connection)
window.show()
sys.exit(app.exec())