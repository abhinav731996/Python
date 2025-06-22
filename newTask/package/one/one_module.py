import sys
import os

sys.path.append(os.getcwd())


from newTask.package.two import two_module


def one_function():
    two_module.two_function()

