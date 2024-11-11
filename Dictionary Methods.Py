# Keys

Student = {
    'Name': 'Snehal',
    'Age': 20,
    'Grade': 'A'
}
keys = Student.keys()
print(keys)

print('============================================')

# Copy

car = {
 'brand': 'Ford',
  'model': 'Mustang',
  'year': 2020
}
items = car.copy()
print(items)

print('========================================================')

# get

Employee ={
    'Id': 11,
    'name': 'Trisha Patel',
    'email':'123@gmail.com'
}
get = Employee.get('name')
print(get)
print('=========================================================')

# update()

Product = {
    'name':'Apple',
    'Location': 'USA',
    'Price': 2000
}
Product.update({'Date': '2020-01-01','Price':4000})

print(Product)

print('======================================================')

# pop()

Order = {
    'Id': 23,
    'product':'Tv',
    'email':'125@gmail.com',
    'price':10000
}
Order.pop('email')

print(Order)

print('======================================================')

# setdefault()

Transaction = {
    'Id': 15,
    'Paymennt Mode':'Online',
    'Amount': 500
}
Mode = Transaction.setdefault('Payment','Offline')

print(Mode)

print('====================================================')