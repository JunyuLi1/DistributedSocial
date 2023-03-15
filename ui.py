# ui.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
"""Module for ui"""
import pathlib
from Profile import *
import ds_client
import LastFM
import OpenWeather
run = False


def menu():
    """Print the menu of instruction."""
    print('\n----------------------------------------------')
    print('Welcome to the file operator.\n')
    print('This operator allows you to do following things:')
    print('\tL: List the contents of the user specified directory.')
    print('\tC: Create a new DSU file with a specified name.')
    print('\tD: Delete a DSU file.')
    print('\tR: Read the content of a DSU file.')
    print('\tQ :Quit the program.')
    print('\tO :Load a DSU file')
    print('\tV: Publish your DSU file journal online.')
    print('If you want to add a post with information '
          'received from WebAPI by @keywords, '
          'please use E loaded by C or O first.')
    print('@keywords will be converted and store '
          'locally and then post online.\n')


def start():
    """Receive the user input and process input"""
    try:
        user_input = input('Please select from [L,C,D,R,Q,O,V]: ')
        assert user_input in ('admin', 'L', 'C', 'D', 'R', 'Q', 'O', 'V')
        return user_input
    except AssertionError:
        print('You select an invalid option, please try again.')


def deter_path(input_lis):
    """Determine a valid path."""
    try:
        assert input_lis[1][len(input_lis[1])-1] != ' '
        path = pathlib.Path(input_lis[1])
        assert path.exists()
        return path
    except AssertionError:
        pass


def path_interact(user_command):
    """Process further command for L."""
    user_input_path = input('Please type a path: ')
    if len(user_input_path) == 0:
        print('In valid path, please try again.\n')
        return path_interact(user_command)
    else:
        inp_lis = [user_command, user_input_path]
        user_input_path = deter_path(inp_lis)
        if user_input_path is not None:
            return inp_lis
        else:
            print('You entered an invalid path, please try again.\n')
            return path_interact(user_command)


def L_option_interact(inp_lis):
    """Ask user for option."""
    try:
        user_option = input('Do you prefer to enter a further option?(Y/N): ')
        assert user_option in ('Y', 'N', 'admin')
        if user_option == 'Y':
            L_option_menu()
            inp_lis = L_option2(inp_lis)
            return inp_lis
        if user_option == 'N':
            return inp_lis
    except AssertionError:
        print('Invalid choice, please enter again.\n')
        L_option_interact(inp_lis)


def L_option_menu():
    """Print menu"""
    print('\n-r: Output directory content recursively.')
    print('\t(You can add -r before following)')
    print('-f: Output only files, excluding directories in the results.')
    print('-s: Output only files that match a given file name.')
    print('-e: Output only files that match a given file extension.\n')


def L_option2(inp_lis):
    """Run L option"""
    try:
        if len(inp_lis) >= 4:
            raise ValueError
        user_option = input('Please enter an option: ')
        assert user_option in ('-r', '-f', '-s', '-e', 'admin')
        if user_option == '-r' and len(inp_lis) < 3:
            user_option3 = input('Do you want a further option?(Y/N): ')
            assert user_option3 in ('Y', 'N', 'admin')
            if user_option3 == 'Y':
                inp_lis.append(user_option)
                L_option2(inp_lis)
                return inp_lis
            elif user_option3 == 'N':
                inp_lis.append(user_option)
                return inp_lis
        elif len(inp_lis) <= 4 and user_option != '-r':
            if user_option != 'admin':
                inp_lis.append(user_option)
                return inp_lis
        else:
            raise AssertionError
    except AssertionError:
        print('Invalid option, please enter again.')
        print('If you already type "-r", please do not type again.\n')
        L_option_interact(inp_lis)
        return inp_lis
    except ValueError:
        return inp_lis


def L_rest():
    """Add -e or -s rest information."""
    user_input = input('Please enter a file name or file extension: ')
    return user_input


def C_interact(inp_lis):
    """Add filename to the list"""
    user_input = input('Please enter a file name that you want to create: ')
    inp_lis.append(user_input)
    return inp_lis


