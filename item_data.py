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
   
    

]


def get_item_names_and_weights(item_list):
    names = [item["name"] for item in item_list]
    weights = [item["weight"] for item in item_list]
    return names, weights


POSSIBLE_ITEM_NAMES, ITEM_WEIGHTS = get_item_names_and_weights(ALL_GAME_ITEMS)

