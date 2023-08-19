#functionaliies related to admin
#  Admin will have the following functionalities: ⬅️
#     👉 1. Add new food items. Food Item will have the following details:
#             🔴 FoodID //It should be generated automatically by the application.
#             🔴 Name
#             🔴 Quantity. For eg, 100ml, 250gm, 4pieces etc
#             🔴 Price
#             🔴 Discount
#             🔴 Stock. Amount left in stock in the restaurant.

#     👉 2. Edit food items using FoodID.

#     👉 3. View the list of all food items.

#     👉 4. Remove a food item from the menu using FoodID.

import json
class admin:
    def __init__(self):
        self.food_id=0
        self.food_item={}

    def add_new_food(self):
        self.food_id+=1
        name = input('enter food name :')
        quantity = (input('enter food quantity :'))
        price = float(input('enter food price :'))
        discount = float (input('enter food discount :'))
        stock = (input('enter food stock :'))
        food_item= {'food_name':name,'food_quantity':quantity,'food_price':price,'food_discount':discount,'food_stock':stock,'discounted_price':price-((price*discount)/100)}
        self.food_item[self.food_id]=food_item
        with open ('food_item.json', 'w' ) as f:
            json.dump(self.food_item,f,indent=4)
        print('food item added succesfully....')
        return self.food_item
    
    def edit_food_items(self):
        with open('food_item.json', 'r') as f:
            data= json.load (f)
        for k,v in data.items():
                print(f'food_ID:{k} || food_item: {v}')
        id= input("enter the food id which you want to edit :")
        item= input("enter the item you want to edit :")
        updated_value= input("enter the updated value :")
        data[id][item]=updated_value
        with open ('food_item.json','w') as f:
            json.dump(data,f,indent=4)
        print ('food item updated successfully...')
        return data
    
    def show_food_items(self):
        with open('food_item.json', 'r') as f:
            data= json.load (f)
        for k,v in data.items():
            print(f'food_ID:{k} || food_item: {v}')
        
    def remove_food_items(self):
        with open('food_item.json', 'r') as f:
            data= json.load (f)
        for k,v in data.items():
            print(f'food ID:{k} || food item: {v}')
        id=input('enter the id which you want to delete :')
        del data[id]
        with open('food_item.json','w')as f:
            json.dump(data,f,indent=4)
        print('food item removed successfully...')
        return data


