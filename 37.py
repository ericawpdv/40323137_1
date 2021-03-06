def symbol0(row):
    s=[
    '☆☆★★★★☆',
    '☆★☆☆☆★★',
    '☆★☆☆☆★★',
    '☆★☆☆★☆★',
    '☆★☆★★☆★',
    '☆★☆★☆☆★',
    '☆★★☆☆☆★',
    '☆★★☆☆☆★',
    '☆☆★★★★☆',
    ]
    return s[row]
  
def symbol1(row):
    s=[
    '☆☆☆★☆☆☆',
    '☆☆★★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆★★★★★★',
    ]
    return s[row]
   
def symbol2(row):
    s=[
    '☆★★★★★☆',
    '☆★☆☆☆☆★',
    '☆☆☆☆☆☆★',
    '☆☆☆☆☆☆★',
    '☆☆★★★★★',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★★★★★★',
    ]
    return s[row]
  
def symbol3(row):
    s=[
    '☆★★★★★☆',
    '☆☆☆☆☆☆★',
    '☆☆☆☆☆☆★',
    '☆☆☆☆☆☆★',
    '☆★★★★★★',
    '☆☆☆☆☆☆★',
    '☆☆☆☆☆☆★',
    '☆☆☆☆☆☆★',
    '☆★★★★★☆',
    ]
    return s[row]
  
def symbol4(row):
    s=[
    '☆☆☆☆☆★☆',
    '☆☆☆☆★★☆',
    '☆☆☆★☆★☆',
    '☆☆★☆☆★☆',
    '☆★☆☆☆★☆',
    '☆★★★★★★',
    '☆☆☆☆☆★☆',
    '☆☆☆☆☆★☆',
    '☆☆☆☆☆★☆',
    ]
    return s[row]
  
def symbol7(row):
    s=[
    '☆★★★★★★',
    '☆★☆☆☆☆★',
    '☆☆☆☆☆☆★',
    '☆☆☆☆☆★☆',
    '☆☆☆★★☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    ]
    return s[row]
  
def symbolE(row):
    s=[
    '☆★★★★★★',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★★★★★☆',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★★★★★★',
    ]
    return s[row]
   
def symbolR(row):
    s=[
    '☆★★★★★☆',
    '☆★☆☆☆☆★',
    '☆★☆☆☆☆★',
    '☆★☆☆☆☆★',
    '☆★★★★★☆',
    '☆★★☆★☆☆',
    '☆★☆☆☆★☆',
    '☆★☆☆☆☆★',
    '☆★☆☆☆☆★',
    ]
    return s[row]
   
def symbolI(row):
    s=[
    '☆★★★★★★',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆☆☆★☆☆☆',
    '☆★★★★★★',
    ]
    return s[row]
   
def symbolC(row):
    s=[
    '☆☆★★★★☆',
    '☆★☆☆☆☆★',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆☆',
    '☆★☆☆☆☆★',
    '☆☆★★★★☆',
    ]
    return s[row]
  
symbollDict={"4":symbol4,"0":symbol0,"3":symbol3,"2":symbol2,"7":symbol7,"1":symbol1,"E":symbolE,"I":symbolI,"R":symbolR,"C":symbolC}
   
row=9
   
while True:
    inp=input("enter a string to display or 'exit' to end program:")
    if inp=='exit':
        break
    for r in range(row):
        for c in inp:
            print(symbollDict[c](r),end=' ')
        print()
print('退出')