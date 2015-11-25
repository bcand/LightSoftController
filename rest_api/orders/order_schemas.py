from marshmallow import Schema, fields, post_load

from .order_classes import *


class StatusSchema(Schema):
    """
    The equivalent Schema of Status Class
    """
    statusCode = fields.Str()
    statusDate = fields.Int()

    @post_load
    def save_object(self, data):
        """
        Construct a Status object
        :param data: The **kwargs of the Status __init__()
        :return: A Status object
        """
        return Status(**data)


class HeaderSchema(Schema):
    """
    The equivalent Schema of Header Class
    """
    orderId = fields.UUID()
    orderType = fields.Str()
    action = fields.Str()
    correlationId = fields.UUID()
    requester = fields.Str()
    status = fields.Nested(StatusSchema)
    createdAt = fields.Int()

    @post_load
    def save_object(self, data):
        """
        Construct a Header object
        :param data: The **kwargs for the Header __init__()
        :return: A Header object
        """
        return Header(**data)


# ========================================================

class AttributeSchema(Schema):
    """
    The equivalent Schema of Attribute Class
    """
    name = fields.Str()
    action = fields.Str()
    value = fields.Str()

    @post_load
    def save_object(self, data):
        """
        Construct an Attribute object
        :param data: The **kwargs for the Attribute __init__()
        :return: An Attribute object
        """
        return Attribute(**data)


class GroupAttributeSchema(Schema):
    """
    The equivalent Schema of Attribute Class
    """
    groupId = fields.UUID()
    name = fields.Str()
    action = fields.Str()
    attributeList = fields.Nested(AttributeSchema, many=True, allow_none=True)

    @post_load
    def save_object(self, data):
        """
        Construct a GroupAttribute object
        :param data: The **kwargs for the GroupAttribute __init__()
        :return: A GroupAttribute object
        """
        return GroupAttribute(**data)


class EmailSchema(Schema):
    """
    The equivalent Schema of Email Class
    """
    emailAddress = fields.Email()

    @post_load
    def save_object(self, data):
        """
        Construct an Email object
        :param data: The **kwargs for the Email __init__()
        :return: An Email object
        """
        return Email(**data)


class PhoneSchema(Schema):
    """
    The equivalent Schema of Phone Class
    """
    phone = fields.Int()

    @post_load
    def save_object(self, data):
        """
        Construct a Phone object
        :param data: The **kwargs for the Phone __init__()
        :return: A Phone object
        """
        return Phone(**data)


class ContactSchema(Schema):
    """
    The equivalent Schema of Contact Class
    """
    identifierList = fields.List(fields.Str(), many=True, allow_none=True)
    contactTypeList = fields.List(fields.Str(), many=True, allow_none=True)
    firstName = fields.Str()
    lastName = fields.Str()
    phoneList = fields.Nested(PhoneSchema, many=True, allow_none=True)
    emailList = fields.Nested(EmailSchema, many=True, allow_none=True)

    @post_load
    def save_object(self, data):
        """
        Construct a Contact object
        :param data: The **kwargs for the Contact __init__()
        :return: A Contact object
        """
        return Contact(**data)


class AddressSchema(Schema):
    """
    The equivalent Schema of Address Class
    """
    identifierList = fields.List(fields.Str(), many=True, allow_none=True)
    addressId = fields.UUID()
    addressTypeList = fields.List(fields.Str(), many=True, allow_none=True)
    addressName = fields.Str()
    label = fields.Str()

    @post_load
    def save_object(self, data):
        """
        Construct an Address object
        :param data: The **kwargs for the Address __init__()
        :return: An Address object
        """
        return Address(**data)


class CustomerSchema(Schema):
    """
    The equivalent Schema of Customer Class
    """
    identifierList = fields.List(fields.Str(), many=True, allow_none=True)
    customerName = fields.Str()
    label = fields.Str()
    addressList = fields.Nested(AddressSchema, many=True, allow_none=True)
    contactList = fields.Nested(ContactSchema, many=True, allow_none=True)
    accountList = fields.List(fields.Str(), many=True,
                              allow_none=True)  # <-------------------------- we dont have any account in the order

    @post_load
    def save_object(self, data):
        """
        Construct a Customer object
        :param data: The **kwargs for the Customer __init__()
        :return: A Customer object
        """
        return Customer(**data)


class ItemSchema(Schema):
    """
    The equivalent Schema of Item Class
    """
    itemId = fields.UUID()
    parentItemId = fields.UUID(allow_none=False, default="none")
    action = fields.Str()
    specType = fields.Str()
    specName = fields.Str()
    status = fields.Nested(StatusSchema)
    customerList = fields.Nested(CustomerSchema, many=True, allow_none=True)
    addressList = fields.Nested(AddressSchema, many=True, allow_none=True)
    contactList = fields.Nested(ContactSchema, many=True, allow_none=True)
    attributeList = fields.Nested(AttributeSchema, many=True, allow_none=True)
    attributeGroupList = fields.Nested(GroupAttributeSchema, many=True, allow_none=True)

    @post_load
    def save_object(self, data):
        """
        Construct an Item object
        :param data: The **kwargs for the Item __init__()
        :return: An Item object
        """
        return Item(**data)


class OrderDetailsSchema(Schema):
    """
    The equivalent Schema of OrderDetail Class
    """
    customer = fields.Nested(CustomerSchema)
    addressList = fields.Nested(AddressSchema, many=True, allow_none=True)
    contactList = fields.Nested(ContactSchema, many=True, allow_none=True)
    attributeList = fields.Nested(AttributeSchema, many=True, allow_none=True)
    attributeGroupList = fields.Nested(GroupAttributeSchema, many=True, allow_none=True)

    @post_load
    def save_object(self, data):
        """
        Construct an OrderDetails object
        :param data: The **kwargs for the OrderDetails __init__()
        :return: An OrderDetails object
        """
        return OrderDetails(**data)


class BodySchema(Schema):
    """
    The equivalent Schema of Body Class
    """
    orderDetails = fields.Nested(OrderDetailsSchema)
    itemList = fields.Nested(ItemSchema, many=True)

    @post_load
    def save_object(self, data):
        """
        Construct a Body object
        :param data: The **kwargs for the Body __init__()
        :return: A Body object
        """
        return Body(**data)


class OrderSchema(Schema):
    """
    The equivalent Schema of Order Class
    """
    identifierList = fields.List(fields.Str(), many=True, allow_none=True)
    header = fields.Nested(HeaderSchema)
    body = fields.Nested(BodySchema)

    @post_load
    def save_object(self, data):
        """
        Construct an Order object
        :param data: The **kwargs for the Order __init__()
        :return: An Order object
        """
        return Order(**data)



###########TESTING ONLY#############

class InnerSimpleSchema(Schema):
    friend = fields.Str()

    @post_load
    def make_inner_simple(self, data):
        return InnerSimple(**data)


class SimpleSchema(Schema):
    age = fields.Int()
    name = fields.Str()
    lastname = fields.Str()
    mylist = fields.List(fields.Str(), many=True)

    contactList = fields.Nested(InnerSimpleSchema, many=True)

    @post_load
    def make_simple(self, data):
        return Simple(**data)

