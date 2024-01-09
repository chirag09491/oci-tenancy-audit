# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlocklistEntry(object):
    """
    An entry for blocklist to describe blocked operation and reason.
    """

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "CREATE_FLEET"
    OPERATION_CREATE_FLEET = "CREATE_FLEET"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "DELETE_FLEET"
    OPERATION_DELETE_FLEET = "DELETE_FLEET"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "MOVE_FLEET"
    OPERATION_MOVE_FLEET = "MOVE_FLEET"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "UPDATE_FLEET"
    OPERATION_UPDATE_FLEET = "UPDATE_FLEET"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "UPDATE_FLEET_AGENT_CONFIGURATION"
    OPERATION_UPDATE_FLEET_AGENT_CONFIGURATION = "UPDATE_FLEET_AGENT_CONFIGURATION"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "DELETE_JAVA_INSTALLATION"
    OPERATION_DELETE_JAVA_INSTALLATION = "DELETE_JAVA_INSTALLATION"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "CREATE_JAVA_INSTALLATION"
    OPERATION_CREATE_JAVA_INSTALLATION = "CREATE_JAVA_INSTALLATION"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "COLLECT_JFR"
    OPERATION_COLLECT_JFR = "COLLECT_JFR"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "REQUEST_CRYPTO_EVENT_ANALYSIS"
    OPERATION_REQUEST_CRYPTO_EVENT_ANALYSIS = "REQUEST_CRYPTO_EVENT_ANALYSIS"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "REQUEST_PERFORMANCE_TUNING_ANALYSIS"
    OPERATION_REQUEST_PERFORMANCE_TUNING_ANALYSIS = "REQUEST_PERFORMANCE_TUNING_ANALYSIS"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "REQUEST_JAVA_MIGRATION_ANALYSIS"
    OPERATION_REQUEST_JAVA_MIGRATION_ANALYSIS = "REQUEST_JAVA_MIGRATION_ANALYSIS"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "DELETE_JMS_REPORT"
    OPERATION_DELETE_JMS_REPORT = "DELETE_JMS_REPORT"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "SCAN_JAVA_SERVER_USAGE"
    OPERATION_SCAN_JAVA_SERVER_USAGE = "SCAN_JAVA_SERVER_USAGE"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "SCAN_LIBRARY_USAGE"
    OPERATION_SCAN_LIBRARY_USAGE = "SCAN_LIBRARY_USAGE"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "EXPORT_DATA_CSV"
    OPERATION_EXPORT_DATA_CSV = "EXPORT_DATA_CSV"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "CREATE_DRS_FILE"
    OPERATION_CREATE_DRS_FILE = "CREATE_DRS_FILE"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "UPDATE_DRS_FILE"
    OPERATION_UPDATE_DRS_FILE = "UPDATE_DRS_FILE"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "DELETE_DRS_FILE"
    OPERATION_DELETE_DRS_FILE = "DELETE_DRS_FILE"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "ENABLE_DRS"
    OPERATION_ENABLE_DRS = "ENABLE_DRS"

    #: A constant which can be used with the operation property of a BlocklistEntry.
    #: This constant has a value of "DISABLE_DRS"
    OPERATION_DISABLE_DRS = "DISABLE_DRS"

    def __init__(self, **kwargs):
        """
        Initializes a new BlocklistEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this BlocklistEntry.
            Allowed values for this property are: "CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION", "COLLECT_JFR", "REQUEST_CRYPTO_EVENT_ANALYSIS", "REQUEST_PERFORMANCE_TUNING_ANALYSIS", "REQUEST_JAVA_MIGRATION_ANALYSIS", "DELETE_JMS_REPORT", "SCAN_JAVA_SERVER_USAGE", "SCAN_LIBRARY_USAGE", "EXPORT_DATA_CSV", "CREATE_DRS_FILE", "UPDATE_DRS_FILE", "DELETE_DRS_FILE", "ENABLE_DRS", "DISABLE_DRS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation: str

        :param reason:
            The value to assign to the reason property of this BlocklistEntry.
        :type reason: str

        """
        self.swagger_types = {
            'operation': 'str',
            'reason': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'reason': 'reason'
        }

        self._operation = None
        self._reason = None

    @property
    def operation(self):
        """
        **[Required]** Gets the operation of this BlocklistEntry.
        The operation type.

        Allowed values for this property are: "CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION", "COLLECT_JFR", "REQUEST_CRYPTO_EVENT_ANALYSIS", "REQUEST_PERFORMANCE_TUNING_ANALYSIS", "REQUEST_JAVA_MIGRATION_ANALYSIS", "DELETE_JMS_REPORT", "SCAN_JAVA_SERVER_USAGE", "SCAN_LIBRARY_USAGE", "EXPORT_DATA_CSV", "CREATE_DRS_FILE", "UPDATE_DRS_FILE", "DELETE_DRS_FILE", "ENABLE_DRS", "DISABLE_DRS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation of this BlocklistEntry.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this BlocklistEntry.
        The operation type.


        :param operation: The operation of this BlocklistEntry.
        :type: str
        """
        allowed_values = ["CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION", "COLLECT_JFR", "REQUEST_CRYPTO_EVENT_ANALYSIS", "REQUEST_PERFORMANCE_TUNING_ANALYSIS", "REQUEST_JAVA_MIGRATION_ANALYSIS", "DELETE_JMS_REPORT", "SCAN_JAVA_SERVER_USAGE", "SCAN_LIBRARY_USAGE", "EXPORT_DATA_CSV", "CREATE_DRS_FILE", "UPDATE_DRS_FILE", "DELETE_DRS_FILE", "ENABLE_DRS", "DISABLE_DRS"]
        if not value_allowed_none_or_none_sentinel(operation, allowed_values):
            operation = 'UNKNOWN_ENUM_VALUE'
        self._operation = operation

    @property
    def reason(self):
        """
        **[Required]** Gets the reason of this BlocklistEntry.
        The reason why the operation is blocklisted.


        :return: The reason of this BlocklistEntry.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this BlocklistEntry.
        The reason why the operation is blocklisted.


        :param reason: The reason of this BlocklistEntry.
        :type: str
        """
        self._reason = reason

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
