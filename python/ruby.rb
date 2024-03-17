class Person
  attr_accessor :name, :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def introduce
    puts "Hi, my name is #{@name} and I am #{@age} years old."
  end
end

# Create a new Person object
person1 = Person.new("Alice", 30)

# Access and print out attributes
puts "Name: #{person1.name}"
puts "Age: #{person1.age}"

# Call the introduce method  
person1.introduce
