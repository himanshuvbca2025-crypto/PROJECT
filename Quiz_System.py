import mysql.connector


class Quiz:
    
    # Sql and Python Connection 
#----------------------------------------------------------
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "himi1229",
                database = "QuizSystem",
                port = 3306
            )
            
            self.cur = self.conn.cursor()
            print("Connected")
            
        except Exception as e:
            print("Error : ",e)
            
#-----------------------------------------------------------

    def registration(self):    
           check = input("User / Admin \n ").lower()
           
           if check == "admin":
               email = input("Enter Your Email : ")
               self.cur.execute("SELECT * FROM Admin WHERE Email = %s", (email,))
               result = self.cur.fetchone()
               
               if result:
                   
                   pass
                   
                   
               else:
                   print("Admin not Exist !")

               
           if check == "user":
               
               username = input("Enter Name : ")
               password = input("Enter Password : ")
               
               self.cur.execute("Insert Into Usser (username, password) VALUES (%s,%s)", (username, password))
               self.conn.commit()
               
               print("Registerd")
               
               print("1.Test")
               print("2.Leader Board")
               
               test = int(input("Select Mode : "))
               
               if test == 1:
                 pass
             
               elif test == 2:
                 pass      
             
           else:
               print("Not")
               
 #-----------------------------------------------------------
      
               