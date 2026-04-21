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
            
#------------------------------------------------------------

    def User(self):
        print("---------------------------------------------------")
        print("             Hello   ")
        print("---------------------------------------------------")
        print("         1. Register")
        print("         2.Login")
        print("---------------------------------------------------")
        
        de = int(input("Select Your Choice  : "))
        
        if de == 1:
            
            username = input("Enter Your FullName : ")
            password = input("Enter Your Password : ")
            
            self.cur.execute("Insert Into Usser (username, password) VALUES (%s,%s)", (username, password))
            self.conn.commit()
            
            
            
              
            print("Registerd")    
                
            print("1.Easy Quiz")
            print("2.Medium Quiz")
            print("3.Hard Quiz")
            print("4.Check Leader Board")
            
            choice = int(input("Select Your Choice : "))
            
            if choice == 1:
                
                pass
            
            elif choice == 2:
                
                pass
             
            elif choice == 3:
                
                pass
            elif choice == 4:
                
                pass
            else:
                
                print("Sorry !")            
            
            
          
        elif de == 2:
            username = input("Enter Name : ")
            password = input("Enter Password : ")
              
            self.cur.execute(
              "SELECT * FROM Usser WHERE username = %s AND password = %s",
            (username, password)
            )
            result = self.cur.fetchone()
            
            if result:
                
                print("Login")
                
            else:
                
                print("Not Found")
          
    def Admin(self):
        email = input("Enter Email : ")
        password = input("Enter Password : ")
        
        self.cur.execute("SELECT * FROM Admin WHERE Email = %s", (email,))
        result = self.cur.fetchone()
               
        if result:
            
            print("1. Edit Question Paper ")
            print("2. Result of student ")     
               
            admin = int(input("Select Your Choice : "))
            
            if admin == 1:
                   
                    q = input("Enter Question: ")
                    o1 = input("Option 1: ")
                    o2 = input("Option 2: ")
                    o3 = input("Option 3: ")
                    o4 = input("Option 4: ")
                    ans = input("Correct Answer: ")
                    cat = input("Category: ")
                    diff = input("Difficulty: ")
                    
                    self.cur.execute("""
                        INSERT INTO Questions 
                        (question, option1, option2, option3, option4, answer, category, difficulty)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (q, o1, o2, o3, o4, ans, cat, diff))

                    self.conn.commit()
                    print("Question Added")
           
            elif admin == 2:
                
                pass
            
            else:
                print("!")
            
        else:
                   print("Admin not Exist !")
                   
                   
                  
                   
#--------------------------------------------------          
print("-----------Welcome------------")  
print("-------------------------------")
print("            User            ")
print("            Admin             ")
print("-------------------------------")

q = Quiz()
select = int(input("Select : "))

if select == 1:
    
 q.User()
 
elif select == 2:
    
    q.Admin()

#--------------------------------------------------      
     