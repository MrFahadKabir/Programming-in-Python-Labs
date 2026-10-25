resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


# Task 1: Display all resources
def display_resources(resources):
    if not resources:
        print("No resources available")
        return

    for resource in resources:
        print(
            "ID:", resource[0],
            "Name:", resource[1],
            "Category:", resource[2],
            "Quantity:", resource[3]
        )


# Task 2: Search by category
def search_by_category(resources, category):
    found = False

    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource)
            found = True

    if not found:
        print("No resources found")


# Task 3: Find unavailable resources
def find_unavailable(resources):
    found = False

    for resource in resources:
        if resource[3] == 0:
            print(resource)
            found = True

    if not found:
        print("No unavailable resources")


# Test all functions
print("ALL RESOURCES")
display_resources(resources)

print("\nELECTRONICS")
search_by_category(resources, "Electronics")

print("\nUNAVAILABLE RESOURCES")
find_unavailable(resources)

print("\nEMPTY LIST TEST")
display_resources([])
# Unknown resource ID
resource_id = 999
found = False

for resource in resources:
    if resource[0] == resource_id:
        print(resource)
        found = True

if not found:
    print("Resource ID not found")


# Negative quantity
quantity = -2

if quantity < 0:
    print("Quantity cannot be negative")