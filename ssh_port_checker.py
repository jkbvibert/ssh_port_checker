import socket, pdb
cluster1 = ['server1','server2','server3']
cluster2 = ['server1','server2','server3']
cluster3 = ['server1','server2','server3']
cluster4 = ['server1','server2','server3']
cluster5 = ['server1','server2','server3']
cluster6 = ['server1','server2','server3']
cluster7 = ['server1','server2','server3']
cluster8 = ['server1','server2','server3']
cluster9 = ['server1','server2','server3']
cluster10 = ['server1','server2','server3']
cluster11 = ['server1','server2','server3']
cluster12 = ['server1','server2','server3']
cluster13 = ['server1','server2','server3']
cluster14 = ['server1','server2','server3']
cluster15 = ['server1','server2','server3']
cluster16 = ['server1','server2','server3']
cluster17 = ['server1','server2','server3']
cluster18 = ['server1','server2','server3']
working = 0
error = 0
unknown = 0
list_of_cluster_names = ['cluster1','cluster2','cluster3','cluster4','cluster5','cluster6','cluster7','cluster8','cluster9','cluster10','cluster11','cluster12','cluster13','cluster14','cluster15','cluster16']
list_w_all_clusters_within_it = [cluster1,cluster2,cluster3,cluster4,cluster5,cluster6,cluster7,cluster8,cluster9,cluster10,cluster11,cluster12,cluster13,cluster14,cluster15,cluster16]
for cluster in list_w_all_clusters_within_it:
    for each in cluster:
        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            so.connect(('%s' % each,22))
            #print("%s -- %s -- Works" % (list_of_cluster_names[list_w_all_clusters_within_it.index(cluster)],each))
            print("{0} -- {1} -- Works".format(list_of_cluster_names[list_w_all_clusters_within_it.index(cluster)],each))
            so.close()
            working += 1
            continue
        except socket.error as e:
            print("{0} -- {1} -- Error on connect -- {2}".format(list_of_cluster_names[list_w_all_clusters_within_it.index(cluster)],each,e))
            so.close()
            error += 1
            continue
        else:        
            print("{0} -- Else loop hit. This means something went really wrong".format(list_of_cluster_names[list_w_all_clusters_within_it.index(cluster)]))
            so.close()
            unknown += 1
            continue
so.close()
total = working+error+unknown
print("{0} servers working (out of {1})".format(working,total))
print("{0} servers with socket errors".format(error))
print("{0} servers with unknown errors".format(unknown))
wait = input("Press Enter to close this dialog box...")
#pdb.set_trace() #then use 'c' to go to the next set_trace (like a breakpoint) and you can print whatever you want to look at
