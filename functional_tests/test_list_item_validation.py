from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit an empty
        # list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # The home page rereshes, and there is an error message saying that they
        # list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy eggs\n')
        self.check_for_row_in_list_table('1: Buy eggs')

        # Perversly, she now decides to enter a second blank item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # She recieves a similar error message
        self.check_for_row_in_list_table('1: Buy eggs')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling in some text
        self.browser.find_element_by_id('id_new_item').send_keys('Make omlette\n')
        self.check_for_row_in_list_table('1: Buy eggs')
        self.check_for_row_in_list_table('2: Make omlette')
