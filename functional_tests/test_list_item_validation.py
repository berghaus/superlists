from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit an empty
        # list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page rereshes, and there is an error message saying that they
        # list items cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        self.get_item_input_box().send_keys('Buy eggs\n')
        self.check_for_row_in_list_table('1: Buy eggs')

        # Perversly, she now decides to enter a second blank item
        self.get_item_input_box().send_keys('\n')

        # She recieves a similar error message
        self.check_for_row_in_list_table('1: Buy eggs')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling in some text
        self.get_item_input_box().send_keys('Make omlette\n')
        self.check_for_row_in_list_table('1: Buy eggs')
        self.check_for_row_in_list_table('2: Make omlette')

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Get the flag\n')
        self.check_for_row_in_list_table('1: Get the flag')

        # She accidentally adds the item again
        self.get_item_input_box().send_keys('Get the flag\n')

        # She sees a helpful error message
        self.check_for_row_in_list_table('1: Get the flag')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # Edith starts a new list in a way that causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # She starts typing in the input box to clear the error
        self.get_item_input_box().send_keys('a')

        # She is pleased to see the error message dissapear
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
