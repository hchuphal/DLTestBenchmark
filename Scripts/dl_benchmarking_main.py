##############################################################################################
#
# Description : DL Testing Benchmarking Python tool to perform benchmakring tasks
# Input  : models and datasets
# Output :  Output of all 7 tasks
# Usage : python2.7 dl_benchmarking.py
# Author : Himanshu
#
##############################################################################################

# -*- coding: utf-8 -*-
import json, os, re, sys, subprocess
from texttable import Texttable
from collections import OrderedDict
from collections import defaultdict
from subprocess import call
from bunch import Bunch
from time import sleep

import inspect

class Formats:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_input(msg, convert_func):
    try:
        value = raw_input(msg)
        if convert_func is not None:
            value = convert_func(value)
    except ValueError:
        value = None
    return value

def valid_int(number):
    if number.isdigit():
        return number
    else:
        raise ValueError

def get_input(msg, name, validate_func, convert_func=None):
    value = read_input(msg, convert_func)
    while not validate_func(value):
        print "Invalid {}".format(name)
        value = read_input(msg, convert_func)
    return value


def get_base_app_directories():
    import master
    base = inspect.getfile(master).split("scripts/code_generator")[0]
    directories = {
        'BASE': base,
        'SON_INIT': "{}{}".format(base, "dist/debian-init.sh")
    }
    return directories


def str_to_bool(string):
    if string in ['YES', 'Y']:
        return True
    elif string in ['NO', 'N']:
        return False
    else:
        raise ValueError

def valid_apps(apps):
    if len(apps) == 0:
        return True
    return all(map(lambda x: x in app_names, apps))


def string_to_list_of_strings(string):
    if string == '':
        return []
    return map(lambda s: s.strip(), string.split(','))


def map_strings_to_list_of_strings(strings):
    return "'{}'".format("','".join(strings))

def _banner(message):
    table = Texttable()
    table.set_deco(Texttable.BORDER)
    table.add_rows([[message]])
    return table.draw()

# Main function which takes the input like APP or infra and perform the actions accordingly
def main():
    os.system('clear')
    print
    print
    print _banner((Formats.OKGREEN + '\n    DL Testing Tools Benchmarking   \n \n Masters Thesis \n').center(50)) + Formats.ENDC
    print
    print
    _main_menu()

def _main_menu():
    print Formats.WARNING + "Welcome : Input options to run DL benchmakring tasks >> " + Formats.ENDC
    print
    print Formats.WARNING +" Select an option to run Benchmarking method >> " + Formats.ENDC
    print Formats.WARNING + "1. Fill out Tool Run Config >> " + Formats.ENDC
    print Formats.WARNING + "2. Check Tool's Run Config " + Formats.ENDC
    print Formats.WARNING + "3. Install Requirements" + Formats.ENDC
    print Formats.WARNING + "4. Execute Benchmarking Tasks " + Formats.ENDC
    print Formats.WARNING + "5. Benchmakring Tasks Info " + Formats.ENDC
    print Formats.WARNING + "6. Check System Configuration" + Formats.ENDC
    print Formats.WARNING + "7. Check Version of the tool and --Help?" + Formats.ENDC
    print Formats.WARNING + "8. EXIT " + Formats.ENDC
    print
    print

    _option = get_input(Formats.OKGREEN +"Enter an option to run the tool [ 1-8 ] = "+ Formats.ENDC,
                     "Invalid Option, Check menu options and select a valid choice!!",
                     lambda x: x>0,
                     valid_int)

    print Formats.WARNING + " >> Enterted Choice : {}".format(_option) + Formats.ENDC
    _menu = {
        '1' : _edit_config,
        '2' : _check_config,
        '3' :  _install_req,
        '4' : _run_tasks,
        '5' : _check_tasks,
        '6' : _system_config,
        '7' : _help_,
        '8' : _quit
    }

    _menu[_option]()
    print


def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()

def _quit():
    exit(0)

def _install_req():
    os.system('pip install -r requirements.txt')


def _help_():
    command_1 = 'Please run as "python2.7 dl_benchmarking_main.py"'
    #print command_1
    print(command_1)

    command_2 = 'python2.7 --version'
    #print command_1
    print("\nDL Testing Tools Benchmarking Design v 1.0 and Python version Installed: ")
    os.system(command_2)
    _main_menu()


def _check_config():
    print
    print
    os.system('clear')
    print "*" * 50
    print "Check the run Config of the DL testing tool before starting Benchmarking Tasks..."
    sleep(1)
    #os.chdir(r"../../")
    command_1 = 'gvim ./temp/run_config_tool.json'
    #print command_1
    os.system(command_1)

    print "*" * 50
    print
    print
    _main_menu()

def _edit_config():
    print
    print
    os.system('clear')
    print "*" * 50
    print "Edit the run Config of the DL testing tool to Execute Benchmarking Tasks..."
    sleep(1)
    #os.chdir(r"../../")
    command_2 = 'gvim run_config1.json'
    #print command_1
    os.system(command_2)

    print "*" * 50
    print
    print
    _main_menu()



def _run_tasks():
    print
    print
    os.system('clear')
    print "*" * 50
    print "Starting Benchmarking Tasks..."
    sleep(1)
    #os.system('cd ../../')
    #os.chdir(r"../../")
    command_1 = 'python2.7 benchmarking_tasks.py'
    #print command_1
    os.system(command_1)

    print "*" * 50
    print
    print
    _main_menu()


def _system_config():
    print
    print "*" * 50
    command_3 = 'python3.7 system.py'
    os.system(command_3)
    print "*" * 50
    print
    _main_menu()


def _check_tasks():
    print("List of Tasks to be Executed as a part Benchmarking Design :")
    os.system('cat tasks_info.txt')
    _main_menu()


def _run_package_level(_vendor, _tech, _input_file, _input_xml, _module_name):
    pass

if __name__ == '__main__':
    main()


