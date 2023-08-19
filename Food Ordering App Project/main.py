#menu driven program
import sys
from admin import *
from user import *


admin = admin()
user = user()

print('welcome to the food ordering app')
while True:
    print('press 1 for admin login')
    print('press 2 for user login')
    print('press 3 for exit')
    option = int(input('enter your choice :'))
    if option ==1:
        print('welcome to admin login page')
        print('press 1 to add food item')
        print('press 2 to edit food')
        print('press 3 to show food')
        print('press 4 to remove food')
        choice = int(input('enter your choice :'))
        if choice ==1:
            admin.add_new_food()
        elif choice == 2:
            admin.edit_food_items()
        elif choice==3:
            admin.show_food_items()
        elif choice==4:
            admin.remove_food_items()
        else:
            print('enter valid input')
    elif option ==2:
        print('welcome to user login')
        print('press 1 for registration')
        print('press 2 for login')
        choice = int(input('enter your choice :'))
        if choice == 1:
            user.register()
        elif choice ==2:
            temp= user.login()
            if temp:
                print('press 1 for place order')
                print('press 2 for order history')
                print('press 3 for update profile')
                option =int(input('enter your choice :'))
                if option ==1:
                    user.place_new_order()
                elif option == 2:
                    user.order_history()
                elif option==3:
                    user.edit_profile()
                else:
                    print('please provide valid input')
            else:
                print('please provide valid credentials')
        else:
            print('please provide valid input')
    elif option==3:
        print('thank you for using this application')
        sys.exit()
    else:
        print('please provide valid input')
