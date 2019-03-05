# coding: utf-8

"""
    Wodby API Client

    Wodby Developer Documentation https://wodby.com/docs/dev  # noqa: E501

    OpenAPI spec version: 3.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wodby.models.instance_type import InstanceType  # noqa: F401,E501
from wodby.models.request_app_create_git import RequestAppCreateGit  # noqa: F401,E501
from wodby.models.request_app_create_services import RequestAppCreateServices  # noqa: F401,E501


class RequestAppCreate(object):
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
        'deployment_type': 'str',
        'docroot': 'str',
        'git': 'RequestAppCreateGit',
        'instance_name': 'str',
        'instance_title': 'str',
        'instance_type': 'InstanceType',
        'name': 'str',
        'org_id': 'str',
        'post_deployment': 'bool',
        'server_id': 'str',
        'services': 'list[RequestAppCreateServices]',
        'sitename': 'str',
        'stack_id': 'str',
        'title': 'str'
    }

    attribute_map = {
        'deployment_type': 'deployment_type',
        'docroot': 'docroot',
        'git': 'git',
        'instance_name': 'instance_name',
        'instance_title': 'instance_title',
        'instance_type': 'instance_type',
        'name': 'name',
        'org_id': 'org_id',
        'post_deployment': 'post_deployment',
        'server_id': 'server_id',
        'services': 'services',
        'sitename': 'sitename',
        'stack_id': 'stack_id',
        'title': 'title'
    }

    def __init__(self, deployment_type='vanilla', docroot=None, git=None, instance_name=None, instance_title=None, instance_type=None, name=None, org_id=None, post_deployment=None, server_id=None, services=None, sitename=None, stack_id=None, title=None):  # noqa: E501
        """RequestAppCreate - a model defined in Swagger"""  # noqa: E501

        self._deployment_type = None
        self._docroot = None
        self._git = None
        self._instance_name = None
        self._instance_title = None
        self._instance_type = None
        self._name = None
        self._org_id = None
        self._post_deployment = None
        self._server_id = None
        self._services = None
        self._sitename = None
        self._stack_id = None
        self._title = None
        self.discriminator = None

        if deployment_type is not None:
            self.deployment_type = deployment_type
        if docroot is not None:
            self.docroot = docroot
        if git is not None:
            self.git = git
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_title is not None:
            self.instance_title = instance_title
        if instance_type is not None:
            self.instance_type = instance_type
        self.name = name
        self.org_id = org_id
        if post_deployment is not None:
            self.post_deployment = post_deployment
        self.server_id = server_id
        if services is not None:
            self.services = services
        if sitename is not None:
            self.sitename = sitename
        self.stack_id = stack_id
        if title is not None:
            self.title = title

    @property
    def deployment_type(self):
        """Gets the deployment_type of this RequestAppCreate.  # noqa: E501


        :return: The deployment_type of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this RequestAppCreate.


        :param deployment_type: The deployment_type of this RequestAppCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["vanilla", "git", "ci"]  # noqa: E501
        if deployment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_type, allowed_values)
            )

        self._deployment_type = deployment_type

    @property
    def docroot(self):
        """Gets the docroot of this RequestAppCreate.  # noqa: E501


        :return: The docroot of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._docroot

    @docroot.setter
    def docroot(self, docroot):
        """Sets the docroot of this RequestAppCreate.


        :param docroot: The docroot of this RequestAppCreate.  # noqa: E501
        :type: str
        """

        self._docroot = docroot

    @property
    def git(self):
        """Gets the git of this RequestAppCreate.  # noqa: E501


        :return: The git of this RequestAppCreate.  # noqa: E501
        :rtype: RequestAppCreateGit
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this RequestAppCreate.


        :param git: The git of this RequestAppCreate.  # noqa: E501
        :type: RequestAppCreateGit
        """

        self._git = git

    @property
    def instance_name(self):
        """Gets the instance_name of this RequestAppCreate.  # noqa: E501


        :return: The instance_name of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this RequestAppCreate.


        :param instance_name: The instance_name of this RequestAppCreate.  # noqa: E501
        :type: str
        """
        if instance_name is not None and not re.search('^[a-z0-9][a-z0-9-]{0,18}[a-z0-9]$', instance_name):  # noqa: E501
            raise ValueError("Invalid value for `instance_name`, must be a follow pattern or equal to `/^[a-z0-9][a-z0-9-]{0,18}[a-z0-9]$/`")  # noqa: E501

        self._instance_name = instance_name

    @property
    def instance_title(self):
        """Gets the instance_title of this RequestAppCreate.  # noqa: E501


        :return: The instance_title of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._instance_title

    @instance_title.setter
    def instance_title(self, instance_title):
        """Sets the instance_title of this RequestAppCreate.


        :param instance_title: The instance_title of this RequestAppCreate.  # noqa: E501
        :type: str
        """

        self._instance_title = instance_title

    @property
    def instance_type(self):
        """Gets the instance_type of this RequestAppCreate.  # noqa: E501


        :return: The instance_type of this RequestAppCreate.  # noqa: E501
        :rtype: InstanceType
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this RequestAppCreate.


        :param instance_type: The instance_type of this RequestAppCreate.  # noqa: E501
        :type: InstanceType
        """

        self._instance_type = instance_type

    @property
    def name(self):
        """Gets the name of this RequestAppCreate.  # noqa: E501


        :return: The name of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RequestAppCreate.


        :param name: The name of this RequestAppCreate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and not re.search('^[a-z0-9][a-z0-9-]{0,28}[a-z0-9]$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-z0-9][a-z0-9-]{0,28}[a-z0-9]$/`")  # noqa: E501

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this RequestAppCreate.  # noqa: E501


        :return: The org_id of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this RequestAppCreate.


        :param org_id: The org_id of this RequestAppCreate.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501
        if org_id is not None and not re.search('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', org_id):  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must be a follow pattern or equal to `/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._org_id = org_id

    @property
    def post_deployment(self):
        """Gets the post_deployment of this RequestAppCreate.  # noqa: E501


        :return: The post_deployment of this RequestAppCreate.  # noqa: E501
        :rtype: bool
        """
        return self._post_deployment

    @post_deployment.setter
    def post_deployment(self, post_deployment):
        """Sets the post_deployment of this RequestAppCreate.


        :param post_deployment: The post_deployment of this RequestAppCreate.  # noqa: E501
        :type: bool
        """

        self._post_deployment = post_deployment

    @property
    def server_id(self):
        """Gets the server_id of this RequestAppCreate.  # noqa: E501


        :return: The server_id of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this RequestAppCreate.


        :param server_id: The server_id of this RequestAppCreate.  # noqa: E501
        :type: str
        """
        if server_id is None:
            raise ValueError("Invalid value for `server_id`, must not be `None`")  # noqa: E501
        if server_id is not None and not re.search('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', server_id):  # noqa: E501
            raise ValueError("Invalid value for `server_id`, must be a follow pattern or equal to `/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._server_id = server_id

    @property
    def services(self):
        """Gets the services of this RequestAppCreate.  # noqa: E501


        :return: The services of this RequestAppCreate.  # noqa: E501
        :rtype: list[RequestAppCreateServices]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this RequestAppCreate.


        :param services: The services of this RequestAppCreate.  # noqa: E501
        :type: list[RequestAppCreateServices]
        """

        self._services = services

    @property
    def sitename(self):
        """Gets the sitename of this RequestAppCreate.  # noqa: E501


        :return: The sitename of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._sitename

    @sitename.setter
    def sitename(self, sitename):
        """Sets the sitename of this RequestAppCreate.


        :param sitename: The sitename of this RequestAppCreate.  # noqa: E501
        :type: str
        """

        self._sitename = sitename

    @property
    def stack_id(self):
        """Gets the stack_id of this RequestAppCreate.  # noqa: E501


        :return: The stack_id of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this RequestAppCreate.


        :param stack_id: The stack_id of this RequestAppCreate.  # noqa: E501
        :type: str
        """
        if stack_id is None:
            raise ValueError("Invalid value for `stack_id`, must not be `None`")  # noqa: E501
        if stack_id is not None and not re.search('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', stack_id):  # noqa: E501
            raise ValueError("Invalid value for `stack_id`, must be a follow pattern or equal to `/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._stack_id = stack_id

    @property
    def title(self):
        """Gets the title of this RequestAppCreate.  # noqa: E501


        :return: The title of this RequestAppCreate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RequestAppCreate.


        :param title: The title of this RequestAppCreate.  # noqa: E501
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
        if not isinstance(other, RequestAppCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
