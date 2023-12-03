import re
import os

main_path = os.getcwd()
main_path_formattable = main_path + "\\%s"

folders = [folder_name for folder_name in os.listdir(main_path) if re.match(r"\d*\-day\-.*", folder_name)]

for folder in folders:
    print(f"{' '.join(folder.split('-')[1:]).replace('-', ' ').upper():=^35s}")
    module = __import__(folder, fromlist=[folder])
    day = getattr(module, folder)
    os.chdir(main_path_formattable % folder)
    day.solve()
    os.chdir(main_path)
    print()
