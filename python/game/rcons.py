import new, default, types, host
from game.gamemodes.exceptionoutput import *

#from www.bf2tech.org
def registerRConCommand(command, function):
    '''Register a custom RCon command by dynamically adding a function that
    implements the new command as a new method of the default.AdminServer class.
    Parameters: command = a string that gives the name of the new RCon command
    function = a function that implements the command.'''
    
    # Put the function into a new instancemethod object bound to the AdminServer
    newMethod = new.instancemethod(function, rconServer, RConServer)
    
    # Create a new class attribute in AdminServer that's wired to our function
    setattr(RConServer, command, newMethod)
     
    # Add the new command into the rcon dispatch table, pointing to our function
    rconServer.rcon_cmds[command] = newMethod
	
		
def init():
	pass

class RConServer(default.AdminServer):
	def onRemoteCommand(self, playerid_or_socket, cmd):
		cmd = cmd.strip()
		interactive = True

		# Is this a non-interactive client?
		if len(cmd) > 0 and cmd[0] == '\x02':
			cmd = cmd[1:]
			interactive = False

		spacepos = cmd.find(' ')
		if spacepos == -1: spacepos=len(cmd)
		subcmd = cmd[0:spacepos]

		ctx = default.CommandContext()
		authed = 1
		if type(playerid_or_socket) == types.IntType:
			ctx.player = playerid_or_socket
			#from sandbox
			if ctx.player == -1: #fix for local servers
				ctx.player = 255
			#########################
			#authed = self.authed_players.has_key(ctx.player)
		else:
			ctx.socket = playerid_or_socket
			#authed = self.authed_sockets.has_key(ctx.socket)
			
		# you can only login unless you are authenticated
		if subcmd != 'login' and not authed:
			ctx.write('error: not authenticated: you can only invoke \'login\'\n')
		else:
			if self.rcon_cmds.has_key(subcmd):
				self.rcon_cmds[subcmd](ctx, cmd[spacepos+1:])
			else:
				ctx.write('unknown command: \'%s\'\n' % (subcmd))

		feedback = ''.join(ctx.output)
		if ctx.socket:
			if interactive:
				ctx.socket.outbuf.enqueue(feedback)
			else:
				ctx.socket.outbuf.enqueue(feedback + '\x04')
		else:
			host.rcon_feedback(ctx.player, feedback)
			#host.rcon_feedback(ctx.player, cmd)
			
rconServer = RConServer(int(default.options['port']))
