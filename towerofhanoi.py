##def tower(height, startpole, auxilary, endpole):
##    if height>=1:
##        tower(height-1,startpole, endpole, auxilary)
##        movedisk(startpole,endpole)
##        tower(height-1,auxilary, startpole, endpole)
##        
##def movedisk(fp,tp):
##    print("moving disk from:",fp," to ",tp)
##
##a = int(input("please enter the number of disks: "))   
##tower(a,"A","B","C")
##
##def tower(height, startpole, midpole, endpole):
##    if height >= 1:
##        tower(height-1, startpole, endpole, midpole)
##        movedisk(startpole, endpole)
##        tower(height-1, midpole, startpole, endpole)
##def movedisk(fp,tp):
##    print("disk moving from ",fp," to ",tp)
##
##a=int(input("please enter number of disks"))
##tower(a,"a","b","c")    
    
##def tower(height,start,middle,end):
##    if height >=1:
##        tower(height-1,start,end,middle)
##        movedisk(start, end)
##        tower(height-1,middle,start,end)
##
##def movedisk(fp,tp):
##    print("moving disk from ",fp, "to ",tp)
##tower(3,'A','B','C')
def tower(height, first, aux, last):
    if height>=1:
        tower(height-1,first,last,aux)
        movedisk(first,last)
        tower(height-1,aux,first,last)
def movedisk(fp,tp):
    print("moving disk from",fp,"To",tp)
a=int(input("Enter the number of disks"))
tower(a,"A","B","C")
        








































































































        





    