def C_O_further(path):
    """Process E AND P"""
    user_inpt = input('Type E(Edit) or P(Print) or V to publish online: ')
    if user_inpt == 'E':
        print('\nHere are some options:\n')
        print('\t1-usr: Add username.')
        print('\t2-pwd: Set password.')
        print('\t3-bio: Add bio.')
        print('\t4-addpost: Add post.')
        print('\t5-delpost: Delete post.')
        print('\t6-Finish choosing.\n')
        user_dic = {}
        while True:
            user_inpt2 = input('Please select number from 1-6:')
            if user_inpt2 == '1':
                user_inpt3 = input('Please enter username: ')
                if ' ' in user_inpt3 or len(user_inpt3) == 0:
                    print('Empty string or whitespace in string.')
                else:
                    user_dic['-usr'] = user_inpt3
            if user_inpt2 == '2':
                user_inpt3 = input('Please enter password: ')
                if ' ' in user_inpt3 or len(user_inpt3) == 0:
                    print('Empty string or whitespace in string.')
                else:
                    user_dic['-pwd'] = user_inpt3
            if user_inpt2 == '3':
                user_inpt3 = input('Please enter bio: ')
                if len(user_inpt3) == 0:
                    print('Empty string.')
                elif user_inpt3.isspace():
                    print('Only a whitespace.')
                else:
                    user_dic['-bio'] = user_inpt3
            if user_inpt2 == '4':
                user_input4 = input('Do you want to add information '
                                    'received from WebAPI?(Y/N): ')
                if user_input4 == 'Y':
                    print('\nYou can include two '
                          'WebAPI keywords')
                    print('\t@weather - receive weather '
                          'information from OpenWeather Website.')
                    print('\t@lastfm - receive top music\'s tags'
                          ' from Lastfm Website.')
                    print('For example, you can enter:"It is '
                          '@weather outside and I am thrilled!"\n')
                user_inpt3 = input('Please enter post: ')
                if len(user_inpt3) == 0:
                    print('Empty string.')
                elif user_inpt3.isspace():
                    print('Only a whitespace.')
                else:
                    if '@weather' in user_inpt3 or '@lastfm' in user_inpt3:
                        user_inpt3 = process_message(user_inpt3)
                    user_dic['-addpost'] = user_inpt3
            if user_inpt2 == '5':
                obj = Profile()
                obj.load_profile(path)
                post = obj.get_posts()
                if len(post) > 0:
                    id = 1
                    for item in post:
                        print(id, item)
                        id += 1
                    user_inpt3 = input('Please enter id: ')
                    if user_inpt3.isdigit() and int(user_inpt3) < len(post)+1:
                        user_dic['-delpost'] = user_inpt3
                    else:
                        print('Entered a wrong id.')
                else:
                    print('No post need to be deleted.')
            if user_inpt2 == '6':
                return user_dic
    if user_inpt == 'P':
        print('\nHere are some options:\n')
        print('\t1-usr: Print username.')
        print('\t2-pwd: Print password.')
        print('\t3-bio: Print bio.')
        print('\t4-posts: Print all post.')
        print('\t5-post: Print post given the id.')
        print('\t6-all: Print all in DSU file.')
        print('\t7-Finish choosing.\n')
        user_list = []
        while True:
            user_inpt2 = input('Please select number from 1-7:')
            if user_inpt2 == '1':
                user_list.append('-usr')
            if user_inpt2 == '2':
                user_list.append('-pwd')
            if user_inpt2 == '3':
                user_list.append('-bio')
            if user_inpt2 == '4':
                user_list.append('-posts')
            if user_inpt2 == '5':
                dic = {}
                obj = Profile()
                obj.load_profile(path)
                post = obj.get_posts()
                if len(post) > 0:
                    id = 1
                    for item in post:
                        print(id, ':', item)
                        id += 1
                    user_inpt3 = input('Please enter id: ')
                    if user_inpt3.isdigit() and int(user_inpt3) < len(post)+1:
                        dic['-post'] = user_inpt3
                        user_list.append(dic)
                    else:
                        print('Entered a wrong id.')
                else:
                    print('No post.')
            if user_inpt2 == '6':
                user_list.append('-all')
            if user_inpt2 == '7':
                return user_list
    if user_inpt == 'V':
        user_str = 'Online'
        return user_str


