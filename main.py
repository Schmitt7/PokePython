import pokedex as dex
import matplotlib.pyplot as plt
import numpy as np


def main():
    
    #retrive pokemon info and save to dictionary
    poke_info1 = dex.get_pokemon(pokemon_name1)
    poke_info2 = dex.get_pokemon(pokemon_name2)

    #Create list of types
    types = []
    types2 = []

    for poke_types in poke_info1["types"]:
        types.append(poke_types["type"]["name"].capitalize())
    

    for poke_types2 in poke_info2["types"]:
        types2.append(poke_types2["type"]["name"].capitalize())

    
    stats = {}
    stats2 = {}


    for s in poke_info1["stats"]:
        stats[s["stat"]["name"]] = s["base_stat"]


    for s2 in poke_info2["stats"]:
        stats2[s2["stat"]["name"]] = s2["base_stat"]

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


    hp2 = stats2.get("hp", 0)
    attack2 = stats2.get("attack", 0)
    defense2 = stats2.get("defense", 0)
    sp_attack2 = stats2.get("special-attack", 0)
    sp_defense2 = stats2.get("special-defense", 0)
    speed2 = stats2.get("speed", 0)



    #Set up radar plot
    labels = ["HP", "Attack", "Defense", "Speed", "Sp. Attack", "Sp. Defense"]
    values = [hp, attack, defense, speed, sp_attack, sp_defense]

    #Append the first value to end of the list making plot circular
    values += values[:1]


    #Set up angles for the radar plot
    #np.linspace(start, stop, num)
    #Start at 0
    #Stop at 2 x pi
    #Number of values shown gotten from length of values list
    angles = np.linspace(0, 2 * np.pi, len(values))


    #Create the Radar Plot

    #Create a figure(fig) and a set of subplots(ax)
    #Set size of figure to 6in by 6in [figsize=(6,6)]
    #subplot_kw=dict(polar=True) tells Matplotlib to create a polar subplot, which is needed for a radar plot.
    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
    
    #ax.fill() fills enclosed area of radar plot with color (blue)
    #angles contain angle positions for each stat
    #values contain the numerical values we use
    #alpha=0.4 sets transparency level of fill (0 is transparent, 1 is opaque)
    ax.fill(angles, values, color='blue', alpha=0.4)


    #ax.plot draws outline of radar plot
    #The line connects the points defined by angles & values
    #linewidth sets thickness of line
    ax.plot(angles, values, color='blue', linewidth=2)


    #ax.set_yticks() specifies the positions of the concentric circles on plot
    ax.set_yticks([50,100,150,200,260])


    #Set labels for the above y ticks
    ax.set_yticklabels(["50", "100", "150", "200", "260"], color="grey", size=8)


    #Set position of catagory labels (HP, Attack, Defense, etc.)
    #angles[:-1] exluddes closing angle that makes graph circular to avoid double labels
    ax.set_xticks(angles[:-1])


    #Assigns the labels to angles 
    ax.set_xticklabels(labels)


    #Display Graph
    plt.title(f"{pokemon_name1.capitalize()} Stats")
    plt.show()



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
        
        print()

        print(f"Name: {poke_info2["name"].capitalize()}")
        print(f"ID: {poke_info2["id"]}")
        print(f"Types: {', '.join(types2)}")
        print(f"Height: {poke_info2["height"]}")
        print(f"Weight: {poke_info2["weight"]}")
        print(f"HP: {hp2}")
        print(f"Attack: {attack2}")
        print(f"Defense: {defense2}")
        print(f"Special Attack: {sp_attack2}")
        print(f"Special Defense: {sp_defense2}")
        print(f"Speed: {speed2}")

        
        

        
        




if __name__ == "__main__":
    
    print("Compare your favorite Pokemon!")
    pokemon_name1 = input("Enter First Pokemons Name: ").lower()
    pokemon_name2 = input("Enter Second Pokemons Name: ").lower()
    
    main()





