# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .create_dr_protection_group_member_details import CreateDrProtectionGroupMemberDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrProtectionGroupMemberFileSystemDetails(CreateDrProtectionGroupMemberDetails):
    """
    Create properties for a file system member.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrProtectionGroupMemberFileSystemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberFileSystemDetails.member_type` attribute
        of this class is ``FILE_SYSTEM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this CreateDrProtectionGroupMemberFileSystemDetails.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this CreateDrProtectionGroupMemberFileSystemDetails.
            Allowed values for this property are: "COMPUTE_INSTANCE", "COMPUTE_INSTANCE_MOVABLE", "COMPUTE_INSTANCE_NON_MOVABLE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE", "LOAD_BALANCER", "NETWORK_LOAD_BALANCER", "FILE_SYSTEM"
        :type member_type: str

        :param destination_availability_domain:
            The value to assign to the destination_availability_domain property of this CreateDrProtectionGroupMemberFileSystemDetails.
        :type destination_availability_domain: str

        :param export_mappings:
            The value to assign to the export_mappings property of this CreateDrProtectionGroupMemberFileSystemDetails.
        :type export_mappings: list[oci.disaster_recovery.models.FileSystemExportMappingDetails]

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str',
            'destination_availability_domain': 'str',
            'export_mappings': 'list[FileSystemExportMappingDetails]'
        }

        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType',
            'destination_availability_domain': 'destinationAvailabilityDomain',
            'export_mappings': 'exportMappings'
        }

        self._member_id = None
        self._member_type = None
        self._destination_availability_domain = None
        self._export_mappings = None
        self._member_type = 'FILE_SYSTEM'

    @property
    def destination_availability_domain(self):
        """
        Gets the destination_availability_domain of this CreateDrProtectionGroupMemberFileSystemDetails.
        The availability domain of the destination mount target.

        Example: `BBTh:region-AD`


        :return: The destination_availability_domain of this CreateDrProtectionGroupMemberFileSystemDetails.
        :rtype: str
        """
        return self._destination_availability_domain

    @destination_availability_domain.setter
    def destination_availability_domain(self, destination_availability_domain):
        """
        Sets the destination_availability_domain of this CreateDrProtectionGroupMemberFileSystemDetails.
        The availability domain of the destination mount target.

        Example: `BBTh:region-AD`


        :param destination_availability_domain: The destination_availability_domain of this CreateDrProtectionGroupMemberFileSystemDetails.
        :type: str
        """
        self._destination_availability_domain = destination_availability_domain

    @property
    def export_mappings(self):
        """
        Gets the export_mappings of this CreateDrProtectionGroupMemberFileSystemDetails.
        A list of mappings between file system exports in the primary region and mount targets in the standby region.


        :return: The export_mappings of this CreateDrProtectionGroupMemberFileSystemDetails.
        :rtype: list[oci.disaster_recovery.models.FileSystemExportMappingDetails]
        """
        return self._export_mappings

    @export_mappings.setter
    def export_mappings(self, export_mappings):
        """
        Sets the export_mappings of this CreateDrProtectionGroupMemberFileSystemDetails.
        A list of mappings between file system exports in the primary region and mount targets in the standby region.


        :param export_mappings: The export_mappings of this CreateDrProtectionGroupMemberFileSystemDetails.
        :type: list[oci.disaster_recovery.models.FileSystemExportMappingDetails]
        """
        self._export_mappings = export_mappings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
