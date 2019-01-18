from collections import defaultdict

class School:
    def __init__(self, name):
        self.name = name
        self._roster = defaultdict(list)
    
    def roster(self):
        return dict(self._roster)
        
    def add_student(self, name, grade):
        self._roster[grade].append(name)
        
    def grade(self, grade):
        return self._roster[grade]
    
    def sort_roster(self):
        self._roster = {k: sorted(v) for k, v in self._roster.items()}
        return self._roster
