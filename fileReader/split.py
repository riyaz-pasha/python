import sys
import os

kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)


def isDirectoryAlreadyExists(dir):
    return os.path.exists(dir)


def createNewDirectory(dir):
    os.mkdir(dir)


def filesInDirectory(dir):
    return os.listdir(dir)


def deleteFileFromDirectory(dir, fileName):
    os.remove(os.path.join(dir, fileName))


def split(fromfile, todir, chunksize=chunksize):
    if not isDirectoryAlreadyExists(todir):
        createNewDirectory(todir)
    else:
        for fileName in filesInDirectory(todir):
            deleteFileFromDirectory(todir, fileName)
    partnum = 0
    input = open(fromfile, 'rb')                   # use binary mode on Windows
    while 1:                                       # eof=empty string from read
        chunk = input.read(chunksize)              # get next part <= chunksize
        if not chunk:
            break
        partnum = partnum+1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()                            # or simply open(  ).write(  )
    input.close()
    assert partnum <= 9999                         # join sort fails if 5 digits
    return partnum


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            interactive = 1
            fromfile = input('File to be split? ')       # input if clicked
            todir = input('Directory to store part files? ')
        else:
            interactive = 0
            fromfile, todir = sys.argv[1:3]                  # args in cmdline
            if len(sys.argv) == 4:
                chunksize = int(sys.argv[3])
        absfrom, absto = map(os.path.abspath, [fromfile, todir])
        print('Splitting', absfrom, 'to', absto, 'by', chunksize)

        try:
            parts = split(fromfile, todir, chunksize)
        except:
            print('Error during split:')
            print(sys.exc_type, sys.exc_value)
        else:
            print('Split finished:', parts, 'parts are in', absto)
        if interactive:
            input('Press Enter key')  # pause if clicked
