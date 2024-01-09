# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220615


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrafficRuleTargetDetails(object):
    """
    Target of the traffic router rule.
    """

    #: A constant which can be used with the type property of a TrafficRuleTargetDetails.
    #: This constant has a value of "VIRTUAL_DEPLOYMENT"
    TYPE_VIRTUAL_DEPLOYMENT = "VIRTUAL_DEPLOYMENT"

    #: A constant which can be used with the type property of a TrafficRuleTargetDetails.
    #: This constant has a value of "VIRTUAL_SERVICE"
    TYPE_VIRTUAL_SERVICE = "VIRTUAL_SERVICE"

    def __init__(self, **kwargs):
        """
        Initializes a new TrafficRuleTargetDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.service_mesh.models.VirtualDeploymentTrafficRuleTargetDetails`
        * :class:`~oci.service_mesh.models.VirtualServiceTrafficRuleTargetDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TrafficRuleTargetDetails.
            Allowed values for this property are: "VIRTUAL_DEPLOYMENT", "VIRTUAL_SERVICE"
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'VIRTUAL_DEPLOYMENT':
            return 'VirtualDeploymentTrafficRuleTargetDetails'

        if type == 'VIRTUAL_SERVICE':
            return 'VirtualServiceTrafficRuleTargetDetails'
        else:
            return 'TrafficRuleTargetDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this TrafficRuleTargetDetails.
        Type of the traffic target.

        Allowed values for this property are: "VIRTUAL_DEPLOYMENT", "VIRTUAL_SERVICE"


        :return: The type of this TrafficRuleTargetDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TrafficRuleTargetDetails.
        Type of the traffic target.


        :param type: The type of this TrafficRuleTargetDetails.
        :type: str
        """
        allowed_values = ["VIRTUAL_DEPLOYMENT", "VIRTUAL_SERVICE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
