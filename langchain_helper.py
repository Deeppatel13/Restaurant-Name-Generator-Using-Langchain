# Importing the necessary libraries
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
import os
from secret_key import groq_api_key

# Set up the API key
os.environ["GROQ_API_KEY"] = groq_api_key

def restaurant_name_and_items(cuisine):

    # Initialize the Groq LLM model with LangChain
    llm = ChatOpenAI(
        model_name="llama3-8b-8192",
        openai_api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

    # Defining the first prompt template
    template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for it. Give me only one name and nothing else."
    )

    # Creating a simple LLMChain
    name_chain = LLMChain(llm=llm, prompt=template_name, output_key="restaurant_name")

    # Defining the second prompt template
    template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest 10 food items for menu for that {restaurant_name}. Provide only a comma-separated list of food items with no extra text."
    )
    # Creating another simple LLMChain
    items_chain = LLMChain(llm=llm, prompt = template_items, output_key="menu_items")
    
    # Combining the two LLMChains with SequentialChain
    chain = SequentialChain(chains=[name_chain, items_chain],
                       input_variables = ['cuisine'],
                       output_variables = ['restaurant_name', 'menu_items']
                       )

    response = chain(cuisine)
    
    return response


if __name__ == "__main__":
    print(restaurant_name_and_items("Italian"))