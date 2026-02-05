from tools.github_tool import search_repositories
from tools.weather_tool import get_weather


def execute_plan(plan: dict) -> dict:
    """
    Executes each step in the plan using the appropriate tool.
    """

    results = {}

    for step in plan.get("steps", []):
        tool = step.get("tool")
        tool_input = step.get("input", {})

        if tool == "github_search":
            results["github"] = search_repositories(
                query=tool_input.get("query", "")
            )

        elif tool == "weather":
            results["weather"] = get_weather(
                city=tool_input.get("city", "")
            )

        else:
            results[tool] = "Unknown tool"

    return results
