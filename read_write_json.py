#create an JSON object (dict python)

import json
data = {}
data['people']=[]
data['people'].append({
   'name':'Jayden Jaymes',
   'website':'www.jaydenmichele.com',
   'from':'Rochester, NY'
})
data['people'].append({
   'name':'August Ames',
   'website':'www.august.co.ca',
   'from':'Ontario, Canada'
})
data['people'].append({
   'name':'Keisha Grey',
   'website':'www.lovelykeisha.com',
   'from':'London, UK'
})

with open('mydata.json','w') as outfile:
   json.dump(data,outfile,sort_keys=True,indent=4)

'''Additionally, a JSON file can be
generated via command line like this '''
#echo '{"people":[{"name":"Scott", "website":"stackabuse.com", "from":"Nebraska"}]}' | python3.8 -m json.tool
'''
Also, don't forget that when reading a JSON file
there should'nt be any chars such as single, double quotes 
&, #, etc, instead write the unicode equivalent
like this
\u0027 to print a single quote
\u0022 to print double quotes
\u002f to print a slash
\u005c to print a backslash
more at: https://everythingfonts.com/unicode/basic-latin
'''

