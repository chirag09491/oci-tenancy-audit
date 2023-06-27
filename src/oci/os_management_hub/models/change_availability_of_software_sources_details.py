# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeAvailabilityOfSoftwareSourcesDetails(object):
    """
    Request body that contains a list of software sources whose availability needs to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeAvailabilityOfSoftwareSourcesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_source_availabilities:
            The value to assign to the software_source_availabilities property of this ChangeAvailabilityOfSoftwareSourcesDetails.
        :type software_source_availabilities: list[oci.os_management_hub.models.SoftwareSourceAvailability]

        """
        self.swagger_types = {
            'software_source_availabilities': 'list[SoftwareSourceAvailability]'
        }

        self.attribute_map = {
            'software_source_availabilities': 'softwareSourceAvailabilities'
        }

        self._software_source_availabilities = None

    @property
    def software_source_availabilities(self):
        """
        Gets the software_source_availabilities of this ChangeAvailabilityOfSoftwareSourcesDetails.
        List of objects containing software source ids and its availability.


        :return: The software_source_availabilities of this ChangeAvailabilityOfSoftwareSourcesDetails.
        :rtype: list[oci.os_management_hub.models.SoftwareSourceAvailability]
        """
        return self._software_source_availabilities

    @software_source_availabilities.setter
    def software_source_availabilities(self, software_source_availabilities):
        """
        Sets the software_source_availabilities of this ChangeAvailabilityOfSoftwareSourcesDetails.
        List of objects containing software source ids and its availability.


        :param software_source_availabilities: The software_source_availabilities of this ChangeAvailabilityOfSoftwareSourcesDetails.
        :type: list[oci.os_management_hub.models.SoftwareSourceAvailability]
        """
        self._software_source_availabilities = software_source_availabilities

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other