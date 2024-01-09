# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManageLicenseDetails(object):
    """
    License information for a given resource.
    """

    #: A constant which can be used with the license property of a ManageLicenseDetails.
    #: This constant has a value of "STANDARD_EDITION"
    LICENSE_STANDARD_EDITION = "STANDARD_EDITION"

    #: A constant which can be used with the license property of a ManageLicenseDetails.
    #: This constant has a value of "ENTERPRISE_EDITION"
    LICENSE_ENTERPRISE_EDITION = "ENTERPRISE_EDITION"

    def __init__(self, **kwargs):
        """
        Initializes a new ManageLicenseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param license:
            The value to assign to the license property of this ManageLicenseDetails.
            Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION"
        :type license: str

        """
        self.swagger_types = {
            'license': 'str'
        }

        self.attribute_map = {
            'license': 'license'
        }

        self._license = None

    @property
    def license(self):
        """
        **[Required]** Gets the license of this ManageLicenseDetails.
        License edition of the monitored resource.

        Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION"


        :return: The license of this ManageLicenseDetails.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """
        Sets the license of this ManageLicenseDetails.
        License edition of the monitored resource.


        :param license: The license of this ManageLicenseDetails.
        :type: str
        """
        allowed_values = ["STANDARD_EDITION", "ENTERPRISE_EDITION"]
        if not value_allowed_none_or_none_sentinel(license, allowed_values):
            raise ValueError(
                f"Invalid value for `license`, must be None or one of {allowed_values}"
            )
        self._license = license

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
