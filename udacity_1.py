colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT


p = []

n = len(colors)
m = len(colors[0])

def seed():
    p=[]
    initial = 1.0/(n*m)

    for i in range(n):
        p.append([])
        for j in range(m):
            p[i].append(initial)
    return p

def move(p, motion):
    post = []
    for i in range(n):
        post.append([])
        for j in range(m):
            post[i].append(p[i][j]*(1-p_move) + p[(i-motion[0]) % n][(j-motion[1]) % m]*p_move)
    return post

def normalize(p):
    total = 0
    for i in range(n):
        total += sum(p[i])
    
    normalizer = 1./total
    
    for i in range(n):
        for j in range(m):
            p[i][j] *= normalizer
    
    return p
            
            
    
def sense(p, measurement):
    for i in range(n):
        for j in range(m):
            p[i][j] *= (sensor_right if (measurement==colors[i][j]) else (1-sensor_right))
            
    return normalize(p)
    

p = seed()

for i in range(len(motions)):
    p = sense(move(p, motions[i]), measurements[i])

#Your probability array must be printed 
#with the following code.

show(p)
