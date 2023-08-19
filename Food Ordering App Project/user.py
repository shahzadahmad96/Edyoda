#functionalities related to user
# The user will have the following functionalities: ⬅️

#     👉 1. Register on the application. Following to be entered for registration:
#             🔴 Full Name
#             🔴 Phone Number
#             🔴 Email
#             🔴 Address
#             🔴 Password

#     👉 2. Log in to the application

#     👉 3. The user will see 3 options:
#             🔴 Place New Order
#             🔴 Order History
#             🔴 Update Profile

#     👉 4. Place New Order: The user can place a new order at the restaurant.
#             🔵 Show list of food. The list item should as follows:
#                 🔴 Tandoori Chicken (4 pieces) [INR 240]
#                 🔴 Vegan Burger (1 Piece) [INR 320]
#                 🔴 Truffle Cake (500gm) [INR 900]
    
#     👉 5. Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]

#     👉 6. Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.

#     👉 7. Order History should show a list of all the previous orders

#     👉 8. Update Profile: the user should be able to update their profile.
# :arrow_right: Upload the python files on Github and submit the Github repo URL on the assignment page


import json
class user:

    def __init__(self):
        self.personal_details = {}
        self.ordered_item = {}


    def register(self):
        Full_Name = input('enter your full name :')
        Phone_Number = int(input('enter your phone number :'))
        self.Email = input('enter your eamail :')
        Address = input('enter your address :')
        self.Password = input ('enter password :')
        user_details={'name':Full_Name,'phone_number':Phone_Number,'email':self.Email,'address':Address,'password':self.Password}
        self.personal_details[self.Email] = user_details
        with open('personal_details.json','w') as f:
            json.dump(self.personal_details,f,indent=4)
        print('comgratulations you have successfully registered...')
        return self.personal_details
    

    def login(self):
        print('welcome to your login page')
        with open('personal_details.json','r') as f:
              data = json.load(f)
        
        email=input('enter your mail id :')
        key =input('enter your password:')
        if email in data:
            if key ==data[email]['password']:
                return True
            else:
                 return False
        else:
            return False
        
    def place_new_order(self):
        order_id=0
        order_id=order_id+1
        self.oredered_food_items =[]
        list_of_food= [{'food_name':'Tandoori Chicken','quantity':'4 pieces','price':'INR 240'},
                       {'food_name':'Vegan Burger','quantity':'1 Piece','price':'INR 320'},
                       {'food_name':'Truffle Cake','quantity':'500gm','price':'INR 900'}]
        print('here is the menu :')
        for i in list_of_food:
            print(i)
        user_input =int(input('enter the food item you want to order :'))
        
        if user_input==0:
                self.oredered_food_items.append(list_of_food[0])
        elif user_input==1:
                self.oredered_food_items.append(list_of_food[1])
        elif user_input==2:
                self.oredered_food_items.append(list_of_food[2])
        else:
                print('choose items from the menu')
        
        print('choose 1 for order confirmation')
        print('choose 2 for order deletion')
        option = int(input('enter a number :'))
        self.ordered_item[order_id]= self.oredered_food_items
        if option ==1:
             print('order placed successfully...')
             with open('order_history.json','w') as f:
                  json.dump(self.ordered_item,f,indent=4)
        else:
             print('order cancelled')
        return self.ordered_item
    
    def order_history(self):
         for k,v in self.ordered_item.items():
              print(f'order id: {k} || order details: {v}')

    def edit_profile(self):
        with open('personal_details.json','r') as f:
              data = json.load(f)
        for k,v in data.items():
             print(f'user mail id: {k} || user details: {v}')
        
        mail_id= input('enter the mail which you want to update')
        field=input('enter the field which you want to update')
        updated_value= input('enter the updated value')
        data[mail_id][field] = updated_value
        with open('personal_detals.json','w') as f:
             json.dump(data,f,indent=4)
        return data
    

x=user()
x.login()







