import sys


class Main:
    def __init__(self):
        with open('./level.dat', 'r') as f:
            self.level = int(f.read())  # 当前关卡
            self.debug = False  # 是否调试
            # 设定debug为在终端中执行命令的参数，该参数需要为True或False，如果都不是，则默认为False
            if len(sys.argv) > 1:
                if sys.argv[1] == 'True':
                    self.debug = True
                else:
                    self.debug = False

    def run(self):
        # 开始游戏
        print('欢迎来到zshMaster')
        if self.debug:
            self.level = 1  # 从头调试
        print('当前关卡：', self.level)
        # 根据当前变量值打开对应的python文件
        while True:
            try:
                exec('import level%d.main' % self.level)
                exec('level{0}.main.Main().run({1})'.format(self.level, self.debug))
                if self.debug:
                    print('执行level%d.main' % self.level)
                self.level += 1
                with open('./level.dat', 'w') as f:
                    f.write(str(self.level))
            except ModuleNotFoundError:
                if self.debug:
                    print('缺失level%s' % self.level)
                break
            except FileNotFoundError:
                if self.debug:
                    print('缺失level%s/main文件' % self.level)
                break
            except Exception as error:
                print(error)
        print('游戏结束')


main = Main()
main.run()
