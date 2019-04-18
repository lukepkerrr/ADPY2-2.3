import psycopg2

CONNECT = 'dbname=netology user=user_netology password=123'

def command_for_add_student(cursor, student):
    cursor.execute('insert into student (name, gpa, birth) values (%s, %s, %s) RETURNING id',
                 (student['name'], student['gpa'], student['birth']))
    return cursor.fetchone()[0]

def create_db(): # создает таблицы
    with psycopg2.connect(CONNECT) as conn:
        with conn.cursor() as curs:
            curs.execute('CREATE TABLE IF NOT EXISTS student ('
                         'id serial PRIMARY KEY,'
                         'name varchar(100),'
                         'gpa numeric(10, 2),'
                         'birth timestamp with time zone);')
            curs.execute('CREATE TABLE IF NOT EXISTS course ('
                         'id serial PRIMARY KEY,'
                         'name varchar(100));')
            curs.execute('CREATE TABLE IF NOT EXISTS student_course ('
                         'id serial PRIMARY KEY,'
                         'student_id INTEGER REFERENCES student(id) ON DELETE CASCADE,'
                         'course_id INTEGER REFERENCES course(id) ON DELETE CASCADE)')
            print('Таблицы созданы')

def delete_db(): #удаляет таблицы (для тестов)
    with psycopg2.connect(CONNECT) as conn:
        with conn.cursor() as curs:
            curs.execute('DROP TABLE student_course')
            curs.execute('DROP TABLE student')
            curs.execute('DROP TABLE course')
            print('Таблицы удалены')

def get_students(course_id): # возвращает студентов определенного курса
    with psycopg2.connect(CONNECT) as conn:
        with conn.cursor() as curs:
            curs.execute('select student.name from student join student_course on student.id = student_course.student_id join course on course.id = student_course.course_id where course.id = %s', (course_id, ))
            return curs.fetchall()

def add_student(student): # просто создает студента
    with psycopg2.connect(CONNECT) as conn:
        with conn.cursor() as curs:
            return command_for_add_student(curs, student)

def add_students(course_id, students): # создает студентов и записывает их на курс
    with psycopg2.connect(CONNECT) as conn:
        with conn.cursor() as curs:

            curs.execute('select * from course where course.id = (%s)', (course_id, ))

            if not curs.fetchone():
                print('Курс не найден')
            else:
                for student in students:
                    curs.execute('insert into student_course (student_id, course_id) values (%s, %s)', (command_for_add_student(curs, student), course_id))
                print('Все студенты успешно записаны')


def add_course(course): # создает курс
    with psycopg2.connect(CONNECT) as conn:
        with conn.cursor() as curs:
            curs.execute('insert into course (name) values (%s) RETURNING id',
                         (course['name'], ))
            return curs.fetchone()[0]

def get_student(student_id):
    with psycopg2.connect(CONNECT) as conn:
        with conn.cursor() as curs:
            curs.execute('select * from student where student.id = %s', (student_id, ))
            return curs.fetchone()[1]


student_for_test_1 = {
    'name': 'Иван Петров',
    'gpa': 4.2,
    'birth': '1999-01-01'
}

student_for_test_2 = {
    'name': 'Петр Иванов',
    'gpa': 3.4,
    'birth': '1998-02-03'
}

student_for_test_3 = {
    'name': 'Семен Сидоров',
    'gpa': 4.4,
    'birth': '2000-04-02'
}

course_for_test_1 = {
    'name': 'Курс 1'
}

course_for_test_2 = {
    'name': 'Курс 2'
}

students_list_for_test = [student_for_test_1, student_for_test_2, student_for_test_3]

create_db()
course_id_1 = add_course(course_for_test_1)
course_id_2 = add_course(course_for_test_2)
print(course_id_1)
print(course_id_2)
add_students(course_id_1, students_list_for_test)
finded_students = get_students(course_id_1)
print(finded_students)
student_id_1 = get_student(1)
print(student_id_1)
# delete_db()
