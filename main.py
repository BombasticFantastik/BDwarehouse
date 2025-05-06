from sqlalchemy import create_engine,Column,Integer,String,Float,Table,MetaData,insert,delete,update
import psycopg2
import abc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base



engine=create_engine('postgresql+psycopg2://postgres:12345@localhost/pis_base')
engine.connect()

metadata = MetaData()