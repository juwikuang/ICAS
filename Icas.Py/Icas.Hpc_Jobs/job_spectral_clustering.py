#Clustering Naming Convention
#algorithm_parameters_attempt_labels.csv
#kmeans_4_1_labels.csv
#kmeans_4_2_labels.csv
#Commmand:#
#bsub < job.bsub
import numpy as np
import pickle
from sklearn.cluster import SpectralClustering
from sklearn import cluster
import os
import threading
import sys

from job_thread_executioner import ThreadExecutioner
from job_basic import createFolders
from job_basic import getParameters

#code for testing
#import os
#os.chdir("C:\\MiCluster.Test\\")
#dataset = "cs_reactivity_wt_21_pca"
#thread_limit=100

methodName = "spectral_clustering"
dataset, thread_limit, rounds = getParameters()
executioner = ThreadExecutioner(thread_limit)
createFolders(methodName, dataset)


def worker(X, n_clusters, assign_labels, round): 
    key = methodName + "/"+dataset+"/individuals/"+methodName+"_"+dataset+"_k_" + str(n_clusters) + "_assign_labels_" + assign_labels + "_round_" + str(round)    
    file = key + "_labels.csv"
    if(os.path.exists(file)):
        return
    method = SpectralClustering(n_clusters = n_clusters, assign_labels = assign_labels)
    method.fit(X)
    np.savetxt(file,method.labels_,fmt = "%d")


X = np.loadtxt("cs_datasets/" + dataset + ".csv",delimiter = ",")
        
for n_clusters in range(3,6):
    for assign_labels in ["kmeans","discretize"]:
        for round in range(0,rounds):
            t = threading.Thread(target=worker, args=(X, n_clusters, assign_labels, round))
            #t.start()
            #t.join();
            executioner.add(t)

executioner.run_all()

print "Job Done!"