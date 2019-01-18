import time
import random

print()
print("-" * 65 )
print()


print("You are taking a stroll through the woods.")
time.sleep(1.5)
print()
print("You hear a russle in the brush to the right.")
time.sleep(1.5)
print()
print("Something jumps out at you.... ")
time.sleep(1.8)
print()
print("A wild Pokemon has appeared!!!!")
time.sleep(1)
print()
print("You engage in battle.")
time.sleep(1)
print()
print("You only have one pokemon, Haunter")
time.sleep(1)
print()
print("Haunter, I choose you!")
print()

poke_health = 100
wild_health = 100

while poke_health > 0 and wild_health > 0:
	print('Poke health: ' + str(poke_health))
	time.sleep(0.5)
	print('Wild Poke Health: ' + str(wild_health))
	time.sleep(0.5)
	print()



	print("Choose your attack.")
	time.sleep(1)
	print("-[1] Shadow Claw 💅🏿 ")
	time.sleep(0.5)
	print("-[2] Astonish 🤯")
	time.sleep(0.5)
	print("-[3] Dark Pulse 🌑")
	time.sleep(0.5)
	print("-[4] Lick 👅")
	time.sleep(0.5)
	print("-[5] Info 📜")
	time.sleep(0.5)
	print("-[6] Capture 🔒")
	attack = input("Pick a move using the corresponding number: > ")
	attack = int(attack)
	print()
	if attack == 1:
		damage = random.randint(5,10)
		wild_health = wild_health - damage
		print()
		time.sleep(0.8)
		print("Haunter uses Shadow Claw 💅🏿  and deals " + str(damage)+ " HP of damage." )
		print()
	elif attack == 2:
		damage = random.randint(15,20)
		wild_health = wild_health - damage
		print()
		time.sleep(0.8)
		print("Haunter uses Astonish 🤯 and deals " + str(damage) + " HP of damage.")
		print()
	elif attack == 3:
		damage = random.randint(15,25)
		wild_health = wild_health - damage
		print()
		time.sleep(0.8)
		print("Haunter uses Dark Pulse 🌑 and deals " + str(damage) + " HP of damage.")
		print()
	elif attack == 4:
		health = random.randint(15,35)
		poke_health = poke_health + health
		print()
		time.sleep(0.8)
		print("Haunter uses Lick 👅 and heals " + str(health) + " HP")
		print()
	elif attack == 5:
		time.sleep(0.8)
		print("Move information")
		print()
		time.sleep(1)
		print("  - Shadow Claw 💅🏿 : Has a damage range of 5 - 10HP")
		print()
		time.sleep(1)
		print("  - Astomish 🤯 : has a damage range of 15 - 20HP")
		print()
		time.sleep(1)
		print("  - Dark Pulse 🌑 : has a damage range of 15 - 25HP")
		print()
		time.sleep(1)
		print("  - Lick 👅 : has a healing factor of 15HP")
		print()
		time.sleep(1)
		print("  - Capture : Can Only occur when Wild Pokémon is low HP.")
		print()
		print()
		time.sleep(1)
		print(" Wild Pokémon information")
		print()
		time.sleep(1)
		print("  - Tackle: Deals a range of 5 - 10 HP of damge to your Pokémon.")
		print()
		time.sleep(1)
		print("  - Blood Drain: Gains a range of 5 - 10 HP of healing and deals a range 5 - 10HP of damage to your Pokémon.")
		print()
		time.sleep(1)
		print("  - Screech : Does a range of 9 - 15 HP damage to your Pokémon. ")
		print()
	elif attack == 6:
		capture_roll = random.randint(0,100)
		if capture_roll > wild_health:
			time.sleep(0.8)
			print("...capturing...")
			time.sleep(0.8)
			print("...capturing...")
			time.sleep(0.8)
			print("...capturing...")
			time.sleep(1)
			print("Wild Pokémon has been captured. Good Job Trainer!")
			break
		else:
			print("Capture has failed, it can only occur when Wild Pokémon is low HP or has fainted.")
	else:
		print("Please input a number again")


	if poke_health <= 0 or wild_health <= 0:
		break

	if attack != 5:
		time.sleep(1)
		#turns = 3
		wild_attack = random.randint(1,4)
		if wild_attack == 1:
			damage = random.randint(5,10)
			poke_health = poke_health - damage
			print()
			time.sleep(0.8)
			print("Wild Pokemon uses Tackle and deals "  + str(damage) + " HP of damage.")
			print()

		elif wild_attack == 2:
			damage = random.randint(5,15)
			health = random.randint(5,15)
			poke_health = poke_health - damage
			wild_health = wild_health + health
			print()
			time.sleep(0.8)
			print("Wild Pokémon uses Blood Drain healing "  + str(health) + " HP and dealing "  + str(damage) + " HP of damage.")
			print()
		elif wild_attack == 3:
			#damage = 5
			#poke_health = poke_health - damage
		else:
			damage = random.randint(9,15)
			poke_health = poke_health - damage
			print()
			time.sleep(0.8)
			print("Wild Pokémon uses Screech and deals "  + str(damage) + " HP of damage.")
			print()

#if wild_attack == 3:
	#poke_health = poke_health - damage
	#turns = turns - 1

#Check and avoid negative HP
if poke_health <= 0:
	print('Your Pokémon has fainted')
if wild_health <= 0:
	print('Wild Pokémon has fainted, you can now capture it!')











