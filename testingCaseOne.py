import sys
import psutil
import shutil
import os
import platform

if __name__=="__main__":
    if len(sys.argv) > 1:
        p = sys.argv[1]
    else:
        p = os.path.abspath(os.path.curdir)


    def argv(p):
        print(p)
        return

    def get_fs_type(p):
        root_type = ""
        for part in psutil.disk_partitions():
            if part.mountpoint == '/':
                root_type = part.fstype
                continue

            if p.startswith(part.mountpoint):
                return part.fstypew

        return root_type

    def disk_info(p):
        return psutil.disk_usage(p)








    print((disk_info(p).total)//(2 ** 30), 'GB')

    print('type of platform: ', sys.platform)
    #
    print('file system: ', get_fs_type("/tmp"))


