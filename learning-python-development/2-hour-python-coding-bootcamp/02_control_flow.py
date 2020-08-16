# Control Flow
# If statements

bank_balance = 100.00
item_cost = 120.50
item_inventory = 1

if item_cost < bank_balance and item_inventory >= 1:
    bank_balance -= item_cost
    print("Transaction Successful")
    print(bank_balance)
elif item_cost == bank_balance and item_inventory >= 1:
    bank_balance -= item_cost
    print("Transaction Successful, but no funds left")
    print(bank_balance)
else:
    if item_inventory < 1:
        print("Item out of stock")
    else:
        print("Transaction failed, insufficient funds")
    print(bank_balance)

# While and For loops

total = 0
index = 1

while index <= 10:
    index += 1
    if index % 2 == 0:
        continue
    total += index

print(total)

roster = ["Kate", "John", "Sarah", "Kevin"]
for name in roster:
    print(name)
