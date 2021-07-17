from Crypto.Cipher import AES
#先下载KEY文件，使用这个key解密每一个ts文件，然后合并MP4。
import requests
uu='http://video1.aa/090712-123/1500kb/hls/'
res = requests.get(uu+'key.key')
key=res.content
cryptor = AES.new(key, AES.MODE_CBC, key)
for i in range(30):
    u='%sKhbR41840%02d.ts'%(uu,i)
    print(u)
    res = requests.get(u)
       
    with open("xx.mp4", 'ab') as f:
        #f.write(res.content)
        f.write(cryptor.decrypt(res.content))
