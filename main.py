from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify_results

# 👇 THIS IS REQUIRED (this is what uvicorn looks for)
app = FastAPI(title="AI Operations Assistant")


class TaskRequest(BaseModel):
    task: str


@app.post("/run")
def run_task(request: TaskRequest):
    """
    Accepts a natural language task and processes it
    using Planner → Executor → Verifier agents.
    """
    plan = create_plan(request.task)
    results = execute_plan(plan)
    final_output = verify_results(results)

    return {
        "task": request.task,
        "plan": plan,
        "result": final_output
    }


# Optional local test (does NOT affect FastAPI)
if __name__ == "__main__":
    task = "Find top Python GitHub repositories and current weather in Delhi"
    plan = create_plan(task)
    results = execute_plan(plan)
    final_output = verify_results(results)
    print(final_output)
