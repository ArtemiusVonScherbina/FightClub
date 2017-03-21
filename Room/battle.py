import random;
class Character:
	BODY_PARTS = ["Head","Torso","Right arm","Left arm","Legs"]
	damage = 25
	health = 100
	health_shield = 100
	target = ""
	state = False

	def __init__ (self, name, race):
		self.name = name
		self.race = race
	
	def hit(self,target):	
		if target==0:
			self.health -= 30
		elif target==1:
			self.health -= 20
		elif 2<= target <=3:
			self.health -= 15
		elif target==4:
			self.health -= 15
	def attack(self,enemy):
		if self.target != enemy.block_part:
			enemy.hit(self.target)
	def body_block(self,block_part):
		self.block_part = block_part
	def choose_target(self,target):
		self.target = target
orc = Character ("Carl","orc")
name = input ("Whats your name?:")
race = input ("Input race:")
player = Character (name,race)
exit = False

while True:
	if (player.health <=0) or (orc.health<=0) or (exit):
		print("Game Over")
		break
	else:
		target = input("Choose the target to attack: ")
		block_part = input("Choose your part to block ")
		if target == "Exit" or block_part == "Exit":
			exit = True
		else:
			orc.choose_target(random.randint(0,4))
			orc.body_block(random.randint(0,4))
			player.choose_target(int(player.BODY_PARTS.index(target)))
			player.body_block(int(player.BODY_PARTS.index(block_part)))
			orc.attack(player)
			player.attack(orc)
		print("Player")
		print("Health: ",player.health)
		print("Target to attack: ",player.BODY_PARTS[player.target])
		print("Target to block: ",player.BODY_PARTS[player.block_part])
		print("Orc")
		print("Health: ",orc.health)
		print("Target to attack: ",orc.BODY_PARTS[orc.target])
		print("Target to block: ",orc.BODY_PARTS[orc.block_part])