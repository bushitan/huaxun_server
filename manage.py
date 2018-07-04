#coding:utf-8
import os
import sys

# from api308.action.api308 import *
# def time_token():
#
#     print 111
#     action_api = ActionAPI308()
#     import threading
#     def fun_timer():
#         print('Hello Timer!')
#         action_api.create()
#         global timer
#         timer = threading.Timer(1024, fun_timer)
#         timer.start()
#     timer = threading.Timer(0, fun_timer)
#     timer.start()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huaxun_server.settings")

    # if lock is False:
    #     time_token()  #发布时开启

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

