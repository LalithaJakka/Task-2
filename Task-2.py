#li=input().split(',')
li=["hello@dhruvsoft.com","jhon@dhruvsoft.com","bob@goggle.com","alice@amazon.com",
"william@salesforce.com","jhon@heroku.com","chiru@nestuite.com","venky@dhruvsoft.com",
"naveen@zoho.com","doe@zoho.com","aws@dhruvsoft.com","rgv@sivio.com","pawan@netsuite.com",
"welcome@dhruvsoft.com"]
nli=[]
eli=[]
for a in li:
  print(a)
dic={}
for i in range(len(li)):
    nli.append(li[i].split('@'))
    eli.append(nli[i][1])
for b in nli:
  print(b)
for c in li:
  print(c)
seli=list(set(eli))
print(seli)
leadlist=[]
for i in range(len(seli)):
    leadlist.append([])
    leadlist[i].append(seli[i])
    for j in range(len(eli)):
        if seli[i]==nli[j][1]:
            leadlist[i].append(nli[j][0])
    dic[seli[i]]=eli.count(seli[i])
for d in leadlist:
  print(d)
print(dic)
