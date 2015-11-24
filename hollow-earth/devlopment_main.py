import engine.Game as Game
import world.Player as Player
 
game = Game.Game()
dev = True
if dev:
	game.player = Player.Player()
	game.player.bypass_creation()
	game.newmap()
	game.run()
else:
	game.welcome()
	game.newplayer()
	game.player = Player.Player()
	game.player.create()
	game.intro()
	game.newmap()
	game.run()
