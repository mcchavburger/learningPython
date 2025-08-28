age = int(input("How old are you?\n"))

# / will return float, // special operator that returns whole number division
decades = age // 10

# special charcter % 'Modulas" will return remander of the number when divided by int (10 in example below)
years = age % 10

print("You are " + str(decades) + " decades and " + str(years) + " old.")