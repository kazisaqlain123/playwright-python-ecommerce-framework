from uuid import uuid4


def generate_unique_email() -> str:
    unique_id = uuid4().hex[:10]

    return f"qa.automation.{unique_id}@example.com"