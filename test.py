import unittest
from mock import patch
from src import build_email, send_email


class EmailTests(unittest.TestCase):
    valid_email = {'From': 'A', 'To': 'B', 'Subject': 'Peasant', 'Message': ['In a bottle.']}

    def test_create_valid_email(self):
        expected = self.valid_email
        result = build_email('A', 'B', 'Peasant', ['In a bottle.'])
        self.assertEqual(expected, result)

    @patch('smtplib.SMTP_SSL')
    @patch('ssl.create_default_context')
    @patch('src.build_email', return_value=valid_email)
    def test_send_email(self, stub_email, stub_context, spy_smtp):
        # Arrange
        message = stub_email()

        # Act
        send_email(message, 'password')

        # Assert
        spy_smtp.assert_called_with('smtp.gmail.com', 465, context=stub_context.return_value)
        spy_result = spy_smtp.return_value
        spy_result.login.assert_called_with(message['From'], 'password')
        spy_result.send_message.assert_called_with(message)
        spy_result.quit.assert_called()


if __name__ == '__main__':
    unittest.main()
