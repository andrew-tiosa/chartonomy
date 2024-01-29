"""you_cant_do_things = True
if you_cant_do_things:
    print("careful, to miss the point is to miss the whole thing")


a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b


andrew = int(input("Enter your problem: "))
if andrew == 1:
    print("You are a loser")    
elif andrew == 2:
    print("You are a winner")
else: 
    print("You are a winner")



# define a function 
def fib(n):    # write Fibonacci series up to n
 Print a Fibonacci series up to n.
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(1332)


# design a class that will take 3 websites and search for a keyword then take the information from it then print out on another page


class AndrewTiosa:
    def __init__(self, name, age, height, weight, aspiration):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.aspiration = aspiration
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
    def """
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key= "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"
)

prompt = "introduce yourself"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)
print (chat_completion.choices[0].message.content)