from dataclasses import dataclass
@dataclass
class order():
        ordnum:str = ""
        date:str = ""
        email:str = ""
        option:str =""
        cost:float = 0.0
        rating:int = 0

def readfromfile():
    counter = 0
    with open ("orders.txt", "r") as readfile:
        line = readfile.readline().rstrip('\n')
        orders = [order() for index in range(505)]
        while line:
            items = line.split(",")
            orders[counter].ordnum = items[0]
            orders[counter].date = items[1]
            orders[counter].email = items[2]
            orders[counter].option = items[3]
            orders[counter].cost = float(items[4])
            orders[counter].rating = int(items[5])
            counter+=1
            line = readfile.readline().rstrip('\n')
    return orders

def findpos(orders):
     position = -1
     index = 0
     month = input("What month do you want to search for: ")
     while position ==-1 and index < len(orders):
          if orders[index].date[3:6] == month and orders[index].rating ==5:
               position = index
          index+=1
     return position

def writedetails(order, position):
     with open ("winningCustomer.txt", "w") as writefile:
          if position >= 0:
            writefile.write(orders[position].ordnum + "," + orders[position].email + "," + str(orders[position].cost))
          else:
             writefile.write("no winner")

def countoption(orders, ption):
     counter = 0
     for index in range(len(orders)):
          if orders[index].option == ption:
               counter+=1
     return counter

def displaynumber(orders):
     delivered = countoption(orders,"Delivery")
     collected = countoption(orders,"Collection")                
     print("There were",delivered,"delivered")
     print("There were",collected,"collected")

orders = readfromfile()
position = findpos(orders)
writedetails(orders, position)
displaynumber(orders)