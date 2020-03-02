import urllib.request, urllib.error, urllib.parse, time

url = input('Enter - ')
img = urllib.request.urlopen(url)
count = 0

print(img.read(3000))

img = urllib.request.urlopen(url)

while True:
    info = img.read(25000)
    if len(info) < 1: break
    count = count + len(info)
    # print('gain:', len(info),'current:', count)


print('\nDone!\nCharacter Count:', count)
img.close()