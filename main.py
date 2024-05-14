#calculation functions

def add(n1, n2):
  return n1 + n2
  
def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


#dictionary
operations = {
  "+":add,
  "-":subtract, 
  "*":multiply,
  "/":divide
}

#recursion

def calculator():
  
#inputs
  n1 = int(input("\nWelcome to your friendly calculator program. Let's get calculating! What's the first number?:"))
  for symbol in operations:
    print(symbol)
  op_symbol = input("Pick an operation from the line above:")
  n2 = int(input("What's the second number?:"))
  
  
  #calculating and printing the answer
  calc_func = operations[op_symbol]
  answer = calc_func(n1,n2)
  print(f"{n1} {op_symbol} {n2} = {answer}")

  #creating a list of answers
  answer_list = [answer]
  
  #function to run next calculation
  
  def again():
    again = input(f"Type 'y' to continue calculation with {answer_list[x]}, or type 'n' to start a new calculation:")
    if again == 'y':
      for symbol in operations:
        print(symbol)
      op_symbol_x = input("Pick an operation from the line above:")
      nx = int(input("What's the next number?:"))
      calc_func = operations[op_symbol_x]
      answer_x = calc_func(answer_list[x],nx)
      print(f"{answer_list[x]} {op_symbol_x} {nx} = {answer_x}")
      answer_list.append(answer_x)
    else:
      calculator()
  #loop to run continuously
  x=0
  for z in answer_list:
    again()
    x += 1
  
calculator()
    