class Main:
    def __init__(self):
        pass

    @staticmethod
    def run(debug):
        print("Hello World!")
        if debug:
            print("Level: Debug Mode")


if __name__ == '__main__':
    main = Main()
    main.run(True)
