# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePipelineRunDetails(object):
    """
    The information about new PipelineRun.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePipelineRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param project_id:
            The value to assign to the project_id property of this CreatePipelineRunDetails.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePipelineRunDetails.
        :type compartment_id: str

        :param pipeline_id:
            The value to assign to the pipeline_id property of this CreatePipelineRunDetails.
        :type pipeline_id: str

        :param display_name:
            The value to assign to the display_name property of this CreatePipelineRunDetails.
        :type display_name: str

        :param configuration_override_details:
            The value to assign to the configuration_override_details property of this CreatePipelineRunDetails.
        :type configuration_override_details: oci.data_science.models.PipelineConfigurationDetails

        :param log_configuration_override_details:
            The value to assign to the log_configuration_override_details property of this CreatePipelineRunDetails.
        :type log_configuration_override_details: oci.data_science.models.PipelineLogConfigurationDetails

        :param step_override_details:
            The value to assign to the step_override_details property of this CreatePipelineRunDetails.
        :type step_override_details: list[oci.data_science.models.PipelineStepOverrideDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePipelineRunDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePipelineRunDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CreatePipelineRunDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'project_id': 'str',
            'compartment_id': 'str',
            'pipeline_id': 'str',
            'display_name': 'str',
            'configuration_override_details': 'PipelineConfigurationDetails',
            'log_configuration_override_details': 'PipelineLogConfigurationDetails',
            'step_override_details': 'list[PipelineStepOverrideDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'pipeline_id': 'pipelineId',
            'display_name': 'displayName',
            'configuration_override_details': 'configurationOverrideDetails',
            'log_configuration_override_details': 'logConfigurationOverrideDetails',
            'step_override_details': 'stepOverrideDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._project_id = None
        self._compartment_id = None
        self._pipeline_id = None
        self._display_name = None
        self._configuration_override_details = None
        self._log_configuration_override_details = None
        self._step_override_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def project_id(self):
        """
        Gets the project_id of this CreatePipelineRunDetails.
        The `OCID`__ of the project to associate the pipeline run with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this CreatePipelineRunDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreatePipelineRunDetails.
        The `OCID`__ of the project to associate the pipeline run with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this CreatePipelineRunDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreatePipelineRunDetails.
        The `OCID`__ of the compartment where you want to create the pipeline run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreatePipelineRunDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreatePipelineRunDetails.
        The `OCID`__ of the compartment where you want to create the pipeline run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreatePipelineRunDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def pipeline_id(self):
        """
        **[Required]** Gets the pipeline_id of this CreatePipelineRunDetails.
        The `OCID`__ of the pipeline for which pipeline run is created.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The pipeline_id of this CreatePipelineRunDetails.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """
        Sets the pipeline_id of this CreatePipelineRunDetails.
        The `OCID`__ of the pipeline for which pipeline run is created.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param pipeline_id: The pipeline_id of this CreatePipelineRunDetails.
        :type: str
        """
        self._pipeline_id = pipeline_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreatePipelineRunDetails.
        A user-friendly display name for the resource.


        :return: The display_name of this CreatePipelineRunDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreatePipelineRunDetails.
        A user-friendly display name for the resource.


        :param display_name: The display_name of this CreatePipelineRunDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def configuration_override_details(self):
        """
        Gets the configuration_override_details of this CreatePipelineRunDetails.

        :return: The configuration_override_details of this CreatePipelineRunDetails.
        :rtype: oci.data_science.models.PipelineConfigurationDetails
        """
        return self._configuration_override_details

    @configuration_override_details.setter
    def configuration_override_details(self, configuration_override_details):
        """
        Sets the configuration_override_details of this CreatePipelineRunDetails.

        :param configuration_override_details: The configuration_override_details of this CreatePipelineRunDetails.
        :type: oci.data_science.models.PipelineConfigurationDetails
        """
        self._configuration_override_details = configuration_override_details

    @property
    def log_configuration_override_details(self):
        """
        Gets the log_configuration_override_details of this CreatePipelineRunDetails.

        :return: The log_configuration_override_details of this CreatePipelineRunDetails.
        :rtype: oci.data_science.models.PipelineLogConfigurationDetails
        """
        return self._log_configuration_override_details

    @log_configuration_override_details.setter
    def log_configuration_override_details(self, log_configuration_override_details):
        """
        Sets the log_configuration_override_details of this CreatePipelineRunDetails.

        :param log_configuration_override_details: The log_configuration_override_details of this CreatePipelineRunDetails.
        :type: oci.data_science.models.PipelineLogConfigurationDetails
        """
        self._log_configuration_override_details = log_configuration_override_details

    @property
    def step_override_details(self):
        """
        Gets the step_override_details of this CreatePipelineRunDetails.
        Array of step override details. Only Step Configuration is allowed to be overridden.


        :return: The step_override_details of this CreatePipelineRunDetails.
        :rtype: list[oci.data_science.models.PipelineStepOverrideDetails]
        """
        return self._step_override_details

    @step_override_details.setter
    def step_override_details(self, step_override_details):
        """
        Sets the step_override_details of this CreatePipelineRunDetails.
        Array of step override details. Only Step Configuration is allowed to be overridden.


        :param step_override_details: The step_override_details of this CreatePipelineRunDetails.
        :type: list[oci.data_science.models.PipelineStepOverrideDetails]
        """
        self._step_override_details = step_override_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreatePipelineRunDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreatePipelineRunDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreatePipelineRunDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreatePipelineRunDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreatePipelineRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreatePipelineRunDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreatePipelineRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreatePipelineRunDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreatePipelineRunDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this CreatePipelineRunDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreatePipelineRunDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this CreatePipelineRunDetails.
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