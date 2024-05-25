# settings.py

import json

# Default settings for the Discord moderation bot
DEFAULT_SETTINGS = {
    "mute_duration": 600,  # Default mute duration in seconds
    "warning_threshold": 3,  # Default number of warnings before action is taken
    "auto_moderation": True,  # Default setting for auto-moderation feature
    "log_channel": "mod-logs"  # Default channel for bot logging
}

# Function to load settings from a JSON file
def load_settings():
    try:
        with open('settings.json', 'r') as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = DEFAULT_SETTINGS
        save_settings(settings)
    
    return settings

# Function to save settings to a JSON file
def save_settings(settings):
    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=4)

# Function to update a specific setting
def update_setting(setting_name, new_value):
    settings = load_settings()
    settings[setting_name] = new_value
    save_settings(settings)

# Function to reset settings to default values
def reset_settings():
    save_settings(DEFAULT_SETTINGS)

# Initialize settings on bot startup
SETTINGS = load_settings()