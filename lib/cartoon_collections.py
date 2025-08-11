def roll_call_dwarves(dwarf_names): 
    i = 0
    while i < len(dwarf_names):
        dwarf_name = dwarf_names[i]
        print(f"{i + 1}. {dwarf_name}")
        i += 1


def summon_captain_planet(planeteer_calls):
    return [f"{planeteer_call.capitalize()}!" for planeteer_call in planeteer_calls ]

def long_planeteer_calls(assorted_words):
    return any(len(assorted_word) > 4 for assorted_word in assorted_words)

def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in foods:
        if item in cheeses:
            return item
    return None
    
