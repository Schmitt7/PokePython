import pokedex as dex


def main():
    
    #retrive pokemon info and save to dictionary
    poke_info1 = dex.get_pokemon(pokemon_name1)
    #poke_info2 = dex.get_pokemon(pokemon_name2)


    #Create list of strings types
    #t is first dictionary
    #Extract name field from each dictionaries "type" key
    #Collects all type names into a list
    #rewrite as for loop
    types = [t["type"]["name"].capitalize() for t in poke_info1["types"]]
    
    #Create dictionary stats
    #key is stat name
    #value is base stat
    stats = {s["stat"]["name"]:
             s["base_stat"] for s in poke_info1["stats"]}
    
    moves = {
        m["move"]["name"].capitalize():{
            "power": m.get("power", "N/A"),
            "accuracy": m.get("accuracy")
        }
        for m in poke_info1["moves"]
    }
    
    #Save specific stats to variables, if no value found then set to 0
    hp = stats.get("hp", 0)
    attack = stats.get("attack", 0)
    defense = stats.get("defense", 0)
    sp_attack = stats.get("special-attack", 0)
    sp_defense = stats.get("special-defense", 0)
    speed = stats.get("speed", 0)





    if poke_info1:
        print(f"Name: {poke_info1["name"].capitalize()}")
        print(f"ID: {poke_info1["id"]}")
        print(f"Types: {', '.join(types)}")
        print(f"Height: {poke_info1["height"]}")
        print(f"Weight: {poke_info1["weight"]}")
        print(f"HP: {hp}")
        print(f"Attack: {attack}")
        print(f"Defense: {defense}")
        print(f"Special Attack: {sp_attack}")
        print(f"Special Defense: {sp_defense}")
        print(f"Speed: {speed}")
        #print("Possible Moves: ")
        #for move, details in moves.items():
            #print(f" {move} - Power: {details['power']}, Accuracy: {details['accuracy']}")
        
        

        
        




if __name__ == "__main__":
    
    print("Compare your favorite Pokemon!")
    pokemon_name1 = input("Enter First Pokemons Name: ").lower()
    #pokemon_name2 = input("Enter Second Pokemons Name: ").lower()
    
    main()





