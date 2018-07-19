import os

def get_filename():

    while True:
        fname = input('please input a file name: ')
        if not os.path.exists(fname):
            break
        print('%s already exists.Try again',fname)

    return fname




def get_conment():



def wfile(fname,conment):




if __name__ == '__main__':
    fname = get_filename()
    conment = get_conment()
    wfile(filename,conment)