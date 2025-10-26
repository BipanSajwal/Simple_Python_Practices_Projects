from queue import PriorityQueue

a = {
   "Algorithm": "A step-by-step procedure to solve a problem or perform a task.",
   "Variable": "A named location in memory used to store data.",
   "Function": "A block of reusable code that performs a specific task.",
   "Loop": "A control structure used to repeat a block of code multiple times.",
   "Dictionary": "A data structure that stores key-value pairs in Python.",
   "List": "An ordered collection of items that can be changed (mutable).",
   "Tuple": "An ordered collection of items that cannot be changed (immutable).",
   "String": "A sequence of characters enclosed in quotes.",
   "Boolean": "A data type that represents either True or False.",
   "Compile": "To convert source code into machine code or bytecode.",
   "Syntax": "The set of rules that defines how a program must be written.",
   "Iteration": "The repetition of a process in a computer program.",
   "Debugging": "The process of finding and fixing errors in a program.",
   "Parameter": "A variable used to pass information into a function."
}

print("Available words:\n")
for word in a.keys():
    print("-", word)

choice = input("\nEnter the word you want to know the meaning of: ")

# Convert input to title case to match keys (e.g., algorithm → Algorithm)
choice = choice.capitalize()

if choice in a:
    print(f"\n Meaning of '{choice}':\n{a[choice]}")
else:
    print("\n Sorry, that word is not in the dictionary.")
