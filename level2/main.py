class Main:
    def __init__(self):
        pass

    @staticmethod
    def run(debug):
        print("Hello World!")
        if debug:
            print("Level 2: Debug Mode")
        input("Press Enter to continue...")


if __name__ == '__main__':
    main = Main()
    main.run(True)
