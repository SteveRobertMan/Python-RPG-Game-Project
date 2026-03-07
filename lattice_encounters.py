import config
import ui_components
import random
import stages # Used to spawn enemies for combat events

def execute_lattice_event(event_id, run_state, player_obj):
    """
    Returns True if completed safely, False if party wiped, or "BATTLE" if a fight was triggered.
    """
    ui_components.clear_screen()
    day = run_state["day"]

    run_state.setdefault("owned_manifolds", [])
    run_state.setdefault("static", 0)
    run_state.setdefault("event_flags", {})
    # Global Style Override
    event_color = "white"
    
    # Safely get a reference to party HP
    def apply_party_damage(pct):
        wiped = True
        for unit_name, (hp, max_hp) in run_state["hp_data"].items():
            dmg = int(max_hp * pct)
            new_hp = max(1, hp - dmg)
            run_state["hp_data"][unit_name] = (new_hp, max_hp)
            if new_hp > 1: wiped = False
        return not wiped

    def apply_party_heal(pct):
        for unit_name, (hp, max_hp) in run_state["hp_data"].items():
            heal = int(max_hp * pct)
            run_state["hp_data"][unit_name] = (min(max_hp, hp + heal), max_hp)

    # ==========================================
    # ID1 - Disciplinary Committee Meeting
    # ==========================================
    if event_id == 1:
        ui_components.print_header("Disciplinary Committee Meeting")
        text = """We’re members of the Kasakura High School Disciplinary Committee.
Club President Masayoshi Kouhei is at the front of the room, briefing the entire Committee about plans to improve patrols outside the school’s area.

A member nudged me from the next seat over, looking concerned.
“Hey. Don’t you think the President’s been talking over this meeting for longer than usual? I’m just…starting to think I’m not gonna get all of this complicated stuff, if this goes on.”"""
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Did you bring the schedule? We can just follow it later.", style=event_color, highlight=False)
        config.console.print("[2] I can review the contents with you after this.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nWhat should we tell him? > ")
        if choice == "1":
            config.console.print("\n[green]A look of relief flashes across the fellow member’s face.[/green]", highlight=False)
            config.console.print("“Oh, really? That’s a relief… Although, I don’t see yours with you. I brought a spare with me, so why don’t you have it as thanks?”", style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Disciplinary Committee Schedule (II).[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Disciplinary Committee Schedule (II)")
        elif choice == "2":
            config.console.print("\n[green]A grin of mischief flashes across the fellow member’s face.[/green]", highlight=False)
            config.console.print("“That so?! That’s so nice of you..! Since you promise to tell me all about it again after the meeting, I think I’ll just head out first! Get some fresh air! Hold this for me too!”", style=event_color, highlight=False)
            config.console.print("Before we could say anything, the Committee member shoved his own bokken to us and impressively darted off.", style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Wooden Bokken (II).[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Wooden Bokken (II)")
        
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID2 - The Overloaded Prototype
    # ==========================================
    elif event_id == 2:
        ui_components.print_header("The Overloaded Prototype")
        text = """We step into a chaotic, sparking room that perfectly resembles Kagaku’s second lab at Kasakura High.
At the center of the room, Kagaku is frantically typing on a terminal while a massive, jury-rigged machine hums violently, emitting dangerous arcs of blue electricity.

"It’s destabilizing! The dimensional friction is too high for these commercial processors!" The phantom Kagaku yells. "If I don't vent the core, the whole lab is going to blow!"
She reaches for a heavily sparking control panel but hesitates, terrified of the lethal voltage."""
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Step in and manually yank the searing-hot processor out for her.", style=event_color, highlight=False)
        config.console.print("[2] Tell her to hit the emergency kill switch and evacuate.", style=event_color, highlight=False)
        config.console.print("[3] Search the surrounding workbenches while she's distracted.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nWhat should we do? > ")
        if choice == "1":
            config.console.print("\nI grit my teeth and dash forward, plunging my hand directly into the sparking console. A violent shock of blue electricity courses through my arm, but I manage to tear the smoking hardware out.", style=event_color, highlight=False)
            apply_party_damage(0.15)
            config.console.print("\n[bold red]- Party takes 15% Max HP damage.[/bold red]", highlight=False)
            config.console.print("[bold cyan]- Gained the manifold Charred Microchip (I)[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Charred Microchip (I)")
        elif choice == "2":
            config.console.print('\n"Shut it down! Get out of here!" I yell. Startled, the phantom Kagaku instinctively slams her fist onto a massive red emergency button. She leaves behind a stash of research funds on the desk as thanks.', style=event_color, highlight=False)
            gain = int(40 * day * random.uniform(1.01, 1.50))
            run_state["static"] += gain
            config.console.print(f"\n[bold honeydew2]- Gained {gain} Static[/bold honeydew2]", highlight=False)
        elif choice == "3":
            config.console.print("\nWhile the scientist is busy panicking, we scavenge a handful of leftover supplies and loose currency she had scattered across her messy workbenches.", style=event_color, highlight=False)
            run_state["static"] += 50
            config.console.print("\n[bold honeydew2]- Gained 50 Static[/bold honeydew2]", highlight=False)
            
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID3 - Pride of the Iron Fist
    # ==========================================
    elif event_id == 3:
        ui_components.print_header("Pride of the Iron Fist")
        text = """The misty void shifts, dropping us into a damp, narrow alleyway near Heiwa Seiritsu High School.
Leaning against a brick wall is a battered delinquent with a buzzcut: Kuroda, the 'Iron Fist of Heiwa'.
He is furiously wrapping his knuckles with thick, blood-stained bandages, muttering to himself.

"Damnit... lost to a Kasakura bookworm. My rapid jabs were supposed to be invincible... I need to punch something to get my pride back."
He looks up, his eyes locking onto us with a sudden, reckless bloodlust.
"You! You Kasakura brats, huh?! Perfect timing!" """
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Accept his challenge.", style=event_color, highlight=False)
        config.console.print("[2] Offer him a critique on his sloppy footwork instead.", style=event_color, highlight=False)
        config.console.print("[3] Throw some loose change at him to buy time and run.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1":
            config.console.print('\n"Bring it on," I say, dropping into a low stance. Kuroda roars, charging forward with his signature rapid-fire piston punches.', style=event_color, highlight=False)
            ui_components.time.sleep(1.5)
            
            enemies = []
            enemies.append(stages.spawn_lattice_enemy("Heiwa Seiritsu Delinquent Leader Fighter", "‘Iron Fist Of Heiwa’ – Kuroda", day, 15, 15))
            enemies.append(stages.spawn_lattice_enemy("Spike Bat Heiwa Seiritsu Delinquent", None, day, 15, 15))
            enemies.append(stages.spawn_lattice_enemy("Chain Fist Heiwa Seiritsu Delinquent", None, day, 15, 15))
            
            config.player_data["current_enemies"] = [e for e in enemies if e]
            config.player_data["lattice_node_type"] = "events"
            config.current_state = config.STATE_BATTLE
            
            run_state["owned_manifolds"].append("Iron Fist Wraps (I)")
            run_state["static"] += int(60 * day * random.uniform(1.01, 1.50))
            return "BATTLE"
            
        elif choice == "2":
            config.console.print('\n"Your punches are fast, but your center of gravity is too high." I say. The phantom Kuroda freezes, blinking, before letting out an annoyed sigh. "Tch... getting lectured by the enemy... but ya ain’t wrong." He unwraps his hands, tossing the durable cloth toward me.', style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Iron Fist Wraps (I)[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Iron Fist Wraps (I)")
        elif choice == "3":
            config.console.print('\nI quickly dig into my pockets, chucking arcade tokens at his face. "Gah! What the—?!" While he is momentarily blinded, we bolt out of the alleyway.', style=event_color, highlight=False)
            loss = int(30 * random.uniform(1.01, 1.50))
            run_state["static"] = max(0, run_state["static"] - loss)
            config.console.print(f"\n[bold red]- Lost {loss} Static[/bold red]", highlight=False)
            
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID4 - Underground Notice
    # ==========================================
    elif event_id == 4:
        ui_components.print_header("Underground Notice")
        text = """We’re in a grimy underground tunnel. Pinned to a rusted bulletin board is a bounty list detailing the names, crimes, and payouts for various 'Ibara' outcasts.
Standing in front of the board is a hooded informant, counting cash. He notices us and draws a dagger.

"Oi. This is restricted underworld intel. Keep walking, or pay the toll to look." """
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Pay the informant's toll for the information.", style=event_color, highlight=False)
        config.console.print("[2] \"We don't pay for what we can take.\"", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1":
            loss = int(60 * random.uniform(1.01, 1.50))
            run_state["static"] = max(0, run_state["static"] - loss)
            config.console.print(f"\nWe hand over a stack of currency. The informant steps aside. This intel will give us an edge.", style=event_color, highlight=False)
            config.console.print(f"\n[bold red]- Lost {loss} Static[/bold red]", highlight=False)
            config.console.print("[bold cyan]- Gained the manifold Underworld Bounty Poster (I)[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Underworld Bounty Poster (I)")
            ui_components.get_player_input("Press Enter to continue...")
            return True
        elif choice == "2":
            config.console.print("\nWe draw our weapons. The informant curses, realizing he's outmatched, but refuses to back down.", style=event_color, highlight=False)
            ui_components.time.sleep(1.5)
            
            enemies = [stages.spawn_lattice_enemy("Raven", "Underworld Informant", day, 15, 15)]
            config.player_data["current_enemies"] = [e for e in enemies if e]
            config.player_data["lattice_node_type"] = "events"
            config.current_state = config.STATE_BATTLE
            
            run_state["owned_manifolds"].append("Underworld Bounty Poster (I)")
            run_state["static"] += int(60 * random.uniform(1.01, 1.50))
            return "BATTLE"

    # ==========================================
    # ID5 - Remnants of the Cargo Bay
    # ==========================================
    elif event_id == 5:
        ui_components.print_header("Remnants of the Cargo Bay")
        text = """The air grows hot and smells of ozone and motor oil. We stand on the metal grating of a cruise ship's armory.
The battle against the three mercenary ninjas—Raven, Falcon, and Eagle—seems to have already concluded here in this timeline echo.
However, scattered across the blasted crates is their discarded gear. We only have time to thoroughly scavenge one pile before the area collapses."""
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Search where the spiky-haired ninja (Raven) deployed his distraction.", style=event_color, highlight=False)
        config.console.print("[2] Search the weapon racks where the ponytail ninja (Eagle) was pinned down.", style=event_color, highlight=False)
        config.console.print("[3] Search near the missile casing where the blonde ninja (Falcon) fell.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nWhere should we search? > ")
        if choice == "1":
            config.console.print("\nHidden beneath a cracked panel, we find an intact, specialized explosive.", style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Mercenary's Smoke Bomb (I)[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Mercenary's Smoke Bomb (I)")
        elif choice == "2":
            config.console.print("\nLodged deeply into a steel beam are the very weapons he used. With a hard tug, I pull them free.", style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Mercenary's Twin Daggers (I)[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Mercenary's Twin Daggers (I)")
        elif choice == "3":
            config.console.print("\nAmidst the rubble, we find the shredded, sweat-stained remnants of his tactical shirt. It's crude, but incredibly durable.", style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Mercenary’s Heavy Torn Sleeves (I)[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Mercenary’s Heavy Torn Sleeves (I)")
            
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID6 - The Captain's Respite
    # ==========================================
    elif event_id == 6:
        ui_components.print_header("The Captain's Respite")
        text = """We step into a pristine, quiet room that mirrors Mei's Division Station Office in Sector II.
Sitting right in the center of the desk is a beautifully crafted, jade-inlaid porcelain teacup, emitting a warm, calming trail of steam.
It seems the Captain stepped out for a rare, much-needed break. The atmosphere is incredibly peaceful."""
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Take a moment to sit on the sofa, drink the tea, and rest.", style=event_color, highlight=False)
        config.console.print("[2] \"Borrow\" the beautiful teacup as a souvenir of Yunhai craftsmanship.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1":
            config.console.print("\nWe pass the teacup around. The herbal blend is masterful, perfectly soothing our frayed nerves and washing away the deep aches.", style=event_color, highlight=False)
            apply_party_heal(0.25)
            config.console.print("\n[bold green]- Party each heals 25% of Max HP.[/bold green]", highlight=False)
        elif choice == "2":
            config.console.print('\n"Mei-san wouldn\'t mind if we took a little memento, right?" We carefully wrap the exquisite teacup.', style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Enforcer Station Tea Cup (I)[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Enforcer Station Tea Cup (I)")
            
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID7 - Polite Escort
    # ==========================================
    elif event_id == 7:
        ui_components.print_header("Polite Escort")
        text = """The mist clears, placing us in an opulent hotel lobby.
A young man with impeccable posture, a pristine white suit, and glowing neon-blue, star-shaped pupils approaches us with a slight bow. It’s a Starguard.
"Ah, there you are," he says politely. "The Starguard security detail is ready to escort you safely, my esteemed clients."
He has mistaken us for VIPs. The sheer pressure radiating from him tells me fighting him would be a terrible idea."""
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] \"Yes, thank you. Lead the way.\"", style=event_color, highlight=False)
        config.console.print("[2] \"You have the wrong people. We aren't your clients.\"", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1":
            config.console.print("\nDeciding it's best not to antagonize a monster, I play along. He escorts us safely through the halls while calmly lecturing us on his family's history. We gained nothing but a history lesson.", style=event_color, highlight=False)
        elif choice == "2":
            config.console.print('\n"You have the wrong people." I shake my head. The Starguard pauses, mildly surprised. "I see. My sincerest apologies for the mix-up. Please, take one of my family\'s spare operational tools to help you avoid the bloodshed."', style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Plasma-Blue Lenses (II).[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Plasma-Blue Lenses (II)")
            
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID8 - The Fairies' Tea Party
    # ==========================================
    elif event_id == 8:
        ui_components.print_header("The Fairies' Tea Party")
        text = """We are dropped into a lush, indoor artificial forest. We are in the Student Council office of Kiryoku Gakuen.
Sitting around a living wood table are three "Fairies": Ayako, Sumiko, and Rina.
Ayako spots us and grins. "Well, look who it is! Care for a welcoming gift from the council? Or perhaps you're here to sweat a little instead?" """
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Ask the 'Forest Guardian' Ayako for a blessing.", style=event_color, highlight=False)
        config.console.print("[2] Ask the 'Lake Strider' Sumiko for a blessing.", style=event_color, highlight=False)
        config.console.print("[3] Ask the 'Nocturnal Companion' Rina for a blessing.", style=event_color, highlight=False)
        config.console.print("[4] \"We're here to sweat!\" Challenge Ayako and Sumiko to a spar!", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1":
            config.console.print('\n"Smart choice!" Ayako laughs brightly, sliding a beautifully carved wooden weapon across the table.', style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Forest Guardian’s Baton (II).[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Forest Guardian’s Baton (II)")
        elif choice == "2":
            config.console.print('\nSumiko offers a polite smile. She hands over a heavily detailed book filled with tactical notes.', style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Lake Strider’s Ledger (II).[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Lake Strider’s Ledger (II)")
        elif choice == "3":
            config.console.print('\nRina simply nods, pulling a stylish red hat from her bag. "For night operations. Keep your head down."', style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold Nocturnal Secretary Beret (II).[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Nocturnal Secretary Beret (II)")
        elif choice == "4":
            config.console.print('\nI crack my knuckles. Ayako’s eyes light up with feral excitement, and Sumiko smiles gracefully.', style=event_color, highlight=False)
            ui_components.time.sleep(1.5)
            
            enemies = []
            enemies.append(stages.spawn_lattice_enemy("‘Forest Guardian’ Fairy Ayako", None, day, 15, 15))
            enemies.append(stages.spawn_lattice_enemy("‘Lake Strider’ Fairy Sumiko", None, day, 15, 15))
            enemies.append(stages.spawn_lattice_enemy("Kiryoku Gakuen Student Council Combatant", "Combatant A", day, 15, 15))
            enemies.append(stages.spawn_lattice_enemy("Kiryoku Gakuen Student Council Combatant", "Combatant B", day, 15, 15))
            
            config.player_data["current_enemies"] = [e for e in enemies if e]
            config.player_data["lattice_node_type"] = "events"
            config.current_state = config.STATE_BATTLE
            
            run_state["owned_manifolds"].append("Forest Guardian’s Baton (II)")
            run_state["owned_manifolds"].append("Lake Strider’s Ledger (II)")
            return "BATTLE"

        if choice in ["1", "2", "3"]:
            ui_components.get_player_input("Press Enter to continue...")
            return True

    # ==========================================
    # ID9 - Covert Observation
    # ==========================================
    elif event_id == 9:
        ui_components.print_header("Covert Observation")
        text = """We are dropped onto the roof of a building overlooking Heiwa Seiritsu High School. We’re wearing dark tactical gear.
Suddenly, a radio crackles on my belt. It's Secretary Miyu's cold voice.
"Operative. Report your status. Are the Heiwa delinquents mobilizing their main force in a unified front, or are they acting chaotically?" """
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] \"They are acting chaotically, waiting for a brawl.\"", style=event_color, highlight=False)
        config.console.print("[2] \"They are mobilizing in a unified, strategic front.\"", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nReport > ")
        if choice == "2":
            config.console.print('\nMiyu sighs. "An idiot, just like them, huh? You are an impostor. Sending enforcement to your coordinates."', style=event_color, highlight=False)
            ui_components.time.sleep(1.5)
            enemies = [
                stages.spawn_lattice_enemy("Infiltrating Heiwa Seiritsu Delinquent Leader", "The Boss’ Operative A", day, 15, 15),
                stages.spawn_lattice_enemy("Infiltrating Kiryoku Gakuen Student Council Combatant", "The Boss’ Operative B", day, 15, 15),
                stages.spawn_lattice_enemy("Infiltrating Kasakura High School Disciplinary Committee Combatant", "The Boss’ Operative C", day, 15, 15)
            ]
            config.player_data["current_enemies"] = [e for e in enemies if e]
            config.player_data["lattice_node_type"] = "events"
            config.current_state = config.STATE_BATTLE
            return "BATTLE"
            
        elif choice == "1":
            config.console.print('\n"That’s accurate." Miyu replies. "Now, second question. Where are the Upperclassmen positioning themselves? On the frontlines with the fodder?"', style=event_color, highlight=False)
            config.console.print("\n[1] \"Yes, the Upperclassmen are leading the charge.\"", style=event_color, highlight=False)
            config.console.print("[2] \"No, they are holding back deep inside the campus.\"", style=event_color, highlight=False)
            choice2 = ui_components.get_player_input("\nReport > ")
            
            if choice2 == "1":
                config.console.print('\n"Incorrect." Miyu states coldly. "An imposter has compromised the operation."', style=event_color, highlight=False)
                ui_components.time.sleep(1.5)
                enemies = [
                    stages.spawn_lattice_enemy("Infiltrating Heiwa Seiritsu Delinquent Leader", "The Boss’ Operative A", day, 15, 15),
                    stages.spawn_lattice_enemy("Infiltrating Kiryoku Gakuen Student Council Combatant", "The Boss’ Operative B", day, 15, 15),
                    stages.spawn_lattice_enemy("Infiltrating Kasakura High School Disciplinary Committee Combatant", "The Boss’ Operative C", day, 15, 15)
                ]
                config.player_data["current_enemies"] = [e for e in enemies if e]
                config.player_data["lattice_node_type"] = "events"
                config.current_state = config.STATE_BATTLE
                return "BATTLE"
            elif choice2 == "2":
                config.console.print('\n"Correct." Miyu affirms. "Maintain your position and document everything on the standardized forms provided in your vest."', style=event_color, highlight=False)
                config.console.print("\n[bold cyan]- Gained the manifold Blank Report Papers (II)[/bold cyan]", highlight=False)
                run_state["owned_manifolds"].append("Blank Report Papers (II)")
                ui_components.get_player_input("Press Enter to continue...")
                return True

    # ==========================================
    # ID10 - The Seditious Encounter
    # ==========================================
    elif event_id == 10:
        ui_components.print_header("The Seditious Encounter")
        text = """A man in tattered leather rags drops from the sky, landing heavily in front of us without making a sound. It's one of the legendary Propagators of the Seditious Garden.
His purple eyes are sharp. "Don't move a single muscle, kids. You're in a very dangerous situation right now." """
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Trust him. Stand completely still and let him inspect us.", style=event_color, highlight=False)
        config.console.print("[2] Refuse and immediately run away into the mist.", style=event_color, highlight=False)
        config.console.print("[3] Draw weapons. We can’t take orders from strangers.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1":
            config.console.print('\nWe stand perfectly still. He reaches behind Benikawa\'s collar and crushes something. "An Ibara planted a tracker on you. Sloppy," he mutters, handing us a mechanical device. "Take this spare one."', style=event_color, highlight=False)
            config.console.print("\n[bold cyan]- Gained the manifold ShinobiTech Tracker Bug (II)[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("ShinobiTech Tracker Bug (II)")
        elif choice == "2":
            config.console.print("\nWe turn and sprint back into the mist. He doesn't chase us, clicking his tongue in mild disappointment.", style=event_color, highlight=False)
        elif choice == "3":
            config.console.print('\n"Foolish weeds," he sighs. In a blur of motion too fast to track, he strikes our pressure points. Agony flares as we are dropped in an instant. He vanishes into the shadows.', style=event_color, highlight=False)
            apply_party_damage(0.15)
            config.console.print("\n[bold red]- Party takes 15% Max HP damage.[/bold red]", highlight=False)
            
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID11 - Enforcing the Peace
    # ==========================================
    elif event_id == 11:
        ui_components.print_header("Enforcing the Peace")
        text = """The air shifts, placing us right in the middle of a massive, multi-way street brawl in the Westward Megastructure's Sector II.
We are wearing the white cloud-patterned cloaks of the Yunhai Association Enforcers. Captain Mei is standing beside us, her Jian drawn.
"The local gangs are completely out of control. We cannot suppress all three factions at once before they destroy the district."
She turns to us. "Alright. Let’s choose a primary target for our own unit to focus our operations on!" """
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Target the Golden Fist Union.", style=event_color, highlight=False)
        config.console.print("[2] Target the Black Water Dock.", style=event_color, highlight=False)
        config.console.print("[3] Target the Twin Mountain Gate.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice in ["1", "2", "3"]:
            ui_components.time.sleep(1.0)
            enemies = []
            if choice == "1":
                config.console.print('\n"I agree. Their numbers will pose a problem... Suppress the Golden Fist Union!" Mei commands.', style=event_color, highlight=False)
                enemies = [
                    stages.spawn_lattice_enemy("Golden Fist Union Gangster", "Golden Fist Union Gangster A", day, 25, 25),
                    stages.spawn_lattice_enemy("Golden Fist Union Gangster", "Golden Fist Union Gangster B", day, 25, 25),
                    stages.spawn_lattice_enemy("Golden Fist Union Gangster", "Golden Fist Union Gangster C", day, 25, 25),
                    stages.spawn_lattice_enemy("Golden Fist Union Gangster Leader", None, day, 25, 25)
                ]
                run_state["owned_manifolds"].append("Gilded Gauntlets (II)")
            elif choice == "2":
                config.console.print('\n"It’s true that they’re the most skilled ones currently. Suppress the Black Water Dock!" Mei commands.', style=event_color, highlight=False)
                enemies = [
                    stages.spawn_lattice_enemy("Black Water Dock Gangster", "Black Water Dock Gangster A", day, 25, 25),
                    stages.spawn_lattice_enemy("Black Water Dock Gangster", "Black Water Dock Gangster B", day, 25, 25),
                    stages.spawn_lattice_enemy("Black Water Dock Gangster", "Black Water Dock Gangster C", day, 25, 25),
                    stages.spawn_lattice_enemy("Black Water Dock Gangster Leader", None, day, 25, 25)
                ]
                run_state["owned_manifolds"].append("Taser-retrofitted Spearhead (II)")
            elif choice == "3":
                config.console.print('\n"You’re right. The most brutal fighters... Suppress the Twin Mountain Gate!" Mei commands.', style=event_color, highlight=False)
                enemies = [
                    stages.spawn_lattice_enemy("Twin Mountain Gate Gangster", "Twin Mountain Gate Gangster A", day, 25, 25),
                    stages.spawn_lattice_enemy("Twin Mountain Gate Gangster", "Twin Mountain Gate Gangster B", day, 25, 25),
                    stages.spawn_lattice_enemy("Twin Mountain Gate Gangster", "Twin Mountain Gate Gangster C", day, 25, 25),
                    stages.spawn_lattice_enemy("Twin Mountain Gate Gangster Leader", None, day, 25, 25)
                ]
                run_state["owned_manifolds"].append("Double Axe Heads (II)")
                
            config.player_data["current_enemies"] = [e for e in enemies if e]
            config.player_data["lattice_node_type"] = "events"
            config.current_state = config.STATE_BATTLE
            return "BATTLE"

    # ==========================================
    # ID12 - The Botanist's Proposition
    # ==========================================
    elif event_id == 12:
        ui_components.print_header("The Botanist's Proposition")
        text = """The chaotic environment of the Lattice stabilizes into a breathtaking, climate-controlled greenhouse.
Standing at a workbench is Kagaku Shamiko, dressed in the green and white training uniform of the Luoxia Gardening School.

"Ah! The Vanguard from Kasakura! Perfect timing!" She waves a beaker. "I'm trying to mass-produce an entirely new, instantaneous battle recovery gadget! Unfortunately, I need a stable biological base serum to work from, and a fresh supply of Yunhai local specialties." """
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] \"We can gather those for you. Give us a few days.\"", style=event_color, highlight=False)
        config.console.print("[2] \"We're in the middle of a warzone. We don't have time to forage.\"", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1":
            config.console.print("\nKagaku's eyes light up. \"Really?! Okay, I need to prep the synthesis equipment. Come back and see me in about two days!\"", style=event_color, highlight=False)
            run_state["event_flags"]["jade_synthesis_day"] = day + 2
        elif choice == "2":
            config.console.print("\nKagaku pouts. \"Alright, alright. Take these research budgets and at least buy the materials if you stumble across any!\"", style=event_color, highlight=False)
            gain = int(150 * random.uniform(1.01, 1.50))
            run_state["static"] += gain
            config.console.print(f"[bold honeydew2]- Gained {gain} Static[/bold honeydew2]", highlight=False)
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID13 - Jade Synthesis (Delayed Event)
    # ==========================================
    elif event_id == 13:
        ui_components.print_header("Jade Synthesis")
        text = """We step back into the lush greenhouse of the Luoxia Gardening School.
Kagaku practically sprints over. "You're back! Tell me you brought the materials! I need a strong base serum and the local botanical samples!" """
        config.console.print(text, style=event_color, highlight=False)
        
        has_reqs = "Hanefuji Healing Serum (I)" in run_state["owned_manifolds"] and "Yunhai Energetic Herbs (II)" in run_state["owned_manifolds"]
        
        if has_reqs:
            config.console.print("\n[1] [Required Manifolds Owned] \"We have exactly what you need. Here are the samples.\"", style=event_color, highlight=False)
        else:
            config.console.print("\n[1] [Missing Required Manifolds]", style="dim", highlight=False)
        config.console.print("[2] \"Sorry, Kagaku. We came up empty-handed.\"", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1" and has_reqs:
            config.console.print("\n\"Yes! This is it!\" Kagaku tosses the ingredients into her machine. \"I've created a super-serum! Take the prototype!\"", style=event_color, highlight=False)
            config.console.print("[bold cyan]- Gained the manifold Azure Jade Serum (IV)[/bold cyan]", highlight=False)
            run_state["owned_manifolds"].append("Azure Jade Serum (IV)")
        else:
            config.console.print("\nKagaku sighs. \"I made some untested, lower-tier prototypes while I waited. Drink up!\" A wave of refreshing energy completely washes away our fatigue.", style=event_color, highlight=False)
            apply_party_heal(0.80)
            config.console.print("[bold green]- Party heals 80% Max HP.[/bold green]", highlight=False)
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID14 - The Queen's Festival
    # ==========================================
    elif event_id == 14:
        ui_components.print_header("The Queen's Festival")
        text = """We are dropped into a vibrant festival at Kiryoku Gakuen.
A booming voice echoes: "Whoever manages to gather all three 'Hidden Treasures of the Fairies' Grove' can trade them in right here! The grand prize is the limited edition 'A Cuteness Comprehensive Guide'!"
Sitting at the grand prize booth is the "Queen of Fairies" Aina, dozing off."""
        config.console.print(text, style=event_color, highlight=False)
        
        has_reqs = all(m in run_state["owned_manifolds"] for m in ["Forest Guardian’s Baton (II)", "Lake Strider’s Ledger (II)", "Nocturnal Secretary Beret (II)"])
        
        if has_reqs:
            config.console.print("\n[1] [Treasures Owned] \"We already have all the 'treasures'. Let's go claim the grand prize.\"", style=event_color, highlight=False)
        else:
            config.console.print("\n[1] [Missing the 3 Fairy Treasures]", style="dim", highlight=False)
        config.console.print("[2] \"We don't have the items. Let's go hit the game booths and try to win them.\"", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1" and has_reqs:
            config.console.print("\nWe place the baton, ledger, and beret onto the counter. Aina stirs, sluggishly pulling out a beautifully bound guidebook. Naganohara is vibrating with pure fangirl excitement.", style=event_color, highlight=False)
            run_state["owned_manifolds"].remove("Forest Guardian’s Baton (II)")
            run_state["owned_manifolds"].remove("Lake Strider’s Ledger (II)")
            run_state["owned_manifolds"].remove("Nocturnal Secretary Beret (II)")
            run_state["owned_manifolds"].append("A Cuteness Comprehensive Guide: “Queen of Fairies” (IV)")
            config.console.print("[bold cyan]- Gained the manifold A Cuteness Comprehensive Guide: “Queen of Fairies” (IV)[/bold cyan]", highlight=False)
        else:
            config.console.print("\nWe try the shooting gallery and obstacle courses. We come up empty-handed on the grand treasures, but trade our tickets for spending money.", style=event_color, highlight=False)
            gain = int(150 * random.uniform(1.01, 1.50))
            run_state["static"] += gain
            config.console.print(f"[bold honeydew2]- Gained {gain} Static[/bold honeydew2]", highlight=False)
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID15 - Whispers of the Fairies' Grove
    # ==========================================
    elif event_id == 15:
        ui_components.print_header("Whispers of the Fairies' Grove")
        text = """We overhear a group of Kiryoku students whispering excitedly.
"Did you hear? The Council is swapping out Aina-sama's 'Fairywings' for a new set! Rumor has it they're giving them away!"
Naganohara immediately stops in her tracks, her eyes sparkling with intense curiosity."""
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] Approach the Kiryoku students and ask about the rumors.", style=event_color, highlight=False)
        config.console.print("[2] Dismiss the rumors as mere gossip. We're too busy.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "2":
            config.console.print('\n"We don\'t have time to chase down rumors." I tell Naganohara. She pouts, but we stay out of trouble.', style=event_color, highlight=False)
            ui_components.get_player_input("Press Enter to continue...")
            return True
            
        config.console.print('\nWe ask for details. A sly girl smirks. "I could really use some pocket change. You want intel? Show me how much you want it~."', style=event_color, highlight=False)
        cost1 = int(100 * random.uniform(0.5, 1.10))
        config.console.print(f"\n[1] [Cost: {cost1} Static] Pay up.", style=event_color, highlight=False)
        config.console.print("[2] \"We're not paying you for high school gossip.\"", style=event_color, highlight=False)
        
        c2 = ui_components.get_player_input("\nDecision > ")
        if c2 == "1" and run_state["static"] >= cost1:
            run_state["static"] -= cost1
            config.console.print('\nShe explains they are auctioning off Aina-sama\'s old possessions. "Wait, what exactly are the \'Fairywings\'?" I ask. She smirks again. "Premium info. Pay up more."', style=event_color, highlight=False)
            cost2 = int(120 * random.uniform(0.5, 1.10))
            config.console.print(f"\n[1] [Cost: {cost2} Static] Pay up.", style=event_color, highlight=False)
            config.console.print("[2] \"That's enough. We're done paying.\"", style=event_color, highlight=False)
            
            c3 = ui_components.get_player_input("\nDecision > ")
            if c3 == "1" and run_state["static"] >= cost2:
                run_state["static"] -= cost2
                config.console.print('\n"The \'Fairywings\' are her absolute cutest custom-made paper wings! If you want to attend the auction, come back tomorrow."', style=event_color, highlight=False)
                run_state["event_flags"]["fairy_auction_day"] = day + 1
            else:
                config.console.print('\n"We\'re cutting our losses." The girls roll their eyes.', style=event_color, highlight=False)
        else:
            config.console.print("\nWe aren't falling for a shakedown.", style=event_color, highlight=False)
            
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID16 - Price of Admission (Delayed Event)
    # ==========================================
    elif event_id == 16:
        ui_components.print_header("Price of Admission")
        text = """We return to Kiryoku Gakuen the next day, meeting the gossip girl.
"You came back! You need an official 'pass' to enter the Council Hall auction tomorrow. Since you guys are from Kasakura, you won't be able to get one. Unless..." She rubs her fingers together."""
        config.console.print(text, style=event_color, highlight=False)
        
        cost1 = int(150 * random.uniform(0.5, 1.10))
        config.console.print(f"\n[1] [Cost: {cost1} Static] Pay up.", style=event_color, highlight=False)
        config.console.print("[2] \"This is a complete scam. Let's just leave.\"", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1" and run_state["static"] >= cost1:
            run_state["static"] -= cost1
            config.console.print('\nI hand over the cash. She hands over one pass. Naganohara volunteers instantly! "Not so fast," the girl interrupts. "She needs a Kiryoku disguise... which I happen to have. For a price."', style=event_color, highlight=False)
            cost2 = int(150 * random.uniform(0.5, 1.10))
            config.console.print(f"\n[1] [Cost: {cost2} Static] Pay up...", style=event_color, highlight=False)
            config.console.print("[2] \"Absolutely not. We’re leaving.\"", style=event_color, highlight=False)
            
            c2 = ui_components.get_player_input("\nDecision > ")
            if c2 == "1" and run_state["static"] >= cost2:
                run_state["static"] -= cost2
                config.console.print('\nYuri groans about wasting money on paper wings, but Naganohara convinces her it’s an artifact of immense morale-boosting power. The auction begins tomorrow.', style=event_color, highlight=False)
                run_state["event_flags"]["fairy_bidding_day"] = day + 1
            else:
                config.console.print('\n"I am not paying for a stolen uniform," I state flatly.', style=event_color, highlight=False)
        else:
            config.console.print('\n"We are being extorted." We walk away.', style=event_color, highlight=False)
            
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID17 - The Bidding War (Delayed Event)
    # ==========================================
    elif event_id == 17:
        ui_components.print_header("The Bidding War")
        text = """It’s the day of the auction. Naganohara, disguised flawlessly, infiltrates the Council Hall while we listen through a comms earbud.
"We will now begin the bidding for Aina-sama's cherished Fairywings!"
The room instantly erupts into a frenzy."""
        config.console.print(text, style=event_color, highlight=False)
        
        costs = [
            int(50 * random.uniform(1.0, 1.10)),
            int(110 * random.uniform(1.0, 1.10)),
            int(150 * random.uniform(1.0, 1.10)),
            int(200 * random.uniform(1.0, 1.10))
        ]
        
        for round_idx in range(4):
            c_cost = costs[round_idx]
            config.console.print(f"\n[1] [Cost: {c_cost} Static] \"We've come this far. Raise the bid!\"", style=event_color, highlight=False)
            config.console.print("[2] \"We can't waste any more money on this. Pull out.\"", style=event_color, highlight=False)
            
            ch = ui_components.get_player_input("\nDecision > ")
            if ch == "1" and run_state["static"] >= c_cost:
                run_state["static"] -= c_cost
                if round_idx < 3:
                    config.console.print('\nNaganohara raises her paddle, our Static draining. Immediately, another fanatic student shouts over her!', style=event_color, highlight=False)
                else:
                    config.console.print('\n"DO IT!" I shout. Naganohara screams an astronomically high bid. "Going once... SOLD!"\nNaganohara practically floats out of the school, presenting us with the ultimate prize.', style=event_color, highlight=False)
                    config.console.print("[bold cyan]- Gained the manifold “Fairywings” (IV)[/bold cyan]", highlight=False)
                    run_state["owned_manifolds"].append("“Fairywings” (IV)")
            else:
                config.console.print('\n"We\'re tapping out. Fall back," I tell her. Defeated, she watches a wealthy student claim the wings.', style=event_color, highlight=False)
                break
                
        ui_components.get_player_input("Press Enter to continue...")
        return True

    # ==========================================
    # ID18 - The Ambitious Executive
    # ==========================================
    elif event_id == 18:
        ui_components.print_header("The Ambitious Executive")
        text = """We find ourselves in an abandoned warehouse district. Standing a few yards away is Adam, the Executive of the Riposte Gang.
This echo of Adam looks younger, ambitious and innocent. He rests a hand on his rapier, eyes narrowing.
"Who goes there? Identify yourselves. Are you with the allied factions, or are you trespassers?" """
        config.console.print(text, style=event_color, highlight=False)
        
        has_reqs = "Sandy Coat (II)" in run_state["owned_manifolds"] and "Punishing Rapier (III)" in run_state["owned_manifolds"]
        if has_reqs:
            config.console.print("\n[1] [Disguise Equipped] We play the part of his subordinates.", style=event_color, highlight=False)
        else:
            config.console.print("\n[1] [Missing Riposte Disguise Gear]", style="dim", highlight=False)
        config.console.print("[2] \"We have no way out of this.\" Draw weapons and strike first.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1" and has_reqs:
            config.console.print('\nAdam\'s tense posture relaxes. "Ah, reinforcements. Make sure you eat before deployment. There\'s a massive gang war three days from now. Be ready." He hands us food. Soon after, the gear loses its magic.', style=event_color, highlight=False)
            run_state["owned_manifolds"].remove("Sandy Coat (II)")
            run_state["owned_manifolds"].remove("Punishing Rapier (III)")
            run_state["owned_manifolds"].append("Towering Souffle Pancakes (II)")
            config.console.print("[bold cyan]- Gained the manifold Towering Souffle Pancakes (II)[/bold cyan]", highlight=False)
            run_state["event_flags"]["underworld_crucible_day"] = day + 3
            ui_components.get_player_input("Press Enter to continue...")
            return True
        elif choice == "2":
            config.console.print('\n"Trespassers!" Adam shouts, drawing his blade as several thugs materialize from the shadows.', style=event_color, highlight=False)
            ui_components.time.sleep(1.5)
            enemies = [
                stages.spawn_lattice_enemy("Adam", None, day, 25, 25, pre_status=[("Riposte", 50, 50)]),
                stages.spawn_lattice_enemy("Riposte Gang Henchman", "Riposte Gang Henchman A", day, 25, 25, pre_status=[("Riposte", 50, 50)]),
                stages.spawn_lattice_enemy("Riposte Gang Henchman", "Riposte Gang Henchman B", day, 25, 25, pre_status=[("Riposte", 50, 50)]),
                stages.spawn_lattice_enemy("Riposte Gang Squad Leader", "Riposte Gang Squad Leader A", day, 25, 25, pre_status=[("Riposte", 50, 50)]),
                stages.spawn_lattice_enemy("Riposte Gang Squad Leader", "Riposte Gang Squad Leader B", day, 25, 25, pre_status=[("Riposte", 50, 50)])
            ]
            config.player_data["current_enemies"] = [e for e in enemies if e]
            config.player_data["lattice_node_type"] = "elites"
            config.current_state = config.STATE_BATTLE
            
            run_state["static"] += int(80 * random.uniform(1.01, 1.50))
            run_state["owned_manifolds"].append("Towering Souffle Pancakes (II)")
            return "BATTLE"

    # ==========================================
    # ID19 - Underworld Crucible (Delayed Event)
    # ==========================================
    elif event_id == 19:
        ui_components.print_header("Underworld Crucible")
        text = """We step back into the warehouse district, still wearing our now-mundane Riposte disguises.
Gangs of all kinds—wielding chains, pipes, and blades—are locked in an incredibly tense standoff. We find young Adam standing near the front lines.
"I will be fine," he smiles. "I must prove my usefulness... Today is a stepping stone for a normal life." """
        config.console.print(text, style=event_color, highlight=False)
        config.console.print("\n[1] \"Here they come.\" Prepare to enter a decisive battle by his side.", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1":
            config.console.print('\nI raise my fists. "We\'ve got your back, Adam."', style=event_color, highlight=False)
            ui_components.time.sleep(1.5)
            enemies = [
                stages.spawn_lattice_enemy("Hisayuki Tadamasa", "Sprinttrack Gang Executive", day, 40, 40, extra_haste=3),
                stages.spawn_lattice_enemy("‘Forest Guardian’ Fairy Ayako", "Fallen Fairies Squad Leader – Deforester", day, 40, 40, extra_haste=3),
                stages.spawn_lattice_enemy("Slender Heiwa Seiritsu Delinquent", "Blood Spill Syndicate Thug", day, 40, 40, extra_haste=3),
                stages.spawn_lattice_enemy("‘Chain Reaper Of Heiwa’ Kurogane", "Blood Spill Syndicate Lieutenant", day, 40, 40, extra_haste=3),
                stages.spawn_lattice_enemy("Infiltrating Kasakura High School Disciplinary Committee Combatant", "Light Breathers Mob Member", day, 40, 40, extra_haste=3),
                stages.spawn_lattice_enemy("Raven", "Kind-Hearted Supportive Mercenary", day, 40, 40, extra_haste=3),
                stages.spawn_lattice_enemy("Kiryoku Gakuen Student Council Combatant", "Fallen Fairies Squad Messenger – Tornwings", day, 40, 40, extra_haste=3),
                stages.spawn_lattice_enemy("Kidnapper Hooligan Leader", "Heavy Basher Of Legends", day, 100, 80, extra_haste=3)
            ]
            config.player_data["current_enemies"] = [e for e in enemies if e]
            config.player_data["lattice_node_type"] = "elites"
            config.current_state = config.STATE_BATTLE
            
            run_state["static"] += int(150 * random.uniform(1.01, 1.50))
            run_state["owned_manifolds"].append("Sword Oil And Cloth (IV)")
            return "BATTLE"

    # ==========================================
    # ID20 - The Operative's Magnum Opus
    # ==========================================
    elif event_id == 20:
        ui_components.print_header("The Operative's Magnum Opus")
        text = """We find ourselves in a secluded alleyway in Sector III. Sitting on a supply crate is the timid, nerdy female operative whose weapon I shattered during our chase.
She is frantically tinkering with the dismantled, sparking components of her beloved custom energy blaster.
"Y-You're back!" she stammers. "Did you find it? Did you find the nozzle part after going out to look for it?!" """
        config.console.print(text, style=event_color, highlight=False)
        
        has_blaster = "Shattered Custom Blaster (I)" in run_state["owned_manifolds"]
        if has_blaster:
            config.console.print("\n[1] [Required Manifold Owned] \"We have it here.\"", style=event_color, highlight=False)
        else:
            config.console.print("\n[1] [Missing Shattered Custom Blaster (I)]", style="dim", highlight=False)
        config.console.print("[2] \"We don't have it.\"", style=event_color, highlight=False)
        
        choice = ui_components.get_player_input("\nDecision > ")
        if choice == "1" and has_blaster:
            run_state["owned_manifolds"].remove("Shattered Custom Blaster (I)")
            config.console.print('\n"Thank you! But... I\'ll have to go through arduous and highly dangerous testing before it becomes operational..."', style=event_color, highlight=False)
            
            win_chance = 0.0
            while True:
                config.console.print(f"\n[1] [Cost: 40 Static] \"Anything we can do to help?\" (Chance: {int(win_chance*100)}%)", style=event_color, highlight=False)
                config.console.print("[2] \"Good luck with that...\"", style=event_color, highlight=False)
                c2 = ui_components.get_player_input("\nDecision > ")
                
                if c2 == "1":
                    if run_state["static"] < 40:
                        config.console.print("[red]Not enough Static![/red]", highlight=False)
                        continue
                    run_state["static"] -= 40
                    
                    if random.random() < win_chance:
                        config.console.print('\nShe makes the final adjustment. The blaster hums with a terrifyingly powerful red glow. "We did it... Please, take it. I want you to use it."', style=event_color, highlight=False)
                        config.console.print("[bold cyan]- Gained the manifold Customized High Energy Blaster (III)[/bold cyan]", highlight=False)
                        run_state["owned_manifolds"].append("Customized High Energy Blaster (III)")
                        break
                    else:
                        win_chance += 0.10
                        if random.choice([True, False]):
                            config.console.print('\nThe weapon violently sparks, exploding into glowing dust! "Oops... hey, sell this alloy dust! Let\'s try again!"', style=event_color, highlight=False)
                            gain = int(20 * random.uniform(1.01, 1.50))
                            run_state["static"] += gain
                            config.console.print(f"[bold honeydew2]- Gained {gain} Static[/bold honeydew2]", highlight=False)
                        else:
                            config.console.print('\nShe pulls the trigger, and it violently explodes. A shockwave of plasma burns across the alleyway! "Agh! B-back to the drawing board!"', style=event_color, highlight=False)
                            apply_party_damage(random.uniform(0.10, 0.15))
                            config.console.print("[bold red]- Party takes Max HP damage.[/bold red]", highlight=False)
                else:
                    break
        else:
            config.console.print('\nThe girl\'s shoulders slump. "I see... so my masterpiece truly has no more hopes..." She sadly packs up her scrap metal.', style=event_color, highlight=False)
            
        ui_components.get_player_input("Press Enter to continue...")
        return True