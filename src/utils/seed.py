import numpy as np
import random

def set_seed(seed: int = 42) -> None:
    """
    This method sets the seed for random number generators across the project.

    Args:
        seed (int, optional): 
            Seed value. Defaults to 42.
    """
    np.random.seed(seed)
    random.seed(seed)
    
    
    