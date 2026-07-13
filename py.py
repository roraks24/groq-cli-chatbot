import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
 )

def chat():

 prompt = input("Enter: ")

 chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt ,
        }
    ],
    model="llama-3.3-70b-versatile",
 )

 print(chat_completion.choices[0].message.content)

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
