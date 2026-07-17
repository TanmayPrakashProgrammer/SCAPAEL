import time
from Organizer_Test_Cases import Test_Query
import subprocess
import platform

if platform.system() == "Windows":
    subprocess.run(["cls"], shell=True)
else:
    subprocess.run(["clear"])


def Organize(data):
    output = ""
    # Add your organization logic here
    return data



start = time.time()
#Running the function with the Test Query

result = Organize(Test_Query)

#Anaysis with YourSelf with Pattern
print("This is the TestCase:")
print("INPUT Token Size:",len(Test_Query))
print("OUTPUT Result Size:",len(result))
print("TESTCASE::: \n",Test_Query)
print("______________________________________________________________________________________")
print("RESULT::: \n",result)

end = time.time()
print(f"Execution time: {end - start} seconds")