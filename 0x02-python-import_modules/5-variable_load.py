#!/usr/bin/python3
import importlib.machinery
loader = importlib.machinery.SourceFileLoader('variable_load_5', './variable_load_5.py')
variable_load_5 = loader.load_module()
print(variable_load_5.a)
