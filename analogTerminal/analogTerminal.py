import os
import socket


class Main:
    def __init__(self):
        self.command = ""
        self.commandList = []

    def splitCommand(self):
        """
        将命令拆分为参数列表
        """
        # 移除command中出现在结尾的空格
        self.command = self.command.rstrip()
        # 将command 拆分为参数列表
        self.commandList = self.command.split(" ")

    def cd(self):
        """
        改变当前目录
        :return: none
        """
        if len(self.commandList) == 2:
            os.chdir(self.commandList[1])
        else:
            raise Exception("参数错误")

    @staticmethod
    def pwd():
        """
        打印当前目录
        :return: none
        """
        print(os.getcwd())

    def rm(self):
        """
        删除文件
        :return: none
        """
        if len(self.commandList) == 2:
            os.remove(self.commandList[1])
        else:
            raise Exception("参数错误")

    def echo(self):
        """
        打印命令行
        :return: none
        """
        if len(self.commandList) == 2:
            print(self.commandList[1])
        else:
            raise Exception("参数错误")

    @staticmethod
    def ls():
        """
        打印当前目录下的文件
        :return: none
        """
        print(os.listdir())

    def mkdir(self):
        """
        创建目录
        :return: none
        """
        if len(self.commandList) == 2:
            os.mkdir(self.commandList[1])
        else:
            raise Exception("参数错误")

    def rmdir(self):
        """
        删除目录
        :return: none
        """
        if len(self.commandList) == 2:
            os.rmdir(self.commandList[1])
        else:
            raise Exception("参数错误")

    def vim(self):
        """
        打开vim
        :return: none
        """
        if len(self.commandList) == 2:
            os.system("vim " + self.commandList[1])
        else:
            raise Exception("参数错误")

    def find(self):
        """
        查找文件
        :return: none
        """
        if len(self.commandList) == 2:
            os.system("find " + self.commandList[1])
        else:
            raise Exception("参数错误")

    def mv(self):
        """
        移动文件
        :return: none
        """
        if len(self.commandList) == 3:
            os.rename(self.commandList[1], self.commandList[2])
        else:
            raise Exception("参数错误")

    def cp(self):
        """
        复制文件
        :return: none
        """
        if len(self.commandList) == 3:
            os.system("cp " + self.commandList[1] + " " + self.commandList[2])
        else:
            raise Exception("参数错误")

    def ps(self):
        """
        打印进程
        :return: none
        """
        if len(self.commandList) == 1:
            os.system("ps")
        else:
            raise Exception("参数错误")

    @staticmethod
    def kill():
        """
        杀死进程
        :return: none
        """
        print("在你熟练掌握zsh之前，请不要杀死未知的进程，否则可能会导致未知的错误")

    @staticmethod
    def sudo():
        """
        执行sudo命令
        :return: none
        """
        print("在你熟练掌握zsh前，请不要使用sudo命令，否则你的系统可能会被攻击")

    def python3(self):
        """
        执行python3
        :return: none
        """
        if len(self.commandList) == 2:
            os.system("python3 " + self.commandList[1])
        else:
            raise Exception("参数错误")

    def help(self):
        """
        打印帮助信息
        :return: none
        """
        if len(self.commandList) == 1:
            print("""
help: 打印帮助信息
exit: 退出程序
cd: 改变当前目录 -- 参数: 目录名
pwd: 打印当前目录 
ls: 打印当前目录下的文件 
mkdir: 创建目录 -- 参数: 目录名
vim: 打开vim -- 参数: 文件名
find: 查找文件 -- 参数: 文件名
mv: 移动文件 -- 参数: 文件名, 目录名
cp: 复制文件 -- 参数: 文件名, 目录名
ps: 打印进程
kill: 杀死进程  
python3: 使用python3执行python脚本 -- 参数: 文件名
WARNING：在你打算删除文件时，请务必加上参数，否则会删除当前目录下的所有文件
以下命令十分危险，请谨慎使用
rm: 删除文件 -- 参数: 文件名
rmdir: 删除目录 -- 参数: 目录名
sudo: 以管理员身份执行命令 -- 参数: 命令
kill: 杀死进程 -- 参数: 进程号
""")
        else:
            raise Exception("参数错误")

    def exit(self):
        """
        退出程序
        :return: none
        """
        if len(self.commandList) == 1:
            exit()
        else:
            raise Exception("参数错误")

    def run(self, userCommand):
        """
        执行命令, 并返回执行结果
        :param userCommand: str
        :return: none
        """
        try:
            self.command = userCommand
            self.splitCommand()
            # 如果用户按下回车键, 则不执行任何命令
            if userCommand == "":
                return
            elif self.commandList[0] == "help":
                self.help()
            elif self.commandList[0] == "exit":
                self.exit()
            elif self.commandList[0] == "cd":
                self.cd()
            elif self.commandList[0] == "pwd":
                self.pwd()
            elif self.commandList[0] == "rm":
                self.rm()
            elif self.commandList[0] == "echo":
                self.echo()
            elif self.commandList[0] == "ls":
                self.ls()
            elif self.commandList[0] == "mkdir":
                self.mkdir()
            elif self.commandList[0] == "rmdir":
                self.rmdir()
            elif self.commandList[0] == "vim":
                self.vim()
            elif self.commandList[0] == "find":
                self.find()
            elif self.commandList[0] == "sudo":
                self.sudo()
            elif self.commandList[0] == "mv":
                self.mv()
            elif self.commandList[0] == "cp":
                self.cp()
            elif self.commandList[0] == "ps":
                self.ps()
            elif self.commandList[0] == "kill":
                self.kill()
            elif self.commandList[0] == "python3":
                self.python3()
            else:
                print("未知命令，请输入help查看帮助，或者输入exit退出程序。在你熟练掌握zsh之前，请不要输入其他命令。")
        except Exception as error:
            print(error)


# 获得用户IP地址
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("114.114.114.114", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    main = Main()
    while True:
        command = input("{}@{}$ ".format(os.getlogin(), get_host_ip()))
        main.run(command)
