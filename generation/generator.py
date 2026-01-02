import json

def generate_test_cases(context, query):
    query_lower = query.lower()
    use_cases = [
        {
            "Use Case Title": "User Signup with Email and Password",
            "Goal": "Allow a new user to create an account using email and password",
            "Preconditions": ["User is not logged in"],
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
                "Signup with weak password"
            ],
            "Boundary Cases": [
                "Password length exactly 8 characters"
            ]
        },
        {
            "Use Case Title": "Signup with Invalid Email",
            "Goal": "Prevent account creation with invalid email",
            "Preconditions": ["User is not logged in"],
            "Test Data": {
                "Invalid Email": "invalidemail",
                "Valid Password": "StrongPass123"
            },
            "Steps": [
                "Open the signup page",
                "Enter an invalid email",
                "Enter a valid password",
                "Click the signup button"
            ],
            "Expected Results": [
                "Account is not created",
                "Error message is displayed"
            ],
            "Negative Cases": [],
            "Boundary Cases": []
        },
        {
    "Use Case Title": "Signup with Existing Email",
    "Goal": "Prevent signup using an already registered email",
    "Preconditions": ["User is not logged in"],
    "Test Data": {
        "Existing Email": "existing@example.com",
        "Valid Password": "StrongPass123"
    },
    "Steps": [
        "Open the signup page",
        "Enter an existing email address",
        "Enter a valid password",
        "Click the signup button"
    ],
    "Expected Results": [
        "Account is not created",
        "Error message indicating email already exists is displayed"
    ],
    "Negative Cases": [],
    "Boundary Cases": []
},
{
    "Use Case Title": "Signup with Weak Password",
    "Goal": "Validate password strength during signup",
    "Preconditions": ["User is not logged in"],
    "Test Data": {
        "Valid Email": "user@example.com",
        "Weak Password": "12345"
    },
    "Steps": [
        "Open the signup page",
        "Enter a valid email address",
        "Enter a weak password",
        "Click the signup button"
    ],
    "Expected Results": [
        "Account is not created",
        "Password validation error message is displayed"
    ],
    "Negative Cases": [],
    "Boundary Cases": [
        "Password length less than minimum required characters"
    ]
}

        
    
    ]
    # ---------------- LOGIN USE CASES ----------------
    login_use_cases = [
        {
            "Use Case Title": "User Login with Valid Credentials",
            "Goal": "Allow a registered user to log in using valid credentials",
            "Preconditions": ["User has an existing account"],
            "Test Data": {
                "Registered Email": "user@example.com",
                "Valid Password": "StrongPass123"
            },
            "Steps": [
                "Open the login page",
                "Enter a registered email address",
                "Enter the correct password",
                "Click the login button"
            ],
            "Expected Results": [
                "User is logged in successfully",
                "User is redirected to the dashboard"
            ],
            "Negative Cases": [],
            "Boundary Cases": []
        },
        {
            "Use Case Title": "Login with Invalid Credentials",
            "Goal": "Prevent login with incorrect credentials",
            "Preconditions": ["User has an existing account"],
            "Test Data": {
                "Registered Email": "user@example.com",
                "Invalid Password": "wrongpass"
            },
            "Steps": [
                "Open the login page",
                "Enter a registered email address",
                "Enter an incorrect password",
                "Click the login button"
            ],
            "Expected Results": [
                "Login is blocked",
                "Error message is displayed"
            ],
            "Negative Cases": [],
            "Boundary Cases": []
        }
    ]

    # ---------------- QUERY-BASED SELECTION ----------------
    if "login" in query_lower and "signup" in query_lower:
        use_cases = use_cases + login_use_cases
    elif "login" in query_lower:
        use_cases = login_use_cases
    elif "signup" in query_lower:
        use_cases = use_cases
    else:
        # default: authentication-related
        use_cases = use_cases + login_use_cases
    

    return json.dumps({"useCases": use_cases}, indent=2)
