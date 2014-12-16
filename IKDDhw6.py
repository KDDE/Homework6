from sklearn.cluster import KMeans

f = open('house-votes-84.data')
fcsv1 = open('cluster1.csv', 'w')
fcsv2 = open('cluster2.csv', 'w')

x = []

for line in f:
    col = line.split(',')
    col[1:] = [v.replace('y', '1') for v in col[1:]]
    col[1:] = [v.replace('n', '-1') for v in col[1:]]
    col[1:] = [v.replace('?', '0') for v in col[1:]]
    x.append(col[1:])

KM = KMeans(n_clusters=2)
P = KM.fit_predict(x)

hit = 0

for i in range(len(P)):
    if P[i] == 1:
	fcsv1.write(str(i+1)+'\n')
    else:
	fcsv2.write(str(i+1)+'\n')

f.close()
fcsv1.close()
fcsv2.close()
