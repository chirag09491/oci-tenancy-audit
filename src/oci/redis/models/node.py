# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220315


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Node(object):
    """
    The details of each node in the Redis cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Node object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param private_endpoint_fqdn:
            The value to assign to the private_endpoint_fqdn property of this Node.
        :type private_endpoint_fqdn: str

        :param private_endpoint_ip_address:
            The value to assign to the private_endpoint_ip_address property of this Node.
        :type private_endpoint_ip_address: str

        :param display_name:
            The value to assign to the display_name property of this Node.
        :type display_name: str

        """
        self.swagger_types = {
            'private_endpoint_fqdn': 'str',
            'private_endpoint_ip_address': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'private_endpoint_fqdn': 'privateEndpointFqdn',
            'private_endpoint_ip_address': 'privateEndpointIpAddress',
            'display_name': 'displayName'
        }

        self._private_endpoint_fqdn = None
        self._private_endpoint_ip_address = None
        self._display_name = None

    @property
    def private_endpoint_fqdn(self):
        """
        **[Required]** Gets the private_endpoint_fqdn of this Node.
        The fully qualified domain name (FQDN) of the API endpoint to access a specific node.


        :return: The private_endpoint_fqdn of this Node.
        :rtype: str
        """
        return self._private_endpoint_fqdn

    @private_endpoint_fqdn.setter
    def private_endpoint_fqdn(self, private_endpoint_fqdn):
        """
        Sets the private_endpoint_fqdn of this Node.
        The fully qualified domain name (FQDN) of the API endpoint to access a specific node.


        :param private_endpoint_fqdn: The private_endpoint_fqdn of this Node.
        :type: str
        """
        self._private_endpoint_fqdn = private_endpoint_fqdn

    @property
    def private_endpoint_ip_address(self):
        """
        **[Required]** Gets the private_endpoint_ip_address of this Node.
        The private IP address of the API endpoint to access a specific node.


        :return: The private_endpoint_ip_address of this Node.
        :rtype: str
        """
        return self._private_endpoint_ip_address

    @private_endpoint_ip_address.setter
    def private_endpoint_ip_address(self, private_endpoint_ip_address):
        """
        Sets the private_endpoint_ip_address of this Node.
        The private IP address of the API endpoint to access a specific node.


        :param private_endpoint_ip_address: The private_endpoint_ip_address of this Node.
        :type: str
        """
        self._private_endpoint_ip_address = private_endpoint_ip_address

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Node.
        A user-friendly name of a Redis cluster node.


        :return: The display_name of this Node.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Node.
        A user-friendly name of a Redis cluster node.


        :param display_name: The display_name of this Node.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
