import json
import os
from typing import Dict, Any


# Function to load settings
def load_config() -> Dict[str, Any]:
    """
    Loads the configuration settings from a JSON file.

    Reads the configuration file located at 'config/config.json' and returns the data as a dictionary.

    Returns:
        Dict[str, Any]: The configuration settings as a dictionary, where the keys are strings 
                        and the values can be of any type.
    """
    config_path = os.path.join("config", "config.json")
    with open(config_path, "r") as f:
        return json.load(f)
