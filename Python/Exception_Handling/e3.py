'''
sys.exit(0):rise system error
os._exit(0)
'''
import sys
print("At the start")
try:
    sys.exit(0)
except SystemExit:
    print("System catch error")
print("At the end ")