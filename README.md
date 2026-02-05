AI Operations Assistant

This project is a simple AI-powered operations assistant that understands a natural language task, breaks it into clear steps, executes those steps using real APIs, and returns a clean, structured result.

I built this project to learn how LLMs can be used beyond chat, especially how they can plan actions and work together with tools and APIs in a structured way.

What does this project do?

The assistant accepts a task like:

“Find top Python GitHub repositories and current weather in Delhi”

It then:

Understands the intent of the task

Creates a step-by-step plan

Calls real APIs to fetch the required information

Returns a structured JSON response

The entire flow is exposed through a FastAPI endpoint, which can be tested using Swagger UI.

How the system works

The project follows a Planner → Executor → Verifier flow:

Planner

Uses a Large Language Model (LLM) to convert the user’s text into a structured JSON plan.

Executor

Executes each step of the plan by calling real third-party APIs such as GitHub and Weather APIs.

Verifier

Validates and cleans the results before returning the final response.

This separation keeps the system easy to understand, debug, and extend.

Project Structure
AI-Assistant-Trulymadly/
│
├── agents/
│   ├── planner.py      # Creates a plan from user input
│   ├── executor.py     # Executes plan steps using tools
│   └── verifier.py     # Verifies and formats final output
│
├── tools/
│   ├── github_tool.py  # GitHub API integration
│   └── weather_tool.py # Weather API integration
│
├── llm/
│   └── llm_client.py   # LLM (Groq) interaction
│
├── main.py             # FastAPI application
├── requirements.txt    # Project dependencies
├── .env.example        # Environment variable example
└── README.md

Technologies Used

Python

FastAPI – for building the API

Groq LLM API – for task planning

GitHub Search API – for repository data

Open-Meteo API – for weather data

How to run the project locally
1. Clone the repository
git clone https://github.com/bansalakshat-12/AI-Assistant-Trulymadly
cd AI-Assistant-Trulymadly

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Set environment variables

Create a .env file using the example below:

GROQ_API_KEY=your_api_key_here

Run the application
python -m uvicorn main:app --reload


Then open the following URL in your browser:

http://127.0.0.1:8000/docs


You can test the API directly from the browser using Swagger UI.

Example API Input
{
  "task": "Find top Python GitHub repositories and current weather in Delhi"
}

Example Output

A list of top GitHub repositories with star counts

Current weather details for the requested city

A structured JSON response combining all results

Why I built this project

I built this project to:

Understand how LLMs can be used for planning and reasoning

Learn how to integrate real-world APIs into an AI system

Practice designing a multi-agent architecture

Expose AI logic through a clean and testable API

Notes

The virtual environment is intentionally not committed to GitHub

API keys are stored securely using environment variables

All dependencies are managed using requirements.txt

License

MIT License