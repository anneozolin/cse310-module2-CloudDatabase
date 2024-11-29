from firebase_config import auth

# Function to sign up a new user
def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("User created successfully!")
        return user
    except Exception as e:
        print("Error signing up:", e)

# Function to log in an existing user
def log_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Logged in successfully!")
        return user
    except Exception as e:
        print("Error logging in:", e)

# Function to get the currently logged-in user's ID
def get_user_id(user):
    return user["localId"] if user else None
