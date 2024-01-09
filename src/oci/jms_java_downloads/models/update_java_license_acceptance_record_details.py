# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateJavaLicenseAcceptanceRecordDetails(object):
    """
    The attributes for updating a Java license acceptance record.
    """

    #: A constant which can be used with the license_acceptance_status property of a UpdateJavaLicenseAcceptanceRecordDetails.
    #: This constant has a value of "ACCEPTED"
    LICENSE_ACCEPTANCE_STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the license_acceptance_status property of a UpdateJavaLicenseAcceptanceRecordDetails.
    #: This constant has a value of "REVOKED"
    LICENSE_ACCEPTANCE_STATUS_REVOKED = "REVOKED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateJavaLicenseAcceptanceRecordDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param license_acceptance_status:
            The value to assign to the license_acceptance_status property of this UpdateJavaLicenseAcceptanceRecordDetails.
            Allowed values for this property are: "ACCEPTED", "REVOKED"
        :type license_acceptance_status: str

        """
        self.swagger_types = {
            'license_acceptance_status': 'str'
        }

        self.attribute_map = {
            'license_acceptance_status': 'licenseAcceptanceStatus'
        }

        self._license_acceptance_status = None

    @property
    def license_acceptance_status(self):
        """
        **[Required]** Gets the license_acceptance_status of this UpdateJavaLicenseAcceptanceRecordDetails.
        Status of license acceptance.

        Allowed values for this property are: "ACCEPTED", "REVOKED"


        :return: The license_acceptance_status of this UpdateJavaLicenseAcceptanceRecordDetails.
        :rtype: str
        """
        return self._license_acceptance_status

    @license_acceptance_status.setter
    def license_acceptance_status(self, license_acceptance_status):
        """
        Sets the license_acceptance_status of this UpdateJavaLicenseAcceptanceRecordDetails.
        Status of license acceptance.


        :param license_acceptance_status: The license_acceptance_status of this UpdateJavaLicenseAcceptanceRecordDetails.
        :type: str
        """
        allowed_values = ["ACCEPTED", "REVOKED"]
        if not value_allowed_none_or_none_sentinel(license_acceptance_status, allowed_values):
            raise ValueError(
                f"Invalid value for `license_acceptance_status`, must be None or one of {allowed_values}"
            )
        self._license_acceptance_status = license_acceptance_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
