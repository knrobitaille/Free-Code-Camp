"""
Created for Free Code Camp project.
    
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
"""
# Category class
class Category:
    # Initialize object
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    # Deposit method
    def deposit(self,amount,description=""):
        self.ledger.append({"amount":amount,"description":description})
        self.balance += amount
    
    # Withdrawl method
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            self.balance -= amount
            return True
        else:
            return False

    # Check balance method
    def get_balance(self):
        return self.balance
        
    #Transfer between categories method
    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            self.withdraw(amount,"Transfer to " + other_category.category)
            other_category.deposit(amount,"Transfer from " + self.category)
            return True
        else:
            return False
        
    # Check balance is greater than amount method
    def check_funds(self,amount):
        """
        I think the descripton in the instruction describes this method backwards 
        to what the test_module actually looks for. It seems it should return True 
        if the amount is less than the balance, not False.

        Description in README.md (as of 09/30/2020):
          A `check_funds` method that accepts an amount as an argument. 
          It returns 'False' if the amount is less than the balance of the 
          budget category and returns 'True' otherwise. This method should be 
          used by both the `withdraw` method and `transfer` method.
        """
        if amount <= self.balance:
            return True
        else:
            return False
        
    # Print / string representation method
    def __str__(self):
        cat_len = len(self.category)
        title = '*'*int((30-cat_len)/2) + self.category + '*'*int((30-cat_len)/2) + '\n'
        transactions = ""
        total = 0
        for tran in self.ledger:
            total += tran['amount']
            a_str = "{:.2f}".format(tran['amount'])
            a_len = len(a_str)
            line = tran['description'][:23].ljust(30 - a_len) + a_str
            transactions += line + '\n'
        return title + transactions + "Total: " + "{:.2f}".format(self.balance)



# Function to display spending in chart
def create_spend_chart(categories):
    # Set up variables
    cat_len = len(categories)
    cat_dict = {}
    total = 0
    # Iterate through category's ledgers to add up withdrawls
    for cat in categories:
        cat_dict[cat.category] = 0
        cat_withdrawls = 0
        for tran in cat.ledger:
            if tran["amount"] < 0:
                cat_withdrawls += -tran["amount"]
        cat_dict[cat.category] += cat_withdrawls
        total += cat_withdrawls
    # Add category and percent spend to a dictionary
    for k, v in cat_dict.items():
        cat_dict[k] = int((v/total)*100 - (v/total*100%10))
    # Create title and set up answer variable (to be returned at end of function)
    title = "Percentage spent by category"+"\n"
    answer = title
    # Create a loop to populate chart with spending
    counter = 100
    while counter >= 0:
        answer += (str(counter)+"| ").rjust(5)
        for k, v in cat_dict.items():
            if v >= counter:
                answer += 'o  '
            else:
                answer += '   '
        answer += '\n'
        counter -= 10
    # Add x axis
    answer += " "*4 + "-"*((cat_len*3)+1) + '\n'
    # Convert category names to a list and add those lists to a list of lists
    cat_list = []
    for k, v in cat_dict.items():
        cat_list.append(list(k))
    # Create x axis labels by iterating through based on length of longest category
    # Then iterates though each category and add appropriate letter or space
    longest_cat_name = max(len(x) for x in cat_list )
    for i in range(longest_cat_name):
        answer += " "*5
        for cat in cat_list:
            if len(cat) >= i+1:
                answer += cat[i] + " "*2
            else:
                answer += " "*3
        answer += "\n"
    # Return answer. Test solution did not seem to want final two spaces
    # Final two spaces would make the answer a "perfect rectangle"
    return answer[:-1]