def L_command(inp_lis):
    """Process L command."""
    global run
    try:
        if len(inp_lis) == 2:
            sort_path_list = []
            for item in pathlib.Path(inp_lis[1]).iterdir():
                if item.is_file():
                    print(item)
                else:
                    sort_path_list.append(item)
            for rest in sort_path_list:
                print(rest)
        elif len(inp_lis) == 3:
            if inp_lis[2] == '-r':
                print_recursion(pathlib.Path(inp_lis[1]))
            if inp_lis[2] == '-f':
                for item in pathlib.Path(inp_lis[1]).iterdir():
                    if item.is_file():
                        print(item)
        elif len(inp_lis) == 4:
            if inp_lis[2] == '-s':
                s_option(inp_lis)
            if inp_lis[2] == '-e':
                e_option(inp_lis)
            if inp_lis[3] == '-f':
                print_recursion_two(pathlib.Path(inp_lis[1]))
        elif len(inp_lis) == 5:
            if inp_lis[3] == '-s':
                s_option_two(inp_lis, pathlib.Path(inp_lis[1]))
                if run is False:
                    raise AssertionError
                run = False
            if inp_lis[3] == '-e':
                e_option_two(inp_lis, pathlib.Path(inp_lis[1]))
                if run is False:
                    raise AssertionError
                run = False
    except AssertionError:
        print('Cannot find the file.')


def print_recursion(re_path):
    """Run -r option."""
    sort_path_list = []
    for item in re_path.iterdir():
        if item.is_file():
            print(item)
        else:
            sort_path_list.append(item)
    for rest in sort_path_list:
        print(rest)
        print_recursion(rest)


def print_recursion_two(re_path_two):
    """Run -f based on -r option."""
    sort_path_list = []
    for item in re_path_two.iterdir():
        if item.is_file():
            print(item)
        else:
            sort_path_list.append(item)
    for rest in sort_path_list:
        print_recursion_two(rest)


def s_option(inpu_lis):
    """Run the function for -s option."""
    count = 0
    for item in pathlib.Path(inpu_lis[1]).iterdir():
        if item.name == inpu_lis[3]:
            print(item)
            count += 1
    if count == 0:
        raise AssertionError


def e_option(re_list):
    """Run the function for -e option."""
    count = 0
    for item in pathlib.Path(re_list[1]).iterdir():
        if item.suffix == f'.{re_list[3]}':
            print(item)
            count += 1
    if count == 0:
        raise AssertionError


def s_option_two(re_list, re_path):
    """Run the function for -s based on -r option."""
    global run
    sort_path_list = []
    for item in re_path.iterdir():
        if item.name == re_list[4] and not item.is_dir():
            print(item)
            run = True
        elif item.is_dir():
            sort_path_list.append(item)
    for rest in sort_path_list:
        s_option_two(re_list, rest)


def e_option_two(re_list, re_path):
    """Run the function for -e based on -r."""
    global run
    sort_path_list = []
    for item in re_path.iterdir():
        if item.suffix == f'.{re_list[4]}' and not item.is_dir():
            run = True
            print(item)
        elif item.is_dir():
            sort_path_list.append(item)
    for rest in sort_path_list:
        e_option_two(re_list, rest)


def C_command(inp_lis):
    """Process C command."""
    try:
        ne_path = f'{inp_lis[1]}/{inp_lis[2]}.dsu'
        if pathlib.Path(ne_path).exists():
            O_command(ne_path)
        else:
            username1 = input('Please enter a username: ')
            assert ' ' not in username1
            assert len(username1) > 0
            password1 = input('Please enter a password: ')
            assert ' ' not in password1
            assert len(password1) > 0
            bio1 = input('Please enter your bio: ')
            assert len(bio1) > 0
            if bio1.isspace():
                raise AssertionError
            dsuserver1 = input('Please enter a server ip address: ')
            assert len(dsuserver1) > 0
            if ' ' in dsuserver1:
                raise AssertionError
            pathlib.Path(ne_path).touch()
            print(pathlib.Path(ne_path), 'CREATED')
            obj = Profile(dsuserver=dsuserver1,
                          username=username1, password=password1)
            obj.bio = bio1
            obj.save_profile(ne_path)
            result = C_O_further(ne_path)
            print(result)
            if type(result) is dict:
                E_command(result, ne_path)
            if type(result) is list:
                P_command(result, ne_path)
            if type(result) is str:
                user_input2 = input('Do you want to publish '
                                    'bio and post together?(Y/N): ')
                if user_input2 == 'Y':
                    publish_together(ne_path)
                else:
                    print('\n1.Publish a post')
                    print('2.Publish a bio')
                    user_input3 = input('Please select a number: ')
                    if user_input3 == '1':
                        publish_change_post(ne_path)
                    else:
                        publish_bio(ne_path)  # call publish online
    except AssertionError:
        print('Cannot enter whitespace for username, password or dsuserver.')
        print('Or you cannot only type a whitespace for bio.\n')
        while True:
            user_option = input('Do you want to try again?(Y/N): ')
            if user_option == 'Y':
                return C_command(inp_lis)
            if user_option == 'N':
                return None


