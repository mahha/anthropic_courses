# Here's the Python translation of the Ruby code:

# ```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    def birthday(self):
        self._age += 1
    
    def introduce(self):
        print(f"Hello, I'm {self._name} and I'm {self._age} years old.")
    
    @classmethod
    def create_family(cls, members):
        return [cls(name, age) for name, age in members]


# Create a family
family = Person.create_family([
    ["Alice", 35],
    ["Bob", 40],
    ["Charlie", 12]
])

# Introduce family members
for person in family:
    person.introduce()

# Celebrate Charlie's birthday
charlie = next(person for person in family if person.name == "Charlie")
charlie.birthday()
charlie.introduce()
# ```

# **Key translations:**

# 1. **Class definition**: `class Person:` instead of `class Person`
# 2. **Constructor**: `__init__` instead of `initialize`
# 3. **Instance variables**: Using `self._name` and `self._age` with `@property` decorators to create read-only attributes (equivalent to Ruby's `attr_reader`)
# 4. **Method naming**: `birthday()` instead of `birthday!` (Python doesn't use `!` in method names)
# 5. **String interpolation**: f-strings `f"..."` instead of `"#{...}"`
# 6. **Class methods**: `@classmethod` decorator instead of `self.`
# 7. **List comprehension**: `[cls(name, age) for name, age in members]` instead of `members.map { |name, age| new(name, age) }`
# 8. **Iteration**: `for person in family:` instead of `family.each(&:introduce)`
# 9. **Find operation**: `next(person for person in family if...)` instead of `family.find { |person| ... }`