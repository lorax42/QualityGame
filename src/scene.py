# Text : str
# Antworten : [str]
# indexRightAnswer : int

import character as c

class scene:

# instance attributes
    def __init__(self, text, answers, influence, indexRA, requiredLevel):
        self.m_text = text
        self.m_answers = answers
        self.m_influ = influence
        self.m_index = indexRA
        self.requiredlvl = requiredLevel

# instance method
    def call(self):
        print(self.m_text)
        i = 0
        for x in self.m_answers:
            print(i + ") " + x)
            i += 1
        ans = int(input("> "))
        c.addPunkte(self.influ[ans])

