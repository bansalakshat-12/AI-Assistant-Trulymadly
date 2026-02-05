# AI Operations Assistant

This project is an AI-powered operations assistant that understands a natural language task, breaks it into steps, executes those steps using real APIs, and returns a structured final result.

I built this project to learn how Large Language Models (LLMs) can be combined with tools and APIs using a clear, multi-agent architecture instead of a simple chatbot approach.

---

## What does this project do?

The assistant takes a task like:

> “Find top Python GitHub repositories and current weather in Delhi”

And then:
- Understands the task
- Creates a step-by-step plan
- Calls real APIs to fetch the required data
- Returns a clean, structured JSON response

The system is exposed through a **FastAPI** endpoint and can be tested locally using **Swagger UI**.

---

## Architecture Overview (Agents + Tools)

The project follows a **Planner → Executor → Verifier** architecture:

### Planner Agent
- Uses an LLM to convert the user’s natural language task into a structured JSON plan.
- Decides which tools need to be used and in what order.

### Executor Agent
- Executes each step of the plan.
- Calls real external APIs through predefined tools (GitHub, Weather).

### Verifier Agent
- Validates the raw results returned by the tools.
- Formats and cleans the final output before returning it to the user.

### Tools
- Tools are simple wrappers around external APIs.
- They are used only by the Executor agent to keep responsibilities separated.

---

## Project Structure

AI-Assistant-Trulymadly/
│
├── agents/
│ ├── planner.py # Converts user input into a plan
│ ├── executor.py # Executes plan steps using tools
│ └── verifier.py # Verifies and formats output
│
├── tools/
│ ├── github_tool.py # GitHub API integration
│ └── weather_tool.py # Weather API integration
│
├── llm/
│ └── llm_client.py # LLM (Groq) interaction
│
├── main.py # FastAPI application
├── requirements.txt # Project dependencies
├── .env.example # Environment variable example
└── README.md


---

## Integrated APIs

- **Groq LLM API** – Used for planning and reasoning
- **GitHub Search API** – Fetches repository data
- **Open-Meteo API** – Provides current weather information

---

## Environment Variables

The project requires the following environment variable:

```env
GROQ_API_KEY=your_api_key_here
An example file is provided as .env.example.

Note: The actual .env file is intentionally not committed to GitHub.

Setup Instructions (Run Locally on Localhost)
1. Clone the repository
git clone https://github.com/bansalakshat-12/AI-Assistant-Trulymadly
cd AI-Assistant-Trulymadly
2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Add environment variables
Create a .env file and add your API key:

GROQ_API_KEY=your_api_key_here
Run the Application
python -m uvicorn main:app --reload
Open the browser at:

http://127.0.0.1:8000/docs
You can test the API directly using Swagger UI.

Example Prompts to Test the System
You can try the following prompts in the /run endpoint:

Find top Python GitHub repositories and current weather in Delhi

Get current weather in Mumbai

Find trending JavaScript repositories on GitHub

Find top AI-related GitHub repositories

Get weather details for Bangalore

Example API Input
{
  "task": "Find top Python GitHub repositories and current weather in Delhi"
}
Known Limitations / Trade-offs
The system supports only predefined tools (GitHub and Weather)

No long-term memory between requests

LLM is used only for planning, not for generating the final response

Error handling is basic and can be extended

The system is designed for clarity and learning, not large-scale production use

Notes
Virtual environment is not committed to GitHub

API keys are stored securely using environment variables

Dependencies are managed using requirements.txt

License
MIT License