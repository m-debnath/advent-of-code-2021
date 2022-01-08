import os
from pathlib import Path

module_name = input("Enter Module Name: ")
print(module_name)

Path(os.path.join(os.getcwd(), "input/" + module_name)).mkdir(parents=True, exist_ok=True)
with open(os.path.join(os.getcwd(), "input/" + module_name, "example.txt"), "w") as f:
    f.write("\n")
with open(os.path.join(os.getcwd(), "input/" + module_name, "puzzle.txt"), "w") as f:
    f.write("\n")
Path(os.path.join(os.getcwd(), "src/" + module_name)).mkdir(parents=True, exist_ok=True)
with open(os.path.join(os.getcwd(), "src/" + module_name, module_name + "_part1.py"), "w") as f:
    f.write("pass\n")
with open(os.path.join(os.getcwd(), "src/" + module_name, module_name + "_part2.py"), "w") as f:
    f.write("pass\n")