import os
with open('usecase.conf', 'r') as file:
    content = file.read()
    print(content)
os.system('git fetch origin')
os.system('git checkout origin/main')
with open('usecase.conf', 'r') as file:
    content = file.read()
    print(content)
