# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceModuleSummary(object):
    """
    Summary information pertaining to a module on a managed instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceModuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ManagedInstanceModuleSummary.
        :type name: str

        :param enabled_stream:
            The value to assign to the enabled_stream property of this ManagedInstanceModuleSummary.
        :type enabled_stream: str

        :param installed_profiles:
            The value to assign to the installed_profiles property of this ManagedInstanceModuleSummary.
        :type installed_profiles: list[str]

        :param active_streams:
            The value to assign to the active_streams property of this ManagedInstanceModuleSummary.
        :type active_streams: list[str]

        :param disabled_streams:
            The value to assign to the disabled_streams property of this ManagedInstanceModuleSummary.
        :type disabled_streams: list[str]

        :param software_source_id:
            The value to assign to the software_source_id property of this ManagedInstanceModuleSummary.
        :type software_source_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'enabled_stream': 'str',
            'installed_profiles': 'list[str]',
            'active_streams': 'list[str]',
            'disabled_streams': 'list[str]',
            'software_source_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'enabled_stream': 'enabledStream',
            'installed_profiles': 'installedProfiles',
            'active_streams': 'activeStreams',
            'disabled_streams': 'disabledStreams',
            'software_source_id': 'softwareSourceId'
        }

        self._name = None
        self._enabled_stream = None
        self._installed_profiles = None
        self._active_streams = None
        self._disabled_streams = None
        self._software_source_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedInstanceModuleSummary.
        The module name.


        :return: The name of this ManagedInstanceModuleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedInstanceModuleSummary.
        The module name.


        :param name: The name of this ManagedInstanceModuleSummary.
        :type: str
        """
        self._name = name

    @property
    def enabled_stream(self):
        """
        Gets the enabled_stream of this ManagedInstanceModuleSummary.
        The stream that is enabled in the module.


        :return: The enabled_stream of this ManagedInstanceModuleSummary.
        :rtype: str
        """
        return self._enabled_stream

    @enabled_stream.setter
    def enabled_stream(self, enabled_stream):
        """
        Sets the enabled_stream of this ManagedInstanceModuleSummary.
        The stream that is enabled in the module.


        :param enabled_stream: The enabled_stream of this ManagedInstanceModuleSummary.
        :type: str
        """
        self._enabled_stream = enabled_stream

    @property
    def installed_profiles(self):
        """
        Gets the installed_profiles of this ManagedInstanceModuleSummary.
        List of installed profiles in the enabled stream of the module.


        :return: The installed_profiles of this ManagedInstanceModuleSummary.
        :rtype: list[str]
        """
        return self._installed_profiles

    @installed_profiles.setter
    def installed_profiles(self, installed_profiles):
        """
        Sets the installed_profiles of this ManagedInstanceModuleSummary.
        List of installed profiles in the enabled stream of the module.


        :param installed_profiles: The installed_profiles of this ManagedInstanceModuleSummary.
        :type: list[str]
        """
        self._installed_profiles = installed_profiles

    @property
    def active_streams(self):
        """
        Gets the active_streams of this ManagedInstanceModuleSummary.
        List of streams that are active in the module.


        :return: The active_streams of this ManagedInstanceModuleSummary.
        :rtype: list[str]
        """
        return self._active_streams

    @active_streams.setter
    def active_streams(self, active_streams):
        """
        Sets the active_streams of this ManagedInstanceModuleSummary.
        List of streams that are active in the module.


        :param active_streams: The active_streams of this ManagedInstanceModuleSummary.
        :type: list[str]
        """
        self._active_streams = active_streams

    @property
    def disabled_streams(self):
        """
        Gets the disabled_streams of this ManagedInstanceModuleSummary.
        List of streams that are disabled in the module.


        :return: The disabled_streams of this ManagedInstanceModuleSummary.
        :rtype: list[str]
        """
        return self._disabled_streams

    @disabled_streams.setter
    def disabled_streams(self, disabled_streams):
        """
        Sets the disabled_streams of this ManagedInstanceModuleSummary.
        List of streams that are disabled in the module.


        :param disabled_streams: The disabled_streams of this ManagedInstanceModuleSummary.
        :type: list[str]
        """
        self._disabled_streams = disabled_streams

    @property
    def software_source_id(self):
        """
        Gets the software_source_id of this ManagedInstanceModuleSummary.
        The OCID of the software source that provides this module and the associated streams.


        :return: The software_source_id of this ManagedInstanceModuleSummary.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this ManagedInstanceModuleSummary.
        The OCID of the software source that provides this module and the associated streams.


        :param software_source_id: The software_source_id of this ManagedInstanceModuleSummary.
        :type: str
        """
        self._software_source_id = software_source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
