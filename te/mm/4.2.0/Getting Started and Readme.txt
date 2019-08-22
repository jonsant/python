Mastermind v.4.2.0
by Ian Mallett
Released 2018-10-16

About:

	Mastermind is a library designed to take most of the guesswork out of network programming.  Essentially, it tries to handle as much as possible for you.  As such, it is very easy to get complete, fast, networked applications up and running.  Conversely, if you want to do deep-level networking, this is not your library.

	Mastermind is based on the client-server model because it is easiest to understand.  See "Notes.txt".

	For licensing, see "Notes.txt".

	The current version of Mastermind (unless I forgot to update it) is the version at the top of this file.  There have been at least one complete rewrites.

Files:

	"examples/*":
		Examples of usage of Mastermind
	"Documentation.txt":
		Complete documentation on Mastermind
	"Notes.txt":
		Notes on how Mastermind works, tips, possible pitfalls, implementation notes
	"Readme.txt":
		This file; getting started with Mastermind
	"TODO.txt":
		Lists possible improvements and all known bugs with Mastermind

Getting Started:

	My recommendation is to reverse engineer the examples in the "examples/" directory.

	The example "examples/basic-test.py" sets up an echo server and then creates a client to send messages to it.

	The example in "examples/chat/*" has clients which try to connect to a chat server.  If one is not available, it creates one and connects to that.  Running multiple instances allows for multiple chat windows linked to the first's server.  If the first is closed, the others close automatically.  This example serves as a more-advanced demonstration of a more-complete application.

Credits:

	--Ian Mallett (me):
		--Writing all versions of this library
		--Being responsible for all aspects of development
	--Matthew Roe:
		--Giving me inspiration for this project
		--A lot of my code (particularly his pickle/unpickle code idea),
		--A quit code tweak
		--Help with `select.select()`
	--Paul Davey:
		--Helping with subclassing
		--Helping with `select.select()`
		--Various other things
	--"PyMike"
		--Use of his testing facilities / server hosting
		--Advice and tweaks
		--Idea to make UDP capabilities.
	--Robin Wellner:
		--Tweak on the pickle/unpickle error checking
	--Andrew Barch:
		--Observation that pickle has security hole (which is why json is now the default).
	--Various others:
		--Encouragement / support / testing help