AutoBanScript for HexChat

The MultiServerAutoBanScript is a Python plugin for HexChat designed to enhance channel management by automatically banning users who frequently join and part or experience ping timeouts within a short period across multiple servers. Additionally, this script stores bans in a file and automatically lifts these bans after a predetermined duration, promoting a balanced approach to moderation.
Features

    Monitors specified channels across multiple IRC servers for join, part, and ping timeout events.
    Automatically bans users by hostname who meet the criteria (e.g., joining and parting 3 times within 90 seconds).
    Stores ban details in a file for persistent tracking across HexChat sessions.
    Automatically removes bans after a specified duration to prevent permanent penalties for temporary disruptions.

Requirements

    HexChat IRC client
    Python 3.x plugin enabled within HexChat

Installation

    Ensure Python 3.x is installed on your system and properly configured as a plugin in HexChat.
    Download the MultiServerAutoBanScript.py file to your HexChat addons directory:
        Linux: ~/.config/hexchat/addons/
        Windows: %APPDATA%\HexChat\addons\
    Restart HexChat, or manually load the script through Window > Plugins and Scripts > Load... and navigate to the downloaded script.

Configuration

Before using the script, you may need to adjust several settings to match your specific needs:

    Monitored Channels: Edit the monitored_channels list within the script to include the channels you wish to monitor.
    Threshold Events and Time Frame: Set threshold_events and time_frame to control the sensitivity of the ban trigger.
    Ban Duration: Adjust ban_duration to specify how long bans should last before being automatically removed.

Usage

Once installed and configured, the script operates automatically in the background. It monitors for specified events in the configured channels and servers, applies bans as configured, and removes these bans after the set duration.
Ban Management

    Bans are stored in a JSON file located in the HexChat configuration directory under addons/autobans.json.
    To manually manage bans or adjust the ban list, edit this file directly. Ensure HexChat is closed or reload the script after making changes to avoid conflicts.

Uninstallation

Remove the MultiServerAutoBanScript.py file from the HexChat addons directory and restart HexChat to deactivate the script.
Contributing

Contributions to the script are welcome. Please feel free to fork the project, make improvements, and submit pull requests with your changes.


This script is provided "as is", without warranty of any kind. Use at your own risk. The authors are not responsible for any damages or disruptions caused by the use of this script.
