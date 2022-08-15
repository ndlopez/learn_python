student_data=[
    {'name':'Cali','id':1,'scores':[68,75,56,81]},
    {'name':'Candice','id':2,'scores':[75,90,64,88]},
    {'name':'Isis','id':3,'scores':[59,74,71,68]},
    {'name':'Amirah','id':4,'scores':[64,58,53,62]},
    ]

def process_stu_dat(data,pass_thr=60,merit_thr=75):
    #perform some basic stats on some student data
    for sdata in data:
        av = sum(sdata['scores'])/float(len(sdata['scores']))
        sdata['avg'] = av
        if av > merit_thr:
            sdata['assess'] = 'passed with merit'
        elif av > pass_thr:
            sdata['assess'] = 'passed'
        else:
            sdata['assess'] = 'failed'
        print("%s's (id:%d) final assessment is: %s"%(sdata['name'],
              sdata['id'],sdata['assess'].upper()))

if __name__ == '__main__':
    process_stu_dat(student_data)
