# coding:utf-8\

from django.apps import AppConfig
import os

default_app_config = 'api.PrimaryBlogConfig'

VERBOSE_APP_NAME = u"1、文章、角色、用户"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class PrimaryBlogConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME