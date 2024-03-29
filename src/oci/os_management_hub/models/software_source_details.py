# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwareSourceDetails(object):
    """
    Identifying information for the specified software source.
    """

    #: A constant which can be used with the software_source_type property of a SoftwareSourceDetails.
    #: This constant has a value of "VENDOR"
    SOFTWARE_SOURCE_TYPE_VENDOR = "VENDOR"

    #: A constant which can be used with the software_source_type property of a SoftwareSourceDetails.
    #: This constant has a value of "CUSTOM"
    SOFTWARE_SOURCE_TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the software_source_type property of a SoftwareSourceDetails.
    #: This constant has a value of "VERSIONED"
    SOFTWARE_SOURCE_TYPE_VERSIONED = "VERSIONED"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwareSourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SoftwareSourceDetails.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this SoftwareSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SoftwareSourceDetails.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this SoftwareSourceDetails.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type software_source_type: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'software_source_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'software_source_type': 'softwareSourceType'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._software_source_type = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SoftwareSourceDetails.
        The OCID of the software source.


        :return: The id of this SoftwareSourceDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SoftwareSourceDetails.
        The OCID of the software source.


        :param id: The id of this SoftwareSourceDetails.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this SoftwareSourceDetails.
        Software source name.


        :return: The display_name of this SoftwareSourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SoftwareSourceDetails.
        Software source name.


        :param display_name: The display_name of this SoftwareSourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SoftwareSourceDetails.
        Software source description.


        :return: The description of this SoftwareSourceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SoftwareSourceDetails.
        Software source description.


        :param description: The description of this SoftwareSourceDetails.
        :type: str
        """
        self._description = description

    @property
    def software_source_type(self):
        """
        Gets the software_source_type of this SoftwareSourceDetails.
        Type of the software source.

        Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The software_source_type of this SoftwareSourceDetails.
        :rtype: str
        """
        return self._software_source_type

    @software_source_type.setter
    def software_source_type(self, software_source_type):
        """
        Sets the software_source_type of this SoftwareSourceDetails.
        Type of the software source.


        :param software_source_type: The software_source_type of this SoftwareSourceDetails.
        :type: str
        """
        allowed_values = ["VENDOR", "CUSTOM", "VERSIONED"]
        if not value_allowed_none_or_none_sentinel(software_source_type, allowed_values):
            software_source_type = 'UNKNOWN_ENUM_VALUE'
        self._software_source_type = software_source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
