import re
import os

main_path = os.getcwd() + "\\%s"

# valid folder names follow "#-day-#" that contain a py file with the same names
folders = list(dict(sorted({folder_name: int(folder_name.split('-')[0]) for folder_name in os.listdir(
    main_path % '') if re.match(r'\d*\-day\-.*', folder_name)}.items(), key=lambda x: x[1])).keys())

for folder in folders:
    print(f"{re.sub(r'[^A-Z ]', '', folder.replace('-', ' ').upper()).strip():=^35s}")
    # solution file from the folder
    module = __import__(folder, fromlist=[folder])
    # get the file as module
    day = getattr(module, folder)
    # change dir to that folder (to access data)
    os.chdir(main_path % folder)
    # invoke the solve command for the module
    day.solve()
    # change dir back to the main path
    os.chdir(main_path % '')
    print()
