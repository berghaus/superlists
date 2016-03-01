from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit an empty
        # list item. She hits Enter on the empty input box

        # The home page rereshes, and there is an error message saying that they
        # list items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversly, she now decides to enter a second blank item

        # She recieves a similar error message

        # And she can correct it by filling in some text
        self.fail('write me!')
