import datetime
import schedule
import time

count_val = 1


def job():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print(str(TNOW) + " Print 5 sec interval for 3 times ")


def test(count_value, value):
    print(value + " count : ", count_value)


def minjob():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print('\n' + str(TNOW) + " This prints every min \n")


def hello():
    return "Hello raka : "


hello_val = hello()


def test_scheduler():
    print("Welcome to Rakesh Kumar ")


schedule.every(2).seconds.do(test_scheduler)

# schedule.every(1).minutes.do(minjob)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
# schedule.every().minute.at(":05").do(job)
# schedule.every().minute.at(":10").do(job)
# schedule.every().minute.at(":15").do(job)

# schedule.every(1).minutes.do(test, count_val, hello_val)

# count_val = count_val + 1


while True:
    # schedule.every(1).minutes.do(test(count_val))

    # schedule.every(1).minutes.do(test, count_val, hello_val)

    # schedule.every(1).minutes.do(test, count_val, hello_val)
    # schedule.every(10).minutes.do(functools.partial(job, 'Hello ', 'world!'))

    test(count_val, hello_val)

    schedule.run_pending()
    count_val = count_val + 1
    time.sleep(1)

# schedule.every(1).minutes.do(minjob)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
# schedule.every().minute.at(":05").do(job)
# schedule.every().minute.at(":10").do(job)
# schedule.every().minute.at(":15").do(job)
