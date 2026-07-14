
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
 )
        
def chat(temperature=1):
 
 while True:

    user_input = input("Enter (or press # to end): ")

    if user_input == "#":
       break
       

    chat_completion = client.chat.completions.create(
      messages=[
        {
           "role" : "user",
           "content" : user_input
        }
       ],
      model="llama-3.3-70b-versatile",
      temperature=temperature,
      max_tokens=20
       )
        
    print(chat_completion.choices[0].message.content)
    print("#-----------------------------------------#")
    print(chat_completion.usage)
    print("#-----------------------------------------#")
    

while True: 

    print("1. Enter the prompt"
        "\n2. Quit"
        )
    
    try:
      choice = int(input("Enter choice: "))

    except ValueError:
       print("invalid input!")
       continue
    
    if choice == 1:
        chat()
        
    elif choice == 2:
        break

    else:
        print("Enter a valid choice!")
