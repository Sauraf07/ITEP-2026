'''
sys.exit(0):rise system error
os._exit(0)
'''
import os
print("At the start")
try:
    os._exit(0)
except SystemExit:
    print("System catch error")
print("At the end ")