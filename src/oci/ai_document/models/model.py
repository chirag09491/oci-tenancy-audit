# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Model(object):
    """
    Machine-learned Model.
    """

    #: A constant which can be used with the model_type property of a Model.
    #: This constant has a value of "KEY_VALUE_EXTRACTION"
    MODEL_TYPE_KEY_VALUE_EXTRACTION = "KEY_VALUE_EXTRACTION"

    #: A constant which can be used with the model_type property of a Model.
    #: This constant has a value of "DOCUMENT_CLASSIFICATION"
    MODEL_TYPE_DOCUMENT_CLASSIFICATION = "DOCUMENT_CLASSIFICATION"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Model object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Model.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Model.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Model.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Model.
        :type compartment_id: str

        :param model_type:
            The value to assign to the model_type property of this Model.
            Allowed values for this property are: "KEY_VALUE_EXTRACTION", "DOCUMENT_CLASSIFICATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param labels:
            The value to assign to the labels property of this Model.
        :type labels: list[str]

        :param is_quick_mode:
            The value to assign to the is_quick_mode property of this Model.
        :type is_quick_mode: bool

        :param max_training_time_in_hours:
            The value to assign to the max_training_time_in_hours property of this Model.
        :type max_training_time_in_hours: float

        :param trained_time_in_hours:
            The value to assign to the trained_time_in_hours property of this Model.
        :type trained_time_in_hours: float

        :param training_dataset:
            The value to assign to the training_dataset property of this Model.
        :type training_dataset: oci.ai_document.models.Dataset

        :param testing_dataset:
            The value to assign to the testing_dataset property of this Model.
        :type testing_dataset: oci.ai_document.models.Dataset

        :param validation_dataset:
            The value to assign to the validation_dataset property of this Model.
        :type validation_dataset: oci.ai_document.models.Dataset

        :param model_version:
            The value to assign to the model_version property of this Model.
        :type model_version: str

        :param project_id:
            The value to assign to the project_id property of this Model.
        :type project_id: str

        :param time_created:
            The value to assign to the time_created property of this Model.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Model.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Model.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Model.
        :type lifecycle_details: str

        :param metrics:
            The value to assign to the metrics property of this Model.
        :type metrics: oci.ai_document.models.ModelMetrics

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Model.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Model.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Model.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'model_type': 'str',
            'labels': 'list[str]',
            'is_quick_mode': 'bool',
            'max_training_time_in_hours': 'float',
            'trained_time_in_hours': 'float',
            'training_dataset': 'Dataset',
            'testing_dataset': 'Dataset',
            'validation_dataset': 'Dataset',
            'model_version': 'str',
            'project_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'metrics': 'ModelMetrics',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'model_type': 'modelType',
            'labels': 'labels',
            'is_quick_mode': 'isQuickMode',
            'max_training_time_in_hours': 'maxTrainingTimeInHours',
            'trained_time_in_hours': 'trainedTimeInHours',
            'training_dataset': 'trainingDataset',
            'testing_dataset': 'testingDataset',
            'validation_dataset': 'validationDataset',
            'model_version': 'modelVersion',
            'project_id': 'projectId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'metrics': 'metrics',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._model_type = None
        self._labels = None
        self._is_quick_mode = None
        self._max_training_time_in_hours = None
        self._trained_time_in_hours = None
        self._training_dataset = None
        self._testing_dataset = None
        self._validation_dataset = None
        self._model_version = None
        self._project_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._metrics = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Model.
        A unique identifier that is immutable after creation.


        :return: The id of this Model.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Model.
        A unique identifier that is immutable after creation.


        :param id: The id of this Model.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Model.
        A human-friendly name for the model, which can be changed.


        :return: The display_name of this Model.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Model.
        A human-friendly name for the model, which can be changed.


        :param display_name: The display_name of this Model.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Model.
        An optional description of the model.


        :return: The description of this Model.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Model.
        An optional description of the model.


        :param description: The description of this Model.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Model.
        The compartment identifier.


        :return: The compartment_id of this Model.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Model.
        The compartment identifier.


        :param compartment_id: The compartment_id of this Model.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this Model.
        The type of the Document model.

        Allowed values for this property are: "KEY_VALUE_EXTRACTION", "DOCUMENT_CLASSIFICATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this Model.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Model.
        The type of the Document model.


        :param model_type: The model_type of this Model.
        :type: str
        """
        allowed_values = ["KEY_VALUE_EXTRACTION", "DOCUMENT_CLASSIFICATION"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def labels(self):
        """
        Gets the labels of this Model.
        The collection of labels used to train the custom model.


        :return: The labels of this Model.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this Model.
        The collection of labels used to train the custom model.


        :param labels: The labels of this Model.
        :type: list[str]
        """
        self._labels = labels

    @property
    def is_quick_mode(self):
        """
        Gets the is_quick_mode of this Model.
        Set to true when experimenting with a new model type or dataset, so model training is quick, with a predefined low number of passes through the training data.


        :return: The is_quick_mode of this Model.
        :rtype: bool
        """
        return self._is_quick_mode

    @is_quick_mode.setter
    def is_quick_mode(self, is_quick_mode):
        """
        Sets the is_quick_mode of this Model.
        Set to true when experimenting with a new model type or dataset, so model training is quick, with a predefined low number of passes through the training data.


        :param is_quick_mode: The is_quick_mode of this Model.
        :type: bool
        """
        self._is_quick_mode = is_quick_mode

    @property
    def max_training_time_in_hours(self):
        """
        Gets the max_training_time_in_hours of this Model.
        The maximum model training time in hours, expressed as a decimal fraction.


        :return: The max_training_time_in_hours of this Model.
        :rtype: float
        """
        return self._max_training_time_in_hours

    @max_training_time_in_hours.setter
    def max_training_time_in_hours(self, max_training_time_in_hours):
        """
        Sets the max_training_time_in_hours of this Model.
        The maximum model training time in hours, expressed as a decimal fraction.


        :param max_training_time_in_hours: The max_training_time_in_hours of this Model.
        :type: float
        """
        self._max_training_time_in_hours = max_training_time_in_hours

    @property
    def trained_time_in_hours(self):
        """
        Gets the trained_time_in_hours of this Model.
        The total hours actually used for model training.


        :return: The trained_time_in_hours of this Model.
        :rtype: float
        """
        return self._trained_time_in_hours

    @trained_time_in_hours.setter
    def trained_time_in_hours(self, trained_time_in_hours):
        """
        Sets the trained_time_in_hours of this Model.
        The total hours actually used for model training.


        :param trained_time_in_hours: The trained_time_in_hours of this Model.
        :type: float
        """
        self._trained_time_in_hours = trained_time_in_hours

    @property
    def training_dataset(self):
        """
        **[Required]** Gets the training_dataset of this Model.

        :return: The training_dataset of this Model.
        :rtype: oci.ai_document.models.Dataset
        """
        return self._training_dataset

    @training_dataset.setter
    def training_dataset(self, training_dataset):
        """
        Sets the training_dataset of this Model.

        :param training_dataset: The training_dataset of this Model.
        :type: oci.ai_document.models.Dataset
        """
        self._training_dataset = training_dataset

    @property
    def testing_dataset(self):
        """
        Gets the testing_dataset of this Model.

        :return: The testing_dataset of this Model.
        :rtype: oci.ai_document.models.Dataset
        """
        return self._testing_dataset

    @testing_dataset.setter
    def testing_dataset(self, testing_dataset):
        """
        Sets the testing_dataset of this Model.

        :param testing_dataset: The testing_dataset of this Model.
        :type: oci.ai_document.models.Dataset
        """
        self._testing_dataset = testing_dataset

    @property
    def validation_dataset(self):
        """
        Gets the validation_dataset of this Model.

        :return: The validation_dataset of this Model.
        :rtype: oci.ai_document.models.Dataset
        """
        return self._validation_dataset

    @validation_dataset.setter
    def validation_dataset(self, validation_dataset):
        """
        Sets the validation_dataset of this Model.

        :param validation_dataset: The validation_dataset of this Model.
        :type: oci.ai_document.models.Dataset
        """
        self._validation_dataset = validation_dataset

    @property
    def model_version(self):
        """
        **[Required]** Gets the model_version of this Model.
        The version of the model.


        :return: The model_version of this Model.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this Model.
        The version of the model.


        :param model_version: The model_version of this Model.
        :type: str
        """
        self._model_version = model_version

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this Model.
        The `OCID`__ of the project that contains the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this Model.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this Model.
        The `OCID`__ of the project that contains the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this Model.
        :type: str
        """
        self._project_id = project_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Model.
        When the model was created, as an RFC3339 datetime string.


        :return: The time_created of this Model.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Model.
        When the model was created, as an RFC3339 datetime string.


        :param time_created: The time_created of this Model.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Model.
        When the model was updated, as an RFC3339 datetime string.


        :return: The time_updated of this Model.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Model.
        When the model was updated, as an RFC3339 datetime string.


        :param time_updated: The time_updated of this Model.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Model.
        The current state of the model.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Model.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Model.
        The current state of the model.


        :param lifecycle_state: The lifecycle_state of this Model.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Model.
        A message describing the current state in more detail, that can provide actionable information if training failed.


        :return: The lifecycle_details of this Model.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Model.
        A message describing the current state in more detail, that can provide actionable information if training failed.


        :param lifecycle_details: The lifecycle_details of this Model.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def metrics(self):
        """
        Gets the metrics of this Model.

        :return: The metrics of this Model.
        :rtype: oci.ai_document.models.ModelMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this Model.

        :param metrics: The metrics of this Model.
        :type: oci.ai_document.models.ModelMetrics
        """
        self._metrics = metrics

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Model.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Model.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Model.
        A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only.
        For example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Model.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Model.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Model.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Model.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Model.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Model.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Model.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Model.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        For example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Model.
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