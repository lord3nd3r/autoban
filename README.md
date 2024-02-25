AutoBanScript for HexChat

AutoBanScript is a Python plugin for HexChat that automatically bans users who join and part (or experience ping timeouts) back to back 3 times within a 90-second window. This script is designed to help maintain channel integrity by mitigating potential spam or flood attacks.
Features

    Monitors specific channels for join, part, and ping timeout events.
    Bans users by hostname if they join and part 3 times within 90 seconds.
    Configurable channel list and thresholds.

Requirements

    HexChat
    Python 3.x installed and configured with HexChat

Installation

    Ensure Python 3.x is installed on your system and the Python plugin is enabled in HexChat.
    Download autoban.py to your HexChat addons directory.
        Linux: ~/.config/hexchat/addons/
        Windows: %APPDATA%\HexChat\addons\
    Restart HexChat or load the script manually via Window > Plugins and Scripts > Load... and select autoban.py.

Configuration

Edit autoban.py to adjust the script to your needs:

    monitored_channels: List the channels you wish to monitor. For example, ["#channel1", "#channel2"].
    threshold_events: The number of join/part events that trigger a ban (default is 3).
    time_frame: The time window (in seconds) in which the join/part events are counted (default is 90 seconds).

Usage

Once installed and configured, the script runs automatically. It monitors the specified channels for join/part activity and bans users who meet the criteria set in the configuration.
Uninstallation

To uninstall the script, simply remove autoban.py from the HexChat addons directory and restart HexChat.


Contributing

Contributions to the script are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.
Support

Disclaimer

This script is provided "as is", without warranty of any kind. Use it at your own risk. The author is not responsible for any damages or issues that may arise from using this script.
