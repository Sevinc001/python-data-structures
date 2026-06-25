# ==========================================
# TASK 1: Dynamic Number List & Average
# ==========================================
numlist = list()
while True:
    inp = input("Please, enter a number:")
    if inp == "done": 
        break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print("Average:", average)
