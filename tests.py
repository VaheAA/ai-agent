from functions.run_python import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    print("Result for just main.py:")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for main.py with arguments")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for tests.py")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for file outside of dir")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for nonexistent file")
    print(result)
    print("")


if __name__ == "__main__":
    test()
