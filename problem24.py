import math
p = []
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
no = set()
for col0 in digits:
    no.add(col0)
    for col1 in digits:
	if col1 in no: continue
    	no.add(col1)
	for col2 in digits:
	    if col2 in no: continue
	    no.add(col2)
	    for col3 in digits:
		if col3 in no: continue
		no.add(col3)
		for col4 in digits:
		    if col4 in no: continue
		    no.add(col4)
		    for col5 in digits:
			if col5 in no: continue
			no.add(col5)
			for col6 in digits:
			    if col6 in no: continue
			    no.add(col6)
			    for col7 in digits:
				if col7 in no: continue
				no.add(col7)
				for col8 in digits:
				    if col8 in no: continue
				    no.add(col8)
				    for col9 in digits:
					if col9 in no: continue
					p.append(col0 + col1 + col2 + col3 + col4 + col5 + col6 + col7 + col8 + col9)
				    no.remove(col8)
				no.remove(col7)
			    no.remove(col6)
			no.remove(col5)
		    no.remove(col4)
		no.remove(col3) 
	    no.remove(col2)
	no.remove(col1)    
    no.remove(col0)
print p[999999]
