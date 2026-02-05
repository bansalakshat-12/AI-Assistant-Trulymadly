def verify_results(results: dict) -> dict:
    """
    Verifies and cleans executor results.
    Ensures required fields exist.
    """

    verified = {}

    if "github" in results and isinstance(results["github"], list):
        verified["github"] = results["github"]
    else:
        verified["github"] = []

    if "weather" in results and isinstance(results["weather"], dict):
        verified["weather"] = results["weather"]
    else:
        verified["weather"] = {}

    return verified
