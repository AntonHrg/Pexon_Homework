import unittest
from urllib import response
from app import app
app.testing = True

class Tests( unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
    
    def tearDown(self) :
        pass

    def test_root(self) :
        response = self.app.get('/', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    #def test_delete(self) :
        #response = self.app.post('/delete/<int:id>', follow_redirects = True)
        #self.assertEqual(response.status_code, 200)

   # def test_update(self) :
      # response = self.app.post('/update/<int:id>', follow_redirects = True)
      # self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()