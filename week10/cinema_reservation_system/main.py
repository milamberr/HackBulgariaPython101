from database_layer.dbconnector import DBConnector
from view.menu import Menu


def main():
    db = DBConnector()
    db.create_database()
    Menu().start()


if __name__ == "__main__":
    main()
