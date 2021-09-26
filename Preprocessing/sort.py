from shutil import copyfile

f = open('HAM10000_metadata.csv', 'r')

redovi = f.readlines()

for red in redovi:
    niz = red.split(',')
    src = '/home/jelena/Downloads/MELANOMA/skin-cancer-mnist-ham10000/images/'
    src = src + niz[1] + '.jpg'
    dest = '/home/jelena/Downloads/MELANOMA/skin-cancer-mnist-ham10000/'
    dest = dest + niz[2] + '/'
    dest = dest + niz[1] + '.jpg'

    try:
        copyfile(src, dest)
    except FileNotFoundError:
        continue;
