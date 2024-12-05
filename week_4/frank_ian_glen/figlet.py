import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
if len(sys.argv) == 1:
    output_font = random.choice(figlet.getFonts())

elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    output_font = sys.argv[2]
    if output_font not in figlet.getFonts():
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

figlet.setFont(font = output_font)

usr_input = input("Input: ").strip()
output_usr = figlet.renderText(usr_input)
print(f"Output:  \n{output_usr}")