def D_command(inp_lis):
    """Process with D command."""
    try:
        if pathlib.Path(inp_lis[1]).suffix != '.dsu':
            raise AssertionError
        else:
            pathlib.Path(inp_lis[1]).unlink()
            print(f'{inp_lis[1]} DELETED')
    except AssertionError:
        print('You did not specify a correct DSU file.')
        while True:
            user_option = input('Do you want to try again?(Y/N): ')
            if user_option == 'Y':
                inp_lis = path_interact(user_command='D')
                return D_command(inp_lis)
            if user_option == 'N':
                return None


def R_command(inp_lis):
    """Process with R command."""
    try:
        if pathlib.Path(inp_lis[1]).suffix != '.dsu':
            raise AssertionError
        else:
            if pathlib.Path(inp_lis[1]).stat().st_size == 0:
                print('EMPTY')
            else:
                file = open(inp_lis[1], 'r')
                content = file.readlines()
                newlis = []
                for item in content:
                    newlis.append(item.strip('\n'))
                for item in newlis:
                    print(item)
                file.close()
    except AssertionError:
        print('You did not specify a correct DSU file.')
        while True:
            user_option = input('Do you want to try again?(Y/N): ')
            if user_option == 'Y':
                inp_lis = path_interact(user_command='D')
                return R_command(inp_lis)
            if user_option == 'N':
                return None


def E_command(inp_dic, inp_path):
    """Run E command"""
    obj = Profile()
    obj.load_profile(inp_path)
    try:
        if '-usr' in inp_dic:
            username1 = inp_dic['-usr']
            obj.username = username1
            obj.save_profile(inp_path)
        if '-pwd' in inp_dic:
            password1 = inp_dic['-pwd']
            obj.password = password1
            obj.save_profile(inp_path)
        if '-bio' in inp_dic:
            bio1 = inp_dic['-bio']
            obj.bio = bio1
            obj.save_profile(inp_path)  # change bio
        if '-addpost' in inp_dic:
            addpost1 = inp_dic['-addpost']
            new_post = Post(entry=addpost1)
            obj.add_post(new_post)
            obj.save_profile(inp_path)  # post online
        if '-delpost' in inp_dic:
            delpost1 = inp_dic['-delpost']
            post = obj.get_posts()
            if delpost1.isdigit() and int(delpost1) < len(post)+1:
                del post[int(delpost1)-1]
            else:
                raise ValueError
            obj.save_profile(inp_path)
    except ValueError:
        print('ERROR OF ID')
        C_O_further(inp_path)
    else:
        print('You command is correctly implemented.\n')
        if '-bio' not in inp_dic:
            publish_change_post(inp_path)
        if '-bio' in inp_dic:
            user_input2 = input('Do you want to publish bio'
                                ' and post together?(Y/N): ')
            if user_input2 == 'Y':
                publish_together(inp_path)
            else:
                print('1.Publish a post')
                print('2.Publish a bio')
                user_input3 = input('Please select a number: ')
                if user_input3 == '1':
                    publish_change_post(inp_path)
                else:
                    publish_bio(inp_path)


def P_command(inp_lis, path):
    """Run P command"""
    obj = Profile()
    obj.load_profile(path)
    for item in inp_lis:
        if type(item) is not dict:
            if item == '-usr':
                print('username:', obj.username)
            if item == '-pwd':
                print('password:', obj.password)
            if item == '-bio':
                print('bio', obj.bio)
            if item == '-posts':
                lis = obj.get_posts()
                id = 1
                for item in lis:
                    print(id, ':', item)
                    id += 1
            if item == '-all':
                print('username:', obj.username)
                print('password:', obj.password)
                print('bio', ':', obj.bio)
                lis = obj.get_posts()
                id = 1
                for item in lis:
                    print(id, ':', item)
                    id += 1
        else:
            id = int(item['-post'])
            print(obj.get_posts()[id-1])
    print('Implemented\n')
    user_input5 = input('Do you want to post online?(Y/N): ')
    if user_input5 == 'Y':
        print('What do you want to do?:')
        print('1.Publish a post')
        print('2.Post a bio')
        print('3.Publish post and bio together')
        user_input3 = input('Please select a number: ')
        if user_input3 == '1':
            publish_change_post(path)
        if user_input3 == '2':
            publish_bio(path)
        if user_input3 == '3':
            publish_together(path)
    else:
        pass


