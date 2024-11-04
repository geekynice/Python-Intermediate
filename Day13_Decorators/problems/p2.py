'''
Problem 2: Decorator for Checking User Permissions
Write a decorator called check_permission that checks if the user has the right permission to execute a function. 
If the user doesn't have the permission, print "Access denied".

Expected Output:
Given:
@check_permission
def delete_account(user):
    print(f"Account for {user['name']} deleted")

user = {'name': 'Alice', 'role': 'admin'}
delete_account(user)

If the user role is 'admin', the output should be:
Account for Alice deleted

If the user role is not 'admin', the output should be:
Access denied
'''
import functools
def check_permission(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get('role') == 'admin':
            return func(user, *args, **kwargs)
        else:
            print('Access denied')
            return 
    return wrapper

@check_permission
def delete_account(user):
    print(f"Account for {user['name']} deleted")

user = {'name': 'Alice', 'role': 'staff'}

delete_account(user)