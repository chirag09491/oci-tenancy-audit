# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetProgressSummary(object):
    """
    Progress details of the executing job for a Database target.
    """

    #: A constant which can be used with the operation_type property of a TargetProgressSummary.
    #: This constant has a value of "STAGE"
    OPERATION_TYPE_STAGE = "STAGE"

    #: A constant which can be used with the operation_type property of a TargetProgressSummary.
    #: This constant has a value of "PRECHECK"
    OPERATION_TYPE_PRECHECK = "PRECHECK"

    #: A constant which can be used with the operation_type property of a TargetProgressSummary.
    #: This constant has a value of "APPLY"
    OPERATION_TYPE_APPLY = "APPLY"

    #: A constant which can be used with the operation_type property of a TargetProgressSummary.
    #: This constant has a value of "ROLLBACK"
    OPERATION_TYPE_ROLLBACK = "ROLLBACK"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetProgressSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this TargetProgressSummary.
            Allowed values for this property are: "STAGE", "PRECHECK", "APPLY", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param progress_of_operation:
            The value to assign to the progress_of_operation property of this TargetProgressSummary.
        :type progress_of_operation: int

        """
        self.swagger_types = {
            'operation_type': 'str',
            'progress_of_operation': 'int'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'progress_of_operation': 'progressOfOperation'
        }

        self._operation_type = None
        self._progress_of_operation = None

    @property
    def operation_type(self):
        """
        Gets the operation_type of this TargetProgressSummary.
        Type of operations being executed.

        Allowed values for this property are: "STAGE", "PRECHECK", "APPLY", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this TargetProgressSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this TargetProgressSummary.
        Type of operations being executed.


        :param operation_type: The operation_type of this TargetProgressSummary.
        :type: str
        """
        allowed_values = ["STAGE", "PRECHECK", "APPLY", "ROLLBACK"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def progress_of_operation(self):
        """
        Gets the progress_of_operation of this TargetProgressSummary.
        Percentage of progress of the operation in execution.


        :return: The progress_of_operation of this TargetProgressSummary.
        :rtype: int
        """
        return self._progress_of_operation

    @progress_of_operation.setter
    def progress_of_operation(self, progress_of_operation):
        """
        Sets the progress_of_operation of this TargetProgressSummary.
        Percentage of progress of the operation in execution.


        :param progress_of_operation: The progress_of_operation of this TargetProgressSummary.
        :type: int
        """
        self._progress_of_operation = progress_of_operation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
