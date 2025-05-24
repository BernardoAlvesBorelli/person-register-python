import register

def ol(*li):
    for index, item in enumerate(li):
        print(f"{index+1}: {item}")

def read_string(msg):
    while True:
        valor = input(msg).strip()
        if not valor:
            print("\033[31mERROR! Empty input!\033[m")
            continue

        correct = ' '.join(p.capitalize() for p in valor.split())
        if valor != correct:
            print("\033[33mWARNING! Names should start with uppercase letters.\033[m")
            print(f"\033[36mSuggested: {correct}\033[m")
            resp = input("Use the suggested version? (Y/N): ").strip().lower()
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
            print("\033[31mERROR! Write only numbers!\033[m")
            continue

def read_options(msg, *valid_options):
    while True:
        try:
            option = int(input(msg))
            if option in valid_options:
                return option
            else:
                print("\033[31mERROR! Invalid Option!\033[m")
        except ValueError:
            print("\033[31mERROR! Write only numbers!\033[m")
            continue

print("="*30)
print(f"{'PERSON':<10}{'REGISTER':^10}{'PYTHON':>10}")
print("AUTHOR: Bernardo Alves Borelli")
print("="*30)

while True:
    ol("List people", "Register people", "Delete person", "Exit system")
    opt = read_options("Write a option: ", 1, 2, 3, 4)
    match opt:
        case 1:
            register.list_people()
        case 2:
            name = read_string("Write person name: ")
            ol("Male", "Female", "Other/Non Binary")
            opt_gender = read_options("Write person gender: ", 1, 2, 3)
            match opt_gender:
                case 1:
                    gender = "Male"
                case 2:
                    gender = "Female"
                case 3:
                    gender = "Other"
            age = read_int("Write person age: ")
            register.register_person(name, gender, age)
        case 3:
            id = read_int("Write the person id: ")
            register.delete_person(id)
        case 4:
            print("Exiting system...")
            break