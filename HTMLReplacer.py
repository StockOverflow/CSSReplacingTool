__author__ = 'Tong'

flags = {'analyst': 'analyst-page home-page ',
         'drawer': 'the-drawer-page ',
         'favour-analyst': 'fol-ana-page ',
         # 'favour-stock': "analyst-page home-page ",
         'homepage': "home-page ",
         # 'search': "analyst-page home-page ",
         'stock': "stock-page home-page ",
         'usersign': 'user-page '}


def replace(filepath, flag):
    replaced_flag = flags.get(flag)
    if replaced_flag is None:
        print(filepath + " was not converted")
        return

    # Open a file
    fo = open(filepath, "r", encoding='utf-8')

    line = fo.readline()
    lines = ""

    while line:
        start = line.find("class=\"")
        if start != -1:
            line = line[:start + 7] + replaced_flag + line[start + 7:]
        lines += line
        line = fo.readline()

    # Close opened file
    fo.close()

    fo = open(filepath, "w", encoding='utf-8')
    fo.write(lines)
    fo.close()

    print(filepath + " converted successfully.")