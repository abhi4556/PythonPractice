'''
Question:
Create a Python decorator called authenticated that simulates a basic authentication mechanism. 
The decorator should take a username and password as arguments. When a function is decorated with @authenticated(username, password),
it should prompt the user to enter a username and password. If the entered values match the ones provided to the decorator,
the function is executed; otherwise, an authentication error message is displayed.

Implement the authenticated decorator and apply it to a sample function to demonstrate its usage.
'''
# Define the authenticated decorator
def authenticated(username, password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            entered_username = input("Enter username: ")
            entered_password = input("Enter password: ")
            
            if entered_username == username and entered_password == password:
                return func(*args, **kwargs)
            else:
                print("Authentication failed. Access denied.")
        return wrapper
    return decorator

# Apply the authenticated decorator to a function
#@authenticated(username="admin", password="secretpassword")
def secure_function():
    print("Access granted. This is a secure function.")

# Test the decorated function
inner_func = authenticated(username="admin", password="secretpassword")
innermost = inner_func(secure_function)
innermost()
