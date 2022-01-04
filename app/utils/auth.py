from flask import session, redirect
from functools import wraps

#We define a function called login_required() 
#that expects to receive another function as an argument
#(which it captures as the func parameter).

#The ultimate goal of the Python decorator that we're building is to redirect a user 
# who isn't logged in (that is, a user for whom no session exists) 
# or to run the original route function for a user who is logged in.


def login_required(func):
  @wraps(func)
  def wrapped_function(*args, **kwargs):
    # if logged in, call original function with original arguments
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)

    return redirect('/login')
  
  return wrapped_function

