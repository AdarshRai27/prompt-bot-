import openai
import os

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"


# Define the chat bot
def prompt_bot():
    print("Hi! I'm a chat bot that can help you find the best prompts for your needs.")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    project = input("What would you like to know about today? ")
    model = input("What AI models are you using? ")
    outcomes = input("What are your desired outcomes? ")

    # Define the prompt based on user needs and goals
    prompt = f"As a {project} user, I want to use {model} to achieve {outcomes}."

    # Generate text based on the prompt using OpenAI's GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        n=1,
        stop=None,
    )

    # Print the generated text
    print(f"Based on your input, here is a prompt that may help you: ")
    print(response.choices[0].text)

    # Ask if the user needs more help
    more_help = input("Do you need more help? (yes/no) ")
    if more_help.lower() == "yes":
        prompt_bot()
    else:
        print("Thank you for using the prompt bot. Good luck with your project!")

# Call the prompt bot
prompt_bot()
