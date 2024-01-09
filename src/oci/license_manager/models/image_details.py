# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageDetails(object):
    """
    Image details associated with the product license.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param listing_id:
            The value to assign to the listing_id property of this ImageDetails.
        :type listing_id: str

        :param package_version:
            The value to assign to the package_version property of this ImageDetails.
        :type package_version: str

        """
        self.swagger_types = {
            'listing_id': 'str',
            'package_version': 'str'
        }

        self.attribute_map = {
            'listing_id': 'listingId',
            'package_version': 'packageVersion'
        }

        self._listing_id = None
        self._package_version = None

    @property
    def listing_id(self):
        """
        **[Required]** Gets the listing_id of this ImageDetails.
        Marketplace image listing ID.


        :return: The listing_id of this ImageDetails.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this ImageDetails.
        Marketplace image listing ID.


        :param listing_id: The listing_id of this ImageDetails.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def package_version(self):
        """
        **[Required]** Gets the package_version of this ImageDetails.
        Image package version.


        :return: The package_version of this ImageDetails.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this ImageDetails.
        Image package version.


        :param package_version: The package_version of this ImageDetails.
        :type: str
        """
        self._package_version = package_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
