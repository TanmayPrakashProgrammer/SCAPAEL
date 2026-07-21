from backend.Abstract import Abstraction
import time



# text = "I want to play a game , which should be nice but I also want that the games has some types of levels too"

# 
# print(Abstraction(text))
#I want to play a game , which should be nice but I also want that the games has some types of levels to
#I want to play a game , which should be nice but I also want that the games has some types of levels too

RUN = True 

while RUN:
    text = input("Enter the text to be Abstracted or Exit to Exit ")
    if (text.lower() == "exit"):
        RUN = False
        break
    Start = time.time()
    result = Abstraction(text)
    End = time.time()
    print("Abstact Result: /n",result)
    print("\n")
    print("Details:")
    print("INPUT SIZE:",len(text))
    print("OUTPUT SIZE:",len(result))
    print("EXECUTION TIME:" ,End - Start, "Seconds")

