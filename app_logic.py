import os

def run_command(user_input):
    os.system("echo " + user_input)

def get_user(request, cursor):
    user_id = request.GET.get("id")
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchone()
