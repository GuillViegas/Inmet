DEBUG = True

DB_CREDENCIAL = {'database': 'inmet', 'port': 5432, 'host': 'localhost', 'password': '123456', 'user': 'postgres'}

SQLALCHEMY_DATABASE_URI = 'postgres://{user}:{password}@{host}:{port}/{database}'.format(**DB_CREDENCIAL)

PATH_STATIONS_FILE = '/Users/viegas/Documents/python/meteo/INMET/stations.csv'

PATH_MENSURATIONS_FILES = '/Users/viegas/Documents/python/meteo/INMET'