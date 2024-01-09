# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerImageDetails(object):
    """
    Container image details required to create a container artifact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerImageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_registry_id:
            The value to assign to the source_registry_id property of this CreateContainerImageDetails.
        :type source_registry_id: str

        :param source_registry_url:
            The value to assign to the source_registry_url property of this CreateContainerImageDetails.
        :type source_registry_url: str

        """
        self.swagger_types = {
            'source_registry_id': 'str',
            'source_registry_url': 'str'
        }

        self.attribute_map = {
            'source_registry_id': 'sourceRegistryId',
            'source_registry_url': 'sourceRegistryUrl'
        }

        self._source_registry_id = None
        self._source_registry_url = None

    @property
    def source_registry_id(self):
        """
        **[Required]** Gets the source_registry_id of this CreateContainerImageDetails.
        The source registry id of the container image.


        :return: The source_registry_id of this CreateContainerImageDetails.
        :rtype: str
        """
        return self._source_registry_id

    @source_registry_id.setter
    def source_registry_id(self, source_registry_id):
        """
        Sets the source_registry_id of this CreateContainerImageDetails.
        The source registry id of the container image.


        :param source_registry_id: The source_registry_id of this CreateContainerImageDetails.
        :type: str
        """
        self._source_registry_id = source_registry_id

    @property
    def source_registry_url(self):
        """
        **[Required]** Gets the source_registry_url of this CreateContainerImageDetails.
        The source registry url of the container image.


        :return: The source_registry_url of this CreateContainerImageDetails.
        :rtype: str
        """
        return self._source_registry_url

    @source_registry_url.setter
    def source_registry_url(self, source_registry_url):
        """
        Sets the source_registry_url of this CreateContainerImageDetails.
        The source registry url of the container image.


        :param source_registry_url: The source_registry_url of this CreateContainerImageDetails.
        :type: str
        """
        self._source_registry_url = source_registry_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
