# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddVcnIpv6CidrDetails(object):
    """
    Details used when adding a ULA or private IPv6 prefix or an IPv6 GUA assigned by Oracle or a BYOIPv6 prefix. You can add only one of these per request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddVcnIpv6CidrDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ipv6_private_cidr_block:
            The value to assign to the ipv6_private_cidr_block property of this AddVcnIpv6CidrDetails.
        :type ipv6_private_cidr_block: str

        :param is_oracle_gua_allocation_enabled:
            The value to assign to the is_oracle_gua_allocation_enabled property of this AddVcnIpv6CidrDetails.
        :type is_oracle_gua_allocation_enabled: bool

        :param byoipv6_cidr_detail:
            The value to assign to the byoipv6_cidr_detail property of this AddVcnIpv6CidrDetails.
        :type byoipv6_cidr_detail: oci.vn_monitoring.models.Byoipv6CidrDetails

        """
        self.swagger_types = {
            'ipv6_private_cidr_block': 'str',
            'is_oracle_gua_allocation_enabled': 'bool',
            'byoipv6_cidr_detail': 'Byoipv6CidrDetails'
        }

        self.attribute_map = {
            'ipv6_private_cidr_block': 'ipv6PrivateCidrBlock',
            'is_oracle_gua_allocation_enabled': 'isOracleGuaAllocationEnabled',
            'byoipv6_cidr_detail': 'byoipv6CidrDetail'
        }

        self._ipv6_private_cidr_block = None
        self._is_oracle_gua_allocation_enabled = None
        self._byoipv6_cidr_detail = None

    @property
    def ipv6_private_cidr_block(self):
        """
        Gets the ipv6_private_cidr_block of this AddVcnIpv6CidrDetails.
        This field is not required and should only be specified if a ULA or private IPv6 prefix is desired for VCN's private IP address space.
        See`IPv6 Addresses`__.

        Example: `2001:0db8:0123::/48` or `fd00:1000:0:1::/64`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :return: The ipv6_private_cidr_block of this AddVcnIpv6CidrDetails.
        :rtype: str
        """
        return self._ipv6_private_cidr_block

    @ipv6_private_cidr_block.setter
    def ipv6_private_cidr_block(self, ipv6_private_cidr_block):
        """
        Sets the ipv6_private_cidr_block of this AddVcnIpv6CidrDetails.
        This field is not required and should only be specified if a ULA or private IPv6 prefix is desired for VCN's private IP address space.
        See`IPv6 Addresses`__.

        Example: `2001:0db8:0123::/48` or `fd00:1000:0:1::/64`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :param ipv6_private_cidr_block: The ipv6_private_cidr_block of this AddVcnIpv6CidrDetails.
        :type: str
        """
        self._ipv6_private_cidr_block = ipv6_private_cidr_block

    @property
    def is_oracle_gua_allocation_enabled(self):
        """
        Gets the is_oracle_gua_allocation_enabled of this AddVcnIpv6CidrDetails.
        Indicates whether Oracle will allocate an IPv6 GUA. Only one prefix of /56 size can be allocated by Oracle as a GUA.


        :return: The is_oracle_gua_allocation_enabled of this AddVcnIpv6CidrDetails.
        :rtype: bool
        """
        return self._is_oracle_gua_allocation_enabled

    @is_oracle_gua_allocation_enabled.setter
    def is_oracle_gua_allocation_enabled(self, is_oracle_gua_allocation_enabled):
        """
        Sets the is_oracle_gua_allocation_enabled of this AddVcnIpv6CidrDetails.
        Indicates whether Oracle will allocate an IPv6 GUA. Only one prefix of /56 size can be allocated by Oracle as a GUA.


        :param is_oracle_gua_allocation_enabled: The is_oracle_gua_allocation_enabled of this AddVcnIpv6CidrDetails.
        :type: bool
        """
        self._is_oracle_gua_allocation_enabled = is_oracle_gua_allocation_enabled

    @property
    def byoipv6_cidr_detail(self):
        """
        Gets the byoipv6_cidr_detail of this AddVcnIpv6CidrDetails.

        :return: The byoipv6_cidr_detail of this AddVcnIpv6CidrDetails.
        :rtype: oci.vn_monitoring.models.Byoipv6CidrDetails
        """
        return self._byoipv6_cidr_detail

    @byoipv6_cidr_detail.setter
    def byoipv6_cidr_detail(self, byoipv6_cidr_detail):
        """
        Sets the byoipv6_cidr_detail of this AddVcnIpv6CidrDetails.

        :param byoipv6_cidr_detail: The byoipv6_cidr_detail of this AddVcnIpv6CidrDetails.
        :type: oci.vn_monitoring.models.Byoipv6CidrDetails
        """
        self._byoipv6_cidr_detail = byoipv6_cidr_detail

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
