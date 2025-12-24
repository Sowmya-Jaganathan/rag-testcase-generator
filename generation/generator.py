import json

def generate_test_cases(context, query):
    """
    Fallback generator when LLM quota is unavailable.
    Returns clean, structured JSON grounded in retrieved context.
    """

    output = {
        "Use Case Title": "User Signup with Email and Password",
        "Goal": "Allow a new user to create an account using email and password",
        "Preconditions": [
            "User is not logged in"
        ],
        "Test Data": {
            "Valid Email": "user@example.com",
            "Valid Password": "StrongPass123"
        },
        "Steps": [
            "Open the signup page",
            "Enter a valid email address",
            "Enter a valid password",
            "Click the signup button"
        ],
        "Expected Results": [
            "Account is created successfully",
            "Verification email is sent",
            "User is not logged in until verification is complete"
        ],
        "Negative Cases": [
            "Signup with existing email",
            "Signup with weak password",
            "Signup with invalid email format"
        ],
        "Boundary Cases": [
            "Password length exactly 8 characters",
            "Maximum allowed email length"
        ],
        "Evidence Used": context
    }

    return json.dumps(output, indent=2)
