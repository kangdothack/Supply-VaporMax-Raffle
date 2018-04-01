import colorama
import datetime

colorama.init()


def stamp():
    timestamp = str('[' + datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3] + ']')
    return timestamp


def s_logging(text):
    print('\n{} {}'.format(stamp(), text))


def r_logging(text):
    print(colorama.Fore.RED, '\n{} {}'.format(stamp(), text))


def ly_logging(text):
    print(colorama.Fore.LIGHTYELLOW_EX, '\n{} {}'.format(stamp(), text))


def y_logging(text):
    print(colorama.Fore.YELLOW, '\n{} {}'.format(stamp(), text))


def lg_logging(text):
    print(colorama.Fore.LIGHTGREEN_EX, '\n{} {}'.format(stamp(), text))


def g_logging(text):
    print(colorama.Fore.GREEN, '\n{} {}'.format(stamp(), text))
