from subprocess import CREATE_NEW_CONSOLE
import time
import sys
import datetime

print('start')
def main():
        when = datetime.datetime.utcnow().isoformat()
        sys.stderr.write('[%s] the default application is running ...' % when)
        print (when)
        time.sleep(5)
if __name__ == '__main__':
    main()
print('end')