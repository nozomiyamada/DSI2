import numpy as np

def gini(values:list) -> float:
    """
    calculate Gini imputiry 1-Σp^2 

    Parameters:
        values (list): list of labels (str)

    Returns:
        Gini impurity score
    """
    probs = [values.count(x)/len(values) for x in set(values)]
    return 1 - sum(p**2 for p in probs)

def entropy(values:list) -> float:
    """
    calculate entropy -Σplog(p)

    Parameters:
        values (list): list of labels (str)

    Returns:
        entropy score
    """
    probs = [values.count(x)/len(values) for x in set(values)]
    return - sum(p * np.log(p) for p in probs)