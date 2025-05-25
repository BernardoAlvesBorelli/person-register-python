# Person Register System in Python

This is my first Python project published on GitHub.  
It was created to test my knowledge of Python, especially with regard to file manipulation, JSON and GUI interaction.  
Now the GUI interaction has arrived, which wasn't in the previous commits, which has changed the way the requirements are installed.

## 📸 Demonstration

![Screenshot of the system functionalities](https://drive.google.com/uc?id=1O9dbrjhsDf2ot9iPnLNrOW3Pp52yb6mi)

## ✅ Features

- ✅ Register people  
- ✅ List people  
- ✅ Delete people  
- ✅ Graphical interface  
- ❌ Edit people (Coming soon)  

## 🛠️ Technologies Used

- Python 3.10.12  
- `tkinter` (standard GUI library in Python)  
- JSON (for data storage)  
- `python-dateutil` (for better date handling)

## 🚀 How to Use

### Clone the project:

```bash
git clone https://github.com/BernardoAlvesBorelli/person-register-python.git
cd person-register-python
```

### (Optional) Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```
### Install Tkinter
Windows

If you're using the official Python installer from python.org, tkinter is included by default.

If you get an error like ModuleNotFoundError: No module named 'tkinter', try reinstalling Python and make sure the "tcl/tk and IDLE" feature is checked.

MacOS

If you installed Python using Homebrew:
```bash
brew install python-tk
```

If using the official installer from python.org, tkinter is usually included. If it's missing:
```bash
brew install python-tk
```

Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3-tk

```

Fedora:
```bash
sudo dnf install python3-tkinter
```

Arch based:
```bash
sudo pacman -S tk
```

### Install requirements:
```bash
.venv/bin/python -m pip install -r requirements.txt # On Windows use: .venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Run project:
```bash
.venv/bin/python main.py # On Windows use: .venv\Scripts\python.exe main.py
```