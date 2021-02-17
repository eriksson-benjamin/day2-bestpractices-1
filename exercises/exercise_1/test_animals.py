import animals

# Birds
print('Dangerous birds:')
dangerous_birds = animals.dangerous.Birds()
dangerous_birds.printMembers()

print('Harmless birds:')
harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

# Mammals
print('\nDangerous mammals:')
dangerous_mammals = animals.dangerous.Mammals()
dangerous_mammals.printMembers()

print('Harmless mammals:')
harmless_mammals = animals.harmless.Mammals()
harmless_mammals.printMembers()

# Fish
print('\nDangerous fish:')
dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()

print('Harmless fish:')
harmless_fish = animals.harmless.Fish()
harmless_fish.printMembers()


