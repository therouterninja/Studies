import unittest
import find_failure

class VersionTestCase(unittest.TestCase):
  def setUp(self):
    self.testdata1 = \
      [("1.1", "GOOD"),
       ("1.2", "GOOD"),
       ("1.3", "GOOD"),
       ("1.5", "GOOD"),
       ("1.6", "GOOD"),
       ("1.9", "GOOD"),
       ("2.0", "GOOD"),
       ("2.2", "GOOD"),
       ("2.4", "GOOD"),
       ("2.6", "GOOD"),
       ("2.7", "BAD"),
       ("2.9", "BAD"),
       ("3.1", "BAD"),
       ("3.2", "BAD"),
       ("3.4", "BAD"),]
    self.testdata2 = \
      [("1.1", "GOOD"),
       ("1.2", "BAD"),]
    self.testdata3 = \
      [("1.1", "GOOD"),
       ("1.2", "BAD"),
       ("1.3", "BAD")]
    self.testdata4 = \
      [("1.1", "GOOD"),
       ("1.2", "GOOD"),
       ("1.3", "BAD")]
    self.testdata5 = \
      [("1.1", "GOOD"),
       ("1.2", "GOOD"),
       ("1.3", "BAD"),
       ("1.4", "BAD")]
    self.testdata6 = \
      [("1.1", "GOOD"),
       ("1.2", "GOOD"),
       ("1.3", "GOOD"),
       ("1.4", "BAD")]

  def testLargeLength(self):
    self.assertEqual(find_failure.FindFailure(self.testdata1, 0, len(self.testdata1)),
                     [('2.6', 'GOOD'), ('2.7', 'BAD')])

  def test2Length(self):
    self.assertEqual(find_failure.FindFailure(self.testdata2, 0, len(self.testdata2)),
                     [('1.1', 'GOOD'), ('1.2', 'BAD')])

  def test3Length(self):
    self.assertEqual(find_failure.FindFailure(self.testdata3, 0, len(self.testdata3)),
                     [('1.1', 'GOOD'), ('1.2', 'BAD')])
    self.assertEqual(find_failure.FindFailure(self.testdata4, 0, len(self.testdata4)),
                     [('1.2', 'GOOD'), ('1.3', 'BAD')])

  def test4Length(self):
    self.assertEqual(find_failure.FindFailure(self.testdata5, 0, len(self.testdata5)),
                     [('1.2', 'GOOD'), ('1.3', 'BAD')])
    self.assertEqual(find_failure.FindFailure(self.testdata6, 0, len(self.testdata6)),
                     [('1.3', 'GOOD'), ('1.4', 'BAD')])

if __name__ == '__main__':
  unittest.main()