def O_command(in_path):
    """Run O command"""
    try:
        if pathlib.Path(in_path).suffix != '.dsu':
            raise AssertionError
        obj = Profile()
        obj.load_profile(in_path)
    except AssertionError:
        print('Cannot edit or print a non DSU file')
    except DsuProfileError:
        print('DSU file has not a correct format.')
    else:
        print('File exist')
        result = C_O_further(in_path)
        if type(result) is dict:
            E_command(result, in_path)
        if type(result) is list:
            P_command(result, in_path)
        if type(result) is str:
            user_input2 = input('Do you want to publish'
                                ' bio and post together?(Y/N): ')
            if user_input2 == 'Y':
                publish_together(in_path)
            else:
                print('\n1.Publish a post')
                print('2.Publish a bio')
                user_input3 = input('Please select a number: ')
                if user_input3 == '1':
                    publish_change_post(in_path)
                else:
                    publish_bio(in_path)


def publish_change_post(path):
    """Publish online."""
    user_input = input('Do you want publish online?(Y/N): ')
    if user_input == 'Y':
        obj = Profile()
        obj.load_profile(path)
        post = obj.get_posts()
        id = 1
        for item in post:
            print(id, ":", item)
            id += 1
        if len(post) > 0:
            user_input2 = input('Please select a valid id.: ')
            if int(user_input2) > len(post):
                print('You select an invalid id')
            else:
                entry = dict(post[int(user_input2)-1])['entry']
                ip = obj.dsuserver
                name = obj.username
                pwd = obj.password
                ds_client.send(ip, 3021, name, pwd, entry)
        else:
            print('No post in the dsu file.')
    else:
        pass


def publish_bio(path):
    """Publish change of bio."""
    user_input1 = input('Do you want publish online?(Y/N): ')
    if user_input1 == 'Y':
        obj = Profile()
        obj.load_profile(path)
        entry = ''
        ip = obj.dsuserver
        name = obj.username
        pwd = obj.password
        bio = obj.bio
        ds_client.send(ip, 3021, name, pwd, entry, bio)  # just bio
    else:
        pass


def publish_together(path):
    """Publish bio and post together."""
    obj = Profile()
    obj.load_profile(path)
    post = obj.get_posts()
    id = 1
    for item in post:
        print(id, ":", item)
        id += 1
    if len(post) > 0:
        user_input2 = input('Please select a valid id.: ')
        if int(user_input2) > len(post):
            print('You select an invalid id')
        else:
            entry = dict(post[int(user_input2) - 1])['entry']
            ip = obj.dsuserver
            name = obj.username
            pwd = obj.password
            bio = obj.bio
            ds_client.send(ip, 3021, name, pwd, entry, bio)
    else:
        obj = Profile()
        obj.load_profile(path)
        entry = ''
        ip = obj.dsuserver
        name = obj.username
        pwd = obj.password
        bio = obj.bio
        ds_client.send(ip, 3021, name, pwd, entry, bio)


def process_message(message):
    """Transclude messages."""
    if '@weather' in message:
        user_input1 = input('Please enter a zip code(5-digits): ')
        user_input2 = input('Please enter a country code(such as US): ')
        user_input3 = input('Please enter your Openweather WebAPI key\n'
                            'You can also use 03657b48a28c90947a8068f1f2608dfc'
                            ' instead of your own: ')
        open_weather = OpenWeather.OpenWeather(user_input1, user_input2)
        open_weather.set_apikey(user_input3)
        open_weather.load_data()
        new_message = open_weather.transclude(message)
        return process_message(new_message)
    if '@lastfm' in message:
        last_fm = LastFM.LastFM()
        user_input = input('Please enter apikey for lastfm WebAPI\n'
                           'You can also use 9e378b414d40568750b1dcbc42d0d6cd'
                           ' instead of your own: ')
        last_fm.set_apikey(user_input)
        last_fm.load_data()
        new_message = last_fm.transclude(message)
        return process_message(new_message)
    return message
