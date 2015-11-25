import random
import engine.bcolors as bcolors

verb_list = ['go','examine','pick']
direct_actions = ['help','look','status']

fail_list_return = ["What the fuck are you trying to do ?", 
	"Did you even read the manual ?",
	"Do you thinks this is a motherfucking game ? ... Well ...",
	"ERROR : User too stupid, cannot understand command...",
	"Maybe you misstyped ? At least I hope...",
	"No way man ! This might even be illegal !",
	"Do you even care about my CPU ?"] 


def do_action(verb,obj,player):
	if verb == 'go':
		a=0
		#TODO: finish
		
	if verb == 'examine':
		flag=False
		for item in player.level.items:
			if item.name == obj.lower():
				message='You examine '+obj+' : '+item.examine
				return message
		if not(flag):
			message='Not such an item in this part of the map.'
			return message
		
	if verb == 'pick':
		flag=False
		for item in player.level.items:
			if item.name == obj.lower():
				flag=True
				index = player.level.items.index(item)
				player.inventory.append(player.level.items.pop(index))
				message='You pick '+obj+' and put it in your pockets'
				return message
		if not(flag):
			message='Not such an item in this part of the map.'
			return message

def do_direct_action(verb,player):
	message=None
	if verb == 'status':
		message=''
		message+=bcolors.bcolors.UNDERLINE+'\tPlayer status'+bcolors.bcolors.ENDC
		message+='\n'
		message+='\tName : '+player.name
		message+='\n'
		message+='\tHP : '+str(player.hp)+'/'+str(player.max_hp)
		array_inventory = []
		for item in player.inventory:
			array_inventory.append(item.name)
		message+='\n'
		message+='\tInventory : '+str(array_inventory)
		if not(player.armor==None):
			message+='\n'
			message+='\tArmor : '+player.armor.name+' (defense : '+str(player.armor_value)+')'
		else:
			message+='\n'
			message+='\tArmor : no armor equiped'
		if not(player.weapon==None):
			message+='\n'
			message+='\tWeapon : '+player.weapon.name+' (attack : '+str(player.weapon_value)+')'
		else:
			message+='\n'
			message+='\tWeapon : no weapon equiped'
		message+='\n'
	if verb == 'help':
		message=''
		message+='You asked for some help'
		message+='\n'
		message+=bcolors.bcolors.UNDERLINE+'\tList of commands'+bcolors.bcolors.ENDC
		message+='\n'
		message+=bcolors.bcolors.UNDERLINE+'\t\tMovements'+bcolors.bcolors.ENDC
		message+='\n'
		message+='\t\tType "go" + direction (n,s,e,w)'
		message+='\n'
		message+=bcolors.bcolors.UNDERLINE+'\t\tDirect actions'+bcolors.bcolors.ENDC
		message+='\n'
		message+='\t\tType (help,look,status)'
		message+='\n'
		message+=bcolors.bcolors.UNDERLINE+'\t\tActions with objects'+bcolors.bcolors.ENDC
		message+='\n'
		message+='\t\tType (examine,pick) + object'
		message+='\n'
	if verb == 'look':
		#CHECK FOR ITEMS
		message=''
		if len(player.level.items) == 0:
			message+='There is no items in this part of the map.'
			message+='\n'
		elif len(player.level.items) == 1:
			message+='You can see a '+player.level.items[0].name
			message+='\n'
		else:
  			message+='You can see '
			for item in player.level.items[:-2]: 
				message+='a '+item.name+', '
			message+='a '+player.level.items[-2].name+' and a '+player.level.items[-1].name+'.'
			message+='\n'
		#CHECK FOR WEAPONS
		if len(player.level.weapons) == 0:
			message+='There is no weapons in this part of the map.'
			message+='\n'
		elif len(player.level.weapons) == 1:
			message+='You can see a '+player.level.weapons[0].name
			message+='\n'
		else:
  			message+='You can see '
			for weapon in player.level.weapons[:-2]: 
				message+='a '+weapon.name+', '
			message+='a '+player.level.weapons[-2].name+' and a '+player.level.weapons[-1].name+'.'
			message+='\n'
		#CHECK FOR MONSTERS
		if len(player.level.monsters) == 0:
			message+='There is no monsters in this part of the map.'
			message+='\n'
		elif len(player.level.monsters) == 1:
			message+='You can see a '+player.level.monsters[0].name
			message+='\n'
		else:
  			message+='You can see '
			for monster in player.level.monsters[:-2]: 
				message+='a '+monster.name+', '
			message+='a '+player.level.monsters[-2].name+' and a '+player.level.monsters[-1].name+'.'
			message+='\n'
		#CHECK FOR AMOURS
		if len(player.level.armors) == 0:
			message+='There is no monsters in this part of the map.'
			message+='\n'
		elif len(player.level.armors) == 1:
			message+='You can see a '+player.level.armors[0].name
			message+='\n'
		else:
  			message+='You can see '
			for armor in player.level.armors[:-2]: 
				message+='a '+armor.name+', '
			message+='a '+player.level.armors[-2].name+' and a '+player.level.armors[-1].name+'.'
			message+='\n'
	return message
		
