import json,sys
values=json.load(open(sys.argv[1]))
tests=json.load(open(sys.argv[2]))
val={}
for a in values['values']:
    val[a['id']]=a['value']
def func(a):
    if type(a)==dict:
        if'id'in a and a['id']in val:
            a['value']=val[a['id']]
        for k in a:
            func(a[k])
    elif type(a)==list:
        for i in a:
            func(i)
func(tests)
json.dump(tests,open(sys.argv[3],'w'),indent=2)
