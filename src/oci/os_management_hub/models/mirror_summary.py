# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MirrorSummary(object):
    """
    Summary of a Mirror
    """

    #: A constant which can be used with the type property of a MirrorSummary.
    #: This constant has a value of "CUSTOM"
    TYPE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the type property of a MirrorSummary.
    #: This constant has a value of "VENDOR"
    TYPE_VENDOR = "VENDOR"

    #: A constant which can be used with the type property of a MirrorSummary.
    #: This constant has a value of "VERSIONED"
    TYPE_VERSIONED = "VERSIONED"

    #: A constant which can be used with the os_family property of a MirrorSummary.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a MirrorSummary.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a MirrorSummary.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the arch_type property of a MirrorSummary.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a MirrorSummary.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a MirrorSummary.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a MirrorSummary.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a MirrorSummary.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the state property of a MirrorSummary.
    #: This constant has a value of "UNSYNCED"
    STATE_UNSYNCED = "UNSYNCED"

    #: A constant which can be used with the state property of a MirrorSummary.
    #: This constant has a value of "QUEUED"
    STATE_QUEUED = "QUEUED"

    #: A constant which can be used with the state property of a MirrorSummary.
    #: This constant has a value of "SYNCING"
    STATE_SYNCING = "SYNCING"

    #: A constant which can be used with the state property of a MirrorSummary.
    #: This constant has a value of "SYNCED"
    STATE_SYNCED = "SYNCED"

    #: A constant which can be used with the state property of a MirrorSummary.
    #: This constant has a value of "FAILED"
    STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MirrorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MirrorSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this MirrorSummary.
        :type display_name: str

        :param type:
            The value to assign to the type property of this MirrorSummary.
            Allowed values for this property are: "CUSTOM", "VENDOR", "VERSIONED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param os_family:
            The value to assign to the os_family property of this MirrorSummary.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this MirrorSummary.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param state:
            The value to assign to the state property of this MirrorSummary.
            Allowed values for this property are: "UNSYNCED", "QUEUED", "SYNCING", "SYNCED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        :param percentage:
            The value to assign to the percentage property of this MirrorSummary.
        :type percentage: int

        :param time_last_synced:
            The value to assign to the time_last_synced property of this MirrorSummary.
        :type time_last_synced: datetime

        :param log:
            The value to assign to the log property of this MirrorSummary.
        :type log: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'type': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'state': 'str',
            'percentage': 'int',
            'time_last_synced': 'datetime',
            'log': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'type': 'type',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'state': 'state',
            'percentage': 'percentage',
            'time_last_synced': 'timeLastSynced',
            'log': 'log'
        }

        self._id = None
        self._display_name = None
        self._type = None
        self._os_family = None
        self._arch_type = None
        self._state = None
        self._percentage = None
        self._time_last_synced = None
        self._log = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MirrorSummary.
        OCID of a software source


        :return: The id of this MirrorSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MirrorSummary.
        OCID of a software source


        :param id: The id of this MirrorSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this MirrorSummary.
        Display name of the mirror


        :return: The display_name of this MirrorSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MirrorSummary.
        Display name of the mirror


        :param display_name: The display_name of this MirrorSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        Gets the type of this MirrorSummary.
        Type of the mirror

        Allowed values for this property are: "CUSTOM", "VENDOR", "VERSIONED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this MirrorSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MirrorSummary.
        Type of the mirror


        :param type: The type of this MirrorSummary.
        :type: str
        """
        allowed_values = ["CUSTOM", "VENDOR", "VERSIONED"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def os_family(self):
        """
        Gets the os_family of this MirrorSummary.
        The OS family the Software Source belongs to

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this MirrorSummary.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this MirrorSummary.
        The OS family the Software Source belongs to


        :param os_family: The os_family of this MirrorSummary.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        Gets the arch_type of this MirrorSummary.
        The architecture type supported by the Software Source

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The arch_type of this MirrorSummary.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this MirrorSummary.
        The architecture type supported by the Software Source


        :param arch_type: The arch_type of this MirrorSummary.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            arch_type = 'UNKNOWN_ENUM_VALUE'
        self._arch_type = arch_type

    @property
    def state(self):
        """
        **[Required]** Gets the state of this MirrorSummary.
        Current state of the mirror

        Allowed values for this property are: "UNSYNCED", "QUEUED", "SYNCING", "SYNCED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this MirrorSummary.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this MirrorSummary.
        Current state of the mirror


        :param state: The state of this MirrorSummary.
        :type: str
        """
        allowed_values = ["UNSYNCED", "QUEUED", "SYNCING", "SYNCED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    @property
    def percentage(self):
        """
        **[Required]** Gets the percentage of this MirrorSummary.
        A decimal number representing the completness percentage


        :return: The percentage of this MirrorSummary.
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this MirrorSummary.
        A decimal number representing the completness percentage


        :param percentage: The percentage of this MirrorSummary.
        :type: int
        """
        self._percentage = percentage

    @property
    def time_last_synced(self):
        """
        **[Required]** Gets the time_last_synced of this MirrorSummary.
        Timestamp of the last time the mirror was sync


        :return: The time_last_synced of this MirrorSummary.
        :rtype: datetime
        """
        return self._time_last_synced

    @time_last_synced.setter
    def time_last_synced(self, time_last_synced):
        """
        Sets the time_last_synced of this MirrorSummary.
        Timestamp of the last time the mirror was sync


        :param time_last_synced: The time_last_synced of this MirrorSummary.
        :type: datetime
        """
        self._time_last_synced = time_last_synced

    @property
    def log(self):
        """
        **[Required]** Gets the log of this MirrorSummary.
        The current log from the management station plugin.


        :return: The log of this MirrorSummary.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """
        Sets the log of this MirrorSummary.
        The current log from the management station plugin.


        :param log: The log of this MirrorSummary.
        :type: str
        """
        self._log = log

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other