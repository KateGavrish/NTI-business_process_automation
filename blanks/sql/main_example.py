from data import db_session


# подключение к существующей бд или создание новой
def main():
    db_session.global_init("db/blogs.sqlite")


if __name__ == '__main__':
    main()