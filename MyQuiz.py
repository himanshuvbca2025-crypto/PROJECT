import mysql.connector
import csv
from datetime import datetime
from tabulate import tabulate

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
            
            
#----------------UserMethod---------------------------------------- 
          
    def User(self):
        
      try:
           print("1.Registration. ")
           print("2.Login. ")  
      
           choice = int(input("Select : "))

           if choice == 1:
            self.registration()
           elif choice == 2:
              self.userLogin()
              
      except Exception as e:
          print("Error > ",e)          
            
#----------------registration Method----------------------------------------           
           
    def registration(self):
        
        try:
           
            name = input("Enter Name : ")
            email = input("Enter Email : ")
            password = input("Enter Password : ")
            
            if name == "" or email == "" or password == "":
             print("\nAll fields are required")
             
            elif not name.isalpha():
                print("\nInvalid Name")
                
            elif "@gmail.com" not in email:
                print("\nEmail is Not Valid")
                
            else:
               self.cur.execute("""Insert Into user (name, email, password) Values (%s,%s,%s )""", 
                             (name, email, password))
               self.conn.commit()
               self.user_id = self.cur.lastrowid
               print("\n----------Registerd----------")
               while True:
                
                
                print("\n1.Start Test. ")
                print("2.LeaderBoard. ")
                print("3.Show History.")
                print("4.Current History")
                print("5.Export Result. ")
                print("6.Exit")

                choice = int(input("\nSelect : "))

                if choice == 1:
                    self.startTest()
                elif choice == 2:
                    self.LeaderBoard()
                elif choice == 3:
                     self.showHistor()
                elif choice == 4:
                     self.showCurrentHistory()
                elif choice == 5:
                       self.ExportResult()
                elif choice == 6:
                    return
                else:
                    print("\nInvalid Choice")
            
        except Exception as e:
            print("Error > ",e)
 
#----------------UserLogin Method----------------------------------------          

           
    def userLogin(self):
        
        try:  
         while True:     
               print("-------------------------")   
               email = input("Enter email : ")
               password = input("Enter Password : ")
        
               
             
               if "@gmail.com" not in email :
                    
                    print("\nCheck it again")
                    continue
               self.cur.execute("Select * from user Where email = %s AND password = %s",(email, password))
               data = self.cur.fetchone()
                     
               if data:
            
                 print("\n-----Login-----\n")
                 self.user_id = data[0]
                 
                 while True:
                 
                  print("     1.Start Test. ")
                  print("     2.LeaderBoard. ")
                  print("     3.Show History.")
                  print("     4.Current History")
                  print("     5.Export Result. ")
                  print("     6.Exit")
            
                  choice = int(input("\nSelect : "))
            
                  if choice == 1:
                      self.startTest()
                  elif choice == 2:
                       self.LeaderBoard()
                  elif choice == 3:
                       self.showHistor()
                  elif choice == 4:
                       self.showCurrentHistory()
                  elif choice == 5:
                        self.ExportResult()
                  elif choice == 6:
                      return
                  else:
                        print("\nInvalid Choice")
                 else:
                   print("\nNot Found")
                   
        except Exception as e:
           print("Error  > ",e)
            
#----------------AdminLogin Method----------------------------------------           
           
    def AdminLogin(self):
        
      try:  
        while True:   
            email = input("Enter Email : ")
            password = input("Enter Password : ")
        
            if "@gmail.com" not in email:    
                print("\nCheck it again !")
                continue
            
            self.cur.execute("Select * From Admin Where email = %s AND password = %s",(email, password))
            print("\n----------Login---------\n")
           
            data = self.cur.fetchone()
        
           
            if data:
              while True: 
                
                print("\n--------------------\n")
                print("1.Add Question. ")
                print("2.Add Subject ")
                print("3.Delete Question. ")
                print("4.Show Question ") 
                print("5.LeaderBoard ") 
                print("6.Viwe Result ") 
                print("7.Exit") 
                
                choice = int(input("\nSelect : "))
                
                if choice == 1:
                    self.addQuestion() 
                elif choice == 2: 
                    self.addSubject()
                elif choice == 3: 
                    self.deleteQuestion()
                elif choice == 4:
                    self.showAll()
                elif choice == 5: 
                    self.LeaderBoard() 
                elif choice == 6: 
                    self.view_all_results()
                elif choice == 7:
                    return
                
                else: print("\nInvalid Choice") 
                
            else: print("\nData Not Found")
        
      except Exception as e:
         print("Error > ",e)
        
