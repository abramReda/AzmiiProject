

import pyttsx


speaker = pyttsx.init()

speaker.setProperty('rate',150)

rate = speaker.getProperty('rate')
print rate

speaker.say(" hallo my name is azmi")
speaker.say("and iam a robot")
speaker.say("i was created at El shorouk academy")
speaker.say("under the supervision fo doctor Abo el oyoun")
speaker.say("and this is the last update and final version to me")
speaker.say("in this version my team give me the abillity of moving my hand like this")
speaker.say("as well as the ability of moving my head")
speaker.say("and they spent some effort to enhace my program nad my speech communication")
speaker.say("and mix all this new features in executable program make me dane")
speaker.say("and when i say dance i mean literally robotics danse and i will show it to you")


speaker.runAndWait()

