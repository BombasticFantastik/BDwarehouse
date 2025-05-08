from sqlalchemy import create_engine
import psycopg2
from PyQt6.QtWidgets import QApplication
from Interface import Warehouse_window
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base



engine=create_engine('postgresql+psycopg2://postgres:12345@localhost/Norwind')
connection=engine.connect()


#metadata = MetaData()

app = QApplication(sys.argv)
window = Warehouse_window(connection)
window.show()
sys.exit(app.exec())