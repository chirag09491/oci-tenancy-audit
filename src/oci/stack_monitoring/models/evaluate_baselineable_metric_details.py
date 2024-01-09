# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EvaluateBaselineableMetricDetails(object):
    """
    Details for Baseline Metric Data to evaluate
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EvaluateBaselineableMetricDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this EvaluateBaselineableMetricDetails.
        :type resource_id: str

        :param items:
            The value to assign to the items property of this EvaluateBaselineableMetricDetails.
        :type items: list[oci.stack_monitoring.models.MetricData]

        """
        self.swagger_types = {
            'resource_id': 'str',
            'items': 'list[MetricData]'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'items': 'items'
        }

        self._resource_id = None
        self._items = None

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this EvaluateBaselineableMetricDetails.
        OCID of the resource


        :return: The resource_id of this EvaluateBaselineableMetricDetails.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this EvaluateBaselineableMetricDetails.
        OCID of the resource


        :param resource_id: The resource_id of this EvaluateBaselineableMetricDetails.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def items(self):
        """
        **[Required]** Gets the items of this EvaluateBaselineableMetricDetails.
        List of Metric data


        :return: The items of this EvaluateBaselineableMetricDetails.
        :rtype: list[oci.stack_monitoring.models.MetricData]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this EvaluateBaselineableMetricDetails.
        List of Metric data


        :param items: The items of this EvaluateBaselineableMetricDetails.
        :type: list[oci.stack_monitoring.models.MetricData]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
