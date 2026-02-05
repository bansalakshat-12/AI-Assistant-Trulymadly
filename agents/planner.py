import json
from llm.llm_client import call_llm


def create_plan(task: str) -> dict:
    """
    Uses LLM to convert a natural language task into a structured plan.
    """

    prompt = f"""
You are a Planner Agent.

Convert the user's task into a JSON execution plan.

Rules:
- Output ONLY valid JSON
- No explanation text
- Available tools:
  1. github_search → input: {{ "query": string }}
  2. weather → input: {{ "city": string }}

User task:
"{task}"

Return JSON in this exact format:
{{
  "steps": [
    {{
      "tool": "github_search",
      "input": {{ "query": "python" }}
    }},
    {{
      "tool": "weather",
      "input": {{ "city": "Delhi" }}
    }}
  ]
}}
"""

    response = call_llm(prompt)
    return json.loads(response)
