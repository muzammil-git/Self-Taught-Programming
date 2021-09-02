# https://www.w3resource.com/JSON/structures.php  JSON Data
# Concept: Key-Value pair, you can retrieve a value from key
# you can check key in dictionary but cant check value
my_dict = {
    "height":"5'10",
    "favorite color":"purple",
    "favorite author":"Cory",
    "snack":"magnum",
}

my_dict["key"] = "value"
my_dict["code"] = 9871

#printing value through key
print(my_dict["key"])

# Exception for putting wrong key
try:
    print(my_dict["cod"])
except Exception:
    print('The Key doesn\'t exist')

#Checks if the key is present in dictionary
if 'code' in my_dict :
    print(my_dict["code"])


#-----------------------x---------------------------------#

# Containers in Container.

#List example

healthy_cart = ["Vegetable", "Juice", "Protein Drinks"]
junk_cart = ["Burgers", "Sandwhich", "Gol Gappa"]

#Putting in tuple
cart = (healthy_cart, junk_cart)

print(cart[0][1])


test  = {
    "location" : (30.8654, 32.6910), # Tuple bcuz coordinates never change
    "celebs" : ["Muzammil", "Ahsan"], # List
    "facts" : {
        "country" : "Pakistan",            #Dictionary
        "city" : "Karachi",
    }
}

print(test["facts"]["country"])

# Retrieving Data inside Tuple
print(test["location"][0])
print(test["location"][1])


#Print all Keys in dictionary
print(test.keys())
#Print all Values in dictionary
print(test.values())

print("-----------------")

customer = {
  "firstName": "Syed Muzammil",
  "lastName": "Ali",
  "age": 20,
  "address":
			  {
                "streetAddress": "144 J B Hazra Road",
                "city": "Karachi",
                "state": "Sindh",
                "postalCode": "75703"
			  },
  "phoneNumber":
			  [
			        {
                      "type": "personal",
                      "number": "03339812411"
			        },
			        {
                      "type": "fax",
                      "number": "91-342-2567692"
			        }
	  		  ]
}

print(customer.keys())
print(customer["address"].keys())
print(customer["address"]["city"])
print(customer["address"]["streetAddress"])
print(customer["address"]["state"])
print(customer["address"]["postalCode"])

print("------------------")

# Through keys(), len(), type() I can determine whats inside and which type is present
print(customer.keys())
print(type(customer["phoneNumber"]))
print(customer["phoneNumber"][0].keys())
print(customer["phoneNumber"][0]["type"])
print(customer)


#print(customer["phoneNumber"][0])