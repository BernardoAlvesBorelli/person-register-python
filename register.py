# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import extra
import json
import os

def load_file():
    if not os.path.exists("person.json"):
        with open("person.json", "wt") as file:
            json.dump([], file)
    with open("person.json", "rt") as file:
        return json.load(file)

person = load_file()

def write_file():
    with open("person.json", "wt") as file:
        json.dump(person, file, indent=4)

def register_person(name, gender, birth_date):
    if not isinstance(name, str) or not name.strip():
        print("\033[31mERROR: Invalid name.\033[m")
        return
    if not isinstance(gender, str):
        print("\033[31mERROR: Invalid gender.\033[m")
        return

    id = max([p["id"] for p in person], default=0) + 1
    personinfo = {"id": id, "name": name.strip(), "gender": gender, "birth_date": birth_date.isoformat()  }
    person.append(personinfo)
    write_file()
    print(f"\033[32mPerson '{name}' registered successfully!\033[m")

def delete_person(id):
    for i, p in enumerate(person):
        if p["id"] == id:
            person.pop(i)
            write_file()
            print(f"\033[32mPerson '{p['name']}' deleted successfully!\033[m")
            break
    else:
        print(f"\033[31mThe id {id} not exists!\033[m")

def list_people():
    if not person:
        print("No people are registered")
        return

    for i in sorted(person, key=lambda x: x['name'].lower()):
        print("="*30)
        print(f"\033[1;32m{i['name']}\033[m")
        print(f"id: {i['id']}")
        print(f"Gender: {i['gender']}")
        print(f"Birth date: {i['birth_date']}")
        print(f"Age: {extra.calculate_age(i['birth_date'])}")
    print("="*30)
