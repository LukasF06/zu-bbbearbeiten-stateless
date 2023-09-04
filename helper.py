from dataclasses import dataclass
import datetime

# Hier werden die Daten gespeichert
items = []


@dataclass
class Todo:
    text: str
    date: datetime
    isCompleted: bool = False

# Ver-BBB-sierung
def add(title, date):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    items.append(Todo(title, date))


def get_all():
    return items


# Hier werden sie an index.html weitergegeben
def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted

def delete():
    items.clear()