import sys

todo = {
    "task":[],
    "status":[]
}
def add(task):
    todo["task"].append(task)
    todo["status"].append("Pending")
    print(todo["task"].index(task)+1," ",task)

def show():
    for index in range(todo["task"]):
        print(index+1,"==>",todo["task"][index])

def delete(number):
    todo["task"].pop((number)-1)

def done(number):
    todo["status"][number-1] = "Complete"

def report():
    print("Pending:",todo["status"].count("Pending"))
    print("Complete:",todo["status"].count("Complete"))

def help():
    print('./todo.py add "todo item"')
    print('./todo.py ls')
    print('./todo.py del NUMBER')
    print('./todo.py done NUMBER')
    print('./todo.py help')
    print('./todo.py report')

if __name__ == "__main__":
    try:
        if "add" in sys.argv:
            add(" ".join(sys.argv[2:]))

        elif "ls" in sys.argv:
            show()

        elif "del" in sys.argv:
            delete(int(sys.argv[-1]))

        elif "done" in sys.argv:
            done(int(sys.argv[-1]))

        elif "report" in sys.argv:
            report()

        elif "help" in sys.argv:
            help()
    except KeyboardInterrupt:
        print(sys.stderr)
        sys.exit(0)