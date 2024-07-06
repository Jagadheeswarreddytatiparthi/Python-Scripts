def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operations_dict={"+":add,"-":sub,"*":mul,"/":div}
def calculator():
    first_number=int(input("enter first number:"))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while  continue_flag:
        op_symbol=input("Pick an operation:")
        second_number=int(input("enter next number:"))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(first_number,second_number)
        print(f"{first_number} {op_symbol} {second_number}={output}")
        should_continue=input(f"enter 'y' to continue calculation with {output}  or 'n' to start new calculation or 'x' to exit:").lower()
        if should_continue=="y" :
            first_number=output
        elif should_continue=="n":
             continue_flage=False
             calculator()
        else:
            continue_flag=False
            print("Bye!")

calculator()
