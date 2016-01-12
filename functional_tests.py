from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicit_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Charlie has heard of a cool new online app. He goes to check out the homepage
        self.browser.get('http://localhost:8000')

        # Charlie notices that the page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "By peacock feathers" into a text box (Charlie likes tying fly-fishing lures)

        # When he hits enter, the page updates, and now the page lists
        # "1: By peacock feathers"

        # There is still a text box inviting him to add another item. He
        # enters "Use peacock feathers to make a fly" (very methodical Charlie!)

        # The page updates again, now with both items on the lists

        # Charlie wonders whether the site will remeber his list. Then he sees that the
        # site has generated a unique URL for him -- there is some explanatory text to
        # this effect

        # He visits the URL and his to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
