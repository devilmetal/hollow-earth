import engine.Game as Game
import world.Player as Player
 
game = Game.Game()
dev = False
if dev:
	game.player = Player.Player()
	game.player.bypass_creation()
	game.newmap()
	game.run()
else:
	game.welcome()
	game.newplayer()
	game.intro()
	game.newmap()
	game.run()
