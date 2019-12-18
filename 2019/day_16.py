from math import floor

data = "12345678"
data="80871224585914546619083218645595"
data ="59705379150220188753316412925237003623341873502562165618681895846838956306026981091618902964505317589975353803891340688726319912072762197208600522256226277045196745275925595285843490582257194963750523789260297737947126704668555847149125256177428007606338263660765335434914961324526565730304103857985860308906002394989471031058266433317378346888662323198499387391755140009824186662950694879934582661048464385141787363949242889652092761090657224259182589469166807788651557747631571357207637087168904251987880776566360681108470585488499889044851694035762709053586877815115448849654685763054406911855606283246118699187059424077564037176787976681309870931"
data = "111111111"
data =[int(d) for d in data]
print(data)

for phase in range(100):
    
    newdata = []
    for a in range(len(data)):

        g=0
        for i,b in enumerate(data):
            mult =[0,1,0,-1][(floor((i+1)/(a+1)))%4]
            g+=b*mult
        newdata.append(abs(g)%10)
    data=newdata

print(data[0:8])

