from datetime import datetime

def get_fest()
    date_format = "%m/%d"
    d=datetime.now().month

    fest={"12":"christmas","2":"valentines day","10":"halloween","8":"independance day"}
    temp=[]
    var=100
    for key in fest:
        if(int(key)-d<0):
            temp.append(12+int(key)-d)
        else:
            temp.append(int(key)-d)

    festival=fest[str(min(temp)+d)]
    return festival
