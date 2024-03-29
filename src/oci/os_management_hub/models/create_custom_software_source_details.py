# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .create_software_source_details import CreateSoftwareSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCustomSoftwareSourceDetails(CreateSoftwareSourceDetails):
    """
    Description of a custom software source to be created.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCustomSoftwareSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.CreateCustomSoftwareSourceDetails.software_source_type` attribute
        of this class is ``CUSTOM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCustomSoftwareSourceDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateCustomSoftwareSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateCustomSoftwareSourceDetails.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this CreateCustomSoftwareSourceDetails.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED"
        :type software_source_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCustomSoftwareSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCustomSoftwareSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vendor_software_sources:
            The value to assign to the vendor_software_sources property of this CreateCustomSoftwareSourceDetails.
        :type vendor_software_sources: list[oci.os_management_hub.models.Id]

        :param custom_software_source_filter:
            The value to assign to the custom_software_source_filter property of this CreateCustomSoftwareSourceDetails.
        :type custom_software_source_filter: oci.os_management_hub.models.CustomSoftwareSourceFilter

        :param is_automatically_updated:
            The value to assign to the is_automatically_updated property of this CreateCustomSoftwareSourceDetails.
        :type is_automatically_updated: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'software_source_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vendor_software_sources': 'list[Id]',
            'custom_software_source_filter': 'CustomSoftwareSourceFilter',
            'is_automatically_updated': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vendor_software_sources': 'vendorSoftwareSources',
            'custom_software_source_filter': 'customSoftwareSourceFilter',
            'is_automatically_updated': 'isAutomaticallyUpdated'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._software_source_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vendor_software_sources = None
        self._custom_software_source_filter = None
        self._is_automatically_updated = None
        self._software_source_type = 'CUSTOM'

    @property
    def vendor_software_sources(self):
        """
        **[Required]** Gets the vendor_software_sources of this CreateCustomSoftwareSourceDetails.
        List of vendor software sources.


        :return: The vendor_software_sources of this CreateCustomSoftwareSourceDetails.
        :rtype: list[oci.os_management_hub.models.Id]
        """
        return self._vendor_software_sources

    @vendor_software_sources.setter
    def vendor_software_sources(self, vendor_software_sources):
        """
        Sets the vendor_software_sources of this CreateCustomSoftwareSourceDetails.
        List of vendor software sources.


        :param vendor_software_sources: The vendor_software_sources of this CreateCustomSoftwareSourceDetails.
        :type: list[oci.os_management_hub.models.Id]
        """
        self._vendor_software_sources = vendor_software_sources

    @property
    def custom_software_source_filter(self):
        """
        Gets the custom_software_source_filter of this CreateCustomSoftwareSourceDetails.

        :return: The custom_software_source_filter of this CreateCustomSoftwareSourceDetails.
        :rtype: oci.os_management_hub.models.CustomSoftwareSourceFilter
        """
        return self._custom_software_source_filter

    @custom_software_source_filter.setter
    def custom_software_source_filter(self, custom_software_source_filter):
        """
        Sets the custom_software_source_filter of this CreateCustomSoftwareSourceDetails.

        :param custom_software_source_filter: The custom_software_source_filter of this CreateCustomSoftwareSourceDetails.
        :type: oci.os_management_hub.models.CustomSoftwareSourceFilter
        """
        self._custom_software_source_filter = custom_software_source_filter

    @property
    def is_automatically_updated(self):
        """
        Gets the is_automatically_updated of this CreateCustomSoftwareSourceDetails.
        Indicates whether service should automatically update the custom software source for the user.


        :return: The is_automatically_updated of this CreateCustomSoftwareSourceDetails.
        :rtype: bool
        """
        return self._is_automatically_updated

    @is_automatically_updated.setter
    def is_automatically_updated(self, is_automatically_updated):
        """
        Sets the is_automatically_updated of this CreateCustomSoftwareSourceDetails.
        Indicates whether service should automatically update the custom software source for the user.


        :param is_automatically_updated: The is_automatically_updated of this CreateCustomSoftwareSourceDetails.
        :type: bool
        """
        self._is_automatically_updated = is_automatically_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