#----------------Add Question Method----------------------------------------           
            
    def addQuestion(self):
        try:
                self.cur.execute("Select * From categories")
                categories = self.cur.fetchall()
                
                for c in categories:
                    print(c)
                    
                categ_id = int(input("Enter Category ID: "))
                set_no = int(input("Enter Set No. "))
                marks = int(input("Enter Mark. "))
                
                
                
                    
                question = input("Enter Question: ")
                op1 = input("Option 1: ")
                op2 = input("Option 2: ")
                op3 = input("Option 3: ")
                op4 = input("Option 4: ")
                correct = input("Correct Answer: ")
                difficulty = input("Difficulty (easy/medium/hard): ")
                  
               
                 
                if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
                    
                 self.cur.execute("""
                      INSERT INTO questions
                      (categ_id,set_no, question_text, option1, option2, option3, option4, correct_answer, difficulty, marks)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                       """, (categ_id,set_no, question, op1, op2, op3, op4, correct, difficulty, marks))
                 self.conn.commit()
                 print("\nQuestion Added")
                else:
                    print("\nWrong Condition Select")
                    
        except Exception as e:
                print("Error > ",e)
        
#----------------Delete Question Method----------------------------------------           

    def deleteQuestion(self):
        try:
            setno = int(input("Enter Set No. "))
            qid = int(input("Enter Question id : "))
            
            self.cur.execute("DELETE FROM questions WHERE set_no = %s AND question_id = %s", (setno,qid))
            
            self.conn.commit()
            
            if self.cur.rowcount > 0:
                print("\nQuestion Deleted")
            else:
                print("\nQuestion is Not Avialable")
        
        except Exception as e:
            print("Error > ",e)
            
#----------------Show All Questio Method----------------------------------------           
           
    def showAll(self):
      
      try:  
        self.cur.execute("Select * From questions ")
        data = self.cur.fetchall()
        
        if len(data) == 0:
            print("\nNo Questions Found")
            return  
           
        for row in data:
            print("\n------------------------")
            print("ID:", row[0])
            print("Category ID:", row[1])
            print("Question:", row[2])
            print("A:", row[3])
            print("B:", row[4])
            print("C:", row[5])
            print("D:", row[6])
            print("Correct Answer:", row[7])
            print("Difficulty:", row[8])
            print("------------------------")

      except Exception as e:
          print("Error > ",e)
           
