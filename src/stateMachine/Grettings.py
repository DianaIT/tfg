#! /usr/bin/env python3
from smach import State
import rospy
from services.Polly import pollySever
from Utils import Utils

class Grettings(State):
    def __init__(self):
        State.__init__(self, outcomes=['2','1','0'], input_keys=['name', 'questions','difficulty'], output_keys=['questions', 'difficulty'])
        self.utils = Utils()

    def execute(self, userdata):
        if not userdata.name:
            return '2'

        self.saveData(userdata)
        self.startTalking(userdata)
        return '1'

    def startTalking(self, userdata):
        message = "Hola, "+ str(userdata.name) + ", soy Jinko. Vamos a empezar..."
        nameAudio = 'grettings-' + userdata.name + ".mp3"
        pollySever.generarAudio(message, nameAudio)

    def saveData(self, userdata):
        rospy.set_param('name', userdata.name)
        rospy.set_param('questions', userdata.questions)
        rospy.set_param('difficulty', userdata.difficulty)
