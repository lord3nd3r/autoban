import hexchat
import time
import json
import os

__module_name__ = "AutoBanScriptWithFileHandling"
__module_version__ = "1.0"
__module_description__ = "Automatically bans users and removes bans after a specified duration, with debug output."

# Configuration
monitored_channels = ["#YOUR_CHANNEL_HERE_1", "#YOUR_CHANNEL_HERE_2"]  # Update with actual channels
threshold_events = 3
time_frame = 90  # Seconds
ban_duration = 3600  # Seconds (e.g., 1 hour)
ban_file_path = os.path.join(hexchat.get_info("configdir"), "addons", "autobans.json")

# Ensure the ban file exists
if not os.path.exists(ban_file_path):
    with open(ban_file_path, 'w') as f:
        json.dump([], f)

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
        add_ban_to_file(hostname, channel, server, current_time)

def add_ban_to_file(hostname, channel, server, timestamp):
    with open(ban_file_path, 'r+') as f:
        bans = json.load(f)
        bans.append({"hostname": hostname, "channel": channel, "server": server, "timestamp": timestamp})
        f.seek(0)
        json.dump(bans, f)
        f.truncate()

def remove_expired_bans():
    with open(ban_file_path, 'r+') as f:
        current_time = time.time()
        bans = json.load(f)
        active_bans = [ban for ban in bans if current_time - ban["timestamp"] < ban_duration]
        
        for ban in bans:
            if current_time - ban["timestamp"] >= ban_duration:
                unban_user(ban["hostname"], ban["channel"], ban["server"])
        
        f.seek(0)
        json.dump(active_bans, f)
        f.truncate()

def ban_user(hostname, channel, server):
    hexchat.command(f"MODE {channel} +b *!*@{hostname}")
    print(f"Banned {hostname} on {channel} on server {server}.")

def unban_user(hostname, channel, server):
    hexchat.command(f"MODE {channel} -b *!*@{hostname}")
    print(f"Unbanned {hostname} on {channel} on server {server}.")

def on_join(word, word_eol, userdata):
    channel = hexchat.get_info("channel")
    server = hexchat.get_info("host")
    if len(word) > 3 and channel in monitored_channels:
        nick = word[0]
        hostname = word[3]  # Adjust if needed
        print(f"Join detected: {nick}, {hostname}, {channel}, {server}")
        update_tracker(nick, hostname, channel, server, "join")

def on_part(word, word_eol, userdata):
    channel = hexchat.get_info("channel")
    server = hexchat.get_info("host")
    if len(word) > 3 and channel in monitored_channels:
        nick = word[0]
        hostname = word[3]  # Adjust if needed
        print(f"Part detected: {nick}, {hostname}, {channel}, {server}")
        update_tracker(nick, hostname, channel, server, "part")

# Periodically check for expired bans to unban
hexchat.hook_timer(ban_duration * 1000, lambda userdata: remove_expired_bans() or True)

print(f"{__module_name__} version {__module_version__} loaded.")
