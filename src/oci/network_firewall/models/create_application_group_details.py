# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApplicationGroupDetails(object):
    """
    Request for creating a application list in a policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApplicationGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateApplicationGroupDetails.
        :type name: str

        :param apps:
            The value to assign to the apps property of this CreateApplicationGroupDetails.
        :type apps: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'apps': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'apps': 'apps'
        }

        self._name = None
        self._apps = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateApplicationGroupDetails.
        Name of the application Group.


        :return: The name of this CreateApplicationGroupDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateApplicationGroupDetails.
        Name of the application Group.


        :param name: The name of this CreateApplicationGroupDetails.
        :type: str
        """
        self._name = name

    @property
    def apps(self):
        """
        **[Required]** Gets the apps of this CreateApplicationGroupDetails.
        Collection of application names.


        :return: The apps of this CreateApplicationGroupDetails.
        :rtype: list[str]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """
        Sets the apps of this CreateApplicationGroupDetails.
        Collection of application names.


        :param apps: The apps of this CreateApplicationGroupDetails.
        :type: list[str]
        """
        self._apps = apps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
