## * means import everything
from utils.stat import *

def standard_scaler(values:list) -> list:
    """
    function for standardization

    Parameters:
        values (list): list of values

    Returns:
        standardized values (z-score)
    """
    m = mean(values)
    s = std(values)
    return [(x-m)/s for x in values]