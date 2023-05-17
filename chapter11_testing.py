import unittest

def get_formatted_name(first, last, middle = ''):
    """Generate a neatly formatted full name"""
    if middle != '':
        fullname = f"{first} {middle} {last}"
    else:
        fullname = f"{first} {last}"
    return fullname.title()


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        """DO name like Janis Joplin work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('Janis', 'Joplin', 'Janis')
        self.assertEqual(formatted_name, "Janis Janis Joplin")



##examples of class test
class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)
    
    def store_response(self, response):
        self.responses.append(response)

    def show_results(self):
        for item in self.responses:
            print(f' - {item}')

class TestAnonymousSurvey(unittest.TestCase):
    
    def setUp(self):
        question = "What language did you forst learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']


    def test_store_single_response(self):
        question = "Whant language did you forst learn to speak?"
        my_survey = AnonymousSurvey(question)
        #my_survey.store_response("polish")
        responses = ['English', 'Spanish', 'Mandarin']
        for item in responses:
            my_survey.store_response(item)
        self.assertIn('English', my_survey.responses)





if __name__ == '__main__':
    unittest.main()



