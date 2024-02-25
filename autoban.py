import hexchat
import time

__module_name__ = "MultiServerAutoBanScript"
__module_version__ = "1.1"
__module_description__ = "Automatically bans users who join/part back to back 3 times in 90 seconds across multiple servers."

# Configuration
monitored_channels = ["#YOUR_CHANNEL_HERE_1", "#YOUR_CHANNEL_HERE_2"]  # Add more channels as needed
threshold_events = 3
time_frame = 90  # In seconds

# Global variable to track join/part events
event_tracker = {}

def update_tracker(nick, hostname, channel, server, event_type):
    current_time = time.time()
    key = (server, hostname, channel, event_type)
    
    if key not in event_tracker:
        event_tracker[key] = []
    
    event_tracker[key].append(current_time)
    
    event_tracker[key] = [t for t in event_tracker[key] if current_time - t <= time_frame]
    
    if len(event_tracker[key]) >= threshold_events:
        ban_user(hostname, channel, server)

def ban_user(hostname, channel, server):
    # Ensure the command is executed in the correct server/channel context
    hexchat.command(f"QUOTE -s {server} MODE {channel} +b *!*@{hostname}")
    print(f"Banned {hostname} on {channel} on server {server} for frequent joins/parts.")

def on_join(word, word_eol, userdata):
    channel = hexchat.get_info("channel")
    server = hexchat.get_info("host")
    if len(word) > 3 and channel in monitored_channels:
        nick = word[0]
        hostname = word[3]  # Extract the hostname
        update_tracker(nick, hostname, channel, server, "join")

def on_part(word, word_eol, userdata):
    channel = hexchat.get_info("channel")
    server = hexchat.get_info("host")
    if len(word) > 3 and channel in monitored_channels:
        nick = word[0]
        hostname = word[3]  # Extract the hostname
        update_tracker(nick, hostname, channel, server, "part")

def on_ping_timeout(word, word_eol, userdata):
    # Placeholder for ping timeout logic. Adjust as necessary.
    pass

hexchat.hook_print("Join", on_join)
hexchat.hook_print("Part", on_part)
hexchat.hook_print("Ping Timeout", on_ping_timeout)

print(f"{__module_name__} version {__module_version__} loaded.")
