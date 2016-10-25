import os
import numpy as np

from scipy.cluster import hierarchy

from job_thread_executioner import ThreadExecutioner
from job_basic import createFolders
from job_basic import getParameters

os.chdir("C:\\MiCluster.Test\\")


methodName = "hierarchical"
dataset, thread_limit, rounds = getParameters()
executioner = ThreadExecutioner(5)
createFolders(methodName, dataset)

#thread_limit = 10
#rounds = 100
#dataset = "cs_rna_distance_triangle_wt_71"


upper_triangle = np.loadtxt("cs_datasets/"+dataset+".txt");

hierarchy_result = hierarchy.linkage(upper_triangle)

for k in range(3,15):
    print "k="+str(k)
    cutree = hierarchy.cut_tree(hierarchy_result, n_clusters=[k])

    alist = []

    for i in range(0,len(cutree)):
        alist.append(cutree[i][0])
        #print i
    
    np.savetxt(methodName+"/"+dataset+"/individuals/"+methodName+"_"+dataset+"_k_"+str(k)+".csv",alist,fmt="%d")

