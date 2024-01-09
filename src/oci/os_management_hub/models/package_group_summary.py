# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PackageGroupSummary(object):
    """
    Yum/DNF package group that associated with a software source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PackageGroupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PackageGroupSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this PackageGroupSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this PackageGroupSummary.
        :type description: str

        :param is_user_visible:
            The value to assign to the is_user_visible property of this PackageGroupSummary.
        :type is_user_visible: bool

        :param is_default:
            The value to assign to the is_default property of this PackageGroupSummary.
        :type is_default: bool

        :param repositories:
            The value to assign to the repositories property of this PackageGroupSummary.
        :type repositories: list[str]

        :param group_type:
            The value to assign to the group_type property of this PackageGroupSummary.
        :type group_type: str

        :param display_order:
            The value to assign to the display_order property of this PackageGroupSummary.
        :type display_order: int

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'is_user_visible': 'bool',
            'is_default': 'bool',
            'repositories': 'list[str]',
            'group_type': 'str',
            'display_order': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'is_user_visible': 'isUserVisible',
            'is_default': 'isDefault',
            'repositories': 'repositories',
            'group_type': 'groupType',
            'display_order': 'displayOrder'
        }

        self._id = None
        self._name = None
        self._description = None
        self._is_user_visible = None
        self._is_default = None
        self._repositories = None
        self._group_type = None
        self._display_order = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PackageGroupSummary.
        Package group identifier.


        :return: The id of this PackageGroupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PackageGroupSummary.
        Package group identifier.


        :param id: The id of this PackageGroupSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PackageGroupSummary.
        Package group name.


        :return: The name of this PackageGroupSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PackageGroupSummary.
        Package group name.


        :param name: The name of this PackageGroupSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PackageGroupSummary.
        description of the package group.


        :return: The description of this PackageGroupSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PackageGroupSummary.
        description of the package group.


        :param description: The description of this PackageGroupSummary.
        :type: str
        """
        self._description = description

    @property
    def is_user_visible(self):
        """
        Gets the is_user_visible of this PackageGroupSummary.
        Indicates if this package group is visible by users.


        :return: The is_user_visible of this PackageGroupSummary.
        :rtype: bool
        """
        return self._is_user_visible

    @is_user_visible.setter
    def is_user_visible(self, is_user_visible):
        """
        Sets the is_user_visible of this PackageGroupSummary.
        Indicates if this package group is visible by users.


        :param is_user_visible: The is_user_visible of this PackageGroupSummary.
        :type: bool
        """
        self._is_user_visible = is_user_visible

    @property
    def is_default(self):
        """
        Gets the is_default of this PackageGroupSummary.
        Indicates if this package group is the default.


        :return: The is_default of this PackageGroupSummary.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this PackageGroupSummary.
        Indicates if this package group is the default.


        :param is_default: The is_default of this PackageGroupSummary.
        :type: bool
        """
        self._is_default = is_default

    @property
    def repositories(self):
        """
        Gets the repositories of this PackageGroupSummary.
        the IDs of the package group's repositories.


        :return: The repositories of this PackageGroupSummary.
        :rtype: list[str]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        """
        Sets the repositories of this PackageGroupSummary.
        the IDs of the package group's repositories.


        :param repositories: The repositories of this PackageGroupSummary.
        :type: list[str]
        """
        self._repositories = repositories

    @property
    def group_type(self):
        """
        Gets the group_type of this PackageGroupSummary.
        Indicates if this is a group, category or environment.


        :return: The group_type of this PackageGroupSummary.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """
        Sets the group_type of this PackageGroupSummary.
        Indicates if this is a group, category or environment.


        :param group_type: The group_type of this PackageGroupSummary.
        :type: str
        """
        self._group_type = group_type

    @property
    def display_order(self):
        """
        Gets the display_order of this PackageGroupSummary.
        Indicates the order to display category or environment.


        :return: The display_order of this PackageGroupSummary.
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """
        Sets the display_order of this PackageGroupSummary.
        Indicates the order to display category or environment.


        :param display_order: The display_order of this PackageGroupSummary.
        :type: int
        """
        self._display_order = display_order

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
