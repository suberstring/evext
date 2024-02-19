class LargeNumber:
    def __init__(self,value,cr=1):
        self.value=value
        self.cr = cr
        int(self.value)
        self.value = str(self.value)


def add_large(a, b):
    a = a.value
    b = b.value
    ta = list(a)
    tb = list(b)
    ta = [int(i) for i in ta]
    tb = [int(i) for i in tb]
    ta = list(reversed(ta))
    tb = list(reversed(tb))
    mlen = max(len(ta), len(tb))
    ta += [0]*(mlen-len(ta))
    tb += [0]*(mlen-len(tb))
    y = [0]*(mlen+1)
    for i in range(0, mlen):
        y[i] += ta[i] + tb[i]
        y[i+1] = int(y[i]/10)
        y[i] %= 10
    if y[mlen] == 0:
        y.pop()
    y = list(reversed(y))
    y = [str(i) for i in y]
    y = ''.join(y)

    return LargeNumber(value=y)


def sub_large(a,b):
    a = a.value
    b = b.value
    a = [int(item) for item in a]
    b = [int(item) for item in b]
    res = ''
    for i in range(len(b)):
        flag_a = len(a)-1-i
        flag_b = len(b)-1-i
        if a[flag_a]>= b[flag_b]:
            res = str(a[flag_a]-b[flag_b])+res
        else:
            res = str(10+a[flag_a]-b[flag_b])+res
            while a[flag_a-1]==0:
                a[flag_a-1]=9
                flag_a -= 1
            a[flag_a-1] -= 1
    for j in range(len(a)-1-i-1,-1,-1):
        res = str(a[j])+res
    zero_flag=0
    for i in range(len(res)):
        if res[i]!='0':
            zero_flag=1
            break
    if zero_flag==0:
        return 0
    return LargeNumber(value=res[i:])



def add(a,b):
    return str(int(a)+int(b))
def mul(a,b):
    a = a.value
    b = b.value
    N=3
    if len(b)>len(a):
        a,b=b,a
    if(len(a)<=N):
        return str(int(a)*int(b))
    mid=len(a)//2
    a1=a[:mid]
    a2=a[mid:]
    return LargeNumber(value=add(mul(a1,b)+"0"*len(a2),mul(a2,b)))