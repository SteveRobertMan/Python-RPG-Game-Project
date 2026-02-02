import sys
from rich.console import Console

# Initialize Rich Console
console = Console()

# Game Constants
GAME_TITLE = "Kokoro No Kata"

# Game States
STATE_TITLE = "TITLE"
STATE_PROLOGUE = "PROLOGUE"
STATE_MAIN_MENU = "MAIN_MENU"
STATE_STAGE_SELECT = "STAGE_SELECT"
STATE_PARTY_MENU = "PARTY_MENU"
STATE_BATTLE = "BATTLE"
STATE_GACHA = "GACHA"
STATE_STORY_ARCHIVE = "STORY_ARCHIVE"
STATE_COUNCIL_LOGS = "COUNCIL_LOGS"
STATE_NODE_SELECT = "NODE_SELECT"
STATE_PARTY_MANAGEMENT = "STATE_PARTY_MANAGEMENT"

# Global Variables (Runtime)
current_state = STATE_TITLE
player_data = {}