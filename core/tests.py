from django.test import TestCase
from unittest.mock import MagicMock
from .reply_factory import generate_bot_responses, record_current_answer, get_next_question, generate_final_response
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST

class ReplyFactoryTests(TestCase):

    def setUp(self):
        self.session = MagicMock()
        self.session.get = MagicMock(return_value=None)
        self.session.save = MagicMock()

    def test_generate_bot_responses_welcome(self):
        message = "start"
        self.session.get = MagicMock(return_value=None)  # Simulate no current_question_id in session
        
        responses = generate_bot_responses(message, self.session)
        
        self.assertIn(BOT_WELCOME_MESSAGE, responses)

    def test_record_current_answer_valid(self):
        answer = "Test Answer"
        current_question_id = 0
        
        success, error = record_current_answer(answer, current_question_id, self.session)
        
        self.assertTrue(success)
        self.assertEqual(error, "")
        self.session.save.assert_called_once()

    def test_record_current_answer_invalid(self):
        answer = ""
        current_question_id = 0
        
        success, error = record_current_answer(answer, current_question_id, self.session)
        
        self.assertFalse(success)
        self.assertNotEqual(error, "")

    def test_get_next_question(self):
        current_question_id = 0
        
        next_question, next_question_id = get_next_question(current_question_id)
        
        self.assertIsNotNone(next_question)
        self.assertEqual(next_question_id, 1)

    def test_generate_final_response(self):
        # Simulate answers in the session
        self.session.get = MagicMock(return_value={
            0: "Answer 1",
            1: "Answer 2"
        })
        
        response = generate_final_response(self.session)
        
        self.assertIn("Your score is", response)

# Running the tests
if __name__ == "__main__":
    import unittest
    unittest.main()
