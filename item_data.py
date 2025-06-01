ALL_GAME_ITEMS = [
    {
        "name": "Rock",
        "weight": 0.80,
        "description": "Rock No value",
        "effect_type": "none"
    },
   
    {
        "name": "Trash",
        "weight": 0.90,
        "description": "Trash No value",
        "effect_type": "none"
        
    },
    {
        "name": "Banana Trash",
        "weight": 0.90,
        "description": "You slipped on a banana and lost 2 health.",
        "effect_type": "fall_and_damage",
        "damage_amount": 2
        

    },
    {
        "name": "Fever.",
        "weight": 0.05,
        "description": " Your body is burning hot!",
        "effect_type": "fever",
        "damage_amount": 30
        
    },
      {
        "name": "Money",
        "weight": 0.8,
        "description": " +1",
        "effect_type": "gold",
        "effect_value": 1
     
        
    },
   
    

]


def get_item_names_and_weights(item_list):
    names = [item["name"] for item in item_list]
    weights = [item["weight"] for item in item_list]
    return names, weights


POSSIBLE_ITEM_NAMES, ITEM_WEIGHTS = get_item_names_and_weights(ALL_GAME_ITEMS)

