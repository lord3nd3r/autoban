AutoBanScript
This script needs to be loaded into HexChat's Python plugin interface. Before using this script, ensure you have the Python plugin enabled in HexChat and Python installed on your system.

This script does the following:

    Monitors specified channels for join, part, and ping timeout events.
    Tracks these events by hostname.
    If a user joins and parts (or has a ping timeout) 3 times within 90 seconds on any of the monitored channels, their hostname is banned from those channels.

Please replace YOUR_CHANNELS_HERE with the actual channels you want to monitor, separated by commas.

Important Notes:

    This script uses a global dictionary event_tracker to track the join/part events and ping timeouts by hostname and channel.
    It assumes that the hostname is available in the join, part, and ping timeout events. You may need to adjust how the hostname is obtained depending on the specific HexChat event payload.
    For ping timeout handling, the script currently lacks a direct way to know which channel the ping timeout event occurred in because HexChat's event for ping timeouts might not provide channel information. This script attempts to apply the ping timeout check across all monitored channels, which may not be perfectly accurate in all cases.
    Make sure to test this script in a controlled environment before using it in live channels to ensure it behaves as expected and doesn't accidentally ban innocent users.
    Replace YOUR_CHANNEL_HERE_1, YOUR_CHANNEL_HERE_2, etc., with the actual channel names you want to monitor.
    
