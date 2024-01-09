# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131

from .continuous_query_start_policy import ContinuousQueryStartPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NoDelayStartPolicy(ContinuousQueryStartPolicy):
    """
    Continuous query start policy that starts the query immediately.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NoDelayStartPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.NoDelayStartPolicy.start_policy_type` attribute
        of this class is ``NO_DELAY_START_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param start_policy_type:
            The value to assign to the start_policy_type property of this NoDelayStartPolicy.
            Allowed values for this property are: "NO_DELAY_START_POLICY", "ABSOLUTE_TIME_START_POLICY"
        :type start_policy_type: str

        """
        self.swagger_types = {
            'start_policy_type': 'str'
        }

        self.attribute_map = {
            'start_policy_type': 'startPolicyType'
        }

        self._start_policy_type = None
        self._start_policy_type = 'NO_DELAY_START_POLICY'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
