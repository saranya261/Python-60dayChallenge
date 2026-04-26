import copy

def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {
                "price": 50000,
                "stock": 10,
                "supplier": {"rating": 4.5}
            }
        },
        {
            "item": "Phone",
            "details": {
                "price": 20000,
                "stock": 25,
                "supplier": {"rating": 4.2}
            }
        }
    ]

def apply_discount(data, roll_number):
    length = len(data)
    index_to_modify = roll_number % length

    for i in range(len(data)):
        data[i]["details"]["price"] *= 0.9
        if i == index_to_modify:
            data[i]["details"]["stock"] -= 5

def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i] == modified[i]:
            unchanged += 1
        else:
            changed += 1

    return (changed, unchanged)

roll_number = int(input("Enter your roll number: "))

original_inventory = create_inventory()
original_safe = copy.deepcopy(original_inventory)

shallow_copy_inventory = original_inventory.copy()
deep_copy_inventory = copy.deepcopy(original_inventory)

apply_discount(shallow_copy_inventory, roll_number)
apply_discount(deep_copy_inventory, roll_number)

shallow_result = compare_data(original_safe, shallow_copy_inventory)
deep_result = compare_data(original_safe, deep_copy_inventory)

print("\n--- ORIGINAL INVENTORY ---")
print(original_safe)

print("\n--- SHALLOW COPY RESULT ---")
print(shallow_copy_inventory)

print("\n--- DEEP COPY RESULT ---")
print(deep_copy_inventory)

print("\n--- DIFFERENCES OBSERVED ---")

print("\nShallow Copy:")
print("Changed Items:", shallow_result[0])
print("Unchanged Items:", shallow_result[1])
print("Observation: Original data is ALSO changed")

print("\nDeep Copy:")
print("Changed Items:", deep_result[0])
print("Unchanged Items:", deep_result[1])
print("Observation: Original data is NOT affected")

print("\n--- TUPLE SUMMARY ---")
print("Shallow Copy:", shallow_result)
print("Deep Copy:", deep_result)
