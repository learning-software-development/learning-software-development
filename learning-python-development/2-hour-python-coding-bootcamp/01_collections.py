# Collections: tupels, list, dictories

full_name = ("First", "Last")
print(full_name)

inventory_item = ("apple", 5)
print(inventory_item)

roster = ["Kate", "John", "Sarah", "Kevin"]
print(roster)
print(roster[1])
print(roster[:3])
print(roster[2:])

inventory = {"apple": 5, "knife": 1, "shoes": 2}
print(inventory)
print(inventory["knife"])

# del full_name
print(len(full_name))
print(min(full_name))
print(max(full_name))

roster[1] = "Adam"
#del roster[2]
# roster.clear()
roster.append("Koos")
roster.pop(0)
print(roster)

print(max(inventory.values()))
print(inventory.items())
