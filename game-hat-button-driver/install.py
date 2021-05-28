#!/usr/bin/env python3
import os, sys
import time

errors = []

avaiable_options = ['-h', '--help', '--no-dep']

usage = '''
Usage:
    sudo python3 install.py [option]

Options:
               --no-dep    Do not download dependencies
    -h         --help      Show this help text and exit
'''
def install():
    options = []
    if len(sys.argv) > 1:
        options = sys.argv[1:]
        for o in options:
            if o not in avaiable_options:
                print("Option {} is not found.".format(o))
                print(usage)
                quit()
    if "-h" in options or "--help" in options:
        print(usage)
        quit()
    print("<name> installation start")
    print("Install dependency")
    if "--no-dep" not in options:
        do(msg="update apt-get",
            cmd='run_command("sudo apt-get update")')
        do(msg="install pip",
            cmd='run_command("sudo apt-get install python3-pip -y")')

        do(msg="install python-uinput",
            cmd='run_command("sudo pip3 install python-uinput")')
        do(msg="install RPi.GPIO",
            cmd='run_command("sudo pip3 install RPi.GPIO")')

    # print("Setup screen")
    # do(msg="enable HDMI force hotplug",
    #     cmd='Config().set("hdmi_drive", "2")')
    # do(msg="set HDMI group",
    #     cmd='Config().set("hdmi_group", "2")')
    # do(msg="set HDMI mode",
    #     cmd='Config().set("hdmi_mode", "87")')
    # do(msg="set HDMI resolution",
    #     cmd='Config().set("hdmi_cvt", "800 480 30 6 0 0 0")')

    print("Setup service")
    do(msg="copy service file",
        cmd='run_command("sudo cp ./gpio-joystick /etc/init.d/gpio-joystick")')
    do(msg="add excutable mode for gpio-joystick",
        cmd='run_command("sudo chmod 777 /etc/init.d/gpio-joystick")')
    do(msg="update service settings for gpio-joystick",
        cmd='run_command("sudo update-rc.d gpio-joystick defaults")')
    do(msg="copy excutable",
        cmd='run_command("sudo cp ./gpio-joystick.py /usr/bin/gpio-joystick")')
    do(msg="add excutable mode for gpio-joystick-service",
        cmd='run_command("sudo chmod +x /usr/bin/gpio-joystick")')

    if len(errors) == 0:
        while True:
            yesno = input("Installation finished, do you want to reboot? (y/N) ")
            yesno = str(yesno).lower()
            if yesno == "y":
                for i in range(5):
                    print("Reboot in %s sec"%(5-i))
                    time.sleep(1)
                run_command("reboot")
            elif yesno == "n":
                print("Finished.")
                break
            else:
                print('Input error, type "Y" to reboot, or "N" to cancel, try again.')
                continue
    else:
        print("\n\nError happened in install process:")
        for error in errors:
            print(error)
        print("Try to fix it yourself, or contact service@sunfounder.com with this message")


def cleanup():
    pass

class Modules(object):
    ''' 
        To setup /etc/modules
    '''

    def __init__(self, file="/etc/modules"):
        self.file = file
        with open(self.file, 'r') as f:
            self.configs = f.read()
        self.configs = self.configs.split('\n')

    def remove(self, expected):
        for config in self.configs:
            if expected in config:
                self.configs.remove(config)
        return self.write_file()

    def set(self, name):
        have_excepted = False
        for i in range(len(self.configs)):
            config = self.configs[i]
            if name in config:
                have_excepted = True
                tmp = name
                self.configs[i] = tmp
                break

        if not have_excepted:
            tmp = name
            self.configs.append(tmp)
        return self.write_file()

    def write_file(self):
        try:
            config = '\n'.join(self.configs)
            # print(config)
            with open(self.file, 'w') as f:
                f.write(config)
            return 0, config
        except Exception as e:
            return -1, e

class Config(object):
    ''' 
        To setup /boot/config.txt
    '''

    def __init__(self, file="/boot/config.txt"):
        self.file = file
        with open(self.file, 'r') as f:
            self.configs = f.read()
        self.configs = self.configs.split('\n')

    def remove(self, expected):
        for config in self.configs:
            if expected in config:
                self.configs.remove(config)
        return self.write_file()

    def set(self, name, value=None):
        have_excepted = False
        for i in range(len(self.configs)):
            config = self.configs[i]
            if name in config:
                have_excepted = True
                tmp = name
                if value != None:
                    tmp += '=' + value
                self.configs[i] = tmp
                break

        if not have_excepted:
            tmp = name
            if value != None:
                tmp += '=' + value
            self.configs.append(tmp)
        return self.write_file()

    def write_file(self):
        try:
            config = '\n'.join(self.configs)
            # print(config)
            with open(self.file, 'w') as f:
                f.write(config)
            return 0, config
        except Exception as e:
            return -1, e

class Cmdline(object):
    ''' 
        To setup /boot/cmdline.txt
    '''

    def __init__(self, file="/boot/cmdline.txt"):
        self.file = file
        with open(self.file, 'r') as f:
            cmdline = f.read()
        self.cmdline = cmdline.strip()
        self.cmds = self.cmdline.split(' ')

    def remove(self, expected):
        for cmd in self.cmds:
            if expected in cmd:
                self.cmds.remove(cmd)
        return self.write_file()

    def write_file(self):
        try:
            cmdline = ' '.join(self.cmds)
            # print(cmdline)
            with open(self.file, 'w') as f:
                f.write(cmdline)
            return 0, cmdline
        except Exception as e:
            return -1, e


def run_command(cmd=""):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    status = p.poll()
    # print(result)
    # print(status)
    return status, result


def do(msg="", cmd=""):
    print(" - %s..." % (msg), end='\r')
    print(" - %s... " % (msg), end='')
    status, result = eval(cmd)
    # print(status, result)
    if status == 0 or status == None or result == "":
        print('Done')
    else:
        print('Error')
        errors.append("%s error:\n  Status:%s\n  Error:%s" %
                      (msg, status, result))

if __name__ == "__main__":
    try:
        install()
    except KeyboardInterrupt:
        print("Canceled.")
        cleanup()

# if __name__ == "__main__":
#     test()
