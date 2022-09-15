import psycopg2
from pg_config import host, user, password, db_name


def postgres(query = 'select 1'):
     # Подключаемся к БД. (Реквизиты подключения указаны в файле pg_config.py)
     try:
          connection = psycopg2.connect(
               host = host,
               user = user,
               password = password,
               database = db_name
          )
          connection.autocommit = True # Выставляем автоматический commit
     
     # Пишем наш запрос к БД
          with connection.cursor() as cursor:
               cursor.execute(
                    f"""{query}"""
               )
               # print(cursor.fetchall()) # Выводим на экран результат нашего запроса  fetchall() - все строки, fetchone() - первая строка,  fetcmany(x) указываем сколько строк
               return cursor.fetchall()
               

     # Обрабатываем ошибки
     except psycopg2.ProgrammingError: # так как данная функция возвращает значения, при инсерте делите и апдейте - значения не возвращаются. Следовательно - ошибка
          pass

     except Exception as _ex:
          print('[INFO] Error while working with PostgreSQL', _ex)

     # Закрываем соединение после выполненных действий с БД
     finally:
          if connection:
               connection.close()
               
               # print('[INFO] PostgreSQL connection closed')

if __name__ == '__main__':
     print(postgres())



     

