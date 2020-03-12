from tkinter import *
from tkinter import simpledialog
from functools  import partial



#creating  a  function  for every mathermatical process (big'n)
def su(v,a,t):
    s = (v*t)-((1/2)*(a*(t**2)))
    return  s, ("img/su.gif")

def sv(u,a,t):
    s = (u*t)+((1/2)*(a*(t**2)))
    return  s, ("img/sv.gif")
                
def sa(u,v,t):
    s=(t/2)*(u+v)
    return  s, ("img/sa.gif")

def st(u,v,a):
    s=((u**2)+(v**2))/(2*a)
    return s, ("img/st.gif")

##

def us(v,a,t):
    u=v - (a*t)
    return u, ("img/us.gif")

def uv(s,a,t):
    u=(s-(a*(t**2)))/(2*t)
    return u, ("img/uv.gif")

def ua(s,v,t):
    u=((2*s)/t)+v
    return  u, ("img/ua.gif")

def ut(s,v,a):
    u=((2*(a*(s)))-(v**2))**(1/2)
    return u, ("img/ut.gif")

##

def  vs(u,a,t):
    v=u + (a*t)
    return v, ("img/vs.gif")

def vu(s,a,t):
    v=(s+(a*(t**2)))/(2*t)
    return v, ("img/vu.gif")

def va(s,u,t):
    v=((2*s)/t)-u
    return v, ("img/va.gif")

def vt(s,a,u):
    v=((u**2)+(2*a*s))**(1/2)
    return v, ("img/vt.gif")

##

def aS(u,v,t):
    a=(v-u)/t
    return a, ("img/aS.gif")

def au(s,v,t):
    a= (2*((v*t)-s))/(t**2)
    return  a, ("img/au.gif")

def av(s,u,t):
    a=(2*(s-(u*t)))/(t**2)
    return a, ("img/av.gif")

def at(s,u,v):
    a = ((v**2)-(u**2))/(2*s)
    print(__name__)
    return a, ("img/at.gif")

##

def ts(u,v,a):
    t=(v-u)/a
    return t, ("img/as.gif")

def tu(s,v,a):
    t=(v-(((v**2)-(2*a*s))**(1/2)))/a
    return t, ("img/tu.gif")

def tv(s,u,a):
    t=((((2*a*s)+(u**2))**(1/2))-u)/a
    return t, ("img/tv.gif")

def ta(s,u,v):
    t=(2*s)/(u+v)
    return t, ("img/ta.gif")
#######
#creating  a 2 dimentional array to look up the  function to  use for every  missing value
global  equationArr
equationArr = ([sv,su,sv,sa,st],
               [us,us,uv,ua,ut],
               [vs,vu,vs,va,vt],
               [aS,au,av,aS,at],
               [ts,tu,tv,ta,ts])
########################################################################


#initialising  a window for  the GUI
root = Tk()
root.title("SUVAT calculator")

#setting  a  global variable to describe the list of  suvat variables.
global suvatList
suvatList=['s','u','v','a','t']

#find null attributes
def findNullAttr(projectile):
    nullArr = []
    for i  in suvatList:
        if ((getattr(projectile, i)=="")or(getattr(projectile, i)==None)):
            nullArr.append(suvatList.index(i))

    if (len(nullArr) == 1):
        nullArr.append(nullArr[0])
    return nullArr
        

#creating a  function to ammend  the values  of the  attributes in the   projectile attribute
def ammendSuvat(label,row):
    pos  = suvatList[row]
    string=label.get()
    setattr(projectile, pos,string)
    labelupdate = getattr(projectile, pos)
    Label (text=labelupdate,width=15, relief=RIDGE).grid(row=row,column=3)

