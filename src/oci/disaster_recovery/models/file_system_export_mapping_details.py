# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FileSystemExportMappingDetails(object):
    """
    The mapping between a file system export in the primary region and a mount target in the standby region.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FileSystemExportMappingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_id:
            The value to assign to the export_id property of this FileSystemExportMappingDetails.
        :type export_id: str

        :param destination_mount_target_id:
            The value to assign to the destination_mount_target_id property of this FileSystemExportMappingDetails.
        :type destination_mount_target_id: str

        """
        self.swagger_types = {
            'export_id': 'str',
            'destination_mount_target_id': 'str'
        }

        self.attribute_map = {
            'export_id': 'exportId',
            'destination_mount_target_id': 'destinationMountTargetId'
        }

        self._export_id = None
        self._destination_mount_target_id = None

    @property
    def export_id(self):
        """
        **[Required]** Gets the export_id of this FileSystemExportMappingDetails.
        The OCID of the export path in the primary region used to mount or unmount the file system.

        Example: `ocid1.export.oc1..uniqueID`


        :return: The export_id of this FileSystemExportMappingDetails.
        :rtype: str
        """
        return self._export_id

    @export_id.setter
    def export_id(self, export_id):
        """
        Sets the export_id of this FileSystemExportMappingDetails.
        The OCID of the export path in the primary region used to mount or unmount the file system.

        Example: `ocid1.export.oc1..uniqueID`


        :param export_id: The export_id of this FileSystemExportMappingDetails.
        :type: str
        """
        self._export_id = export_id

    @property
    def destination_mount_target_id(self):
        """
        **[Required]** Gets the destination_mount_target_id of this FileSystemExportMappingDetails.
        The OCID of the destination mount target in the destination region which is used to export the file system.

        Example: `ocid1.mounttarget.oc1..uniqueID`


        :return: The destination_mount_target_id of this FileSystemExportMappingDetails.
        :rtype: str
        """
        return self._destination_mount_target_id

    @destination_mount_target_id.setter
    def destination_mount_target_id(self, destination_mount_target_id):
        """
        Sets the destination_mount_target_id of this FileSystemExportMappingDetails.
        The OCID of the destination mount target in the destination region which is used to export the file system.

        Example: `ocid1.mounttarget.oc1..uniqueID`


        :param destination_mount_target_id: The destination_mount_target_id of this FileSystemExportMappingDetails.
        :type: str
        """
        self._destination_mount_target_id = destination_mount_target_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
