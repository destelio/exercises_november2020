import itertools 
  
def create_sentences(a,b,c):
    
# initializing list of list AND sort them alphabetically, first  
    a.sort()
    b.sort()
    c.sort()
    all_list = [a,b,c]

    res = list(itertools.product(*all_list))

    #result_str = ""
    list_all = list(res)
    str_all =""
    
    z = len(list_all)
    #print(z)
    for item in list_all:
        z1 = list_all.index(item)
        #print(item)
        list_a = list(item)
        #print(type(list_a))
        #print(list_a)
        k = len(list_a)

        #print(k)
        for i in range(k):
            ## print(z1)
            

            f = list_a[i]
            #print(f)
            if i ==  k-1:
                if z1 == z-1:
                    str_all = str_all+" "+f+"."
                else:
                    str_all = str_all+" "+f+". "
            elif i == 0:
                str_all = str_all+""+f

            else:
                str_all = str_all+" "+f
    return str_all


f1 = ["Mark", "Mary"]
f2 = ["loves", "hates"]
f3 = ["apples", "bananas"]

def test_answer():
#assert inc(3) == 5
    assert create_sentences(f1, f2, f3) == "Mark hates apples. Mark hates bananas. Mark loves apples. Mark loves bananas. Mary hates apples. Mary hates bananas. Mary loves apples. Mary loves bananas."