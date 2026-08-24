# A dictionary stores information as key-value pairs.
#
# Here:
# country = key
# capital = value

capitals = {
    "india": "New Delhi",
    "france": "Paris",
    "germany": "Berlin",
    "japan": "Tokyo",
    "australia": "Canberra",
    "canada": "Ottawa",
    "united kingdom": "London"
}

# Ask the user to enter a country.

country = input("Enter a country name: ")

# strip() removes unnecessary spaces before or after the text.
# lower() converts text to lowercase.
#
# This allows:
# India
# INDIA
# india
#
# to all be treated as "india".

country = country.strip().lower()

# "in" checks whether the country exists as a key in the dictionary.

if country in capitals:

    # capitals[country] gets the value associated with the country.

    print("Capital:", capitals[country])

else:
    print("Country not found in the dictionary.")
