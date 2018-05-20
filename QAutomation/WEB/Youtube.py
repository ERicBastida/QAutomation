import QAWebTest

# class videoTest2(QAWebTest.TestCase):
#
#     def conf(self):
#         self.setURL("https://www.youtube.com/")
#
#     def setUp(self):
#
#
#         super(self.__class__, self).setUp()
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
#     def test_error(self):
#         """ This test should be marked as error one. """
#         raise ValueError
#
#     def test_fail(self):
#         """ This test should fail. """
#         self.assertEqual(1, 2)


class videoTest(QAWebTest.TestCase):

    def conf(self):
        self.setURL("https://www.youtube.com")
        self.setRotatable(True)

    def setUp(self,flag=None):

        self.conf()
        super(self.__class__, self).setUp()

    def test_Search(self):

        self.driver.get(self.getURL())
        self.waitElement(self.driver,10,xpathElement="//input[@id='search']")
        self.driver.find_element_by_xpath("//input[@id='search']").send_keys("La mona jimenez")
        self.driver.find_element_by_xpath("//form[@id='search-form']/button").click()
        self.waitElement(self.driver,10,xpathElement="//*[@id='contents']")




if __name__=="__main__":
    print "aloja"

