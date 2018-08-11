# import os,sys
#
# def listfiel(path):
#     if os.path.isdir(path):
#         print(path+':')
#         content=os.listdir(path)
#         print(content)
#         for fname in content:
#             fname=os.path.join(path,fname)
#             listfiel(fname)
#
# if __name__ == '__main__':
#     listfiel('/boot')

import os,time,tarfile,hashlib,pickle

def checkmd5(fname):
    m=hashlib.md5
    with open(fname,'rb') as obj:
        while True:
            data =obj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()
def full(srcfile,desfile,md5file):
    fname=os.path.basename(srcfile.rstrip('/'))
    fname='%s_full_%s.tar.gz' % (fname,time.strftime('%Y%m%d'))
    fname=os.path.join(desfile,fname)
    md5dict={}

    tar=tarfile.open(fname,'w:gz')
    tar.add(srcfile)
    tar.close()

    for path,folders,files in os.walk(srcfile):
         for eachfile in files:
             key=os.path.join(path,eachfile)
             md5dict[key]=checkmd5(key)

