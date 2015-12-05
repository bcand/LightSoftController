

# class restTesting(TestCase):
#     """
#     Test for checking if the rest_api is responsive. Note that the server needs to be running
#     """
#
#     def setUp(self):
#         self.factory = APIRequestFactory(enforce_csrf_checks=True)
#         self.url = 'http://127.0.0.0.1:8080/albums/'
#
#         module_dir = os.path.dirname(__file__)  # get current directory
#         file_path = os.path.join(module_dir, 'order.json')
#
#
#
#     def test_if_can_post_random_json(self):
#         json1= {
#             "key": "value",
#             "key2": "key2",
#             "inner": {
#                 "hey": "ho"
#                     },
#             "lets": "go"
#                 }
#         # print "json1 is %s" %type(json1)
#         r = self.factory.post(self.url, json1,  format='json')
#         #using rest_album view function to generate the responce
#         response= rest_album(r)
#         self.assertEqual(response.status_code , status.HTTP_200_OK)
#
#     def test_if_can_post_order(self):
#         """test how the rest_api responds when feeding the order.json"""
#
#         #read file contents
#         module_dir = os.path.dirname(__file__)  # get current directory
#         file_path = os.path.join(module_dir, 'order.json') #open order.json located in the same folder
#         file_desc = open(file_path,'r')
#         order=file_desc.read()
#         order=ast.literal_eval(order) # convert order to dictionary
#         print  type(order)
#         r = self.factory.post(self.url, order,  format='json')
#         #using rest_album view function to generate the responce
#         response= rest_album(r)
#         self.assertEqual(response.status_code , status.HTTP_200_OK)