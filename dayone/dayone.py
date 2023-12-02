def part_one():
    import re;print(sum(int(_[0]+_[-1])for l in open('i', 'r')if (_:=re.sub('\D','',l))))

def part_two():
    mapping={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
    import re;print(sum(list(map(lambda x:[(vals:=sorted([j for sub in[[(str(val),match.start())for match in re.finditer(key,x)]for key,val in mapping.items()if key in x]for j in sub],key=lambda item:item[1])),int(vals[0][0]+vals[-1][0])][1],open('i','r').readlines()))))
    
def solve():
    part_one()
    part_two()
    
if __name__ == "__main__":
    solve()
    