
import sys

def hexToRGB(str):
    r = int(str[1:3], 16)
    g = int(str[3:5], 16)
    b = int(str[5:7], 16)
    return f"{r},{g},{b}"

colours = ["" for i in range(0, 22)]

input_file = open(sys.argv[1], "rt")
input_file.close()

output = "\n"
output += "Windows Registry Editor Version 5.00\n"
output += "\n"
output += "[HKEY_CURRENT_USER\\Software\\SimonTatham\\PuTTY\\Sessions\\Default%20Settings]\n"
output += "\"Colour0\"=\""+hexToRGB(colours[0])+"\"\n"
output += "\"Colour1\"=\""+hexToRGB(colours[1])+"\"\n"
output += "\"Colour2\"=\""+hexToRGB(colours[2])+"\"\n"
output += "\"Colour3\"=\""+hexToRGB(colours[3])+"\"\n"
output += "\"Colour4\"=\""+hexToRGB(colours[4])+"\"\n"
output += "\"Colour5\"=\""+hexToRGB(colours[5])+"\"\n"
output += "\"Colour6\"=\""+hexToRGB(colours[6])+"\"\n"
output += "\"Colour7\"=\""+hexToRGB(colours[7])+"\"\n"
output += "\"Colour8\"=\""+hexToRGB(colours[8])+"\"\n"
output += "\"Colour9\"=\""+hexToRGB(colours[9])+"\"\n"
output += "\"Colour10\"=\""+hexToRGB(colours[10])+"\"\n"
output += "\"Colour11\"=\""+hexToRGB(colours[11])+"\"\n"
output += "\"Colour12\"=\""+hexToRGB(colours[12])+"\"\n"
output += "\"Colour13\"=\""+hexToRGB(colours[13])+"\"\n"
output += "\"Colour14\"=\""+hexToRGB(colours[14])+"\"\n"
output += "\"Colour15\"=\""+hexToRGB(colours[15])+"\"\n"
output += "\"Colour16\"=\""+hexToRGB(colours[16])+"\"\n"
output += "\"Colour17\"=\""+hexToRGB(colours[17])+"\"\n"
output += "\"Colour18\"=\""+hexToRGB(colours[18])+"\"\n"
output += "\"Colour19\"=\""+hexToRGB(colours[19])+"\"\n"
output += "\"Colour20\"=\""+hexToRGB(colours[20])+"\"\n"
output += "\"Colour21\"=\""+hexToRGB(colours[21])+"\"\n"

output_name = sys.argv[1].split(".")[0] + "_PuTTY.reg"

