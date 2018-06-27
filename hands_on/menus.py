#!python2
# -*-utf8-*-

class Command(object):
    """docstring for Command"""
    name = 'nothing'

    def __init__(self, name):
        super(Command, self).__init__()
        self.name = name
        
    def execute() :
        pass

class MenuInvoker(object):
    """MenuInvoker class holds slots of Command object, works for invoking these command per request"""
    slots = []

    def __init__(self):
        super(MenuInvoker, self).__init__()
        command = Command("Exit")
        def exit0() :
            print 'exiting...'
            exit()
        command.execute = exit0
        self.slots.append(command)
    
    def addCommand(self, command) :
        self.slots.append(command)

    def start(self) :
        while True:
            print('------------------menus------------------')
            for (i, c) in enumerate(self.slots):
                print(str(i) + '\t' + c.name)

            try:
                inStr = input("Select one item to execute:")
                inInt = int(inStr)
                if (inInt < 0) or (inInt >= len(self.slots)) :
                    print("Invalid selection!")
                else :
                    self.slots[inInt].execute()
                    print("Item " + inStr + " finished!")
                print('')
            except Exception:
                # print e
                exit()

if __name__ == '__main__':
    try:
        import __builtin__
        input = getattr(__builtin__, 'raw_input')
    except (ImportError, AttributeError):
        pass
    
    #main()
    invoker = MenuInvoker()

    # no param command
    command1 = Command('print hello world')
    def printHelloWorld():
        print 'Hello World!'
    command1.execute = printHelloWorld
    invoker.addCommand(command1)

    # command with param
    command2 = Command('a method with parameter')
    def parameterizedMethod():
        param = raw_input('  please input a param->')
        print 'You just input ' + param
    command2.execute = parameterizedMethod
    invoker.addCommand(command2)

    invoker.start()