def calcNull(projectile, nullAttr,mode):
    if mode  ==  1:
        tempVar =  nullAttr[1]
        nullAttr[1] =  nullAttr[0]
        nullAttr[0] = tempVar
    popArr  =  []
    for i in  suvatList:
        if ((getattr(projectile, i) != None)and(getattr(projectile,i)!= "")):
            popArr.append(getattr(projectile, i))
        print(popArr,"popArr")
    f=equationArr[nullAttr[0]][nullAttr[1]]
    result, imagefile = f(int(popArr[0]),int(popArr[1]),int(popArr[2]))
    print  (result)
    if mode  ==  1:
        tempVar =  nullAttr[1]
        nullAttr[1] =  nullAttr[0]
        nullAttr[0] = tempVar

    resultw = Toplevel()
    image = PhotoImage(file=imagefile)
    Label(master = resultw,image=image).grid(row=0,column=0)
    objectFound = str(suvatList[nullAttr[0]])
    printline=("Result for " + objectFound +  " is " + str(result))
    print(printline,nullAttr[0],suvatList[nullAttr[0]])
    Label(master = resultw,text=printline).grid(row=1,column=0) 
    resultw.mainloop()
        

#main calculation function   
def mainCalc(projectile):
    #finding null attributes
    nullAttr = findNullAttr(projectile)
    print(nullAttr)
    Button(text="find " + suvatList[nullAttr[0]] +  "  without " +  suvatList[nullAttr[1]],command=partial(calcNull,projectile,nullAttr,0)).grid(row=5,column=2,pady=10)
    if(nullAttr[0] !=nullAttr[1]):
        Button(text="find " + suvatList[nullAttr[1]] +  "  without " +  suvatList[nullAttr[0]],command=partial(calcNull,projectile,nullAttr,1)).grid(row=5,column=3,pady=10)

#finding original  suvat entry
def projectileInfo(projectile):
    r=0
    #looping to create labels to indicate which  field is which  variable in projectile and  creating  a  label  box  for each  variable for  future updates
    for  i in suvatList:
        Label(text=i  + " =",width=15, relief=RIDGE).grid(row=r,column=1)
        Label(text="",width=15,relief=RIDGE).grid(row=r,column=3)
        r+=1


    #creating update functions for each  variable in projectile, using recursion onlcik of the buttons
    #s
    se = Entry(root)
    se.grid(row=0,column=2)
    sb =  Button(root,text="Enter",command=partial(ammendSuvat,se,0))
    sb.grid(row=0,column=4)
    #u
    ue = Entry(root)
    ue.grid(row=1,column=2)
    ub =  Button(root,text="Enter",command=partial(ammendSuvat,ue,1))
    ub.grid(row=1,column=4)
    #v
    ve = Entry(root)
    ve.grid(row=2,column=2)
    vb =  Button(root,text="Enter",command=partial(ammendSuvat,ve,2))
    vb.grid(row=2,column=4)
    #a
    ae = Entry(root)
    ae.grid(row=3,column=2)
    ab =  Button(root,text="Enter",command=partial(ammendSuvat,ae,3))
    ab.grid(row=3,column=4)
    #t
    te = Entry(root)
    te.grid(row=4,column=2)
    tb =  Button(root,text="Enter",command=partial(ammendSuvat,te,4))
    tb.grid(row=4,column=4)
    

#creating  a Projectile() class
class Projectile:

    objType  = "Projectile"
    
    #initialise
    def  __init__(self,s,u,v,a,t):
        self.s=s
        self.u=u
        self.v=v
        self.a=a
        self.t=t


#initialising the projectile  object  using the Projectile() class
projectile=Projectile(None,None,None,None,None)

#creating a table/grid for displaying the values of the attributes in the object projectile, and to edit said attributes.
projectileInfo(projectile)

Button(root,text="Scan for missing variables", command=partial(mainCalc,projectile)).grid(row=5,column=0,pady=10)

#using https://jameskennedymonash.wordpress.com/suvat-rearranged-3/ as  a  source for these equations

    


#drawing  the window using our code
root.mainloop()

