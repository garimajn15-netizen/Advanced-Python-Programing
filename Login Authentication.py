# Decorator for login authentication
def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func()
        else:
            print(" Access Denied! Please log in first.")
    return wrapper


# Protected function
@login_required
def view_dashboard():
    print(" Welcome! You have successfully accessed the dashboard.")


# Main Program
status = input("Are you logged in? (yes/no): ").lower()

if status == "yes":
    view_dashboard(True)
else:
    view_dashboard(False)
