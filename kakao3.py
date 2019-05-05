import re

def split_filename(filename):
    head, number, _ = re.findall('([a-zA-Z]+)([0-9]+)([a-zA-Z]*)', filename)[0]
    return head.lower(), int(number)

def order_files(files):

    def key_function(x):
        head, number = split_filename(x)
        return (head, number)

    return sorted(files, key=key_function)

print(order_files(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
