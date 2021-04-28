#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import requests

formula_tree = {}
pub = rospy.Publisher('formula', String, queue_size=10)

def setup():
    rospy.init_node('formula_accessor', anonymous=True)
    make_get_request('reliability', 'BSN_1619579410796', 'G1')

def make_get_request(reliCost, id, goal):
    response = requests.get('http://pistargodatcc.herokuapp.com/formula/' + reliCost + '?id=' + id + '&goal=' + goal)
    formula_tree = response.json()
    print(formula_tree['formula'])
    rospy.loginfo('Got the formula tree')
    return formula_tree['formula']


def get_formula_tree(data):
    reliCost, id, goal = str(data).split(';')
    return make_get_request(reliCost, id, goal)

def get_formula_callback(data):
    d = data.data
    rospy.loginfo('Data received from sub: ' + d)
  
    get_formula_tree(d)
    print(formula_tree)
    pub.publish(get_formula_tree(d))
    # rospy.loginfo('Published the formula ' + formula_tree['formula'])  

def body():
    rospy.Subscriber("get_formula", String, get_formula_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        setup()
        body()
    except rospy.ROSInterruptException:
        pass