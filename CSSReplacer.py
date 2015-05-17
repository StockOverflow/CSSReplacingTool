__author__ = 'Tong'

flags = {'analyst': '.analyst-page .home-page ',
         'drawer': '.the-drawer-page ',
         'homepage': ".home-page ",
         # 'search': ".analyst-page .home-page ",
         'stock': ".stock-page .home-page ",
         'followed_analysts': ".fol-ana-page ",
         'usersign': '.user-page '}


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
        if line.find('{') != -1:
            if line.find('.inner-wrapper') != -1:
                line = replaced_flag[:-1] + line
            elif line.find('*') == -1 and line.find('body') == -1:
                line = replaced_flag + line
        lines += line
        line = fo.readline()

    # Close opened file
    fo.close()

    fo = open(filepath, "w", encoding='utf-8')
    fo.write(lines)
    fo.close()

    print(filepath + " converted successfully.")
