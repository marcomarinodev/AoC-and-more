from collections import defaultdict, deque
from fractions import Fraction
import sys
import hashlib
 
def md5(x):
    return hashlib.md5(str.encode(x)).hexdigest()
 
# sys.stdout.flush()
 
from itertools import permutations, combinations
# permutations(list[, r]) # r-length tuples
# combinations(list, r) # r-length sorted tuples
 
def gcd(x, y):
    while y!=0:
        x,y = y,x%y
    return x
 
def sign(x):
    if x>0:
        return 1
    if x<0:
        return -1
    return 0
 
# take 2d array, reflect horizontally
def reflect(a):
    return [l[::-1] for l in a]
 
# take 2d array, rotate 90 degrees clockwise
def rotate(a):
    n=len(a)
    m=len(a[0])
    return [[a[n-1-j][i] for j in range(n)] for i in range(m)]
 
# dirs in [4, 8]
# returns coordinates of neighbors of (x, y)
# in a grid where 0 <= x < xn, 0 <= y < yn
def neighbor(x, y, dirs, xn=None, yn=None):
    assert dirs in [4, 8]
    ret = []
    if dirs==4:
        dxy = [(-1,0),(0,-1),(1,0),(0,1)]
    else:
        dxy = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if xn is not None:
            if nx<0 or nx>=xn:
                continue
        if yn is not None:
            if ny<0 or ny>=yn:
                continue
        ret.append((nx,ny))
    return ret
 
# replace every letter of s that is in cs with a space (or anything else)
def strclean(s, cs, to=" "):
    for c in cs:
        s=s.replace(c, to)
    return s
 
# return only integers from a list of strings
def extract_ints(a):
    ret = []
    for x in a:
        try:
            v=int(x)
            ret.append(v)
        except:
            continue
    return ret
 
def isplit(s, delim=None):
    tokens = s.split(delim) if delim is not None else s.split()
    ret = []
    for x in tokens:
        try:
            v = int(x)
            ret.append(v)
        except:
            ret.append(x)
    return ret
 
def grid(dims, val):
    if len(dims)==1:
        return [val for _ in range(dims[0])]
    return [grid(dims[1:], val) for _ in range(dims[0])]
 
dat = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".strip().split("\n\n")
 
dat2 = """
 
""".strip().split("\n")
 
def solve():
    global dat
    global dat2
    # dat=dat2  # sample test
    a = dat[0].split("\n")
    b = "".join(dat[1].split("\n"))
    ans=0
    n = len(a)
    m = len(a[0])
    for i in range(n):
        a[i] = [c for c in a[i]]
        for j in range(m):
            if a[i][j]=="@":
                sx=i
                sy=j
                a[i][j]="."
                break
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    for mv in b:
        if mv == "^":
            d=1
        elif mv == "<":
            d=0
        elif mv == ">":
            d=2
        else:
            d=3
        k=1
        flag=False
        blocked=False
        while True:
            nx=sx+dx[d]*k
            ny=sy+dy[d]*k
            if a[nx][ny]=="#":
                blocked=True
                break
            elif a[nx][ny]==".":
                flag=True
                break
            k+=1
        if not blocked:
            a[nx][ny], a[sx+dx[d]][sy+dy[d]] = a[sx+dx[d]][sy+dy[d]], a[nx][ny]
            sx+=dx[d]
            sy+=dy[d]
    ans=0
    for i in range(n):
        for j in range(m):
            if a[i][j]=="O":
                ans+=100*i+j
    print(ans)
 
def trypush(a, sx, sy, dx, dy):
    nx=sx+dx
    ny=sy+dy
    if a[nx][ny]=="#":
        return False
    elif a[nx][ny]==".":
        return True
    elif dy==0:
        if a[nx][ny]=="]":
            return trypush(a, nx, ny, dx, dy) and trypush(a, nx, ny-1, dx, dy)
        elif a[nx][ny]=="[":
            return trypush(a, nx, ny, dx, dy) and trypush(a, nx, ny+1, dx, dy)
    elif dy==-1: # push left
        if a[nx][ny]=="]":
            return trypush(a, nx, ny-1, dx, dy)
    elif dy==1: # push right
        if a[nx][ny]=="[":
            return trypush(a, nx, ny+1, dx, dy)
 
def push(a, sx, sy, dx, dy):
    nx=sx+dx
    ny=sy+dy
    if a[nx][ny]=="#":
        return
    elif a[nx][ny]==".":
        a[sx][sy], a[nx][ny] = a[nx][ny], a[sx][sy]
        return
    elif dy==0:
        if a[nx][ny]=="]":
            push(a, nx, ny, dx, dy)
            push(a, nx, ny-1, dx, dy)
            a[sx][sy], a[nx][ny] = a[nx][ny], a[sx][sy]
            return
        elif a[nx][ny]=="[":
            push(a, nx, ny, dx, dy)
            push(a, nx, ny+1, dx, dy)
            a[sx][sy], a[nx][ny] = a[nx][ny], a[sx][sy]
            return
    elif dy==-1: # push left
        if a[nx][ny]=="]":
            push(a, nx, ny-1, dx, dy)
            a[nx][ny-1], a[nx][ny], a[sx][sy] = a[nx][ny], a[sx][sy], a[nx][ny-1]
            return
    elif dy==1: # push right
        if a[nx][ny]=="[":
            push(a, nx, ny+1, dx, dy)
            a[nx][ny+1], a[nx][ny], a[sx][sy] = a[nx][ny], a[sx][sy], a[nx][ny+1]
            return
 
def solve2():
    global dat
    global dat2
    # dat=dat2  # sample test
    a = dat[0].split("\n")
    b = "".join(dat[1].split("\n"))
    ans=0
    n = len(a)
    m = len(a[0])*2
    for i in range(n):
        na = []
        for c in a[i]:
            if c=="#":
                na.append("#")
                na.append("#")
            elif c=="O":
                na.append("[")
                na.append("]")
            elif c==".":
                na.append(".")
                na.append(".")
            else:
                na.append("@")
                na.append(".")
        a[i] = na
        for j in range(m):
            if a[i][j]=="@":
                sx=i
                sy=j
                a[i][j]="."
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    for mv in b:
        if mv == "^":
            d=1
        elif mv == "<":
            d=0
        elif mv == ">":
            d=2
        else:
            d=3
        if trypush(a, sx, sy, dx[d], dy[d]):
            push(a, sx, sy, dx[d], dy[d])
            sx+=dx[d]
            sy+=dy[d]
    ans=0
    for i in range(n):
        for j in range(m):
            if a[i][j]=="[":
                ans+=100*i+j
    print(ans)
 
 
solve()
# solve2()