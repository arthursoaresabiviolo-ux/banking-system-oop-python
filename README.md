#Banking System - Object-Oriented Programming in Python
##Overview

This project was developed with the purpose of improving my knowledge of **Object-Oriented Programming (OOP)** using Python.
During the development, several important OOP concepts and Python features were explored and implemented in practice.

The system simulates a simple banking environment, applying good programming practices and object-oriented design principles.

---

**##Concepts Practiced**
**###Object-Oriented Programming (OOP)**

The project was built following the main pillars of OOP:

**- Encapsulation**
  - Use of Python conventions such as `_attribute` to indicate protected attributes.
  - Controlled access to data through methods and properties.
**- Inheritance**
  - Creation of child classes inheriting attributes and behaviors from parent classes.
  - Code reuse and better organization of responsibilities.
**- Polymorphism**
  - Different classes implementing methods with distinct behaviors while sharing the same interface.
**- Abstraction**
  - Abstract classes and abstract methods were implemented to define common behaviors for subclasses.

---

**##Python Features and Libraries Used**
###`abc`**Module**

The project uses Python's built-in `abc` module to create abstract base classes.

```python
from abc import ABC, abstractmethod
```
This allowed the creation of generic structures that must be implemented by subclasses.

---

###`@abstractmethod`

Abstract methods were used to enforce method implementation in derived classes.

Example:

```python
@abstractmethod
def withdraw(self, amount):
    pass
```

---

###`super()`

The `super()` function was used to access constructors and methods from parent classes.

Example:

```python
super().__init__(balance, account_number, agency)
```
This improves code reuse and avoids duplication.

---

###Constructors (`__init__`)

Constructors were implemented to initialize object attributes when instances are created.

Example:

```python
def __init__(self, balance, number, agency):
    self._balance = balance
    self._number = number
    self._agency = agency
```

---

###Properties (`@property`)

Properties were used to safely expose internal attributes.

Example:

```python
@property
def balance(self):
    return self._balance
```

---

##Project Goals

The main goal of this project was to strengthen practical knowledge in:

- Python programming
- Object-oriented design
- Class relationships
- Code organization
- Software architecture fundamentals
- Reusability and maintainability

---

##Technologies Used
- Python 3
- `abc` module
