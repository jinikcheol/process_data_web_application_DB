from database import connection

# 해야 할 일 내용 가져오기
# 최근에 작성된 순서대로
def get_todolist():
    conn = connection.get_connection()

    sql = '''
        select todo_content, todo_importance
        from todo
        where todo_status = 1
        order by todo_idx ASC
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    data_list = []

    for obj in row :
        data_dic = {
            'todo_content' : obj[0],
            'todo_importance' : obj[1]
        }
        data_list.append(data_dic)

    conn.close

    return data_list