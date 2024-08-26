import os

# Access the checklist parameter value once and split into a list
selected_options = os.environ.get("MY_CHECKLIST").split(',')

# Iterate over the list and print Narendra + each option
for option in selected_options:
    result = f"Narendra+{option}"
    print(result)