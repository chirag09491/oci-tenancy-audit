# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSecurityRuleDetails(object):
    """
    Reqeust for creating Security Rule used in the firewall policy rules.
    Security Rules determine whether to block or allow a session based on traffic attributes,
    such as  the source and destination IP address, protocol/port, and the HTTP(S) target URL.
    """

    #: A constant which can be used with the action property of a CreateSecurityRuleDetails.
    #: This constant has a value of "ALLOW"
    ACTION_ALLOW = "ALLOW"

    #: A constant which can be used with the action property of a CreateSecurityRuleDetails.
    #: This constant has a value of "DROP"
    ACTION_DROP = "DROP"

    #: A constant which can be used with the action property of a CreateSecurityRuleDetails.
    #: This constant has a value of "REJECT"
    ACTION_REJECT = "REJECT"

    #: A constant which can be used with the action property of a CreateSecurityRuleDetails.
    #: This constant has a value of "INSPECT"
    ACTION_INSPECT = "INSPECT"

    #: A constant which can be used with the inspection property of a CreateSecurityRuleDetails.
    #: This constant has a value of "INTRUSION_DETECTION"
    INSPECTION_INTRUSION_DETECTION = "INTRUSION_DETECTION"

    #: A constant which can be used with the inspection property of a CreateSecurityRuleDetails.
    #: This constant has a value of "INTRUSION_PREVENTION"
    INSPECTION_INTRUSION_PREVENTION = "INTRUSION_PREVENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSecurityRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateSecurityRuleDetails.
        :type name: str

        :param condition:
            The value to assign to the condition property of this CreateSecurityRuleDetails.
        :type condition: oci.network_firewall.models.SecurityRuleMatchCriteria

        :param action:
            The value to assign to the action property of this CreateSecurityRuleDetails.
            Allowed values for this property are: "ALLOW", "DROP", "REJECT", "INSPECT"
        :type action: str

        :param inspection:
            The value to assign to the inspection property of this CreateSecurityRuleDetails.
            Allowed values for this property are: "INTRUSION_DETECTION", "INTRUSION_PREVENTION"
        :type inspection: str

        :param position:
            The value to assign to the position property of this CreateSecurityRuleDetails.
        :type position: oci.network_firewall.models.RulePosition

        """
        self.swagger_types = {
            'name': 'str',
            'condition': 'SecurityRuleMatchCriteria',
            'action': 'str',
            'inspection': 'str',
            'position': 'RulePosition'
        }

        self.attribute_map = {
            'name': 'name',
            'condition': 'condition',
            'action': 'action',
            'inspection': 'inspection',
            'position': 'position'
        }

        self._name = None
        self._condition = None
        self._action = None
        self._inspection = None
        self._position = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateSecurityRuleDetails.
        Name for the Security rule, must be unique within the policy.


        :return: The name of this CreateSecurityRuleDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateSecurityRuleDetails.
        Name for the Security rule, must be unique within the policy.


        :param name: The name of this CreateSecurityRuleDetails.
        :type: str
        """
        self._name = name

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this CreateSecurityRuleDetails.

        :return: The condition of this CreateSecurityRuleDetails.
        :rtype: oci.network_firewall.models.SecurityRuleMatchCriteria
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this CreateSecurityRuleDetails.

        :param condition: The condition of this CreateSecurityRuleDetails.
        :type: oci.network_firewall.models.SecurityRuleMatchCriteria
        """
        self._condition = condition

    @property
    def action(self):
        """
        **[Required]** Gets the action of this CreateSecurityRuleDetails.
        Types of Action on the Traffic flow.

          * ALLOW - Allows the traffic.
          * DROP - Silently drops the traffic, e.g. without sending a TCP reset.
          * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable.
          * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection.

        Allowed values for this property are: "ALLOW", "DROP", "REJECT", "INSPECT"


        :return: The action of this CreateSecurityRuleDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this CreateSecurityRuleDetails.
        Types of Action on the Traffic flow.

          * ALLOW - Allows the traffic.
          * DROP - Silently drops the traffic, e.g. without sending a TCP reset.
          * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable.
          * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection.


        :param action: The action of this CreateSecurityRuleDetails.
        :type: str
        """
        allowed_values = ["ALLOW", "DROP", "REJECT", "INSPECT"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                f"Invalid value for `action`, must be None or one of {allowed_values}"
            )
        self._action = action

    @property
    def inspection(self):
        """
        Gets the inspection of this CreateSecurityRuleDetails.
        Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT.

          * INTRUSION_DETECTION - Intrusion Detection.
          * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as described in `type`.

        Allowed values for this property are: "INTRUSION_DETECTION", "INTRUSION_PREVENTION"


        :return: The inspection of this CreateSecurityRuleDetails.
        :rtype: str
        """
        return self._inspection

    @inspection.setter
    def inspection(self, inspection):
        """
        Sets the inspection of this CreateSecurityRuleDetails.
        Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT.

          * INTRUSION_DETECTION - Intrusion Detection.
          * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as described in `type`.


        :param inspection: The inspection of this CreateSecurityRuleDetails.
        :type: str
        """
        allowed_values = ["INTRUSION_DETECTION", "INTRUSION_PREVENTION"]
        if not value_allowed_none_or_none_sentinel(inspection, allowed_values):
            raise ValueError(
                f"Invalid value for `inspection`, must be None or one of {allowed_values}"
            )
        self._inspection = inspection

    @property
    def position(self):
        """
        Gets the position of this CreateSecurityRuleDetails.

        :return: The position of this CreateSecurityRuleDetails.
        :rtype: oci.network_firewall.models.RulePosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this CreateSecurityRuleDetails.

        :param position: The position of this CreateSecurityRuleDetails.
        :type: oci.network_firewall.models.RulePosition
        """
        self._position = position

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
