from win10toast import ToastNotifier
import time

notifier = ToastNotifier()

while True:
    if (time.gmtime().tm_min) % 15 == 0:
        notifier.show_toast("Break!", "Stretch a bit..You're awesome", duration=15)
        time.sleep(60)