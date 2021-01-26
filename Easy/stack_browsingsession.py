browsing_session = []  # setting to empty list/stack.

# if user navigate to website no. 1
browsing_session.append(1)  # add the address to the current website.
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)  # [1,2,3]

try:
    user_input = ' '
    while(browsing_session):  # Till length of stack is not zero.
        user_input = input('Click Back button?:Yes/No ')
        # checking if stack is empty or not.
        if(user_input == 'Yes'):
            # remove last item from the stack and return it.
            browsing_session.pop()
            # this means this expression is true which is browsing_session is not empty.
            if browsing_session:
                # returns item on top of the stack.
                print('redirect', browsing_session[-1])
            else:
                # if it is empty , we disable the back button.
                print('disable')
        else:
            break
except:
    print('Error')
