import hexchat
import time
import os
import json

__module_name__ = "MultiServerAutoBanScript"
__module_version__ = "1.0"
__module_description__ = "Automatically bans and unbans users based on specified criteria."

# Configuration
monitored_channels = ["#YOUR_CHANNEL_HERE_1", "#YOUR_CHANNEL_HERE_2"]
threshold_events = 3
time_frame = 90  # Seconds
ban_duration = 3600  # Seconds (1 hour for example)
ban_file_path = os.path.join(hexchat.get_info("configdir"), "addons", "autobans.json")

# Ensure the ban file exists
if not os.path.exists(ban_file_path):
    with open(ban_file_path, 'w') as f:
        json.dump([], f)

# Function to add a ban to the file
def add_ban_to_file(hostname, channel, server, timestamp):
    with open(ban_file_path, 'r+') as f:
        bans = json.load(f)
        bans.append({"hostname": hostname, "channel": channel, "server": server, "timestamp": timestamp})
        f.seek(0)
        json.dump(bans, f)
        f.truncate()

# Function to remove expired bans
def remove_expired_bans():
    with open(ban_file_path, 'r+') as f:
        current_time = time.time()
        bans = json.load(f)
        updated_bans = [ban for ban in bans if current_time - ban["timestamp"] < ban_duration]
        
        # Unban process
        for ban in bans:
            if current_time - ban["timestamp"] >= ban_duration:
                hexchat.command(f"QUOTE -s {ban['server']} MODE {ban['channel']} -b *!*@{ban['hostname']}")
                print(f"Unbanned {ban['hostname']} on {ban['channel']} on server {ban['server']}.")
        
        f.seek(0)
        json.dump(updated_bans, f)
        f.truncate()

# Modify existing functions to use add_ban_to_file and periodically call remove_expired_bans
# For example, in ban_user function, after banning a user, call add_ban_to_file
# Also, ensure to periodically call remove_expired_bans, possibly by using hexchat.hook_timer

# Example modification to ban_user function
def ban_user(hostname, channel, server):
    timestamp = time.time()
    hexchat.command(f"QUOTE -s {server} MODE {channel} +b *!*@{hostname}")
    print(f"Banned {hostname} on {channel} on server {server} for frequent joins/parts.")
    add_ban_to_file(hostname, channel, server, timestamp)

# Periodically check for expired bans to unban
hexchat.hook_timer(ban_duration * 1000, lambda userdata: remove_expired_bans() or True)

# Make sure to include the rest of the previously provided script logic here
