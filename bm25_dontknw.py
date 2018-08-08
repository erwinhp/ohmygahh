Q=tokener
k=2
b=0.75
FinScore=[]
IDF=[]
tmpLbl=[]
for i in graphf:##list Constructed graph
    tmpstr=''
    token=regexp_tokenize(i[0], pattern=r"\s|[\.,;']", gaps=True)
    for ii in token:
        for l in uri3:
           if l[1]==ii:##get the label doc
               tmpstr=tmpstr+' '+str(l[0])
    tmpLbl.append(l[0])
#IDF  
for i in Q:##query
    qi=0##query on D
    N=len(graphf)##How many D
    strLbl=''#get all D Length
    for ii in tmpLbl:
        if (i) in (ii):
            qi=qi+1
        strLbl=strLbl+' '+ii
    tokener=word_tokenize(re.sub(r'''[/.!$%^&*()?'`",:;|0-9+-=]''', '', strLbl).lower())
    lenD=len(tokener)
    AvgLen=lenD/N ##avarage len of all D
    if qi==0:
        qi=1
    IDFq=math.log(N-qi+0.5/qi+0.5)
    IDF.append([IDFq,i])
#TF
for i in tmpLbl:##list doc want to be ranked
    TF=[]
    tmpTF=''
    tmpScore=0
    for j in Q:
        tokener = word_tokenize(re.sub(r'''[/.!$%^&*()?'`",:;|0-9+-=]''', '', i).lower())
        LenToken=(len(tokener))
        count=Counter(tokener)##get counter of word in d
        CountTFq=tokener.count(str(j))##qi,di counting how many qi in di
        keyMax=max(count.keys(), key=(lambda k: count[k]))
        maxTaksen=(count[keyMax])
        TFq=0.5+(0.5*(CountTFq/maxTaksen))
##            tmpTF=tmpTF+' '+str(TFq)
        for IDFq in IDF:
            if IDFq[1]==j:
                score=IDFq[0]*(TFq*(k+1)/TFq+k*(1-b+b*(LenToken/AvgLen)))##score on qi to di
                tmpScore=tmpScore+score
    FinScore.append(tmpScore)
