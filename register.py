import json
import os

if not os.path.exists("person.json"):
    with open("person.json", "wt") as file:
        json.dump([], file)

with open("person.json", "rt") as file:
    person = json.load(file)

def write_file():
    with open("person.json", "wt") as file:
        json.dump(person, file)

def register_person(name, gender, age):
    if not isinstance(name, str) or not name.strip():
        print("\033[31mERROR: Invalid name.\033[m")
        return
    if not isinstance(gender, str):
        print("\033[31mERROR: Invalid gender.\033[m")
        return
    if not isinstance(age, int) or age < 0 or age > 120:
        print("\033[31mERROR: Age must have 0 to 120.\033[m")
        return

    id = max([p["id"] for p in person], default=0) + 1
    personinfo = {"id": id, "name": name.strip(), "gender": gender, "age": age}
    person.append(personinfo)
    write_file()

def delete_person(id):
    for i, p in enumerate(person):
        if p["id"] == id:
            person.pop(i)
            write_file()
            break
    else:
        print(f"\033[31mThe id {id} not exists!\033[m")

def list_people():
    if not person:
        print("No person registered")
        return

    for i in sorted(person, key=lambda x: x['name'].lower()):
        print("="*30)
        print(f"\033[1;32m{i['name']}\033[m")
        print(f"id: {i['id']}")
        print(f"Gender: {i['gender']}")
        print(f"Age: {i['age']}")
    print("="*30)
