import json
from pathlib import Path

DATA = Path('data/tasks.json')

def load_tasks():
    if not DATA.exists():
        return []
    return json.loads(DATA.read_text())

def save_tasks(tasks):
    DATA.parent.mkdir(exist_ok=True)
    DATA.write_text(json.dumps(tasks, indent=2))

while True:
    print('1 - Add task')
    print('2 - List tasks')
    print('0 - Exit')

    option = input('Choose: ')

    if option == '1':
        task = input('Task: ')
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)

    elif option == '2':
        tasks = load_tasks()
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    elif option == '0':
        break
