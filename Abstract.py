import time
from Abstract_Test_Cases import TestCases
#Here You will Import the Files Regarding BERT



#_____________________Write the Funtion Here
def Abstraction(data):
    Output = ""
    a = 0
    for i in range(1,1000):
        a = a+1

    return Output


#_____________________

def CheckResult():
    pass



#These are the Test Cases:


# TestCases  = [
#     "I want the apple who is red in color but it may possible if its yellow to how we will know about whether the apple is good or not",
#     "Test Case 2",
#     "Test Case 3",
# ]



#_______________________________________________
#Here I am RUNNING YOUR Code with Test Cases

passed_test = 0
total_test = len(TestCases)
start = time.time()
for i in TestCases:
    a = Abstraction(i)
    if(len(a) < len(i)):
        passed_test = passed_test + 1


end = time.time()
if(passed_test == total_test):
    print("Test Case: Cleared:",passed_test,"/",total_test)
    print("YOUR Function is ready to Use")
    print(f"Execution time: {end - start:.4f} seconds")
elif(passed_test <= total_test and passed_test != 0):
    print("Test Case: Cleared:",passed_test,"/",total_test)
    print("YOUR Function is partially correct")
    print(f"Execution time: {end - start:.4f} seconds")
else:
    print("The Function is Not Good to run")
    print(f"Execution time: {end - start:.4f} seconds")


