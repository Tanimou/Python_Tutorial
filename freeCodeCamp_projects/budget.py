"""
  Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. 
  When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. 
  The class should also contain the following methods:

?1.A deposit method that accepts an amount and description. If no description is given, it should default to an empty string.
?The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.

?2.A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. 
?If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.

?3.A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.

?4.A transfer method that accepts an amount and another budget category as arguments. 
?The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
?The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". 
?If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.

?5.A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
?This method should be used by both the withdraw method and transfer method.

When the budget object is printed it should display:

?1.A title line of 30 characters where the name of the category is centered in a line of * characters.

?2.A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. 
?The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.

?3.A line displaying the category total.

Here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

#Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. 
#It should return a string that is a bar chart.

#The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. 
#Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. 
#The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. 
#Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

#This function will be tested with up to four categories.

#Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

!Percentage spent by category
!100|          
! 90|          
! 80|          
! 70|          
! 60| o        
! 50| o        
! 40| o        
! 30| o        
! 20| o  o     
! 10| o  o  o  
!  0| o  o  o  
!    ----------
!     F  C  A  
!     o  l  u  
!     o  o  t  
!     d  t  o  
!        h     
!        i     
!        n     
!        g

Hint: to get the percentage spent in each category based only on withdrawls:
1.we calculate the total of withdrawls spent in each category t
2.then we calculate the total of withdrawls of all categories T
3.then we do t/T to have the average for each category and we truncate the result to be rounded down to the nearest 10
4.and we multiply the result by 100 to have the percentage
"""

def truncate(n):
  return int(n*10)/10


def getTotals(categ):
  total = 0
  breakdown = []
  for c in categ:
    #*get the total of withdrawls of all categories
    total += c.get_withdrawls()
    breakdown.append(c.get_withdrawls())
 # print(total)
 # print(breakdown)
 # print(list(map(lambda x: truncate(x/total)*100, breakdown)))
  return list(map(lambda x: truncate(x/total)*100, breakdown))


def create_spend_chart(categories):
  #*the variable totals will have the percentage of each category, already rounded down to the nearest 10
  totals = getTotals(categories)
  res = "Percentage spent by category\n"

  #*we loop through 100 down to 0 with the step of 10
  #*and for each i, we're gonna create the line that represents the percentage for each category
  for i in range(100, -1, -10):
    cat_spaces = " "
    #*for each category, we have to put "o" to all the percentage line, up to the percentage of the category
    for total in totals:
      #*if the percentage line i is <= the percentage of the category total, then put o else put "   "(3 spaces)
      cat_spaces += "o  " if i <= total else "   "
    #*then we constituate the line to be printed
    res += f"{str(i).rjust(3)}|{cat_spaces}" + "\n"

  x_axis = ""
  dashes = "-"+"---"*len(categories)
  #*we find the category that has the highest length
  names = [category.name for category in categories]
  maxi = max(names, key=len)
  print(maxi)
  #*here x will acting like an index of a list,the same index for all categories's name
  for x in range(len(maxi)):
    #*the starting position to print
    nameStr = "     "
    #*for each category's name, we're gonna print each character of the category's name in one line and so on(ainsi de suite)
    for name in names:
      #*if we reach the end of name(if we finished printing each character of a category's  name but not for the others ),then print "  "
      #*else print each character of the category's name
      nameStr += "   " if x >= len(name) else f'{name[x]}  '

    #*after that we return to the next line
    #*and we can only return to the next line as long as we haven't print yet the longest category name
    if (x != len(maxi)-1):
      nameStr += "\n"

    #*and finally we constituate our line to be printed
    #*and we do that till we print all categories's name  
    x_axis += nameStr
  #*and at the very end we concatenate the whole thing (title+charbar+dash-lines+categories's names)
  res += dashes.rjust(len(dashes)+4)+"\n"+x_axis
  return res


class Category:
  def __init__(self, categ):
    self.name = categ
    self.ledger = []

  def deposit(self, amount, description=""):
      dico = {"amount": amount, "description": description}
      self.ledger.append(dico)

  def check_funds(self, amount):
    return self.get_balance() >= amount

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      dico2 = {"amount": -amount, "description": description}
      self.ledger.append(dico2)

      return True
    else:
      return False
  #*get all the withdrawls of the category
  def get_withdrawls(self):
    return sum(item["amount"] for item in self.ledger if item["amount"] < 0)

  def get_balance(self):
    return sum(self.ledger[i]["amount"] for i in range(len(self.ledger)) if self.ledger[i]["amount"] > 0)+sum(self.ledger[i]["amount"] for i in range(len(self.ledger)) if self.ledger[i]["amount"] < 0)

  def transfer(self, transfert_amount, categ):
    if self.check_funds(transfert_amount):
      d = f'Transfer to {categ.name}'
      self.withdraw(transfert_amount, d)
      dd = f'Transfer from {self.name}'
      categ.deposit(transfert_amount, dd)
      return True
    else:
      return False

  def __repr__(self):
    string2 = self.name.center(30, "*")+"\n"

    for i in range(len(self.ledger)):
      linel = self.ledger[i]["description"]
      linel = linel[:23]
      string2 += f"{linel.ljust(23)}"

      line = "{:.2f}".format(self.ledger[i]["amount"]).rjust(7)
      string2 += line+"\n"
    string2 += "Total: {}".format(sum(self.ledger[i]["amount"]
                                  for i in range(len(self.ledger))))

    return string2


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))





