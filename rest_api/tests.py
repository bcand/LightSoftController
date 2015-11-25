# import requests
# from rest_framework import status
# from django.test import TestCase
#
#
# class Rest_Api_Order_Testing(TestCase):
#     """Testing the REST API"""
#     order = {
#   "identifierList": [],
#   "header": {
#     "orderId": "532a1f27-1ac6-4c8c-ab36-e60f4609c352",
#     "orderType": "FULFILLMENT",
#     "action": "CREATE",
#     "correlationId": "0a1fe509-5ec2-4404-82d4-4adca82402fc",
#     "requester": "LIGHTSOFT_PORTAL",
#     "status": {
#       "statusCode": "CREATED",
#       "statusDate": 1447759226798
#     },
#     "createdAt": 0
#   },
#   "body": {
#     "orderDetails": {
#       "customer": {
#         "identifierList": [],
#         "customerName": "University Z",
#         "label": "Uni Z",
#         "addressList": [],
#         "contactList": [
#           {
#             "identifierList": [],
#             "contactTypeList": [
#               "INITIATOR"
#             ],
#             "firstName": "Mary",
#             "lastName": "Smith",
#             "phoneList": [],
#             "emailList": [
#               {
#                 "emailAddress": "mary@uniz.gr"
#               }
#             ]
#           }
#         ],
#         "accountList": []
#       },
#       "addressList": [],
#       "contactList": [],
#       "attributeList": [],
#       "attributeGroupList": []
#     },
#     "itemList": [
#       {
#         "itemId": "890de319-adc4-440b-a991-cd4dd2aaad7c",
#         "action": "CREATE",
#         "specType": "PRODUCT",
#         "specName": "OPTICAL_LINE_PRODUCT",
#         "status": {
#           "statusCode": "CREATED",
#           "statusDate": 1447759226798
#         },
#         "customerList": [],
#         "addressList": [],
#         "contactList": [],
#         "attributeList": [],
#         "attributeGroupList": []
#       },
#       {
#         "itemId": "5d0b62d1-c053-4a83-ada0-0bd24453d1cb",
#         "parentItemId": "890de319-adc4-440b-a991-cd4dd2aaad7c",
#         "action": "CREATE",
#         "specType": "SERVICE",
#         "specName": "OPTICAL_LINE_SERVICE",
#         "status": {
#           "statusCode": "CREATED",
#           "statusDate": 1447759226798
#         },
#         "customerList": [
#           {
#             "identifierList": [],
#             "customerName": "University ?",
#             "label": "Uni A",
#             "addressList": [
#               {
#                 "identifierList": [],
#                 "addressId": "0abb3119-83c8-4f77-9ce2-16a483ac1789",
#                 "addressTypeList": [
#                   "TERMINATION_POINT"
#                 ],
#                 "addressName": "Termination Point of University A",
#                 "label": "TERMINATION_POINT_A"
#               }
#             ],
#             "contactList": [
#               {
#                 "identifierList": [],
#                 "contactTypeList": [
#                   "BENEFICIARY"
#                 ],
#                 "firstName": "John",
#                 "lastName": "Brown",
#                 "phoneList": [],
#                 "emailList": [
#                   {
#                     "emailAddress": "john@unia.gr"
#                   }
#                 ]
#               }
#             ],
#             "accountList": []
#           },
#           {
#             "identifierList": [],
#             "customerName": "University ?",
#             "label": "Uni B",
#             "addressList": [
#               {
#                 "identifierList": [],
#                 "addressId": "c8ff4273-afaf-4f48-b65e-8c0baa4f9687",
#                 "addressTypeList": [
#                   "TERMINATION_POINT"
#                 ],
#                 "addressName": "Termination Point of University B",
#                 "label": "TERMINATION_POINT_B"
#               }
#             ],
#             "contactList": [
#               {
#                 "identifierList": [],
#                 "contactTypeList": [
#                   "BENEFICIARY"
#                 ],
#                 "firstName": "Nick",
#                 "lastName": "Taylor",
#                 "phoneList": [],
#                 "emailList": [
#                   {
#                     "emailAddress": "dimi@unib.gr"
#                   }
#                 ]
#               }
#             ],
#             "accountList": []
#           }
#         ],
#         "addressList": [],
#         "contactList": [],
#         "attributeList": [
#           {
#             "name": "TYPE",
#             "action": "CREATE",
#             "value": "Type"
#           },
#           {
#             "name": "DESCRIPTION",
#             "action": "CREATE",
#             "value": "Description"
#           },
#           {
#             "name": "SPEED",
#             "action": "CREATE",
#             "value": "Very fast"
#           }
#         ],
#         "attributeGroupList": [
#           {
#             "groupId": "336ff81f-c909-4187-87b1-bed8fe89e8db",
#             "name": "TERMINATION_POINT_CHARACTERISTICS",
#             "action": "CREATE",
#             "attributeList": [
#               {
#                 "name": "CHARACTERISTIC_A",
#                 "action": "CREATE",
#                 "value": "Characteristic A Value"
#               },
#               {
#                 "name": "CHARACTERISTIC_B",
#                 "action": "CREATE",
#                 "value": "Characteristic B Value"
#               },
#               {
#                 "name": "TERMINATION_POINT_ADDRESS",
#                 "action": "CREATE",
#                 "value": "0abb3119-83c8-4f77-9ce2-16a483ac1789"
#               }
#             ]
#           },
#           {
#             "groupId": "0dd2f4b0-f694-4401-ab00-98b01ec271e9",
#             "name": "TERMINATION_POINT_CHARACTERISTICS",
#             "action": "CREATE",
#             "attributeList": [
#               {
#                 "name": "CHARACTERISTIC_A",
#                 "action": "CREATE",
#                 "value": "Characteristic A Value"
#               },
#               {
#                 "name": "CHARACTERISTIC_B",
#                 "action": "CREATE",
#                 "value": "Characteristic B Value"
#               },
#               {
#                 "name": "TERMINATION_POINT_ADDRESS",
#                 "action": "CREATE",
#                 "value": "c8ff4273-afaf-4f48-b65e-8c0baa4f9687"
#               }
#             ]
#           }
#         ]
#       }
#     ]
#   }
# }
#     def test_order_deserialization(self):
#         """Test deserialization of the order.json"""
#         # script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
#         # print script_dir
#         # rel_path = "order.json"
#         # abs_file_path = os.path.join(script_dir, rel_path)
#         # desc = open(abs_file_path, 'r')
#         # order = desc.read()
#         # order = ast.literal_eval(order)
#         r = requests.post("http://127.0.0.1:8000/order/", json=self.order)
#         self.assertEqual(r.status_code, status.HTTP_200_OK)
