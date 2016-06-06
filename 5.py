pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold

def get_wooden_legs_and_gold(pirates):
    rich_with_wooden_legs = []
    for pirate in pirates:
        if pirate['has_wooden_leg'] == True and pirate['gold'] > 15:
            rich_with_wooden_legs.append(pirate['Name'])
    return rich_with_wooden_legs

print(get_wooden_legs_and_gold(pirates))
