# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityPolicy(object):
    """
    A security policy defines a security requirement for resources in a security zone. If a security zone enables a policy (using a recipe), then any action that attempts to violate that policy is denied.
    """

    #: A constant which can be used with the owner property of a SecurityPolicy.
    #: This constant has a value of "CUSTOMER"
    OWNER_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the owner property of a SecurityPolicy.
    #: This constant has a value of "ORACLE"
    OWNER_ORACLE = "ORACLE"

    #: A constant which can be used with the lifecycle_state property of a SecurityPolicy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SecurityPolicy.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SecurityPolicy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SecurityPolicy.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SecurityPolicy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SecurityPolicy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SecurityPolicy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SecurityPolicy.
        :type id: str

        :param friendly_name:
            The value to assign to the friendly_name property of this SecurityPolicy.
        :type friendly_name: str

        :param display_name:
            The value to assign to the display_name property of this SecurityPolicy.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SecurityPolicy.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SecurityPolicy.
        :type compartment_id: str

        :param owner:
            The value to assign to the owner property of this SecurityPolicy.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type owner: str

        :param category:
            The value to assign to the category property of this SecurityPolicy.
        :type category: str

        :param services:
            The value to assign to the services property of this SecurityPolicy.
        :type services: list[str]

        :param time_created:
            The value to assign to the time_created property of this SecurityPolicy.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SecurityPolicy.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SecurityPolicy.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SecurityPolicy.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SecurityPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SecurityPolicy.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SecurityPolicy.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'friendly_name': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'owner': 'str',
            'category': 'str',
            'services': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'friendly_name': 'friendlyName',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'owner': 'owner',
            'category': 'category',
            'services': 'services',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._friendly_name = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._owner = None
        self._category = None
        self._services = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SecurityPolicy.
        Unique identifier that is immutable on creation


        :return: The id of this SecurityPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityPolicy.
        Unique identifier that is immutable on creation


        :param id: The id of this SecurityPolicy.
        :type: str
        """
        self._id = id

    @property
    def friendly_name(self):
        """
        Gets the friendly_name of this SecurityPolicy.
        A shorter version of the security policy's name


        :return: The friendly_name of this SecurityPolicy.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """
        Sets the friendly_name of this SecurityPolicy.
        A shorter version of the security policy's name


        :param friendly_name: The friendly_name of this SecurityPolicy.
        :type: str
        """
        self._friendly_name = friendly_name

    @property
    def display_name(self):
        """
        Gets the display_name of this SecurityPolicy.
        The security policy's full name


        :return: The display_name of this SecurityPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SecurityPolicy.
        The security policy's full name


        :param display_name: The display_name of this SecurityPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SecurityPolicy.
        The security policy's description


        :return: The description of this SecurityPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SecurityPolicy.
        The security policy's description


        :param description: The description of this SecurityPolicy.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SecurityPolicy.
        The id of the security policy's compartment


        :return: The compartment_id of this SecurityPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SecurityPolicy.
        The id of the security policy's compartment


        :param compartment_id: The compartment_id of this SecurityPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this SecurityPolicy.
        The owner of the security policy

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The owner of this SecurityPolicy.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this SecurityPolicy.
        The owner of the security policy


        :param owner: The owner of this SecurityPolicy.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(owner, allowed_values):
            owner = 'UNKNOWN_ENUM_VALUE'
        self._owner = owner

    @property
    def category(self):
        """
        Gets the category of this SecurityPolicy.
        The category of security policy


        :return: The category of this SecurityPolicy.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this SecurityPolicy.
        The category of security policy


        :param category: The category of this SecurityPolicy.
        :type: str
        """
        self._category = category

    @property
    def services(self):
        """
        Gets the services of this SecurityPolicy.
        The list of services that the security policy protects


        :return: The services of this SecurityPolicy.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this SecurityPolicy.
        The list of services that the security policy protects


        :param services: The services of this SecurityPolicy.
        :type: list[str]
        """
        self._services = services

    @property
    def time_created(self):
        """
        Gets the time_created of this SecurityPolicy.
        The time the security policy was created. An RFC3339 formatted datetime string.


        :return: The time_created of this SecurityPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityPolicy.
        The time the security policy was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this SecurityPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SecurityPolicy.
        The time the security policy was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this SecurityPolicy.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SecurityPolicy.
        The time the security policy was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this SecurityPolicy.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SecurityPolicy.
        The current state of the security policy

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SecurityPolicy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SecurityPolicy.
        The current state of the security policy


        :param lifecycle_state: The lifecycle_state of this SecurityPolicy.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SecurityPolicy.
        A message describing the current state in more detail. For example, this can be used to provide actionable information for a resource in a `Failed` state.


        :return: The lifecycle_details of this SecurityPolicy.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SecurityPolicy.
        A message describing the current state in more detail. For example, this can be used to provide actionable information for a resource in a `Failed` state.


        :param lifecycle_details: The lifecycle_details of this SecurityPolicy.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SecurityPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this SecurityPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SecurityPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this SecurityPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SecurityPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this SecurityPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SecurityPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this SecurityPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SecurityPolicy.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this SecurityPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SecurityPolicy.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this SecurityPolicy.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
