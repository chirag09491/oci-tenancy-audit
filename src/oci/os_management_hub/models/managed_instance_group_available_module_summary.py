# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceGroupAvailableModuleSummary(object):
    """
    Summary information pertaining to a module stream profile provided by a software source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceGroupAvailableModuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ManagedInstanceGroupAvailableModuleSummary.
        :type name: str

        :param software_source_id:
            The value to assign to the software_source_id property of this ManagedInstanceGroupAvailableModuleSummary.
        :type software_source_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'software_source_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'software_source_id': 'softwareSourceId'
        }

        self._name = None
        self._software_source_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedInstanceGroupAvailableModuleSummary.
        The name of the module that is available to be enabled on the managed instance group.


        :return: The name of this ManagedInstanceGroupAvailableModuleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedInstanceGroupAvailableModuleSummary.
        The name of the module that is available to be enabled on the managed instance group.


        :param name: The name of this ManagedInstanceGroupAvailableModuleSummary.
        :type: str
        """
        self._name = name

    @property
    def software_source_id(self):
        """
        Gets the software_source_id of this ManagedInstanceGroupAvailableModuleSummary.
        The OCID of the software source that provides this module.


        :return: The software_source_id of this ManagedInstanceGroupAvailableModuleSummary.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this ManagedInstanceGroupAvailableModuleSummary.
        The OCID of the software source that provides this module.


        :param software_source_id: The software_source_id of this ManagedInstanceGroupAvailableModuleSummary.
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