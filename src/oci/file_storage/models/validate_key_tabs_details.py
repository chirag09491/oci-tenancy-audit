# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidateKeyTabsDetails(object):
    """
    Validate keytabs request details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidateKeyTabsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mount_target_id:
            The value to assign to the mount_target_id property of this ValidateKeyTabsDetails.
        :type mount_target_id: str

        :param key_tab_secret_details:
            The value to assign to the key_tab_secret_details property of this ValidateKeyTabsDetails.
        :type key_tab_secret_details: oci.file_storage.models.KeyTabSecretDetails

        """
        self.swagger_types = {
            'mount_target_id': 'str',
            'key_tab_secret_details': 'KeyTabSecretDetails'
        }

        self.attribute_map = {
            'mount_target_id': 'mountTargetId',
            'key_tab_secret_details': 'keyTabSecretDetails'
        }

        self._mount_target_id = None
        self._key_tab_secret_details = None

    @property
    def mount_target_id(self):
        """
        Gets the mount_target_id of this ValidateKeyTabsDetails.
        The `OCID`__ of the mount target whose keytabs are to be validated.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The mount_target_id of this ValidateKeyTabsDetails.
        :rtype: str
        """
        return self._mount_target_id

    @mount_target_id.setter
    def mount_target_id(self, mount_target_id):
        """
        Sets the mount_target_id of this ValidateKeyTabsDetails.
        The `OCID`__ of the mount target whose keytabs are to be validated.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param mount_target_id: The mount_target_id of this ValidateKeyTabsDetails.
        :type: str
        """
        self._mount_target_id = mount_target_id

    @property
    def key_tab_secret_details(self):
        """
        Gets the key_tab_secret_details of this ValidateKeyTabsDetails.

        :return: The key_tab_secret_details of this ValidateKeyTabsDetails.
        :rtype: oci.file_storage.models.KeyTabSecretDetails
        """
        return self._key_tab_secret_details

    @key_tab_secret_details.setter
    def key_tab_secret_details(self, key_tab_secret_details):
        """
        Sets the key_tab_secret_details of this ValidateKeyTabsDetails.

        :param key_tab_secret_details: The key_tab_secret_details of this ValidateKeyTabsDetails.
        :type: oci.file_storage.models.KeyTabSecretDetails
        """
        self._key_tab_secret_details = key_tab_secret_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
