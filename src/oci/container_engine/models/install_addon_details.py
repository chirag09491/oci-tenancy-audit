# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180222


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstallAddonDetails(object):
    """
    The properties that define to install/enable addon on a cluster
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstallAddonDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param addon_name:
            The value to assign to the addon_name property of this InstallAddonDetails.
        :type addon_name: str

        :param version:
            The value to assign to the version property of this InstallAddonDetails.
        :type version: str

        :param configurations:
            The value to assign to the configurations property of this InstallAddonDetails.
        :type configurations: list[oci.container_engine.models.AddonConfiguration]

        """
        self.swagger_types = {
            'addon_name': 'str',
            'version': 'str',
            'configurations': 'list[AddonConfiguration]'
        }

        self.attribute_map = {
            'addon_name': 'addonName',
            'version': 'version',
            'configurations': 'configurations'
        }

        self._addon_name = None
        self._version = None
        self._configurations = None

    @property
    def addon_name(self):
        """
        **[Required]** Gets the addon_name of this InstallAddonDetails.
        The name of the addon.


        :return: The addon_name of this InstallAddonDetails.
        :rtype: str
        """
        return self._addon_name

    @addon_name.setter
    def addon_name(self, addon_name):
        """
        Sets the addon_name of this InstallAddonDetails.
        The name of the addon.


        :param addon_name: The addon_name of this InstallAddonDetails.
        :type: str
        """
        self._addon_name = addon_name

    @property
    def version(self):
        """
        Gets the version of this InstallAddonDetails.
        The version of addon to be installed.


        :return: The version of this InstallAddonDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this InstallAddonDetails.
        The version of addon to be installed.


        :param version: The version of this InstallAddonDetails.
        :type: str
        """
        self._version = version

    @property
    def configurations(self):
        """
        Gets the configurations of this InstallAddonDetails.
        Addon configuration details.


        :return: The configurations of this InstallAddonDetails.
        :rtype: list[oci.container_engine.models.AddonConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this InstallAddonDetails.
        Addon configuration details.


        :param configurations: The configurations of this InstallAddonDetails.
        :type: list[oci.container_engine.models.AddonConfiguration]
        """
        self._configurations = configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
