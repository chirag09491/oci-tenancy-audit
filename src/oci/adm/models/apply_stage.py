# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421

from .remediation_run_stage import RemediationRunStage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplyStage(RemediationRunStage):
    """
    An apply stage merges the changes if the pull request is accepted.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplyStage object with values from keyword arguments. The default value of the :py:attr:`~oci.adm.models.ApplyStage.type` attribute
        of this class is ``APPLY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this ApplyStage.
            Allowed values for this property are: "CREATED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this ApplyStage.
        :type time_created: datetime

        :param time_started:
            The value to assign to the time_started property of this ApplyStage.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this ApplyStage.
        :type time_finished: datetime

        :param type:
            The value to assign to the type property of this ApplyStage.
            Allowed values for this property are: "DETECT", "RECOMMEND", "VERIFY", "APPLY"
        :type type: str

        :param summary:
            The value to assign to the summary property of this ApplyStage.
        :type summary: str

        :param remediation_run_id:
            The value to assign to the remediation_run_id property of this ApplyStage.
        :type remediation_run_id: str

        :param previous_stage_type:
            The value to assign to the previous_stage_type property of this ApplyStage.
            Allowed values for this property are: "DETECT", "RECOMMEND", "VERIFY", "APPLY"
        :type previous_stage_type: str

        :param next_stage_type:
            The value to assign to the next_stage_type property of this ApplyStage.
            Allowed values for this property are: "DETECT", "RECOMMEND", "VERIFY", "APPLY"
        :type next_stage_type: str

        :param pull_request_properties:
            The value to assign to the pull_request_properties property of this ApplyStage.
        :type pull_request_properties: oci.adm.models.PullRequestProperties

        :param pipeline_properties:
            The value to assign to the pipeline_properties property of this ApplyStage.
        :type pipeline_properties: oci.adm.models.PipelineProperties

        """
        self.swagger_types = {
            'status': 'str',
            'time_created': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'type': 'str',
            'summary': 'str',
            'remediation_run_id': 'str',
            'previous_stage_type': 'str',
            'next_stage_type': 'str',
            'pull_request_properties': 'PullRequestProperties',
            'pipeline_properties': 'PipelineProperties'
        }

        self.attribute_map = {
            'status': 'status',
            'time_created': 'timeCreated',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'type': 'type',
            'summary': 'summary',
            'remediation_run_id': 'remediationRunId',
            'previous_stage_type': 'previousStageType',
            'next_stage_type': 'nextStageType',
            'pull_request_properties': 'pullRequestProperties',
            'pipeline_properties': 'pipelineProperties'
        }

        self._status = None
        self._time_created = None
        self._time_started = None
        self._time_finished = None
        self._type = None
        self._summary = None
        self._remediation_run_id = None
        self._previous_stage_type = None
        self._next_stage_type = None
        self._pull_request_properties = None
        self._pipeline_properties = None
        self._type = 'APPLY'

    @property
    def pull_request_properties(self):
        """
        Gets the pull_request_properties of this ApplyStage.

        :return: The pull_request_properties of this ApplyStage.
        :rtype: oci.adm.models.PullRequestProperties
        """
        return self._pull_request_properties

    @pull_request_properties.setter
    def pull_request_properties(self, pull_request_properties):
        """
        Sets the pull_request_properties of this ApplyStage.

        :param pull_request_properties: The pull_request_properties of this ApplyStage.
        :type: oci.adm.models.PullRequestProperties
        """
        self._pull_request_properties = pull_request_properties

    @property
    def pipeline_properties(self):
        """
        Gets the pipeline_properties of this ApplyStage.

        :return: The pipeline_properties of this ApplyStage.
        :rtype: oci.adm.models.PipelineProperties
        """
        return self._pipeline_properties

    @pipeline_properties.setter
    def pipeline_properties(self, pipeline_properties):
        """
        Sets the pipeline_properties of this ApplyStage.

        :param pipeline_properties: The pipeline_properties of this ApplyStage.
        :type: oci.adm.models.PipelineProperties
        """
        self._pipeline_properties = pipeline_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
