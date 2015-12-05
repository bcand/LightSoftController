class Status():
    def __init__(self, statusCode, statusDate):
        """
        Create a status Object
        :param statusCode: The status Code
        :param statusDate: The status Date
        :return: status Obj
        """
        self.statusCode = statusCode
        self.statusDate = statusDate


class Header():
    def __init__(self, orderId, orderType, action, correlationId, requester, status, createdAt):
        """
        Create a Header Object
        :param orderId: The order Id
        :param orderType: The Order Type
        :param action: The Order Action
        :param correlationId: The correlation Id
        :param requester: The Requester
        :param status: A Status Object
        :param createdAt: Time created
        :return: Header Object
        """
        self.orderId = orderId
        self.orderType = orderType
        self.action = action
        self.correlationId = correlationId
        self.requester = requester
        self.status = status
        self.createdAt = createdAt


class Email():
    def __init__(self, emailAddress):
        """
        Create an Email Object
        :param emailAddress: The email address
        :return: Email Object
        """
        self.emailAddress = emailAddress


class Phone():
    def __init__(self, phone):
        """ Create a Phone object
        :param phone: The phone
        :return: The Phone Object
        """
        self.phone = phone


class Contact():
    def __init__(self, identifierList, contactTypeList, firstName, lastName, phoneList, emailList):
        """
        Create a Contact
        :param identifierList: The identifier list
        :param contactTypeList: The contact type list
        :param firstName: The contact's firstname
        :param lastName: The contact's lastname
        :param phoneList: The contact's phone list
        :param emailList: The contact's mail list
        :return: A Contact Object
        """
        self.identifierList = identifierList
        self.contactTypeList = contactTypeList
        self.firstName = firstName
        self.lastName = lastName
        self.phoneList = phoneList
        self.emailList = emailList


class Attribute():
    def __init__(self, name, action, value):
        """
        Create an attribute
        :param name: the name of the attribute
        :param action: the action of the attribute
        :param value: the value of the attribute
        :return: The attribute object
        """
        self.name = name
        self.action = action
        self.value = value


class GroupAttribute():
    def __init__(self, groupId, name, action, attributeList):
        """
        Create a GroupAttribute object
        :param groupId: The id of the group
        :param name: The name
        :param action: The corresponding action
        :param attributeList: The list of attributes
        :return: The GroupAttribute object
        """
        self.groupId = groupId
        self.name = name
        self.action = action
        self.attributeList = attributeList


class Address():
    def __init__(self, identifierList, addressId, addressTypeList, addressName, label):
        """
        Create and Address object
        :param identifierList: The identifier list
        :param addressId: The address id
        :param addressTypeList: The address type list
        :param addressName: The address name
        :param label: The corresponding label
        :return: The Address object
        """
        self.identifierList = identifierList
        self.addressId = addressId
        self.addressTypeList = addressTypeList
        self.addressName = addressName
        self.label = label


class Customer():
    def __init__(self, identifierList, customerName, label, addressList, contactList, accountList):
        """
        Create a Customer object
        :param identifierList: The identifier list
        :param customerName: The customer name
        :param label: The label
        :param addressList: The list of Addresses
        :param contactList: The list of Contact
        :param accountList: The list of Accounts
        :return: The Customer object
        """
        self.identifierList = identifierList
        self.customerName = customerName
        self.label = label
        self.addressList = addressList
        self.contactList = contactList
        self.accountList = accountList


class Item():
    def __init__(self, itemId, action, specType, specName, status, customerList, addressList, contactList,
                 attributeList, attributeGroupList, parentItemId='empty'):
        """ Create an Item object
        :param itemId: The item id
        :param action: The action
        :param specType: The specType
        :param specName: The specName
        :param status: the status
        :param customerList: The customer list
        :param addressList: The address list
        :param contactList: The contact list
        :param attributeList: The attribute list
        :param attributeGroupList: The attributeGroup list
        :param parentItemId: The parentItemId if present, defaults to 'empty'
        :return: The Item Object
        """
        self.itemId = itemId

        self.action = action
        self.specType = specType
        self.specName = specName
        self.status = status
        self.customerList = customerList
        self.addressList = addressList
        self.contactList = contactList
        self.attributeList = attributeList
        self.attributeGroupList = attributeGroupList
        self.parentItemId = parentItemId


class OrderDetails():
    def __init__(self, customer, addressList, contactList, attributeList, attributeGroupList):
        """
        Create an OrderDetail object
        :param customer: The customer object
        :param addressList: The Address list
        :param contactList: The Contact list
        :param attributeList: The Attribute list
        :param attributeGroupList:  The AttributeGroup list
        :return: An OrderDetail obj
        """
        self.customer = customer
        self.addressList = addressList
        self.contactList = contactList
        self.attributeList = attributeList
        self.attributeGroupList = attributeGroupList


class Body():
    def __init__(self, orderDetails, itemList):
        """
        Create a Body object
        :param orderDetails: The orderDetails
        :param itemList: The itemList
        :return: A Body object
        """
        self.orderDetails = orderDetails
        self.itemList = itemList


class Order():
    def __init__(self, identifierList, header, body):
        """
        Create an Order object
        :param identifierList: The identifierList
        :param header: The header object
        :param body: The body object
        :return: An Order object
        """
        self.identifierList = identifierList
        self.header = header
        self.body = body




############ TESTING ONLY #############
class InnerSimple(object):
    def __init__(self, friend):
        self.friend = friend


class Simple(object):
    def __init__(self, age, name, lastname, contactList):
        self.age = age
        self.name = name
        self.lastname = lastname
        self.contactList = contactList