#----------------Start Test Method----------------------------------------           
    
         
    def startTest(self):
     try:
          self.cur.execute("SELECT * FROM categories")
          categories = self.cur.fetchall()

          for c in categories:
            print(c)

          categ_id = int(input("Select Category ID: "))
          difficulty = input("Enter Difficulty (easy / medium / hard): ")
          set_no = int(input("Enter Set No: "))
          
         
          
          self.cur.execute("""
            SELECT question_id, question_text, option1, option2, option3, option4, correct_answer, marks
            FROM questions
            WHERE categ_id=%s AND difficulty=%s AND set_no=%s
            ORDER BY RAND()
            LIMIT 5
        """, (categ_id, difficulty, set_no))

          questions = self.cur.fetchall()

          score = 0
          total = 0

          for q in questions:
            print("\n", q[1])
            print("1.", q[2])
            print("2.", q[3])
            print("3.", q[4])
            print("4.", q[5])

            try:
                ans = int(input("Enter Answer (1-4): "))
            except:
                print("\nInvalid Input")
                continue
            
            if ans < 1 or ans > 4:
                print("Wrong choice skipped")
                continue
            options = [q[2], q[3], q[4], q[5]]

            total += q[7]  
    
            selected_answer = options[ans - 1].strip().lower()
            correct_answer = q[6].strip().lower()

            if selected_answer == correct_answer:
                 score += q[7]

       
          print(f"\nFinal Score: {score} out of {total}")

       
          self.cur.execute("""
            INSERT INTO quiz_attempt
            (user_id, categ_id, set_no, score, total_questions, date_time)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (self.user_id, categ_id, set_no, score, total, datetime.now()))

          self.conn.commit()

     except Exception as e:
        print("Error > ", e)    
        
        
#----------------LeaderBoard Method----------------------------------------           
         
    def LeaderBoard(self):
        
      try:  
        self.cur.execute(""" 
                         Select u.name, MAX(q.score)
                         From quiz_attempt q
                         Join user u ON q.user_id = u.user_id
                         Group BY u.user_id, u.name
                         ORDER BY MAX(q.score) DESC
                         LIMIT 5                        
                         """) 
        
        data = self.cur.fetchall()
        
        print("\n--- LEADERBOARD ---")
        # rank = 1

        
        headers = ["Name", "Score"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    
      except Exception as e:
          print("Error > ",e)
          
#----------------Show History Method----------------------------------------           
       
    def showHistor(self):
      try:  
        self.cur.execute("""
            SELECT c.categ_name,q.set_no, q.score, q.total_questions, q.date_time
    FROM quiz_attempt q
    INNER JOIN categories c ON q.categ_id = c.categ_id
    WHERE q.user_id = %s
        """, (self.user_id,))

        data = self.cur.fetchall()

        print("\n--- HISTORY ---")

        headers = ["Category", "Set", "Gain Marks", "Total Marking", "Date"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
     
      except Exception as e:
          print("Error > ",e)
           
     
     
#----------------ExportResult Method----------------------------------------           
       
    def ExportResult(self):
        try:  
          self.cur.execute("""
            SELECT c.categ_name,q.set_no, q.score, q.total_questions, q.date_time
            FROM quiz_attempt q
            JOIN categories c ON q.categ_id=c.categ_id
            WHERE q.user_id=%s
          """, (self.user_id,))

          data = self.cur.fetchall()

          with open("result.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Category", "Set ","score", "Total", "Date"])

            for row in data:
                writer.writerow(row)

          print("\nExport Done")
          
        except Exception as e:
            print("Error > ",e)
              
#----------------ViweAllResult Method----------------------------------------           
          
          
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
            

#----------------Add Subject Method----------------------------------------           
          
    def addSubject(self):
        try:
            
            newQ = input("Enter Subject Name : ")
            
            if newQ != "":
                
             self.cur.execute("Insert into categories (categ_name) VALUES (%s)",(newQ,))
             self.conn.commit()
             print("\nSubject is Added")
            else:
                print("\nNo Data inserted ")
                
        except Exception as e:
            print("Error > ",e)       
            
     
    def showCurrentHistory(self):
     try:
        self.cur.execute("""
            SELECT c.categ_name, q.set_no, q.score, q.total_questions, q.date_time
            FROM quiz_attempt q
            INNER JOIN categories c ON q.categ_id = c.categ_id
            WHERE q.user_id = %s
            ORDER BY q.date_time DESC
            LIMIT 1
        """, (self.user_id,))

        data = self.cur.fetchall()

        if len(data) == 0:
            print("\nNo Recent Attempt Found ")
            return

        print("\n--- CURRENT TEST RESULT ---")

        from tabulate import tabulate
        headers = ["Category", "Set", "Score", "Total", "Date"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

     except Exception as e:
        print("Error > ", e)   
#----------------Createtion Object and main Menu----------------------------------------           
       
q = MyQuiz()
try:
        print("- - - - - - MENU - - - - - - \n")
        print("           1.USER    ")  
        print("           2.ADMIN    ") 
        choice = int(input("Select : "))
        
        if choice == 1:
            q.User()
        elif choice == 2:
            q.AdminLogin()
        elif choice == 3:
            print("Thanks")
            
        
except Exception as e:
        print("Error >> ",e)