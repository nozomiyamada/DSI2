def mean(values:list) -> float:
    return sum(values)/len(values)

def std(values:list) -> float:
    m = mean(values)
    return (sum((x-m)**2 for x in values)/len(values))**0.5