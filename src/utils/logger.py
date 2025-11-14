from logging.handlers import RotatingFileHandler
import logging
import os

def setup_logging(log_file: str, level = logging.INFO) -> None:
    """
    The function sets up the global logging configuration

    Args:
        log_file (str): 
            Path to save logs
        level (_type_, optional): 
            Minimum logging level. Defaults to logging.INFO.
    """
    log_parent_dir = os.path.join("artifacts", "logs")
    os.makedirs(log_parent_dir, exist_ok=True)
    log_dir = os.path.join(log_parent_dir, f"{log_file}")
    
    # remove previous handlers
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)
        
    # Setting up console handlers
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("[%(levelname)s] %(name)s %(message)s")
    )
    
    # Setting up file handler
    file_handler = RotatingFileHandler(log_dir, mode="a", maxBytes=5*1024*1024, backupCount=5)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s %(message)s"
        )
    )
        
    logging.basicConfig(
        handlers=[console_handler, file_handler],
        style="%",
        level = level,
        datefmt="%Y-%m-%d %H:%M"
    )