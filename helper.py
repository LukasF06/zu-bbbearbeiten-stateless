from dataclasses import dataclass

# Hier werden die Daten gespeichert
items = []


@dataclass
class Todo:
    text: str
    isCompleted: bool = False

# Ver-BBB-sierung
def add(title):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Todo(title))


def get_all():
    return items


# Hier werden sie an index.html weitergegeben
def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted