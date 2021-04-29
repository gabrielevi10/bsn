#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import requests

formula_tree = {}
pub = rospy.Publisher('formula', String, queue_size=10)
g3t11 = {}
g3t12 = {}
g3t13 = {}
g3t14 = {}
g3t15 = {}
g3t16 = {}
g3t1 = {}

def update():
    global formula_tree, g3t1, g3t11, g3t12, g3t13, g3t14, g3t15, g3t16
    g3t1 = formula_tree['subNodes'][0]['subNodes'][0]['subNodes'][0]
    g3t11 = formula_tree['subNodes'][0]['subNodes'][0]['subNodes'][0]['subNodes'][0]
    g3t12 = formula_tree['subNodes'][0]['subNodes'][0]['subNodes'][0]['subNodes'][1]
    g3t13 = formula_tree['subNodes'][0]['subNodes'][0]['subNodes'][0]['subNodes'][2]
    g3t14 = formula_tree['subNodes'][0]['subNodes'][0]['subNodes'][0]['subNodes'][3]
    g3t15 = formula_tree['subNodes'][0]['subNodes'][0]['subNodes'][0]['subNodes'][4]
    g3t16 = formula_tree['subNodes'][0]['subNodes'][0]['subNodes'][0]['subNodes'][5]

def setup():
    global formula_tree
    rospy.init_node('formula_accessor', anonymous=True)
    formula_tree = make_get_request('reliability', 'BSN_1619661787700', 'G1')
    update()
    pub.publish(formula_tree['formula'])
    

def get_task(goal):
    global g3t1, g3t11, g3t12, g3t13, g3t14, g3t15, g3t16
    if goal == 'G3_T1_1': 
        return g3t11
    elif goal == 'G3_T1_2': 
        return g3t12
    elif goal == 'G3_T1_3': 
        return g3t13
    elif goal == 'G3_T1_4': 
        return g3t14
    elif goal == 'G3_T1_5': 
        return g3t15
    elif goal == 'G3_T1_6':
        return g3t16
  

# GET
def make_get_request(reliCost, id, goal):
    response = requests.get('http://pistargodatcc.herokuapp.com/formula/' + reliCost + '?id=' + id + '&goal=' + goal)
    formula_tree = response.json()
    rospy.loginfo('Got the formula tree')
    return formula_tree


def get_formula_tree(data):
    reliCost, id, goal = str(data).split(';')
    return make_get_request(reliCost, id, goal)

def get_formula_callback(data):
    global formula_tree
    d = data.data
    rospy.loginfo('Data received from sub: ' + d)
    
    if not formula_tree:
        formula_tree = get_formula_tree(d)
        
    pub.publish(formula_tree['formula'])
    # rospy.loginfo('Published the formula ' + formula_tree['formula'])  

def remove_task(data):
    global g3t1, g3t16
    reliCost, id, goal = str(data).split(';')
    task = get_task(goal)
    g3t1['subNodes'].remove(task)
    response = requests.put('http://pistargodatcc.herokuapp.com/formula/' + reliCost + '?id=' + id + '&goal=G3_T1&shouldPersist=false', json=g3t1)
    formula_tree = response.json()
    rospy.loginfo('Edited the formula tree')
    return formula_tree 

def add_task(data):
    global g3t1, g3t16
    reliCost, id, goal = str(data).split(';')
    task = get_task(goal)
    g3t1['subNodes'].append(task)
    response = requests.put('http://pistargodatcc.herokuapp.com/formula/' + reliCost + '?id=' + id + '&goal=G3_T1&shouldPersist=false', json=g3t1)
    formula_tree = response.json()
    rospy.loginfo('Edited the formula tree')
    return formula_tree 


def remove_task_callback(data):
    global formula_tree
    d = data.data
    rospy.loginfo('Data received from sub: ' + d)

    formula_tree = remove_task(d)
    g3t1 = formula_tree['subNodes'][0]['subNodes'][0]['subNodes'][0]

    pub.publish(formula_tree['formula'])

def add_task_callback(data):
    global formula_tree
    d = data.data
    rospy.loginfo('Data received from sub: ' + d)

    formula_tree = add_task(d)
    g3t1 = formula_tree['subNodes'][0]['subNodes'][0]['subNodes'][0]

    pub.publish(formula_tree['formula'])

def body():
    rospy.Subscriber("get_formula", String, get_formula_callback)
    rospy.Subscriber("remove_task", String, remove_task_callback)
    rospy.Subscriber("add_task", String, add_task_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        setup()
        body()
    except rospy.ROSInterruptException:
        pass