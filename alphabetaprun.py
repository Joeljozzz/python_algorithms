###alphabetapruning
##tree=[[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
##root=0
##pruned=0
##def children(branch,depth,alpha,beta):
##    global root
##    global tree
##    global pruned
##    i=0
##    for child in branch:
##        if type(child)==list:
##            (nalpha,nbeta)=children(child,depth+1,alpha,beta)
##            if depth%2==1:
##                beta = nalpha if nalpha<beta else beta
##            else:
##                alpha = nbeta if nbeta>alpha else alpha
##            branch[i]=alpha if depth%2==0 else beta
##            i+=1
##        else:
##            if depth%2==0 and alpha<child:
##                alpha=child
##            if depth%2==1 and beta>child:
##                beta=child
##            if alpha>=beta:
##                pruned+=1
##                break
##    if depth==root:
##        tree=alpha if root==0 else beta
##    return(alpha,beta)
##def alphabeta(treee=tree,start=root,upper=-15,lower=15):
##    global tree
##    global pruned
##    global root
##    (alpha,beta)=children(tree,start,upper,lower)
##    if __name__ == "__main__":
##        print("(alpha,beta): ",alpha,beta)
##        print("Result: ",tree)
##        print("times pruned: ",pruned)
##        return(alpha,beta,tree,pruned)
##if __name__ == "__main__":
##    alphabeta(None)

tree=[[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
pruned=0
root=0
def children(branch,depth,alpha,beta):
    global root
    global tree
    global pruned
    i=0
    for child in branch:
        if type(child)==list:
            (nalpha,nbeta)=children(child,depth+1,alpha,beta)
            if depth%2==1:
                beta=nalpha if nalpha<beta else beta
            else:
                alpha=nbeta if nbeta>alpha else alpha
            branch[i]=alpha if depth%2==0 else beta
            i+=1
        else:
            if depth%2==0 and child>alpha:
                alpha=child
            if depth%2==1 and child<beta:
                beta=child
            if alpha>=beta:
                pruned+=1
                break
    if depth==root:
        tree=alpha if root==0 else beta
    return(alpha,beta)
def alphabeta(tree1=tree,start=root,upper=-15,lower=15):
    global root
    global pruned
    global tree
    (alpha,beta)=children(tree,start,upper,lower)
    print("(alpha,beta: )",alpha,beta)
    print("result: ",tree)
    print("pruned: ",pruned)
alphabeta(None)
            





































        
        

        
