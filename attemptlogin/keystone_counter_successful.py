#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginsuccessful = 0 # counter for fails

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'successful pattern' appears in the line...
        if "-] Authorization failed" in line:
            loginsuccessful += 1 # this is the same as loginsuccessful = loginsuccessful + 1

print("The number of successful log in attempts is", loginsuccessful)

