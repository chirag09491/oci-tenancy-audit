# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220509


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDiscoveryScheduleDetails(object):
    """
    Information about discovery schedule to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDiscoveryScheduleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDiscoveryScheduleDetails.
        :type display_name: str

        :param execution_recurrences:
            The value to assign to the execution_recurrences property of this UpdateDiscoveryScheduleDetails.
        :type execution_recurrences: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDiscoveryScheduleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDiscoveryScheduleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'execution_recurrences': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'execution_recurrences': 'executionRecurrences',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._execution_recurrences = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDiscoveryScheduleDetails.
        A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateDiscoveryScheduleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDiscoveryScheduleDetails.
        A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDiscoveryScheduleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def execution_recurrences(self):
        """
        Gets the execution_recurrences of this UpdateDiscoveryScheduleDetails.
        Recurrence specification for the discovery schedule execution.


        :return: The execution_recurrences of this UpdateDiscoveryScheduleDetails.
        :rtype: str
        """
        return self._execution_recurrences

    @execution_recurrences.setter
    def execution_recurrences(self, execution_recurrences):
        """
        Sets the execution_recurrences of this UpdateDiscoveryScheduleDetails.
        Recurrence specification for the discovery schedule execution.


        :param execution_recurrences: The execution_recurrences of this UpdateDiscoveryScheduleDetails.
        :type: str
        """
        self._execution_recurrences = execution_recurrences

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDiscoveryScheduleDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateDiscoveryScheduleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDiscoveryScheduleDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateDiscoveryScheduleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDiscoveryScheduleDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateDiscoveryScheduleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDiscoveryScheduleDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateDiscoveryScheduleDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
