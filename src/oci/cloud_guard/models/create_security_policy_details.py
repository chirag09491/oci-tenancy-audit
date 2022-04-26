# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSecurityPolicyDetails(object):
    """
    The information about new SecurityPolicy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSecurityPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param friendly_name:
            The value to assign to the friendly_name property of this CreateSecurityPolicyDetails.
        :type friendly_name: str

        :param display_name:
            The value to assign to the display_name property of this CreateSecurityPolicyDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateSecurityPolicyDetails.
        :type description: str

        :param category:
            The value to assign to the category property of this CreateSecurityPolicyDetails.
        :type category: str

        :param services:
            The value to assign to the services property of this CreateSecurityPolicyDetails.
        :type services: list[str]

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSecurityPolicyDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSecurityPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSecurityPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'friendly_name': 'str',
            'display_name': 'str',
            'description': 'str',
            'category': 'str',
            'services': 'list[str]',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'friendly_name': 'friendlyName',
            'display_name': 'displayName',
            'description': 'description',
            'category': 'category',
            'services': 'services',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._friendly_name = None
        self._display_name = None
        self._description = None
        self._category = None
        self._services = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def friendly_name(self):
        """
        Gets the friendly_name of this CreateSecurityPolicyDetails.
        SecurityPolicy friendly name


        :return: The friendly_name of this CreateSecurityPolicyDetails.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """
        Sets the friendly_name of this CreateSecurityPolicyDetails.
        SecurityPolicy friendly name


        :param friendly_name: The friendly_name of this CreateSecurityPolicyDetails.
        :type: str
        """
        self._friendly_name = friendly_name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateSecurityPolicyDetails.
        SecurityPolicy Identifier


        :return: The display_name of this CreateSecurityPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSecurityPolicyDetails.
        SecurityPolicy Identifier


        :param display_name: The display_name of this CreateSecurityPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateSecurityPolicyDetails.
        Security policy description


        :return: The description of this CreateSecurityPolicyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateSecurityPolicyDetails.
        Security policy description


        :param description: The description of this CreateSecurityPolicyDetails.
        :type: str
        """
        self._description = description

    @property
    def category(self):
        """
        Gets the category of this CreateSecurityPolicyDetails.
        The category of security policy.


        :return: The category of this CreateSecurityPolicyDetails.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this CreateSecurityPolicyDetails.
        The category of security policy.


        :param category: The category of this CreateSecurityPolicyDetails.
        :type: str
        """
        self._category = category

    @property
    def services(self):
        """
        Gets the services of this CreateSecurityPolicyDetails.
        The list of services for policy.


        :return: The services of this CreateSecurityPolicyDetails.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this CreateSecurityPolicyDetails.
        The list of services for policy.


        :param services: The services of this CreateSecurityPolicyDetails.
        :type: list[str]
        """
        self._services = services

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSecurityPolicyDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateSecurityPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSecurityPolicyDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateSecurityPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSecurityPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this CreateSecurityPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSecurityPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this CreateSecurityPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSecurityPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateSecurityPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSecurityPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateSecurityPolicyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
