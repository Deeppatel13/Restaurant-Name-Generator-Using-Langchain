# Restaurant-Name-Generator-Application-Using-Langchain
This is a Restaurant Name Generator project using the Langchain Library and open source LLAMA Models.

**Overview** - 

The Restaurant Name Generator is a simple web application that suggests unique restaurant names and sample menu items based on a selected nationality. It is built using Streamlit for the frontend and LangChain with the Groq API to access the LLaMA model for the backend.

**Features** -

* User-friendly interface with a clean layout.

* A picker with five nationalities to choose from.

* Generates a restaurant name based on the selected nationality.

* Suggests a list of menu items relevant to the chosen nationality.

**Tech Stack** - 

* Frontend: Streamlit

* Backend: LangChain

* LLM API: Groq API (LLaMA model)

**How to get GROQ API Key?**

Visit "https://console.groq.com/playground" --> Login --> Go to "API Keys" option on the left --> Select "Create API Key" --> Give a key name --> Save the API Key somewhere (It won't be display again after this) --> Use this key in "secret_key.py" file.

**How It Works** - 

* The user selects a nationality from the picker on the left side.

* The application sends the selected nationality as input to the LLM via the Groq API.

* The LLaMA model processes the request and generates a restaurant name along with relevant menu items.

* The suggested name and menu items are displayed on the right side of the interface.

**Snapshots of the Project**

<img src="Screenshot%202025-02-27%20230120.jpg" alt="App Screenshot 1" width="900" height="500">

<img src="Screenshot%202025-02-27%20230404.jpg" alt="App Screenshot 2" width="900" height="500">

**References** - 

* YouTube video - "https://youtu.be/nAmC7SoVLd8?si=c2MLCfkUCUf4KoKO"
