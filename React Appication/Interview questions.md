# Python & FastAPI Interview Questions — Complete Answer Guide

A complete, easy-to-follow reference covering Core Python, FastAPI, and scenario-based system design questions, with clear explanations and code examples.

---

## Table of Contents

**Part 1: Python**
1. [Basic Python](#basic-python)
2. [Data Types](#data-types)
3. [String Questions](#string-questions)
4. [Functions](#functions)
5. [OOP](#oop)
6. [Exception Handling](#exception-handling)
7. [File Handling](#file-handling)
8. [Modules and Packages](#modules-and-packages)
9. [Memory & Internals](#memory--internals)
10. [Multithreading & Multiprocessing](#multithreading--multiprocessing)
11. [Async Programming](#async-programming)
12. [Iterators & Generators](#iterators--generators)
13. [Advanced Python](#advanced-python)
14. [Coding Questions](#coding-questions)

**Part 2: FastAPI**
15. [Basics](#fastapi-basics)
16. [Routing](#routing)
17. [Dependency Injection](#dependency-injection)
18. [Pydantic](#pydantic)
19. [SQLAlchemy](#sqlalchemy)
20. [Relationships](#relationships)
21. [Authentication](#authentication)
22. [File Upload](#file-upload)
23. [Middleware](#middleware)
24. [Exception Handling (FastAPI)](#exception-handling-fastapi)
25. [Deployment](#deployment)
26. [Practical Questions](#practical-questions)

**Part 3**
27. [Scenario-Based Questions](#scenario-based-questions)

---

## Basic Python

**1. What are the features of Python?**
Python is interpreted, dynamically typed, and has automatic memory management. It supports multiple paradigms (procedural, object-oriented, functional), has a huge standard library ("batteries included"), is portable across platforms, uses simple/readable syntax, and integrates well with other languages (C/C++ via extensions).

**2. Why is Python called an interpreted language?**
Python code is executed line-by-line by an interpreter (CPython) rather than being fully compiled to native machine code ahead of time. Internally, source code is first compiled to bytecode (`.pyc`), which the Python Virtual Machine then interprets — so it's technically a hybrid, but from a user's perspective it behaves as interpreted since there's no separate manual compile step.

**3. What is the difference between Python 2 and Python 3?**
| Python 2 | Python 3 |
|---|---|
| `print` is a statement | `print()` is a function |
| Integer division truncates (`5/2 = 2`) | True division (`5/2 = 2.5`) |
| Strings are ASCII by default | Strings are Unicode by default |
| `xrange()` for ranges | Only `range()` (memory efficient) |
| End of life (no longer supported) | Actively maintained |

**4. What are Python keywords?**
Reserved words that have special meaning to the interpreter and cannot be used as identifiers (variable/function names), e.g. `if`, `else`, `for`, `while`, `class`, `def`, `return`, `import`, `True`, `False`, `None`, `lambda`, `try`, `except`. You can list them with `import keyword; keyword.kwlist`.

**5. What are identifiers?**
Names used to identify variables, functions, classes, modules, etc. Rules: must start with a letter or underscore, can contain letters/digits/underscores, are case-sensitive, and cannot be a reserved keyword. Example: `my_var`, `_temp`, `total2`.

**6. Explain Python's memory management.**
Python manages memory automatically via a private heap. Objects are allocated on this heap, and memory is managed through **reference counting** plus a **cyclic garbage collector** that detects and cleans up reference cycles (objects referencing each other) that reference counting alone can't free. Python also uses memory pools (via `pymalloc`) for small objects to reduce fragmentation.

**7. What is PEP 8?**
PEP 8 is Python's official style guide describing coding conventions — naming conventions (snake_case for variables/functions, PascalCase for classes), indentation (4 spaces), line length (79 characters), whitespace rules, and import ordering — to keep code consistent and readable across projects.

**8. What is the difference between == and is?**
- `==` checks **value equality** (do the objects contain the same data?).
- `is` checks **identity equality** (do both references point to the same object in memory?).
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b   # True (same values)
a is b   # False (different objects)
```

**9. What is the difference between id() and type()?**
`id()` returns the unique memory identity (address) of an object. `type()` returns the class/type of an object. Both are useful for debugging — `id()` to check if two variables reference the same object, `type()` to check what kind of object you're working with.

**10. What are mutable and immutable objects?**
- **Mutable**: can be changed after creation — `list`, `dict`, `set`.
- **Immutable**: cannot be changed after creation; any "modification" creates a new object — `int`, `float`, `str`, `tuple`, `frozenset`.
```python
s = "hello"
s[0] = "H"   # TypeError, strings are immutable
```

---

## Data Types

**11. What are Python's built-in data types?**
Numeric (`int`, `float`, `complex`), Sequence (`str`, `list`, `tuple`, `range`), Mapping (`dict`), Set types (`set`, `frozenset`), Boolean (`bool`), Binary (`bytes`, `bytearray`, `memoryview`), and `NoneType`.

**12. Difference between List and Tuple.**
| List | Tuple |
|---|---|
| Mutable | Immutable |
| Slower (extra overhead for mutability) | Faster |
| `[1, 2, 3]` | `(1, 2, 3)` |
| More memory | Less memory |
| Not hashable (can't be a dict key) | Hashable (can be a dict key if elements are hashable) |

**13. Difference between Set and Dictionary.**
A **set** is an unordered collection of unique, hashable elements (`{1, 2, 3}`) used for membership testing and eliminating duplicates. A **dictionary** stores key-value pairs (`{"a": 1, "b": 2}`) used for fast lookups by key. Both use hash tables internally, giving average O(1) lookup.

**14. Can dictionary keys be mutable?**
No. Dictionary keys must be hashable, and mutable objects like lists and dicts are unhashable, so they can't be used as keys. Tuples *can* be keys — but only if all their elements are themselves hashable/immutable.

**15. Why are tuples immutable?**
By design, to make them hashable (usable as dict keys/set elements), safer for sharing across code (no accidental modification), and faster/more memory-efficient than lists since Python can make certain internal optimizations knowing the size and contents won't change.

**16. Explain shallow copy and deep copy.**
- **Shallow copy**: creates a new outer object but copies references to nested objects — inner mutable objects are still shared.
- **Deep copy**: recursively copies everything, including nested objects, so the copy is fully independent.
```python
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)       # shallow
c = copy.deepcopy(a)   # deep
b[0][0] = 99
print(a[0][0])  # 99 -> shallow copy shares inner list
print(c[0][0])  # 1  -> deep copy is independent
```

**17. Difference between copy() and deepcopy().**
`copy.copy(obj)` performs a shallow copy (one level deep). `copy.deepcopy(obj)` recursively copies all nested objects, so changes to nested structures in the copy don't affect the original. `deepcopy` is slower and uses more memory but is fully safe for nested mutable data.

**18. What is slicing?**
Extracting a sub-portion of a sequence (list, string, tuple) using `sequence[start:stop:step]`. `start` is inclusive, `stop` is exclusive, `step` is the increment.
```python
nums = [0,1,2,3,4,5]
nums[1:4]     # [1, 2, 3]
nums[::2]     # [0, 2, 4]
nums[::-1]    # [5, 4, 3, 2, 1, 0] (reversed)
```

**19. What is negative indexing?**
Indexing from the end of a sequence, where `-1` refers to the last element, `-2` the second-last, and so on. Useful for accessing elements without knowing the sequence length.
```python
s = "python"
s[-1]   # 'n'
s[-2]   # 'o'
```

**20. How do you remove duplicates from a list?**
```python
# Order not preserved
unique = list(set(my_list))

# Order preserved (Python 3.7+)
unique = list(dict.fromkeys(my_list))
```

---

## String Questions

**21. Strings are immutable. What does that mean?**
Once a string object is created, its content cannot be changed in place. Any operation that appears to "modify" a string (concatenation, replace, upper, etc.) actually creates and returns a brand-new string object, leaving the original untouched.

**22. Reverse a string without using [::-1].**
```python
def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

# Or using reversed() + join
def reverse_string2(s):
    return "".join(reversed(s))
```

**23. Count vowels in a string.**
```python
def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)

print(count_vowels("Hello World"))  # 3
```

**24. Find duplicate characters.**
```python
def find_duplicates(s):
    seen = {}
    for ch in s:
        seen[ch] = seen.get(ch, 0) + 1
    return {ch: count for ch, count in seen.items() if count > 1}

print(find_duplicates("programming"))
# {'r': 2, 'g': 2, 'm': 2}
```

**25. Check whether a string is a palindrome.**
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Madam"))  # True
```


---

## Functions

**26. What is the difference between parameters and arguments?**
A **parameter** is the variable listed in a function's definition. An **argument** is the actual value passed to the function when it is called.
```python
def greet(name):    # 'name' is a parameter
    print(f"Hi {name}")

greet("Alice")       # "Alice" is an argument
```

**27. Explain positional and keyword arguments.**
**Positional arguments** are matched to parameters based on their order. **Keyword arguments** are matched by explicitly naming the parameter, regardless of order.
```python
def info(name, age):
    print(name, age)

info("Bob", 25)          # positional
info(age=25, name="Bob") # keyword
```

**28. What are *args and **kwargs?**
`*args` collects any number of extra **positional** arguments into a tuple. `**kwargs` collects any number of extra **keyword** arguments into a dictionary.
```python
def demo(*args, **kwargs):
    print(args)    # (1, 2, 3)
    print(kwargs)  # {'x': 10, 'y': 20}

demo(1, 2, 3, x=10, y=20)
```

**29. What is a lambda function?**
A small, anonymous, single-expression function defined with the `lambda` keyword instead of `def`. Used for short, throwaway functions, often passed to `map()`, `filter()`, or `sorted()`.
```python
square = lambda x: x * x
print(square(5))  # 25
```

**30. Difference between lambda and a normal function.**
| Lambda | Normal function (`def`) |
|---|---|
| Anonymous (usually) | Has a name |
| Single expression only | Can have multiple statements |
| No `return` keyword needed (implicit) | Needs explicit `return` |
| Less readable for complex logic | Better for complex/reusable logic |

**31. What are recursive functions?**
Functions that call themselves to solve a problem by breaking it into smaller sub-problems, with a base case to stop the recursion.
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

**32. What are generators?**
Functions that use `yield` instead of `return` to produce a sequence of values lazily, one at a time, pausing state between values. Memory-efficient since the entire sequence isn't built in memory at once.
```python
def counter(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in counter(5):
    print(num)
```

**33. Difference between yield and return.**
`return` exits a function immediately and sends back a single value, ending execution. `yield` pauses the function, returns a value to the caller, and preserves state so execution can resume on the next call — turning the function into a generator.

**34. What are decorators?**
Functions that wrap another function to add extra behavior (logging, timing, access control) without modifying the original function's code, applied using `@decorator_name` syntax.
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**35. How do decorators work internally?**
A decorator is a higher-order function: `@decorator` above `def func():` is syntactic sugar for `func = decorator(func)`. The decorator takes the original function as an argument, defines an inner "wrapper" that adds logic around a call to it, and returns that wrapper.

---

## OOP

**36. What are the four pillars of OOP?**
**Encapsulation** (bundling data and methods, restricting direct access), **Abstraction** (hiding complex implementation, exposing only essentials), **Inheritance** (a class acquiring properties/behavior from a parent), and **Polymorphism** (the same interface behaving differently for different objects).

**37. Difference between abstraction and encapsulation.**
**Abstraction** hides *implementation complexity*, showing only what's necessary (via abstract classes/interfaces). **Encapsulation** hides *data* by bundling it with methods and restricting access (via private/protected attributes, getters/setters). Abstraction is a design concern; encapsulation is an implementation/data-protection concern.

**38. Difference between inheritance and composition.**
**Inheritance** ("is-a") — a class derives from a parent and inherits its attributes/methods. **Composition** ("has-a") — a class contains an instance of another class as an attribute, delegating behavior instead of inheriting it. Composition is often preferred since it's more flexible and avoids fragile inheritance chains.

**39. What is polymorphism?**
The ability of different classes/objects to respond to the same method call in their own way. Achieved naturally in Python via duck typing.
```python
class Dog:
    def sound(self): return "Bark"
class Cat:
    def sound(self): return "Meow"

for animal in [Dog(), Cat()]:
    print(animal.sound())
```

**40. Explain method overriding.**
When a subclass provides its own implementation of a method already defined in its parent class, replacing the parent's version when called on a subclass instance.
```python
class Animal:
    def speak(self): return "..."
class Dog(Animal):
    def speak(self): return "Woof"  # overrides parent
```

**41. Explain method overloading in Python.**
Python doesn't support true method overloading (same name, different signatures) like Java/C++. It's simulated using default arguments, `*args`/`**kwargs`, or `functools.singledispatch`.

**42. What is super()?**
A built-in function used inside a subclass to call methods from its parent class — commonly used in `__init__` to initialize inherited attributes.
```python
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

**43. Difference between class variables and instance variables.**
**Class variables** are shared across all instances (defined in the class body). **Instance variables** are unique per object (defined in `__init__` via `self.`).
```python
class Car:
    wheels = 4              # class variable (shared)
    def __init__(self, color):
        self.color = color  # instance variable (unique)
```

**44. Difference between @classmethod, @staticmethod, and instance methods.**
| Type | First argument | Access |
|---|---|---|
| Instance method | `self` | Instance and class data |
| `@classmethod` | `cls` | Class state, not tied to an instance |
| `@staticmethod` | none required | No implicit access — a plain function grouped in the class |

**45. What is the MRO (Method Resolution Order)?**
The order Python searches through a class hierarchy to resolve which method/attribute to use, relevant in multiple inheritance. Python uses the **C3 linearization algorithm**. Inspect via `ClassName.__mro__` or `ClassName.mro()`.

---

## Exception Handling

**46. What is exception handling?**
A mechanism to gracefully detect and respond to runtime errors using `try`/`except` blocks, preventing crashes and allowing controlled recovery or cleanup.

**47. Difference between syntax errors and runtime errors.**
A **syntax error** violates Python's grammar and is caught before the program runs (e.g., a missing colon). A **runtime error (exception)** occurs during execution of otherwise valid code (e.g., dividing by zero).

**48. Explain try, except, else, and finally.**
```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")   # runs only on exception
else:
    print("No error occurred")       # runs only if no exception
finally:
    print("Always runs")             # runs no matter what
```

**49. How do you create a custom exception?**
```python
class InsufficientBalanceError(Exception):
    def __init__(self, message="Balance too low"):
        super().__init__(message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError()
```

**50. What is exception propagation?**
When an exception isn't caught where it occurs, it "bubbles up" to the calling function, continuing up the call stack until caught by an `except` block or reaching the top level and crashing the program with a traceback.

---

## File Handling

**51. Modes of opening a file.**
| Mode | Meaning |
|---|---|
| `'r'` | Read (default) |
| `'w'` | Write (overwrites/creates) |
| `'a'` | Append |
| `'x'` | Create, fail if exists |
| `'b'` | Binary mode (e.g. `'rb'`) |
| `'t'` | Text mode (default) |
| `'+'` | Read and write (e.g. `'r+'`) |

**52. Difference between read(), readline(), and readlines().**
`read()` reads the entire file as one string. `readline()` reads a single line at a time. `readlines()` reads all lines into a list of strings.

**53. Difference between write() and writelines().**
`write()` writes a single string. `writelines()` writes a list of strings — but doesn't add newlines automatically, so `\n` must be included manually.

**54. What is the purpose of the with statement?**
Creates a **context manager** that handles setup/cleanup automatically — ensuring a file is closed even if an exception occurs.
```python
with open("data.txt", "r") as f:
    content = f.read()
# file auto-closed here
```

**55. How do you handle large files efficiently?**
Avoid loading the whole file into memory — stream it line by line or in chunks.
```python
with open("large_file.txt") as f:
    for line in f:
        process(line)

with open("large_file.bin", "rb") as f:
    while chunk := f.read(8192):
        process(chunk)
```

---

## Modules and Packages

**56. Difference between a module and a package.**
A **module** is a single `.py` file. A **package** is a directory of related modules, traditionally marked by `__init__.py`.

**57. What is __init__.py?**
A special file marking a directory as a package. Runs automatically on import; commonly used to expose submodules/functions at the package level.

**58. Explain __name__ == "__main__".**
Every module has a built-in `__name__`. When run directly it's `"__main__"`; when imported, it's the module's name. This lets code distinguish "run directly" from "imported":
```python
def main():
    print("Running directly")

if __name__ == "__main__":
    main()
```

**59. Difference between import module and from module import *.**
`import module` keeps the namespace clean (`module.name`). `from module import *` dumps all public names into the current namespace — discouraged due to naming conflicts and unclear origin.

**60. What is sys.path?**
A list of directories Python searches to locate modules on `import`, including the script's directory, site-packages, and `PYTHONPATH` entries. Inspect via `import sys; sys.path`.


---

## Memory & Internals

**61. How does Python manage memory?**
Through a private heap managed by the interpreter, using **reference counting** to track how many references point to an object, freeing it when the count hits zero, plus a **cyclic garbage collector** to catch reference cycles.

**62. What is reference counting?**
Every object keeps a count of how many references point to it. When a new reference is made, the count increases; when a reference is deleted or goes out of scope, it decreases. When it reaches zero, the object's memory is deallocated immediately.

**63. What is the Garbage Collector?**
A background mechanism (`gc` module) that detects and cleans up **reference cycles** (e.g., two objects referencing each other) that reference counting alone cannot free, preventing memory leaks.

**64. What is the Global Interpreter Lock (GIL)?**
A mutex in CPython that allows only one thread to execute Python bytecode at a time, even on multi-core systems. It simplifies memory management (protects reference counts from race conditions) but limits true parallelism for CPU-bound multithreaded code.

**65. Why is Python slower than Java or C++?**
Python is dynamically typed (type checks happen at runtime), interpreted rather than compiled to native machine code, and has higher-level abstractions/overhead per operation. Java/C++ are statically typed and compiled ahead of time (or JIT-compiled), enabling more aggressive optimization.

**66. What is a .pyc file?**
A compiled bytecode file generated by Python when a module is imported, cached (typically in a `__pycache__` folder) so subsequent imports skip re-compiling the source, speeding up load time.

**67. When is bytecode generated?**
When a `.py` file is imported (not necessarily when run as the main script directly, though CPython compiles it in memory either way). The compiled bytecode is cached to a `.pyc` file for future imports if the source hasn't changed.

**68. What is the difference between the compiler and interpreter in Python?**
Python's **compiler** translates source code into bytecode (an intermediate, platform-independent representation). The **interpreter** (Python Virtual Machine) then executes that bytecode instruction by instruction. So Python is technically compiled to bytecode first, then interpreted.

---

## Multithreading & Multiprocessing

**69. What is multithreading?**
Running multiple threads (lightweight units of a process) concurrently within the same process, sharing memory space. In Python, useful for I/O-bound tasks (network calls, file I/O) but limited for CPU-bound tasks due to the GIL.

**70. Difference between multiprocessing and multithreading.**
| Multithreading | Multiprocessing |
|---|---|
| Multiple threads in one process | Multiple separate processes |
| Shared memory | Separate memory space per process |
| Limited by GIL for CPU-bound work | True parallelism (bypasses GIL) |
| Lower overhead | Higher overhead (process creation, IPC) |
| Good for I/O-bound tasks | Good for CPU-bound tasks |

**71. What is a daemon thread?**
A background thread that runs alongside the main program and is automatically terminated when the main program exits, regardless of whether it has finished. Set via `thread.daemon = True`.

**72. What is a race condition?**
A bug that occurs when multiple threads/processes access and modify shared data concurrently, and the final outcome depends on the unpredictable timing/order of execution, potentially producing incorrect results.

**73. What is a deadlock?**
A situation where two or more threads/processes are each waiting for a resource held by the other, so none of them can proceed — the program hangs indefinitely.

**74. What is a Lock?**
A synchronization primitive (`threading.Lock`) used to ensure only one thread can access a critical section of code / shared resource at a time, preventing race conditions.
```python
import threading
lock = threading.Lock()
with lock:
    # critical section
    shared_counter += 1
```

**75. Explain the GIL with an example.**
Even with multiple threads, only one executes Python bytecode at any instant.
```python
import threading

def cpu_task():
    total = 0
    for i in range(10**7):
        total += i

t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)
t1.start(); t2.start()
t1.join(); t2.join()
# This does NOT run ~2x faster on multi-core CPUs because of the GIL —
# for CPU-bound work like this, multiprocessing would actually be faster.
```

---

## Async Programming

**76. What is asynchronous programming?**
A concurrency model where tasks can start, pause (while waiting on I/O), and resume without blocking the whole program, allowing a single thread to handle many operations concurrently — ideal for I/O-bound workloads like network requests.

**77. Difference between synchronous and asynchronous programming.**
**Synchronous** code executes one operation at a time, blocking until each completes before moving to the next. **Asynchronous** code can start an operation, move on to other work while it's pending (e.g., waiting on a network response), and resume once it's ready — improving throughput for I/O-heavy tasks.

**78. What is an event loop?**
The core of Python's `asyncio` — a loop that continuously monitors and schedules asynchronous tasks/coroutines, running whichever is ready to proceed while others are waiting on I/O, giving the illusion of concurrency on a single thread.

**79. What are async and await?**
`async def` defines a coroutine function. `await` pauses execution of that coroutine until the awaited operation (another coroutine or async I/O call) completes, yielding control back to the event loop in the meantime so other tasks can run.
```python
import asyncio

async def fetch_data():
    await asyncio.sleep(2)  # simulates I/O wait
    return "data"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

**80. Difference between asyncio.gather() and sequential execution.**
Sequential `await` calls run one after another, each waiting for the previous to finish — total time is the sum of all. `asyncio.gather()` runs multiple coroutines concurrently, waiting for the I/O of all of them in parallel — total time is close to the *slowest* one, not the sum.
```python
# Sequential: ~6 seconds total
await task1()  # 2s
await task2()  # 2s
await task3()  # 2s

# Concurrent: ~2 seconds total
await asyncio.gather(task1(), task2(), task3())
```

---

## Iterators & Generators

**81. What is an iterator?**
An object that implements `__iter__()` and `__next__()`, allowing sequential access to elements one at a time via `next()`, raising `StopIteration` when exhausted.

**82. Difference between iterable and iterator.**
An **iterable** is any object that can return an iterator (implements `__iter__()`) — like a list or string. An **iterator** is the object actually doing the iterating (implements both `__iter__()` and `__next__()`) and keeps track of state/position. Every iterator is an iterable, but not every iterable is an iterator.

**83. How does next() work?**
`next(iterator)` calls the iterator's `__next__()` method, returning the next item in the sequence and advancing its internal state. When there are no more items, it raises `StopIteration` (which `for` loops catch automatically to end the loop).

**84. Why are generators memory efficient?**
Generators produce values one at a time, on demand ("lazily"), rather than computing and storing an entire sequence in memory upfront. This is especially valuable for large or infinite sequences.

**85. What is lazy evaluation?**
Deferring computation of a value until it's actually needed, rather than computing it eagerly ahead of time. Generators, `map()`, `filter()`, and `range()` in Python 3 all use lazy evaluation to save memory and avoid unnecessary work.

---

## Advanced Python

**86. What is monkey patching?**
Dynamically modifying or extending a class or module at runtime — e.g., replacing a method on an existing class — without changing its original source code. Useful for testing/mocking but risky in production due to unpredictable side effects.
```python
class Dog:
    def bark(self): return "Woof"

def new_bark(self): return "Bark!"
Dog.bark = new_bark  # monkey patch
```

**87. What are context managers?**
Objects that define `__enter__()` and `__exit__()` methods to manage setup and teardown of resources, used with the `with` statement (e.g., automatically closing files or releasing locks).
```python
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")

with MyContext():
    print("Inside block")
```

**88. What is metaclass?**
A "class of a class" — it defines how classes themselves are constructed. By default, classes are instances of `type`. Custom metaclasses (subclassing `type`) let you control class creation behavior, e.g., automatically registering subclasses or enforcing constraints.

**89. What is introspection?**
The ability of a program to examine the type, attributes, or structure of objects at runtime, e.g., `type()`, `dir()`, `isinstance()`, `hasattr()`, `getattr()`, `inspect` module.

**90. Explain duck typing.**
"If it walks like a duck and quacks like a duck, it's a duck" — Python cares about whether an object *has* the required method/attribute, not its actual class/type. This enables flexible polymorphism without explicit interfaces.

**91. What is dependency injection?**
A design pattern where an object's dependencies (services, configs, other objects it needs) are provided ("injected") from outside rather than being created internally — improving testability and decoupling. FastAPI's `Depends()` is a direct implementation of this pattern.

**92. Explain SOLID principles in Python.**
- **S**ingle Responsibility — a class should have one reason to change.
- **O**pen/Closed — open for extension, closed for modification.
- **L**iskov Substitution — subclasses should be substitutable for their base class without breaking behavior.
- **I**nterface Segregation — prefer many specific interfaces over one general-purpose one.
- **D**ependency Inversion — depend on abstractions, not concrete implementations.

**93. What are design patterns?**
Reusable, proven solutions to common software design problems, categorized as **Creational** (Singleton, Factory, Builder), **Structural** (Adapter, Decorator, Facade), and **Behavioral** (Observer, Strategy, Command).

**94. Explain Singleton in Python.**
A pattern that restricts a class to only ever having one instance.
```python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # True
```

**95. What are dataclasses?**
A decorator (`@dataclass` from the `dataclasses` module) that auto-generates boilerplate methods like `__init__`, `__repr__`, and `__eq__` for classes that primarily store data, reducing repetitive code.
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)  # Point(x=1, y=2)
```


---

## Coding Questions

**96. Reverse a string.**
```python
s = "python"
print(s[::-1])  # nohtyp
```

**97. Reverse a list.**
```python
lst = [1, 2, 3, 4]
print(lst[::-1])       # [4, 3, 2, 1]
lst.reverse()           # in-place reversal
```

**98. Find the second-largest element.**
```python
def second_largest(nums):
    unique = list(set(nums))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

print(second_largest([10, 20, 4, 45, 99]))  # 45
```

**99. Remove duplicates.**
```python
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))  # preserves order

print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
```

**100. Find the frequency of each character.**
```python
from collections import Counter

def char_frequency(s):
    return dict(Counter(s))

print(char_frequency("hello"))  # {'h':1, 'e':1, 'l':2, 'o':1}
```

**101. Check for a palindrome.**
```python
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
```

**102. Find factorial recursively.**
```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))  # 120
```

**103. Generate Fibonacci numbers.**
```python
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))  # [0,1,1,2,3,5,8,13,21,34]
```

**104. Check for prime numbers.**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True
```

**105. Merge two sorted lists.**
```python
def merge_sorted(a, b):
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

print(merge_sorted([1, 3, 5], [2, 4, 6]))  # [1,2,3,4,5,6]
```

---

# Part 2: FastAPI Interview Questions

## FastAPI Basics

**106. What is FastAPI?**
A modern, high-performance Python web framework for building APIs, built on top of **Starlette** (for the web layer) and **Pydantic** (for data validation), with native support for async, automatic OpenAPI/Swagger docs, and type-hint-based validation.

**107. Why is FastAPI faster than Flask?**
FastAPI is built on **ASGI** (asynchronous), enabling non-blocking I/O and true concurrency for I/O-bound workloads, while Flask traditionally runs on **WSGI** (synchronous, one request per worker thread at a time). FastAPI also uses Pydantic (with a Rust-based core in v2) for fast, compiled data validation.

**108. What is ASGI?**
**Asynchronous Server Gateway Interface** — a spec for Python web servers/frameworks to handle asynchronous requests, supporting async I/O, WebSockets, and long-lived connections, unlike the older synchronous WSGI standard.

**109. Difference between WSGI and ASGI.**
| WSGI | ASGI |
|---|---|
| Synchronous | Supports both sync and async |
| One request per thread/process at a time | Handles many concurrent connections via async |
| No WebSocket support | Supports WebSockets, long-lived connections |
| Used by Flask, Django (traditional) | Used by FastAPI, Starlette, Django Channels |

**110. Explain the FastAPI request lifecycle.**
1. Request hits the ASGI server (e.g., Uvicorn).
2. Routed to the matching path operation function based on the URL/method.
3. Middleware executes (e.g., CORS, logging).
4. Dependencies (`Depends()`) are resolved.
5. Request body/params validated against Pydantic models.
6. Path operation function executes (business logic).
7. Response is serialized (using response model if defined) and returned through middleware back to the client.

**111. How does FastAPI generate Swagger documentation?**
FastAPI automatically inspects your route definitions, Pydantic models, and type hints to build an **OpenAPI schema** in the background, which it then renders as interactive documentation at `/docs` (Swagger UI) and `/redoc` (ReDoc) — no manual doc-writing required.

**112. What is OpenAPI?**
A standardized specification (format) for describing REST APIs — endpoints, request/response schemas, parameters, authentication methods — in a machine-readable (JSON/YAML) way, enabling automatic doc generation and client SDK generation.


---

## Routing

**113. Difference between GET, POST, PUT, PATCH, and DELETE.**
| Method | Purpose |
|---|---|
| `GET` | Retrieve a resource (no body, idempotent) |
| `POST` | Create a new resource |
| `PUT` | Replace/update an entire resource (idempotent) |
| `PATCH` | Partially update a resource |
| `DELETE` | Remove a resource |

**114. What are path parameters?**
Values embedded directly in the URL path, used to identify a specific resource.
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

**115. What are query parameters?**
Optional key-value pairs appended to the URL after `?`, typically used for filtering, sorting, or pagination.
```python
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
# /items?skip=5&limit=20
```

**116. Difference between path and query parameters.**
Path parameters are part of the URL structure and identify a specific resource (`/users/5`) — typically required. Query parameters come after `?` and are used for optional filters/options (`/users?active=true`) — typically optional with defaults.

**117. How do you organize routes?**
Using **`APIRouter`** to split routes into separate modules/files by feature (e.g., `users.py`, `posts.py`), then including them in the main app with prefixes and tags.
```python
# routers/users.py
from fastapi import APIRouter
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list_users():
    return []

# main.py
from routers import users
app.include_router(users.router)
```

---

## Dependency Injection

**118. What is Depends()?**
A FastAPI utility used to declare a **dependency** — a function (or class) that FastAPI automatically calls and injects its return value into your path operation function. Used for shared logic like DB sessions, authentication, or common query parameters.
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
```

**119. How does dependency injection work in FastAPI?**
When a route declares a parameter with `Depends(some_function)`, FastAPI calls `some_function` (resolving its own dependencies recursively first), caches the result per-request by default, and passes the return value into your endpoint — decoupling business logic from setup/teardown code.

**120. Can dependencies depend on other dependencies?**
Yes — dependencies can themselves declare `Depends()` on other dependencies, forming a chain/tree. FastAPI resolves the entire dependency graph automatically and reuses results within the same request (unless `use_cache=False`).

**121. Why is dependency injection useful?**
It promotes code reuse (shared logic like DB sessions, auth checks, pagination defaults), separation of concerns, and easier testing (dependencies can be overridden with mocks via `app.dependency_overrides`).

---

## Pydantic

**122. What is Pydantic?**
A data validation and settings management library that uses Python type hints to validate, parse, and serialize data at runtime, raising clear validation errors when data doesn't match the expected schema.

**123. Why does FastAPI use Pydantic?**
To automatically validate request bodies/query params against defined schemas, serialize response data, generate accurate OpenAPI documentation from type hints, and provide clear, automatic error messages — all with minimal boilerplate.

**124. Difference between request and response models.**
A **request model** defines and validates the shape of incoming data (what the client sends). A **response model** (`response_model=...`) defines and filters what data is sent back to the client — useful for hiding sensitive fields like passwords.
```python
class UserCreate(BaseModel):    # request model
    username: str
    password: str

class UserOut(BaseModel):        # response model (no password!)
    id: int
    username: str

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    ...
```

**125. What is model_config = ConfigDict(from_attributes=True)?**
A Pydantic v2 setting that allows a model to be created directly from an object's attributes (e.g., an SQLAlchemy ORM instance) rather than only from a dictionary — essential for converting DB models into Pydantic response models.
```python
class UserOut(BaseModel):
    id: int
    username: str
    model_config = ConfigDict(from_attributes=True)
```

**126. Difference between BaseModel and SQLAlchemy models.**
A Pydantic **`BaseModel`** defines the shape/validation of data for API input/output (in-memory, not persisted). A **SQLAlchemy model** maps to a database table and handles persistence, queries, and relationships. They serve different layers — API schema vs. database schema — and are typically kept as separate classes.

**127. What are validators?**
Custom methods (decorated with `@field_validator` in Pydantic v2, or `@validator` in v1) that let you add custom validation/transformation logic to a field beyond simple type checking.
```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator("age")
    @classmethod
    def check_age(cls, v):
        if v < 0:
            raise ValueError("Age must be positive")
        return v
```


---

## SQLAlchemy

**128. What is an ORM?**
**Object-Relational Mapper** — a library that lets you interact with a relational database using Python objects/classes instead of writing raw SQL, mapping tables to classes and rows to instances.

**129. Why use SQLAlchemy?**
It provides a powerful, flexible ORM plus a Core SQL toolkit, supports multiple databases, handles connection pooling, migrations (with Alembic), relationship management, and reduces boilerplate/raw SQL while still allowing fine-grained control when needed.

**130. Difference between Session and AsyncSession.**
`Session` is SQLAlchemy's standard synchronous interface for executing queries and managing transactions. `AsyncSession` is the asynchronous counterpart (used with `async`/`await` and an async DB driver like `asyncpg`), suited for FastAPI's async endpoints to avoid blocking the event loop.

**131. Explain the repository pattern.**
A design pattern that abstracts data access logic behind a dedicated "repository" class/interface, so business logic doesn't directly depend on ORM/query details. This improves testability (mock the repository) and keeps database logic centralized and swappable.
```python
class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()
```

**132. What is select()?**
The SQLAlchemy 2.0-style construct used to build SQL SELECT queries in a unified way for both Core and ORM usage.
```python
from sqlalchemy import select
stmt = select(User).where(User.id == 1)
result = db.execute(stmt)
```

**133. Difference between scalar() and scalars().**
`scalar()` returns a single value (the first column of the first row) from a result, or `None`. `scalars()` returns an iterable of single-column values across all rows (commonly used to get a list of ORM objects directly, e.g., `db.execute(stmt).scalars().all()`).

**134. What is flush()?**
Sends pending changes (INSERTs/UPDATEs/DELETEs) to the database within the current transaction, without committing it — useful when you need a generated ID (like an auto-increment primary key) before the transaction is finalized.

**135. Difference between flush() and commit().**
`flush()` pushes pending SQL statements to the DB but keeps the transaction open (changes are visible within the transaction, but not yet permanent and can still be rolled back). `commit()` finalizes the transaction, making all changes permanent, and typically triggers a flush automatically beforehand.

**136. Why do we use refresh()?**
`db.refresh(obj)` re-fetches an object's current state from the database after a commit — useful to get DB-generated values (auto-increment IDs, default timestamps, triggers) that were set at the database level, not known in Python before the insert.

**137. Difference between add() and merge().**
`add()` adds a new (transient) object to the session to be inserted. `merge()` takes a possibly-detached object and either updates the corresponding existing row (if a matching primary key exists) or inserts it — useful for reattaching objects that came from outside the current session.

---

## Relationships

**138. Explain One-to-One relationships.**
Each row in Table A corresponds to exactly one row in Table B, typically enforced via a unique foreign key. Example: a `User` has exactly one `Profile`.
```python
class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="profile")
```

**139. Explain One-to-Many relationships.**
One row in Table A can relate to many rows in Table B, but each row in Table B relates back to only one row in Table A. Example: one `Author` has many `Books`.
```python
class Author(Base):
    books = relationship("Book", back_populates="author")

class Book(Base):
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
```

**140. Explain Many-to-Many relationships.**
Rows in Table A can relate to many rows in Table B, and vice versa, implemented via a separate **association table** holding foreign keys to both sides. Example: `Students` and `Courses` (a student takes many courses; a course has many students).
```python
enrollment = Table(
    "enrollment", Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)
```

**141. What is back_populates?**
Used in SQLAlchemy relationships to explicitly link two sides of a relationship together, so changes on one side (e.g., appending to a list) automatically reflect on the other side in Python, keeping both sides in sync in memory.

**142. Difference between joinedload() and selectinload().**
Both are eager-loading strategies to avoid the N+1 query problem. `joinedload()` uses a SQL `JOIN` to fetch related data in a single query. `selectinload()` issues a second separate `SELECT ... WHERE id IN (...)` query to fetch all related rows at once — often more efficient for one-to-many relationships with many rows, avoiding row duplication from joins.

**143. What is lazy loading?**
The default relationship-loading strategy where related objects are only fetched from the database when they're actually accessed, not when the parent object is loaded — can cause the N+1 query problem if accessed in a loop.

**144. What is eager loading?**
Loading related objects upfront, in the same query (or a controlled set of queries) as the parent object, using `joinedload()` or `selectinload()`, to avoid multiple round-trips to the database (the N+1 problem).

---

## Authentication

**145. What is JWT?**
**JSON Web Token** — a compact, self-contained, digitally signed token format used to securely transmit claims (user identity, permissions) between parties, commonly used for stateless authentication in APIs.

**146. Explain JWT structure.**
A JWT has three Base64Url-encoded parts separated by dots: `header.payload.signature`.
- **Header** — specifies the algorithm (e.g., HS256) and token type.
- **Payload** — contains claims (user ID, expiration, roles, etc.).
- **Signature** — verifies the token hasn't been tampered with, computed using a secret key (or private key for asymmetric algorithms).

**147. Difference between authentication and authorization.**
**Authentication** verifies *who you are* (login, credential check). **Authorization** determines *what you're allowed to do* once identified (permissions, roles, access control) — authentication always happens first.

**148. What is a Bearer token?**
A token sent in the `Authorization` HTTP header as `Authorization: Bearer <token>`, signaling that the bearer (holder) of the token is granted access — no additional proof of identity is required beyond possessing the token.

**149. Where is the JWT stored?**
Commonly in browser **localStorage** or **sessionStorage** (simple but vulnerable to XSS), or in an **HttpOnly cookie** (safer against XSS, but needs CSRF protection). The right choice depends on the security requirements of the application.

**150. How do you protect routes?**
By adding an authentication dependency (`Depends()`) that validates the token/credentials before the route logic executes, raising an `HTTPException(401)` if invalid.
```python
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_jwt(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return payload

@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user
```

**151. What is token expiration?**
A timestamp (`exp` claim) embedded in the JWT indicating when the token becomes invalid, limiting the window an attacker could misuse a stolen token, and forcing periodic re-authentication or token refresh.

**152. How do you refresh a token?**
Issue a short-lived **access token** alongside a longer-lived **refresh token**. When the access token expires, the client sends the refresh token to a dedicated endpoint, which verifies it and issues a new access token (and often a new refresh token) without requiring the user to log in again.

---

## File Upload

**153. Difference between bytes and UploadFile.**
Using `bytes` as a parameter type reads the **entire file into memory** as raw bytes immediately — simple but memory-heavy for large files. `UploadFile` wraps a **SpooledTemporaryFile**, streaming data and only fully loading into memory if it exceeds a size threshold (then spilling to disk) — more efficient for large files.

**154. Why is UploadFile preferred?**
It's more memory-efficient for large files (uses spooled temp storage instead of loading everything into RAM), supports async read operations, and exposes useful metadata like filename and content-type.

**155. How do you save uploaded files?**
```python
from fastapi import UploadFile, File
import shutil

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
```

**156. How do you serve static files?**
Mount a `StaticFiles` instance at a URL path.
```python
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
```

---

## Middleware

**157. What is middleware?**
Code that runs before and/or after every request in the application, used for cross-cutting concerns like logging, authentication checks, CORS, request timing, or modifying requests/responses globally.

**158. Explain CORS.**
**Cross-Origin Resource Sharing** — a browser security mechanism that restricts web pages from making requests to a different domain/origin than the one that served the page, unless the server explicitly allows it via specific response headers.

**159. Why is CORS required?**
Without it, browsers block frontend applications hosted on one origin (e.g., `myapp.com`) from calling an API on a different origin (e.g., `api.myapp.com`) as a security default, so the API server must explicitly opt in to allow specific origins/methods/headers.

**160. How do you implement custom middleware?**
```python
from starlette.middleware.base import BaseHTTPMiddleware

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        response.headers["X-Process-Time"] = str(time.time() - start)
        return response

app.add_middleware(TimingMiddleware)
```


---

## Exception Handling (FastAPI)

**161. What is HTTPException?**
A built-in FastAPI exception class used to return proper HTTP error responses (status code + detail message) from within a route or dependency.
```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
```

**162. How do you create a global exception handler?**
Using `@app.exception_handler()` to catch a specific exception type anywhere in the app and return a consistent, custom response.
```python
from fastapi.responses import JSONResponse

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(status_code=400, content={"detail": str(exc)})
```

**163. Difference between validation errors and HTTP exceptions.**
**Validation errors** (`RequestValidationError`) are automatically raised by FastAPI/Pydantic when incoming data doesn't match the expected schema (returns 422 by default). **HTTP exceptions** (`HTTPException`) are manually raised in your own code to signal specific error conditions (404, 403, 401, etc.) with a custom status code and message.

---

## Deployment

**164. What is Uvicorn?**
A lightning-fast **ASGI server** implementation used to run FastAPI (and other ASGI) applications, handling the actual HTTP request/response cycle and async event loop.

**165. What is Gunicorn?**
A mature, production-grade **WSGI** process manager, commonly used together with Uvicorn (via `uvicorn.workers.UvicornWorker`) to manage multiple Uvicorn worker processes, handling process restarts, load balancing across workers, and better production stability.

**166. Difference between development and production servers.**
Development servers (e.g., `uvicorn main:app --reload`) prioritize convenience — auto-reload on code changes, verbose debug output — but run a single process, which isn't robust or performant enough for real traffic. Production setups run multiple worker processes (often via Gunicorn + Uvicorn workers), behind a reverse proxy (Nginx), with proper logging, monitoring, and no auto-reload.

**167. How do you deploy FastAPI?**
Common approaches: containerize with Docker, run behind Gunicorn managing multiple Uvicorn workers, put Nginx in front as a reverse proxy/load balancer with HTTPS termination, and deploy to a cloud platform (AWS ECS/EKS, GCP Cloud Run, Azure, or a VPS) — often orchestrated with CI/CD pipelines.

**168. What is Docker?**
A containerization platform that packages an application with all its dependencies, libraries, and runtime into a single portable, isolated **container** image, ensuring the app runs consistently across different environments (dev, staging, production).

**169. Why use Docker with FastAPI?**
Ensures consistent environments across dev/staging/production, simplifies dependency management, makes scaling and orchestration easier (Kubernetes, ECS), and streamlines CI/CD deployment pipelines.

---

## Practical Questions

**170. How would you implement pagination?**
```python
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Item).offset(skip).limit(limit).all()
# GET /items?skip=20&limit=10
```

**171. How would you implement search?**
```python
@app.get("/items/search")
def search_items(q: str, db: Session = Depends(get_db)):
    return db.query(Item).filter(Item.name.ilike(f"%{q}%")).all()
```

**172. How would you upload an image?**
```python
@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "File must be an image")
    contents = await file.read()
    with open(f"images/{file.filename}", "wb") as f:
        f.write(contents)
    return {"filename": file.filename}
```

**173. How would you implement role-based authorization?**
```python
def require_role(role: str):
    def role_checker(user=Depends(get_current_user)):
        if user["role"] != role:
            raise HTTPException(403, "Not authorized")
        return user
    return role_checker

@app.delete("/admin/users/{id}")
def delete_user(id: int, user=Depends(require_role("admin"))):
    ...
```

**174. How would you hash passwords?**
Using `passlib` (bcrypt) — never store plaintext passwords.
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain, hashed) -> bool:
    return pwd_context.verify(plain, hashed)
```

**175. How would you implement soft delete?**
Add an `is_deleted` (or `deleted_at`) column instead of physically removing rows, and filter it out in default queries.
```python
class Item(Base):
    is_deleted = Column(Boolean, default=False)

def soft_delete(item_id: int, db: Session):
    item = db.query(Item).filter(Item.id == item_id).first()
    item.is_deleted = True
    db.commit()

# Always filter it out by default
db.query(Item).filter(Item.is_deleted == False).all()
```


---

# Scenario-Based Questions

**176. Design a Blog API using FastAPI.**
Core entities: `User`, `Post`, `Comment`. Suggested structure:
```
app/
├── main.py
├── models/        # SQLAlchemy models (User, Post, Comment)
├── schemas/        # Pydantic schemas (request/response)
├── routers/         # users.py, posts.py, comments.py
├── services/        # business logic
├── repositories/    # DB query layer
└── core/            # config, security, DB session
```
Key endpoints: `POST /auth/login`, `POST /posts`, `GET /posts`, `GET /posts/{id}`, `PUT /posts/{id}`, `DELETE /posts/{id}`, `POST /posts/{id}/comments`. Use JWT auth to identify the post author, and check ownership before allowing edits/deletes.

**177. Implement JWT authentication for a Library Management System.**
1. `POST /auth/register` — create user, hash password with bcrypt.
2. `POST /auth/login` — verify credentials, issue an access token (`exp` ~15-30 min) and refresh token (`exp` days).
3. Protect routes (e.g., `POST /books/{id}/borrow`) with a `Depends(get_current_user)` dependency that decodes and validates the JWT.
4. Use role claims in the token (`member` vs `librarian`) to restrict admin actions like adding/removing books via a `require_role("librarian")` dependency.
5. `POST /auth/refresh` — exchange a valid refresh token for a new access token.

**178. Design the relationships for a Student-Course Enrollment System.**
- `Student` ↔ `Course`: **Many-to-Many** via an `enrollments` association table (also useful to store `enrollment_date`, `grade`).
- `Course` → `Instructor`: **Many-to-One** (one instructor teaches many courses).
- `Student` → `Department`: **Many-to-One**.
```python
class Enrollment(Base):
    __tablename__ = "enrollments"
    student_id = Column(ForeignKey("students.id"), primary_key=True)
    course_id = Column(ForeignKey("courses.id"), primary_key=True)
    grade = Column(String, nullable=True)
    enrolled_at = Column(DateTime, default=datetime.utcnow)
```

**179. How would you upload profile images and store their paths in the database?**
1. Accept the file via `UploadFile`, validate content-type/size.
2. Generate a unique filename (e.g., UUID + extension) to avoid collisions/overwrites.
3. Save the file to disk (or cloud storage like S3) under a dedicated directory.
4. Store only the **relative path/URL** (not the binary) in the `User.profile_image_url` column.
5. Serve it back via a static file mount or a CDN/S3 URL.

**180. Explain how you would structure a FastAPI project using routers, services, repositories, and models.**
A layered architecture keeps concerns separated and testable:
- **`models/`** — SQLAlchemy ORM classes (DB table definitions).
- **`schemas/`** — Pydantic models (API request/response contracts).
- **`repositories/`** — raw DB query logic (CRUD operations against models), isolates SQLAlchemy specifics.
- **`services/`** — business logic that calls repositories, applies validation/rules, orchestrates multiple repositories if needed.
- **`routers/`** — thin HTTP layer; parses requests, calls services, returns responses. No business logic here.

This keeps routes thin, business logic testable independent of HTTP, and the database layer swappable.

**181. How would you prevent users from editing another user's blog?**
In the update/delete route, after fetching the post, compare `post.author_id` with the `id` of the authenticated user (from the JWT/`Depends(get_current_user)`), and raise `HTTPException(403, "Not authorized")` if they don't match — ownership checks should always happen server-side, never trusted from client input.
```python
@app.put("/posts/{post_id}")
def update_post(post_id: int, data: PostUpdate, user=Depends(get_current_user), db=Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(404, "Post not found")
    if post.author_id != user.id:
        raise HTTPException(403, "Not authorized to edit this post")
    ...
```

**182. How would you optimize an API suffering from the N+1 query problem?**
Identify where a parent list is loaded and then each item triggers a separate query for related data (e.g., loading 50 posts then querying each post's author individually = 51 queries). Fix by using **eager loading** with `selectinload()` or `joinedload()` to fetch related data in one or two queries total instead of N+1.
```python
stmt = select(Post).options(selectinload(Post.author))
posts = db.execute(stmt).scalars().all()
```

**183. How would you implement a global exception handler?**
Register handlers at the app level for both expected and unexpected errors, ensuring consistent error response format across the whole API.
```python
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.exception_handler(Exception)
async def unhandled_exception_handler(request, exc):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(status_code=500, content={"error": "Internal server error"})
```

**184. How would you add logging to your FastAPI application?**
Use Python's built-in `logging` module configured at startup, plus middleware to log each request's method, path, status code, and duration.
```python
import logging, time
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

@app.middleware("http")
async def log_requests(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    logger.info(f"{request.method} {request.url.path} - {response.status_code} - {duration:.3f}s")
    return response
```
For production, ship logs to a centralized system (ELK, CloudWatch, Datadog) with structured (JSON) log format.

**185. How would you test your FastAPI endpoints?**
Use `TestClient` (from `fastapi.testclient`, built on `httpx`) with `pytest`, overriding dependencies (like the DB session) to use a test database.
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={"username": "test", "password": "pass123"})
    assert response.status_code == 201
    assert response.json()["username"] == "test"
```
For async endpoints, `httpx.AsyncClient` with `pytest-asyncio` is commonly used. Use `app.dependency_overrides[get_db] = override_get_db` to point tests at an isolated test database (e.g., SQLite in-memory or a dedicated test Postgres DB).

---

## Quick Reference: Key Takeaways

- **Memory & Concurrency**: Python uses reference counting + GC for memory; the GIL limits true multithreaded parallelism for CPU-bound work — use `multiprocessing` for CPU-bound, `asyncio`/threads for I/O-bound.
- **OOP**: Favor composition over deep inheritance chains; understand `@classmethod` vs `@staticmethod` vs instance methods.
- **FastAPI**: Built on Starlette (ASGI) + Pydantic; `Depends()` powers dependency injection; always separate request/response schemas.
- **SQLAlchemy**: Use `selectinload`/`joinedload` to avoid N+1 queries; understand `flush()` vs `commit()`.
- **Security**: Always hash passwords (bcrypt), validate JWTs server-side, and enforce ownership/role checks on every mutating endpoint.

---

*This README was compiled as a complete, interview-ready reference for Python and FastAPI. Practice explaining these concepts out loud and be ready to write the code examples from scratch on a whiteboard or in a live coding round.*