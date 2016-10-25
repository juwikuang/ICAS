#file content:
#dm1g	+	AT1G78080.1	1396	GTGACGGAATTTGAAGAGTCCACCGCTGGATCTTGGCCGTTGTCGGAC	IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII	0	8:G>A,34:C>G
#dm4g	+	AT5G07220.1	565	AGGTCAAAGCTTGTTGTTAAAGAAGATCCAATTTCTCAGGAGAAACGT	IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII	0	0:C>A
#dm5g	+	AT2G41840.1	843	GTCGATTGCCTTCAGAAGACTTACGGATTCCTTACCCCAGAGTTCTGG	IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII	0	0:T>G
#dm6g	+	AT3G03470.1	995	GAGTTTCTTAACGCAGCTACGGATCCAACGGCGACGTCGATGCAGTGG	IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII	0	
#dm7g	+	AT2G15960.1	1	ACTCTCGTTCATAATGAGATATTAAGATCAACAAAAGGAAAGAATGGC	IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII	0	0:T>A
#dm9g	+	AT1G15350.1	530	GATGTAAATCAAGGTCTTCTCCTTTGGAATCAGACACGGGAGCGTTGG	IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII	2	0:T>G,20:T>C
#dm9g	+	AT1G15350.3	493	GATGTAAATCAAGGTCTTCTCCTTTGGAATCAGACACGGGAGCGTTGG	IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII	2	0:T>G,20:T>C

countDict={}
f=open("F:\\JIC\\COUNT-FINDER\\chunk-1-k0-L48.map",mode="r")
for line in f.readlines() :
    if(line==""):
        continue
    
    arr=line.split("\t")
    if(len(arr)<=3):
        continue
    key = arr[2]+","+arr[3]
    if(countDict.has_key(key)):
        countDict[key]=countDict[key]+1
    else:
        countDict[key]=1
f.close()

f=open("F:\\JIC\\COUNT-FINDER\\result.csv","w")
f.write("target,position,count\n")
for key in countDict:
    f.write(key+","+str( countDict[key])+"\n")
f.close()
#print(countDict)