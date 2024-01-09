# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210929


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseObject(object):
    """
    Database objects to include or exclude from migration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param owner:
            The value to assign to the owner property of this DatabaseObject.
        :type owner: str

        :param object_name:
            The value to assign to the object_name property of this DatabaseObject.
        :type object_name: str

        :param type:
            The value to assign to the type property of this DatabaseObject.
        :type type: str

        :param is_omit_excluded_table_from_replication:
            The value to assign to the is_omit_excluded_table_from_replication property of this DatabaseObject.
        :type is_omit_excluded_table_from_replication: bool

        """
        self.swagger_types = {
            'owner': 'str',
            'object_name': 'str',
            'type': 'str',
            'is_omit_excluded_table_from_replication': 'bool'
        }

        self.attribute_map = {
            'owner': 'owner',
            'object_name': 'objectName',
            'type': 'type',
            'is_omit_excluded_table_from_replication': 'isOmitExcludedTableFromReplication'
        }

        self._owner = None
        self._object_name = None
        self._type = None
        self._is_omit_excluded_table_from_replication = None

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this DatabaseObject.
        Owner of the object (regular expression is allowed)


        :return: The owner of this DatabaseObject.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this DatabaseObject.
        Owner of the object (regular expression is allowed)


        :param owner: The owner of this DatabaseObject.
        :type: str
        """
        self._owner = owner

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this DatabaseObject.
        Name of the object (regular expression is allowed)


        :return: The object_name of this DatabaseObject.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this DatabaseObject.
        Name of the object (regular expression is allowed)


        :param object_name: The object_name of this DatabaseObject.
        :type: str
        """
        self._object_name = object_name

    @property
    def type(self):
        """
        Gets the type of this DatabaseObject.
        Type of object to exclude.
        If not specified, matching owners and object names of type TABLE would be excluded.


        :return: The type of this DatabaseObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DatabaseObject.
        Type of object to exclude.
        If not specified, matching owners and object names of type TABLE would be excluded.


        :param type: The type of this DatabaseObject.
        :type: str
        """
        self._type = type

    @property
    def is_omit_excluded_table_from_replication(self):
        """
        Gets the is_omit_excluded_table_from_replication of this DatabaseObject.
        Whether an excluded table should be omitted from replication. Only valid for database objects that have are of type TABLE and that are included in the exludeObjects.


        :return: The is_omit_excluded_table_from_replication of this DatabaseObject.
        :rtype: bool
        """
        return self._is_omit_excluded_table_from_replication

    @is_omit_excluded_table_from_replication.setter
    def is_omit_excluded_table_from_replication(self, is_omit_excluded_table_from_replication):
        """
        Sets the is_omit_excluded_table_from_replication of this DatabaseObject.
        Whether an excluded table should be omitted from replication. Only valid for database objects that have are of type TABLE and that are included in the exludeObjects.


        :param is_omit_excluded_table_from_replication: The is_omit_excluded_table_from_replication of this DatabaseObject.
        :type: bool
        """
        self._is_omit_excluded_table_from_replication = is_omit_excluded_table_from_replication

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
