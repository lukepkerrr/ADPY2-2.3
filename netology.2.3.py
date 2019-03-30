import psycopg2


def create_db(): # создает таблицы
    with psycopg2.connect('dbname=netology user=user_netology password=123') as conn:
        with conn.cursor() as curs:
            curs.execute('CREATE TABLE student ('
                         'id integer PRIMARY KEY,'
                         'name varchar(100),'
                         'gpa numeric(10, 2),'
                         'birth timestamp with time zone);')
            curs.execute('CREATE TABLE course ('
                         'id integer PRIMARY KEY,'
                         'name varchar(100));')
            curs.execute('CREATE TABLE student_course ('
                         'id serial PRIMARY KEY,'
                         'student_id INTEGER REFERENCES student(id),'
                         'couse_id INTEGER REFERENCES course(id))')
            print('БД созданы')

def delete_bd(): #удаляет таблицы (для тестов)
    with psycopg2.connect('dbname=netology user=user_netology password=123') as conn:
        with conn.cursor() as curs:
            curs.execute('DROP TABLE student_course')
            curs.execute('DROP TABLE student')
            curs.execute('DROP TABLE course')
            print('БД удалены')

def get_students(course_id): # возвращает студентов определенного курса
    with psycopg2.connect('dbname=netology user=user_netology password=123') as conn:
        with conn.cursor() as curs:
            curs.execute('select student.id, student.name from course join student_course on student.id = student_course. where course.id = %s', (course, ))
            print(curs.fetchone()[1])

def add_students(course_id, students): # создает студентов и записывает их на курс
    pass


def add_student(student): # просто создает студента
    with psycopg2.connect('dbname=netology user=user_netology password=123') as conn:
        with conn.cursor() as curs:
            curs.execute('insert into student (id, name) values (%s, %s)', (course['id'], course['name']))
            print('Курс успешно добавлен')

def add_course(course): # создает курс
    with psycopg2.connect('dbname=netology user=user_netology password=123') as conn:
        with conn.cursor() as curs:
            curs.execute('insert into course (id, name, gpa, birth) values (%s, %s, %s, %s)', (student['id'], student['name'], student['gpa'], student['birth']))
            print('Студент успешно добавлен')

def get_student(student_id):
    with psycopg2.connect('dbname=netology user=user_netology password=123') as conn:
        with conn.cursor() as curs:
            curs.execute('select * from student where student.id = %s', (student_id, ))
            print(curs.fetchone()[1])


student_for_test_1 = {
    'id': 1,
    'name': 'Иван Петров',
    'gpa': 4.2,
    'birth': '1999-01-01'
}

student_for_test_2 = {
    'id': 2,
    'name': 'Петр Иванов',
    'gpa': 3.4,
    'birth': '1998-02-03'
}

student_for_test_3 = {
    'id': 3,
    'name': 'Семен Сидоров',
    'gpa': 4.4,
    'birth': '2000-04-02'
}

course_for_test_1 = {
    'id': 1,
    'name': 'Курс 1'
}

course_for_test_2 = {
    'id': 2,
    'name': 'Курс 2'
}


#create_db()
#delete_bd()


#add_student(student_for_test)
get_student(1)