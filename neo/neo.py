#!/opt/rangal/apps/python/venv3/bin/python
from py2neo import NodeSelector
from py2neo import Graph, Node, Relationship

class Neo():
    def __init__(self, hostname='localhost',  password='jy1met2'):
        self.host = hostname
        self.password = password

    def save_node(self, label, properties_dict, unique=True):
        ''' create neo4j node, with a label, and properties '''
        if unique == True:
            length, lst = self.exists_node(label, properties_dict['name'])
            if length > 0: 
               #exists update
               g = Graph(password=self.password)
               b = lst[0]
               g.merge(b)
               for k,v in properties_dict.items():
                   b[k] = v 
               #b['age'] = properties_dict['age']
               #b['x'] = 8
               g.push(b)
          
            else:
                #does not exist, insert new
                g = Graph(password=self.password)
                tx = g.begin()
                a = Node(label, **properties_dict)
                tx.create(a)
                tx.commit()
        else:
            # allow new duplicate nodes, why???
            raise Exception("do not allow duplicate named nodes")

    def exists_node(self, label, name):
        ''' checks to see if a node exists by name '''
        print("lookup ", label, " ",  name)
        g = Graph(password=self.password)
        selector = NodeSelector(g)
        selected = selector.select(label,name = name) 
        ret = list(selected)
        return len(ret), ret

if __name__ == '__main__':
    n = Neo()

    props = {'_id':10000001, 'name':'rhada', 'type':'dog', 'age':15}

    print( n.exists_node('Animal', 'Zoe'))
    props1 = {'_id':10000007, 'name':'Zoe', 'type':'llama', 'age':88888888}
    n.save_node('Animal', props1)
    print( n.exists_node('Animal', 'rhada'))
    print( n.exists_node('Animal', 'Sage'))
    print( n.exists_node('Animal', 'Spyrte'))

    print( n.exists_node('Animal', 'Princess'))
    props3 = {'_id':10000008, 'name':'Princess', 'type':'Labrador', 'age':67}
    n.save_node('Animal', props3)
    print( n.exists_node('Animal', 'Princess'))
