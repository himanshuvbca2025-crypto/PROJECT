import mysql.connector
import csv
from datetime import datetime


class MyQuiz:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="himi1229",
                database="MyPython",
                port=3306
            )
            self.cur = self.conn.cursor()
            print("Connected Successfully")

        except Exception as e:
            print("Error:", e)




    def registration(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        role = "user"

        self.cur.execute("""
            INSERT INTO user (name, email, password, role)
            VALUES (%s, %s, %s, %s)
        """, (name, email, password, role))

        self.conn.commit()
        print("Registration Successful")

    def login(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        self.cur.execute("""
            SELECT * FROM user WHERE email=%s AND password=%s
        """, (email, password))

        data = self.cur.fetchone()

        if data:
            print("Login Successful")
            self.user_id = data[0]
            role = data[4]

            if role == "admin":
                self.admin_Menu()
            else:
                self.user_Menu()
        else:
            print("Invalid Credentials")

    def admin_Menu(self):
        while True:
            print("\n--- ADMIN PANEL ---")
            print("1. Add Category")
            print("2. Add Question")
            print("3. View All Results")
            print("4. Export Results")
            print("5. Exit")

            choice = int(input("Select: "))

            if choice == 1:
                self.add_category()

            elif choice == 2:
                self.add_question()

            elif choice == 3:
                self.view_all_results()

            elif choice == 4:
                self.export_result()

            elif choice == 5:
                break

            else:
                print("Invalid Choice")

    def add_category(self):
        name = input("Enter Category: ")

        self.cur.execute("""
            INSERT INTO categories (categ_name)
            VALUES (%s)
        """, (name,))

        self.conn.commit()
        print("Category Added")

    def add_question(self):
        self.cur.execute("SELECT * FROM categories")
        categories = self.cur.fetchall()

        for c in categories:
            print(c)

        categ_id = int(input("Enter Category ID: "))
        question = input("Enter Question: ")
        op1 = input("Option 1: ")
        op2 = input("Option 2: ")
        op3 = input("Option 3: ")
        op4 = input("Option 4: ")
        correct = input("Correct Answer: ")
        difficulty = input("Difficulty (easy/medium/hard): ")

        self.cur.execute("""
            INSERT INTO questions
            (categ_id, question_text, option1, option2, option3, option4, correct_answer, difficulty)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (categ_id, question, op1, op2, op3, op4, correct, difficulty))

        self.conn.commit()
        print("Question Added")

    def user_Menu(self):
        while True:
            print("\n--- USER PANEL ---")
            print("1. Start Quiz")
            print("2. View Leaderboard")
            print("3. Export Result")
            print("4. View History")
            print("5. Exit")

            choice = int(input("Select: "))

            if choice == 1:
                self.start_quiz()

            elif choice == 2:
                self.view_leaderboard()

            elif choice == 3:
                self.export_result()

            elif choice == 4:
                self.view_history()

            elif choice == 5:
                break

            else:
                print("Invalid")

    def start_quiz(self):
        self.cur.execute("SELECT * FROM categories")
        categories = self.cur.fetchall()

        for c in categories:
            print(c)

        categ_id = int(input("Select Category ID: "))
        difficulty = input("Enter Difficulty: ")

        self.cur.execute("""
            SELECT question_id, question_text, option1, option2, option3, option4, correct_answer
            FROM questions
            WHERE categ_id=%s AND difficulty=%s
            LIMIT 5
        """, (categ_id, difficulty))

        questions = self.cur.fetchall()

        score = 0
        total = len(questions)

        for q in questions:
            print("\n", q[1])
            print("1.", q[2])
            print("2.", q[3])
            print("3.", q[4])
            print("4.", q[5])

            ans = input("Enter Answer: ")

            if ans == q[6]:
                score += 1

        print(f"\nScore: {score}/{total}")

        self.cur.execute("""
            INSERT INTO quiz_attempt
            (user_id, categ_id, score, total_questions, date_time)
            VALUES (%s,%s,%s,%s,%s)
        """, (self.user_id, categ_id, score, total, datetime.now()))

        self.conn.commit()

    def view_leaderboard(self):
        self.cur.execute("""
            SELECT u.name, MAX(q.score)
            FROM quiz_attempt q
            JOIN user u ON q.user_id = u.user_id
            GROUP BY u.user_id, u.name
            ORDER BY MAX(q.score) DESC
            LIMIT 5
        """)

        data = self.cur.fetchall()

        print("\n--- LEADERBOARD ---")
        rank = 1

        for row in data:
            print(f"{rank}. {row[0]} - {row[1]}")
            rank += 1

    def view_history(self):
        self.cur.execute("""
            SELECT categ_id, score, total_questions, date_time
            FROM quiz_attempt
            WHERE user_id=%s
        """, (self.user_id,))

        data = self.cur.fetchall()

        print("\n--- HISTORY ---")

        for row in data:
            print(row)

    def export_result(self):
        self.cur.execute("""
            SELECT c.categ_name, q.score, q.total_questions, q.date_time
            FROM quiz_attempt q
            JOIN categories c ON q.categ_id=c.categ_id
            WHERE q.user_id=%s
        """, (self.user_id,))

        data = self.cur.fetchall()

        with open("result.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Category", "Score", "Total", "Date"])

            for row in data:
                writer.writerow(row)

        print("Export Done")

    # ---------------- VIEW ALL RESULTS ----------------
    def view_all_results(self):
        self.cur.execute("""
            SELECT u.name, c.categ_name, q.score, q.total_questions, q.date_time
            FROM quiz_attempt q
            JOIN user u ON q.user_id=u.user_id
            JOIN categories c ON q.categ_id=c.categ_id
        """)

        data = self.cur.fetchall()

        print("\n--- ALL RESULTS ---")

        for row in data:
            print(row)


q = MyQuiz()

while True:
    print("\n--- MAIN MENU ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Select: ")

    if choice == "1":
        q.registration()

    elif choice == "2":
        q.login()

    elif choice == "3":
        break

    else:
        print("Invalid")
        
        
        
        
        
        #    def deleteQuestion(self):
    # try:
    #     qid = int(input("Enter Question ID to delete: "))

    #     self.cur.execute(
    #         "DELETE FROM questions WHERE id = %s",
    #         (qid,)
    #     )

    #     self.conn.commit()

    #     if self.cur.rowcount > 0:
    #         print("Question Deleted Successfully")
    #     else:
    #         print("No Question Found with this ID")

    # except Exception as e:
    #     print("Error:", e)