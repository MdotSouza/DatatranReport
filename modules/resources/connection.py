from sqlalchemy import create_engine

class Conn:
    def __init__(self):
        USER, PSWD, HOST, DB = "postgres", "postgres", "localHOST", "postgres"
        self.__engine = create_engine(f"postgresql+psycopg2://{USER}:{PSWD}@{HOST}/{DB}")
        return self.__engine