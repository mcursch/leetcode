import os



def traverse_directory(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            if '-' in dirname and 'site-packages' not in dirname and 'pip' not in dirname:
                number = dirname.split(' ')[0]
                if len(number) < 5:
                    new_number = number
                    if int(number) < 100:
                        new_number = new_number = '000' + number
                    if 100 <= int(number) < 1000:
                        new_number = '00' + number
                    if 1000 <= int(number) < 10000:
                        new_number = '0' + number
                    arr_name = dirname.split(' ')
                    arr_name[0] = new_number
                    new_name = ' '.join(arr_name)
                    os.rename(dirname, new_name)



    # for filename in filenames:
        #     if '000' in filename:
        #         pass
        #     else:
        #         number = filename.split(' ')
        #         print(number)

traverse_directory('dirname')