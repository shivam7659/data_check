import os
with open('usecase.conf', 'r') as file:
    content = file.read()
    print(content)
os.system('git fetch origin main:main')
os.system('git checkout main')
with open('usecase.conf', 'r') as file:
    content = file.read()
    print(content)

os.system('git checkout -')
with open('usecase.conf', 'r') as file:
    content = file.read()
    print(content)

