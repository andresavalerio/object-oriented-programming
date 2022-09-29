# DIP - Dependency Inversion Principle
![](https://deviq.com/static/ad798f1c95da21c81b1be504460264c7/7f61c/Dependency-Inversion-400x400.webp)

_One image says more that thousand words. Thank you [DevIQ](https://deviq.com/principles/dependency-inversion-principle)  for the image_

**Dependency Inversion Principle** is of the five SOLID principles. **SOLID** was created by [Uncle Bob](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod) (author of Clean Code), but only became an acronym with [Michael Feathers.](https://michaelfeathers.silvrback.com/)

> Depend on abstractions, not on concretions.

**DIP** is the fifth SOLID principle that states:
1. High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces);
2. Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.

In a more traditional architecture, we often create high-level components that depend directly on low-level components. This design, however, increases complexity and creates a codependent system.

![](https://upload.wikimedia.org/wikipedia/commons/4/42/Traditional_Layers_Pattern.png)

_Traditional Layers Pattern. Special thanks for [Klodr and Wikipedia](https://en.wikipedia.org/wiki/File:Traditional_Layers_Pattern.png)_

On the other hand, we have the Dependency Inversion Principle, that relies on interfaces for high and low-level components to communicate. These interfaces are abstractions that can be used by the system as models for inheritance and implementation.

![](https://upload.wikimedia.org/wikipedia/commons/8/8d/DIPLayersPattern.png)

_Dependency Inversion Pattern. Special thanks for [Klodr and Wikipedia](https://en.wikipedia.org/wiki/File:Traditional_Layers_Pattern.png)_

## Coding Examples
Let's use the example of a bakery. If you want to define a function that cooks some food, you could do as follows:
```python
def cook():
    bread = Bread()
    bread.bake()

cook()
```
This approach, however, would lead to a _`cook` function that is completely dependent on `Bread` class._ If you want to bake a cookie or a pie, you'll need to create a new function or update this one. 

```python
def cook(food: str):
    if food == 'bread':
        bread = Bread()
        bread.bake()
    
    if food == 'cookie':
        cookie = Cookie()
        cookie.bake()

cook('cookie')
```
Updating at each interaction would definitely solve the problem, _but the problem of depending on other classes remains._ We could, then, **create an abstraction that works as an interface for both the `cook` function and the classes that it interacts with.** That would lead to the `Bakeable` class, an abstract class that only works for interface purposes, no implementation is needed.
```python
from abc import ABC, abstractmethod

class Bakeable(ABC):
    @abstractmethod
    def bake(self):
        pass
```

Now, for each class that can be baked, I can create a class that inherits `Bakeable` class.

```python
class Cookie(Bakeable):
    def bake(self):
        print("baking cookie")

def cook(bakeable: Bakeable):
    bakeable.bake()
```

See now that the `cook` function doesn't need to know with bakeble its being cooked to run. **`Bakeable` is an interface that connects the `cook `function with all possible food that may use it.**

> :brain: **Food for your thought:** Python has the [duck-typing principle](https://docs.python.org/3/glossary.html#term-duck-typing) (“If it looks like a duck and quacks like a duck, it must be a duck.”), which means that _you'll not necessarily need the ABC library to create a system that works._

## Resources
[abc library](https://docs.python.org/3/library/abc.html)

[Bakeable interface](https://stackoverflow.com/questions/61358683/dependency-inversion-in-python/68911711#68911711)

[Switch interface](https://medium.com/@zackbunch/python-dependency-inversion-8096c2d5e46c)

[Uncle Bob Principles of OOD](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod) 