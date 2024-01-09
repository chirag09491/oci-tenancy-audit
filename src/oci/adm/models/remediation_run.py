# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemediationRun(object):
    """
    A remediation run represents an execution of a Remediation Recipe to detect and fix vulnerabilities based on current state of the
    Vulnerabilities curated in the Knowledge Base.
    A Run can be triggered manually or when a new CVE is discovered.
    """

    #: A constant which can be used with the remediation_run_source property of a RemediationRun.
    #: This constant has a value of "MANUAL"
    REMEDIATION_RUN_SOURCE_MANUAL = "MANUAL"

    #: A constant which can be used with the remediation_run_source property of a RemediationRun.
    #: This constant has a value of "KNOWLEDGE_BASE"
    REMEDIATION_RUN_SOURCE_KNOWLEDGE_BASE = "KNOWLEDGE_BASE"

    #: A constant which can be used with the current_stage_type property of a RemediationRun.
    #: This constant has a value of "DETECT"
    CURRENT_STAGE_TYPE_DETECT = "DETECT"

    #: A constant which can be used with the current_stage_type property of a RemediationRun.
    #: This constant has a value of "RECOMMEND"
    CURRENT_STAGE_TYPE_RECOMMEND = "RECOMMEND"

    #: A constant which can be used with the current_stage_type property of a RemediationRun.
    #: This constant has a value of "VERIFY"
    CURRENT_STAGE_TYPE_VERIFY = "VERIFY"

    #: A constant which can be used with the current_stage_type property of a RemediationRun.
    #: This constant has a value of "APPLY"
    CURRENT_STAGE_TYPE_APPLY = "APPLY"

    #: A constant which can be used with the lifecycle_state property of a RemediationRun.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a RemediationRun.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a RemediationRun.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a RemediationRun.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a RemediationRun.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a RemediationRun.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a RemediationRun.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a RemediationRun.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new RemediationRun object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RemediationRun.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this RemediationRun.
        :type display_name: str

        :param stages:
            The value to assign to the stages property of this RemediationRun.
        :type stages: list[oci.adm.models.StageSummary]

        :param remediation_recipe_id:
            The value to assign to the remediation_recipe_id property of this RemediationRun.
        :type remediation_recipe_id: str

        :param remediation_run_source:
            The value to assign to the remediation_run_source property of this RemediationRun.
            Allowed values for this property are: "MANUAL", "KNOWLEDGE_BASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type remediation_run_source: str

        :param time_created:
            The value to assign to the time_created property of this RemediationRun.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RemediationRun.
        :type time_updated: datetime

        :param time_started:
            The value to assign to the time_started property of this RemediationRun.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this RemediationRun.
        :type time_finished: datetime

        :param current_stage_type:
            The value to assign to the current_stage_type property of this RemediationRun.
            Allowed values for this property are: "DETECT", "RECOMMEND", "VERIFY", "APPLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type current_stage_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RemediationRun.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RemediationRun.
            Allowed values for this property are: "ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RemediationRun.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RemediationRun.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this RemediationRun.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'stages': 'list[StageSummary]',
            'remediation_recipe_id': 'str',
            'remediation_run_source': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'current_stage_type': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'stages': 'stages',
            'remediation_recipe_id': 'remediationRecipeId',
            'remediation_run_source': 'remediationRunSource',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'current_stage_type': 'currentStageType',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._stages = None
        self._remediation_recipe_id = None
        self._remediation_run_source = None
        self._time_created = None
        self._time_updated = None
        self._time_started = None
        self._time_finished = None
        self._current_stage_type = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RemediationRun.
        The Oracle Cloud Identifier (`OCID`__) of the remediation run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this RemediationRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RemediationRun.
        The Oracle Cloud Identifier (`OCID`__) of the remediation run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this RemediationRun.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this RemediationRun.
        The name of the remediation run.


        :return: The display_name of this RemediationRun.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RemediationRun.
        The name of the remediation run.


        :param display_name: The display_name of this RemediationRun.
        :type: str
        """
        self._display_name = display_name

    @property
    def stages(self):
        """
        Gets the stages of this RemediationRun.
        The list of remediation run stage summaries.


        :return: The stages of this RemediationRun.
        :rtype: list[oci.adm.models.StageSummary]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this RemediationRun.
        The list of remediation run stage summaries.


        :param stages: The stages of this RemediationRun.
        :type: list[oci.adm.models.StageSummary]
        """
        self._stages = stages

    @property
    def remediation_recipe_id(self):
        """
        **[Required]** Gets the remediation_recipe_id of this RemediationRun.
        The Oracle Cloud Identifier (`OCID`__) of the Remediation Recipe.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The remediation_recipe_id of this RemediationRun.
        :rtype: str
        """
        return self._remediation_recipe_id

    @remediation_recipe_id.setter
    def remediation_recipe_id(self, remediation_recipe_id):
        """
        Sets the remediation_recipe_id of this RemediationRun.
        The Oracle Cloud Identifier (`OCID`__) of the Remediation Recipe.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param remediation_recipe_id: The remediation_recipe_id of this RemediationRun.
        :type: str
        """
        self._remediation_recipe_id = remediation_recipe_id

    @property
    def remediation_run_source(self):
        """
        **[Required]** Gets the remediation_run_source of this RemediationRun.
        The source that triggered the Remediation Recipe.

        Allowed values for this property are: "MANUAL", "KNOWLEDGE_BASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The remediation_run_source of this RemediationRun.
        :rtype: str
        """
        return self._remediation_run_source

    @remediation_run_source.setter
    def remediation_run_source(self, remediation_run_source):
        """
        Sets the remediation_run_source of this RemediationRun.
        The source that triggered the Remediation Recipe.


        :param remediation_run_source: The remediation_run_source of this RemediationRun.
        :type: str
        """
        allowed_values = ["MANUAL", "KNOWLEDGE_BASE"]
        if not value_allowed_none_or_none_sentinel(remediation_run_source, allowed_values):
            remediation_run_source = 'UNKNOWN_ENUM_VALUE'
        self._remediation_run_source = remediation_run_source

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this RemediationRun.
        The creation date and time of the remediation run (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this RemediationRun.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RemediationRun.
        The creation date and time of the remediation run (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this RemediationRun.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this RemediationRun.
        The date and time the remediation run was last updated (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this RemediationRun.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RemediationRun.
        The date and time the remediation run was last updated (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this RemediationRun.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_started(self):
        """
        Gets the time_started of this RemediationRun.
        The date and time of the start of the remediation run (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_started of this RemediationRun.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this RemediationRun.
        The date and time of the start of the remediation run (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_started: The time_started of this RemediationRun.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this RemediationRun.
        The date and time of the finish of the remediation run (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_finished of this RemediationRun.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this RemediationRun.
        The date and time of the finish of the remediation run (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_finished: The time_finished of this RemediationRun.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def current_stage_type(self):
        """
        Gets the current_stage_type of this RemediationRun.
        The type of the current stage of the remediation run.

        Allowed values for this property are: "DETECT", "RECOMMEND", "VERIFY", "APPLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The current_stage_type of this RemediationRun.
        :rtype: str
        """
        return self._current_stage_type

    @current_stage_type.setter
    def current_stage_type(self, current_stage_type):
        """
        Sets the current_stage_type of this RemediationRun.
        The type of the current stage of the remediation run.


        :param current_stage_type: The current_stage_type of this RemediationRun.
        :type: str
        """
        allowed_values = ["DETECT", "RECOMMEND", "VERIFY", "APPLY"]
        if not value_allowed_none_or_none_sentinel(current_stage_type, allowed_values):
            current_stage_type = 'UNKNOWN_ENUM_VALUE'
        self._current_stage_type = current_stage_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RemediationRun.
        The compartment Oracle Cloud Identifier (`OCID`__) of the remediation run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this RemediationRun.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RemediationRun.
        The compartment Oracle Cloud Identifier (`OCID`__) of the remediation run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this RemediationRun.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RemediationRun.
        The current lifecycle state of the remediation run.

        Allowed values for this property are: "ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RemediationRun.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RemediationRun.
        The current lifecycle state of the remediation run.


        :param lifecycle_state: The lifecycle_state of this RemediationRun.
        :type: str
        """
        allowed_values = ["ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this RemediationRun.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this RemediationRun.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RemediationRun.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this RemediationRun.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this RemediationRun.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this RemediationRun.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RemediationRun.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this RemediationRun.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this RemediationRun.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this RemediationRun.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this RemediationRun.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this RemediationRun.
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
