from AogokeClient import AogokeClient
import Utils, RequestHandling, CommandLine #Init modules
import AogokeClient as ac
import json
import sys
import os

try:
	DEBUG = os.environ["AODebug"] == "true"
except Exception:
	DEBUG = False

with open("AogokeConfig.json","r") as r:
	AogokeConfig = json.load(r)

# registerCommands()
client = AogokeClient()

if not DEBUG:
	ac.connect(client, AogokeConfig["Token"])
	sys.exit(0)