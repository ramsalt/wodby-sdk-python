# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StackServiceImplementation(object):
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
        'default': 'bool',
        'docker_image': 'str',
        'name': 'str',
        'title': 'str'
    }

    attribute_map = {
        'default': 'default',
        'docker_image': 'docker_image',
        'name': 'name',
        'title': 'title'
    }

    def __init__(self, default=None, docker_image=None, name=None, title=None):  # noqa: E501
        """StackServiceImplementation - a model defined in Swagger"""  # noqa: E501

        self._default = None
        self._docker_image = None
        self._name = None
        self._title = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if docker_image is not None:
            self.docker_image = docker_image
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title

    @property
    def default(self):
        """Gets the default of this StackServiceImplementation.  # noqa: E501


        :return: The default of this StackServiceImplementation.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this StackServiceImplementation.


        :param default: The default of this StackServiceImplementation.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def docker_image(self):
        """Gets the docker_image of this StackServiceImplementation.  # noqa: E501


        :return: The docker_image of this StackServiceImplementation.  # noqa: E501
        :rtype: str
        """
        return self._docker_image

    @docker_image.setter
    def docker_image(self, docker_image):
        """Sets the docker_image of this StackServiceImplementation.


        :param docker_image: The docker_image of this StackServiceImplementation.  # noqa: E501
        :type: str
        """

        self._docker_image = docker_image

    @property
    def name(self):
        """Gets the name of this StackServiceImplementation.  # noqa: E501


        :return: The name of this StackServiceImplementation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StackServiceImplementation.


        :param name: The name of this StackServiceImplementation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """Gets the title of this StackServiceImplementation.  # noqa: E501


        :return: The title of this StackServiceImplementation.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this StackServiceImplementation.


        :param title: The title of this StackServiceImplementation.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if not isinstance(other, StackServiceImplementation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other