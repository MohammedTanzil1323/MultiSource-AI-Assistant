# MultiSource-AI-Assistant

# LangChain Search Engine with LLaMA

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Setup](#setup)
6. [Getting Started](#getting-started)
7. [Functionality](#functionality)
   - [Chat Interface](#chat-interface)
   - [Search Engine Tools](#search-engine-tools)
8. [Code Explanation](#code-explanation)
   - [Library Imports](#library-imports)
   - [Tool Initialization](#tool-initialization)
   - [Creating the Chat Interface](#creating-the-chat-interface)
   - [Main Functionality](#main-functionality)
9. [Future Enhancements](#future-enhancements)
10. [Contributing](#contributing)

## Introduction

The **LangChain Search Engine with LLaMA** is an interactive web application built using Streamlit, designed to facilitate advanced web searching. By integrating LangChain, a powerful framework for developing applications with Language Models (LLMs), the application utilizes tools such as DuckDuckGo, Arxiv, Wikipedia, and Yahoo Finance to provide comprehensive and intelligent responses to user queries. 

This project harnesses the capabilities of the ChatGroq API with LLaMA as the underlying model, offering users the ability to explore a vast array of information sources effortlessly.

## Features

- **Interactive Chat Interface**: Seamlessly interact with the application through a user-friendly chat interface.
- **Multi-Tool Search Capabilities**: Utilize various search engines and tools including DuckDuckGo, Arxiv, Wikipedia, and Yahoo Finance for diverse information retrieval.
- **Natural Language Understanding**: Input questions in natural language and receive contextually relevant responses.
- **Streaming Responses**: Experience real-time responses from the chatbot as it processes queries.

## Requirements

Before running the application, ensure you have the following software and libraries installed:

### Python Version

The application requires Python 3.8 or higher.

### Required Libraries

The following Python packages are necessary to execute the application:

- `streamlit`: For creating an interactive web application.
- `langchain`: For utilizing language models and chains.
- `langchain_groq`: For integrating with the Groq API.
- `langchain_community`: For accessing community tools and utilities.

Install these requirements using pip:

```bash
pip install streamlit langchain langchain_groq langchain_communit
```
## Installation
Clone the repository to your local machine: ``` bash
git clone https://github.com/MohammedTanzil1323/MultiSource-AI-Assistant.git
cd langchain-search-engine ```

## Setup

GROQ_API_KEY=your_groq_api_key

To store sensitive information such as API keys, create a .env file in your project directory and include your Groq API key:
## Getting Started
To run the application, execute the following command in your terminal:
``` bash
streamlit run app1.py
```

This command will start the Streamlit server and open the application in your default web browser.

## Functionality
## Chat Interface
The core of the application is its chat interface, which allows users to input queries naturally. After starting the application, enter your Groq API key in the sidebar to authenticate with the API. Upon successful entry, you will see a welcome message from the assistant.

## Search Engine Tools
The application is equipped with several integrated tools that allow for a wide range of searches:

DuckDuckGoSearchRun: This tool enables web searches using DuckDuckGo, ensuring privacy while retrieving information.
ArxivQueryRun: This tool interfaces with Arxiv to search for academic papers.
WikipediaQueryRun: This tool fetches information from Wikipedia, providing quick overviews on various topics.
YahooFinanceNewsTool: This tool provides access to the latest news and updates related to finance.
These tools enhance the assistant's capability to deliver accurate and relevant results based on user queries.

## Code Explanation
## Library Imports
The project imports essential libraries for functionality:

Streamlit: For rendering the web interface.
LangChain and LangChain Community: For implementing language models and available tools.
ChatGroq: To interface with the Groq API.

## Tool Initialization

The initialize_tools() function sets up the search tools utilized in the application. By calling this function, you can create instances of each tool, which can then be used to respond to user queries.

## Creating the Chat Interface

The create_chat_interface() function establishes the UI elements for the chat, including a title and an input field for the Groq API key. This method also manages the display of chat messages, maintaining user and assistant dialogues in the session state.

## Main Functionality

The main() function orchestrates the entire application flow:

It initializes the chat interface and retrieves the API key.
It listens for user input; upon receiving a prompt, it logs the interaction in the session state.
The LLM (in this case, ChatGroq with the LLaMA model) is initialized with the Groq API key, and an agent is set up using the previously initialized tools.
The agent processes the chat history and retrieves a response, which is then displayed in the chat interface.

## Future Enhancements
Enhancements could include:

Support for Additional Tools: Adding more APIs or search engines for a wider set of data sources.
User Authentication: Implementing a user authentication system to save session histories.
Enhanced Natural Language Processing: Improve the model's ability to understand complex queries and context.
Multi-language Support: Add capabilities to query and retrieve information in multiple languages.
UI Enhancements: Providing options for users to customize the appearance of the chat interface.
## Contributing
We welcome contributions! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and write clear, descriptive commit messages.
Submit a pull request detailing your changes.
If you encounter any bugs or have feature requests, please use the issue tracker.

License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
LangChain: A robust framework for combining LLMs and various utilities.
Groq: A high-performance API for engaging with AI models.
Streamlit: An open-source app framework tailored for Machine Learning and Data Science applications.
Community Tools: For various tools enhancing the model’s functionality.

## Contact Information
For more details or inquiries, feel free to reach out


