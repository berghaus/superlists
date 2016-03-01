from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Charlie has heard of a cool new online app. He goes to check out the homepage
        self.browser.get(self.server_url)

        # Charlie notices that the header and page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy peacock feathers" into a text box (Charlie likes tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When he hits enter, he is taken to a new URL, and the page lists
        # "1: Buy peacock feathers" as an item in the to-do list table
        inputbox.send_keys(Keys.ENTER)
        charlie_list_url = self.browser.current_url
        self.assertRegex(charlie_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting him to add another item. He
        # enters "Use peacock feathers to make a fly" (very methodical Charlie!)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, now with both items on the lists
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # A new user, Louise, comes along to the site

        ## We use a new browser session to ensure that no information of
        ## Charlie's session is coming through from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Louise visits the home page. There is no sign of Charlie's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Louise starts a new list by entering a new item. She is less
        # interesting than Charlie ...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Louise gets her own unique url
        louise_list_url = self.browser.current_url
        self.assertRegex(louise_list_url, '/lists/.+')
        self.assertNotEqual(louise_list_url, charlie_list_url)

        # Again, there is no trace of Charlie's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go to sleep
