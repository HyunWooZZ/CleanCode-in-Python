import contextlib
import os

@contextlib.contextmanager
def text_open(location):
    try:
        text = open(location, 'r')
        yield text
    finally:
        text.close()

if __name__ == "__main__":
    file_location = os.path.join(os.getcwd(), 'sample/example.txt')
    with text_open(file_location) as t:
        print(t.read())

