import os


data = os.popen("netsh wlan show profiles").read()
data = data.split("\n")

profiles = []
for i in data:

    if "All User Profile" in i:

        # if found
        # split the item
        i = i.split(":")

        # item at index 1 will be the wifi name
        i = i[1]

        profiles.append(i)


for a in profiles:

    rst = os.popen("netsh wlan show profile name=" + a + " key=clear").read()
    print(rst)


input("")
