# coding: utf-8

"""
    Wodby API Reference

    # Introduction  The Wodby API is organized around REST. Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors. We use built-in HTTP features, like HTTP authentication and HTTP verbs, which are understood by off-the-shelf HTTP clients.  JSON is returned by all API responses, including errors.  # Authentication  Authenticate your account by including your secret key in API requests. You can manage your API keys in the Dashboard. Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.  All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.  Example of authenticated request: ``` curl https://api.wodby.com/api/v3/user -H 'X-API-KEY: YOUR_API_KEY' ```   # noqa: E501

    OpenAPI spec version: 3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RequestAppCreateServices(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enable': 'bool',
        'implementation': 'str',
        'name': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'implementation': 'implementation',
        'name': 'name'
    }

    def __init__(self, enable=None, implementation=None, name=None):  # noqa: E501
        """RequestAppCreateServices - a model defined in Swagger"""  # noqa: E501

        self._enable = None
        self._implementation = None
        self._name = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if implementation is not None:
            self.implementation = implementation
        self.name = name

    @property
    def enable(self):
        """Gets the enable of this RequestAppCreateServices.  # noqa: E501


        :return: The enable of this RequestAppCreateServices.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this RequestAppCreateServices.


        :param enable: The enable of this RequestAppCreateServices.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def implementation(self):
        """Gets the implementation of this RequestAppCreateServices.  # noqa: E501


        :return: The implementation of this RequestAppCreateServices.  # noqa: E501
        :rtype: str
        """
        return self._implementation

    @implementation.setter
    def implementation(self, implementation):
        """Sets the implementation of this RequestAppCreateServices.


        :param implementation: The implementation of this RequestAppCreateServices.  # noqa: E501
        :type: str
        """

        self._implementation = implementation

    @property
    def name(self):
        """Gets the name of this RequestAppCreateServices.  # noqa: E501


        :return: The name of this RequestAppCreateServices.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RequestAppCreateServices.


        :param name: The name of this RequestAppCreateServices.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestAppCreateServices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