def decode_action(sentence,player):
	flag = False
	#parse first "argument"
	if sentence: #if user entered something
		splited_sentence = sentence.split()
		verb = splited_sentence[0].lower()
		if verb in verb_list:
			flag = True
			if len(splited_sentence)<2:
				message = verb.capitalize()+" what ?"
				return message
			else:
				obj = splited_sentence[1].lower()
				message = do_action(verb,obj,player)
				return message
		if verb in direct_actions:
			message = do_direct_action(verb,player)
			return message		
	if not(flag):
		#select insult
		insult = random.choice(fail_list_return)
		return insult


		
		
'''
from Dunnet 

(setq dun-verblist '((die . dun-die) (ne . dun-ne) (north . dun-n) 
		     (south . dun-s) (east . dun-e) (west . dun-w)
		     (u . dun-up) (d . dun-down) (i . dun-inven)
		     (inventory . dun-inven) (look . dun-examine) (n . dun-n)
		     (s . dun-s) (e . dun-e) (w . dun-w) (se . dun-se)
		     (nw . dun-nw) (sw . dun-sw) (up . dun-up) 
		     (down . dun-down) (in . dun-in) (out . dun-out)
		     (go . dun-go) (drop . dun-drop) (southeast . dun-se)
		     (southwest . dun-sw) (northeast . dun-ne)
		     (northwest . dun-nw) (save . dun-save-game)
		     (restore . dun-restore) (long . dun-long) (dig . dun-dig)
		     (shake . dun-shake) (wave . dun-shake)
		     (examine . dun-examine) (describe . dun-examine) 
		     (climb . dun-climb) (eat . dun-eat) (put . dun-put)
		     (type . dun-type)  (insert . dun-put)
		     (score . dun-score) (help . dun-help) (quit . dun-quit) 
		     (read . dun-examine) (verbose . dun-long) 
		     (urinate . dun-piss) (piss . dun-piss)
		     (flush . dun-flush) (sleep . dun-sleep) (lie . dun-sleep) 
		     (x . dun-examine) (break . dun-break) (drive . dun-drive)
		     (board . dun-in) (enter . dun-in) (turn . dun-turn)
		     (press . dun-press) (push . dun-press) (swim . dun-swim)
		     (on . dun-in) (off . dun-out) (chop . dun-break)
		     (switch . dun-press) (cut . dun-break) (exit . dun-out)
		     (leave . dun-out) (reset . dun-power) (flick . dun-press)
		     (superb . dun-superb) (answer . dun-answer)
		     (throw . dun-drop) (l . dun-examine) (take . dun-take)
		     (get . dun-take) (feed . dun-feed)))
'''
