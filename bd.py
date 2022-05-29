import psycopg2

class BotDB:

    def __init__(self, db_uri):  # initialization bd
        self.conn = psycopg2.connect(db_uri, sslmode="require")
        self.cursor = self.conn.cursor()

    def add_data(self, user_id, username, first_name, last_name, phone, join_day):  # add user id and join day to bd
        self.cursor.execute("INSERT INTO userschannel(users_id, usernames, first_names, last_names, phones, join_day) VALUES (%s, %s, %s, %s, %s, %s)",
                            (user_id, username, first_name, last_name, phone, join_day))
        return self.conn.commit()

    def delete_data(self, user_id, username, first_name, last_name, phone, join_day):
        self.cursor.execute(f"DELETE from userschannel users_id WHERE users_id = {user_id}")
        self.conn.commit()

        self.cursor.execute(f"DELETE from userschannel usernames WHERE usernames = {username}")
        self.conn.commit()

        self.cursor.execute(f"DELETE from userschannel first_names WHERE first_names = {first_name}")
        self.conn.commit()

        self.cursor.execute(f"DELETE from userschannel last_names WHERE last_names = {last_name}")
        self.conn.commit()

        self.cursor.execute(f"DELETE from userschannel phones WHERE phones = {phone}")
        self.conn.commit()

        self.cursor.execute(f"DELETE from userschannel join_day WHERE join_day = {join_day}")
        self.conn.commit()

    def close(self):  # close bd
        self.conn.close()