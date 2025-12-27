class Person
    attr_reader :name, :age
  
    def initialize(name, age)
      @name = name
      @age = age
    end
  
    def birthday!
      @age += 1
    end
  
    def introduce
      puts "Hello, I'm #{@name} and I'm #{@age} years old."
    end
  
    def self.create_family(members)
      members.map { |name, age| new(name, age) }
    end
  end
  
  # Create a family
  family = Person.create_family([
    ["Alice", 35],
    ["Bob", 40],
    ["Charlie", 12]
  ])
  
  # Introduce family members
  family.each(&:introduce)
  
  # Celebrate Charlie's birthday
  charlie = family.find { |person| person.name == "Charlie" }
  charlie.birthday!
  charlie.introduce