import logging
import yaml

logger = logging.getLogger(__name__)

def load_config(config_path: str) -> dict:
    """
    This methods loads and returns the global configurations file.

    Args:
        config_path (str): 
            Path to configurations file

    Returns:
        dict: 
            Loaded configurations (as a dictionary)
    """
    with open(config_path, "r") as f:
        logger.info("Loading global configuration")
        configs = yaml.safe_load(f)
        logger.info("Successfully loaded configurations")
    return configs