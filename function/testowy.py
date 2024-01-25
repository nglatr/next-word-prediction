import json
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import GPT4All

template = """You are a next word prediction function. The user gives you the input: {string}. What word could user type after that string."""
prompt = PromptTemplate(template=template, input_variables=["string"])
local_path = ("C:/Users/damia/Documents/Srudia/Erasmus/Semestr1/TSCD/makit-llm-lambda-main/function/gpt4all-falcon-q4_0.gguf")
llm = GPT4All(model=local_path, verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm)

def main():
    # Read input from the terminal
    string = input("Enter the action: ")

    if not string:
        print("Error: No action was provided.")
        return

    response = llm_chain.invoke(string)

    # Display the response in the terminal
    print(response)

if __name__ == "__main__":
    main()
