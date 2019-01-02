from proxypool.scheduler import Scheduler
#import sys
#import io
from proxypool.file import file

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    try:

        print("程序启动")

        s = Scheduler()
        s.run()

        print("程序结束")
    except Exception as e:
        print("程序异常")
        print("main 异常"+e.args)
        file.ErrorWrite("main 异常"+e.args)
        main()


if __name__ == '__main__':
    main()
