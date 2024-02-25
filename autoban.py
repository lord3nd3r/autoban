import hexchat

__module_name__ = "AutoBanScript"
__module_version__ = "1.0"
__module_description__ = "Automatically bans users who join/part back to back 3 times in 90 seconds."

# Configuration
monitored_channels = ["#freenode", "#linux"]  # Add more channels as needed
threshold_events = 3
time_frame = 90  # In seconds

# Global variable to track join/part events
event_tracker = {}

def get_hostname_from_word(word):
    try:
        full_identity = word[0]  # This might need adjustment based on the event
        nickname, _, hostname = full_identity.partition('@')
        return hostname
    except ValueError:
        # In case the structure is not as expected
        return None

def update_tracker(nick, hostname, channel, event_type):
    if not hostname:  # If hostname extraction failed, do not proceed
        return

    # (Existing logic to update the tracker and possibly ban users remains unchanged)

def on_join(word, word_eol, userdata):
    channel = hexchat.get_info("channel")
    hostname = get_hostname_from_word(word)
    if channel in monitored_channels and hostname:
        update_tracker(word[0], hostname, channel, "join")

def on_part(word, word_eol, userdata):
    channel = hexchat.get_info("channel")
    hostname = get_hostname_from_word(word)
    if channel in monitored_channels and hostname:
        update_tracker(word[0], hostname, channel, "part")

def on_ping_timeout(word, word_eol, userdata):
    # Adjust the logic for ping timeout event to correctly handle the hostname extraction
    # Note: The ping timeout might not provide direct channel or hostname info in some cases

