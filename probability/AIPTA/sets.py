import unittest

class TestingSets(unittest.TestCase):
    def setUp(self):
        self.bisayaSpeakingStudents = set(list(range(15,31,1)))
        self.waraySpeakingStudents = set(list(range(1,22,1)))
        self.totalStudents = set(list(range(1,31,1)))
        self.dualDialect = set(list(range(15,22,1)))
        self.pureBisayaSpeakers = set(list(range(22,31,1)))
        self.pureWaraySpeakers = self.waraySpeakingStudents.difference(self.dualDialect) 

    def test_total_students_bisaya_waray_equality(self):
        assert self.totalStudents == self.bisayaSpeakingStudents | self.waraySpeakingStudents
        assert self.totalStudents == self.pureBisayaSpeakers | \
                                     self.pureWaraySpeakers  | \
                                     self.dualDialect

    def test_dual_dialect(self):
        # assume students 15 to 21 are dual dialect
        assert self.dualDialect.issubset(self.bisayaSpeakingStudents) & \
               self.dualDialect.issubset(self.waraySpeakingStudents)

    def test_pure_bisaya_speakers(self):
        assert self.pureBisayaSpeakers == self.bisayaSpeakingStudents.difference(self.dualDialect)
        assert len(self.pureBisayaSpeakers) == 9, "Expected is 9"
        assert self.pureBisayaSpeakers not in self.waraySpeakingStudents

    def test_pure_waray_speakers(self):
        assert self.pureWaraySpeakers == set(list(range(1,15,1)))
        assert self.pureWaraySpeakers not in self.bisayaSpeakingStudents

if __name__ == '__main__':
    unittest.main()    
