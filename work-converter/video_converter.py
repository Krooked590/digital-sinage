import sys
#import cloudconvert
from time import sleep
from subprocess import call

if (len(sys.argv)) < 2:
    sys.exit(1)

path = sys.argv[1].strip()

print("converting...")
call(["./HandBrakeCLI", "-i", path + ".m4v", "-o", path + ".mp4"])
print("conversion complete...")

# api_key = ""
# with open('.ccapi', 'r') as file:
#     api_key = file.readline().strip()

# api = cloudconvert.Api(api_key)

# print('uploading...')
# process = api.convert({
#     "inputformat": "m4v",
#     "outputformat": "mp4",
#     "input": "upload",
#     "timeout": 0,
#     "file": open(path + '.m4v', 'rb')
# })

#print('finished upload...converting...')
# process.wait()
#print('finished conversion...downloading...')
# process.download(path + '.mp4')
#print('download complete!')
#sleep(3)