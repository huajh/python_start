from urllib.request import urlretrieve


def fristNonBlank(lines):
    for eachline in lines:
        if not eachline.strip():
            continue
        else:
            return eachline


def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print(fristNonBlank(lines))
    lines.reverse()
    print(fristNonBlank(lines))


def download(url='http://www.baidu.com', process=firstLast):
    try:
        retval = urlretrieve(url)[1]
        print(retval)
    except IOError:
        retval = None
    if retval:
        process(retval)


if __name__ == '__main__':
    download()
