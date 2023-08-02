import validators
import webbrowser


def openlink(data):
    if validators.url(data):
        webbrowser.open(data)
    else:
        print('\n\nNot a url')
