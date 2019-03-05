# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class App(object):
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
        'created': 'int',
        'git_repo_id': 'str',
        'id': 'str',
        'name': 'str',
        'org_id': 'str',
        'status': 'str',
        'title': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'created': 'created',
        'git_repo_id': 'git_repo_id',
        'id': 'id',
        'name': 'name',
        'org_id': 'org_id',
        'status': 'status',
        'title': 'title',
        'updated': 'updated'
    }

    def __init__(self, created=None, git_repo_id=None, id=None, name=None, org_id=None, status=None, title=None, updated=None):  # noqa: E501
        """App - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._git_repo_id = None
        self._id = None
        self._name = None
        self._org_id = None
        self._status = None
        self._title = None
        self._updated = None
        self.discriminator = None

        self.created = created
        if git_repo_id is not None:
            self.git_repo_id = git_repo_id
        self.id = id
        self.name = name
        self.org_id = org_id
        self.status = status
        self.title = title
        self.updated = updated

    @property
    def created(self):
        """Gets the created of this App.  # noqa: E501


        :return: The created of this App.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this App.


        :param created: The created of this App.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def git_repo_id(self):
        """Gets the git_repo_id of this App.  # noqa: E501


        :return: The git_repo_id of this App.  # noqa: E501
        :rtype: str
        """
        return self._git_repo_id

    @git_repo_id.setter
    def git_repo_id(self, git_repo_id):
        """Sets the git_repo_id of this App.


        :param git_repo_id: The git_repo_id of this App.  # noqa: E501
        :type: str
        """
        if git_repo_id is not None and not re.search('^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?$', git_repo_id):  # noqa: E501
            raise ValueError("Invalid value for `git_repo_id`, must be a follow pattern or equal to `/^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?$/`")  # noqa: E501

        self._git_repo_id = git_repo_id

    @property
    def id(self):
        """Gets the id of this App.  # noqa: E501


        :return: The id of this App.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this App.


        :param id: The id of this App.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and not re.search('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this App.  # noqa: E501


        :return: The name of this App.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this App.


        :param name: The name of this App.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this App.  # noqa: E501


        :return: The org_id of this App.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this App.


        :param org_id: The org_id of this App.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501
        if org_id is not None and not re.search('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', org_id):  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must be a follow pattern or equal to `/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._org_id = org_id

    @property
    def status(self):
        """Gets the status of this App.  # noqa: E501


        :return: The status of this App.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this App.


        :param status: The status of this App.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ok", "error", "creating", "deleting"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def title(self):
        """Gets the title of this App.  # noqa: E501


        :return: The title of this App.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this App.


        :param title: The title of this App.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def updated(self):
        """Gets the updated of this App.  # noqa: E501


        :return: The updated of this App.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this App.


        :param updated: The updated of this App.  # noqa: E501
        :type: int
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

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
        if not isinstance(other, App):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
