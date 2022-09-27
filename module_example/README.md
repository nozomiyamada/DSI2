# example of self-made module #1

### put the `.py` in the same directiory
The easiest and most convenient way as long as you use only some self-made functions. 

- make functions in `funcs.py`
- put in the same directory of `module_test1.ipynb`
- in the `.py` file, you can import other liblaries such as `numpy`

~~~
module_example/
　├ funcs.py
　└ module_test1.ipynb
~~~

`funcs.py` has 2 functions

- `gini(values)`: function to calculate Gini impurity
- `entropy(values)`: function to calculate entropy

~~~python
import numpy as np

def gini(values:list) -> float:
    probs = [values.count(x)/len(values) for x in set(values)]
    return 1 - sum(p**2 for p in probs)

def entropy(values:list) -> float:
    probs = [values.count(x)/len(values) for x in set(values)]
    return - sum(p * np.log(p) for p in probs)
~~~

In `module_test1.ipynb`, just import `funcs`

~~~python
"""import self-made module"""
import funcs
~~~

When use the functions, call them with dot-notation

~~~python
"""call functions in funcs.py"""

labels = ['A','A','A','B','B','C']

print(funcs.gini(labels))
print(funcs.entropy(labels))

> 0.6111111111111112
> 1.0114042647073518
~~~

You can also use the libraries that are imported in your self `.py` with dot-notation.

~~~python
""""call numpy already imported in funcs.py"""
funcs.np.mean([1,2,3])

> 2.0


"""This does not work"""
np.mean([1,2,3])

> NameError: name 'np' is not defined
~~~

Or, you can import functions directory by `from ... import ...`

~~~python
from funcs import gini, entropy

print(gini(labels))
print(entropy(labels))

> 0.6111111111111112
> 1.0114042647073518
~~~



# example of self-made module #2
### create directory and `__init__.py`

If your module is complicated or contains sub-modules, you should make it a package by creating a new directory.

Now, let's create a package `utils`

~~~
module_example/
　├ utils/
　│　├ __init__.py
　│　├ stat.py
　│　└ scaler.py
　└ module_test2.ipynb
~~~

`stat.py` has 2 functions

- `mean(values)`: function to calculate mean of input values
- `std(values)`: function to calculate standard deviation of input values

~~~python
def mean(values:list) -> float:
    return sum(values)/len(values)

def std(values:list) -> float:
    m = mean(values)
    return (sum((x-m)**2 for x in values)/len(values))**0.5
~~~

`scaler.py` has `standard_scale()` function, which use the functions defined in `stat.py`

when import functions from other files, must specify the package (directory) name  and use dot-notation like `utils.XXX`

~~~python
""" * means import everything"""
from utils.stat import *

def standard_scaler(values:list) -> list:
    m = mean(values)
    s = std(values)
    return [(x-m)/s for x in values]
~~~

And in `__init__.py`, you can select which functions to assign to the package. In this case, only `standard_scaler` can be called.

~~~python
from utils.scaler import standard_scaler
~~~

`module_test2.ipynb` is in the same directory as `utils`, so you can call `standard_scaler` as below

~~~python
from utils import standard_scaler

values = [4,5,2,4,8,3,7,5,5,4,6,9,8,7,6]

standard_scaler(values)

> [-0.7954716334459858,...
~~~