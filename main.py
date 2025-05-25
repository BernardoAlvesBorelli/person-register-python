# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import register
import datetime
from dateutil.relativedelta import relativedelta

def opt_menu(*li):
    for index, item in enumerate(li):
        print(f"{index+1}: {item}")

def read_string(msg):
    while True:
        valor = input(msg).strip()
        if not valor:
            print("\033[31mERROR! Input cannot be empty!\033[m")
            continue

        correct = ' '.join(p.capitalize() for p in valor.split())
        if valor != correct:
            print("\033[33mWARNING! Names should start with uppercase letters.\033[m")
            print(f"\033[36mSuggested: {correct}\033[m")
            resp = input("Use the suggested version? (y/n): ").strip().lower()
            if resp == "y":
                return correct
            elif resp == "n":
                return valor
            else:
                print("\033[31mInvalid response. Try again.\033[m")
        else:
            return valor


def read_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("\033[31mERROR! Please enter numbers only!\033[m")
            continue

def read_options(msg, *valid_options):
    while True:
        try:
            option = int(input(msg))
            if option in valid_options:
                return option
            else:
                print("\033[31mERROR! Invalid option!\033[m")
        except ValueError:
            print("\033[31mERROR! Please enter numbers only!\033[m")
            continue

def read_birthdate(msg):
    while True:
        dt = str(input(msg))
        try:
            birth_date = datetime.datetime.strptime(dt, "%Y-%m-%d").date()
        except ValueError:
            print("\033[31mERROR! The date format in invalid or this day does not exists!\033[m")
            continue
        else:
            today = datetime.date.today()
            min_date = today - relativedelta(years=120)
            if birth_date < min_date:
                print("\033[31mERROR! Age must be less than 120!\033[m")
            elif birth_date > today: 
                print("\033[31mERROR! The date entered is in the future!\033[m")
            else:
                return birth_date

print("="*30)
print(f"{'PERSON':<10}{'REGISTER':^10}{'PYTHON':>10}")
print("AUTHOR: Bernardo Alves Borelli")
print("="*30)

while True:
    opt_menu("List people", "Register person", "Delete person", "Exit system")
    opt = read_options("Enter an option: ", 1, 2, 3, 4)
    match opt:
        case 1:
            register.list_people()
        case 2:
            name = read_string("Enter person’s name: ")
            opt_menu("Male", "Female", "Other/Non Binary")
            opt_gender = read_options("Enter person’s gender: ", 1, 2, 3)
            match opt_gender:
                case 1:
                    gender = "Male"
                case 2:
                    gender = "Female"
                case 3:
                    gender = "Other"
            birth_date = read_birthdate("Enter person’s birth date (YYYY-MM-DD): ")
            register.register_person(name, gender, birth_date)
        case 3:
            id = read_int("Write the person’s id: ")
            register.delete_person(id)
        case 4:
            print("Exiting system... Goodbye!")
            break