# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNewsReportDetails(object):
    """
    The information about the news report to be updated.
    """

    #: A constant which can be used with the status property of a UpdateNewsReportDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a UpdateNewsReportDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a UpdateNewsReportDetails.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    #: A constant which can be used with the news_frequency property of a UpdateNewsReportDetails.
    #: This constant has a value of "WEEKLY"
    NEWS_FREQUENCY_WEEKLY = "WEEKLY"

    #: A constant which can be used with the locale property of a UpdateNewsReportDetails.
    #: This constant has a value of "EN"
    LOCALE_EN = "EN"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNewsReportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this UpdateNewsReportDetails.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"
        :type status: str

        :param news_frequency:
            The value to assign to the news_frequency property of this UpdateNewsReportDetails.
            Allowed values for this property are: "WEEKLY"
        :type news_frequency: str

        :param locale:
            The value to assign to the locale property of this UpdateNewsReportDetails.
            Allowed values for this property are: "EN"
        :type locale: str

        :param content_types:
            The value to assign to the content_types property of this UpdateNewsReportDetails.
        :type content_types: oci.opsi.models.NewsContentTypes

        :param ons_topic_id:
            The value to assign to the ons_topic_id property of this UpdateNewsReportDetails.
        :type ons_topic_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateNewsReportDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateNewsReportDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'status': 'str',
            'news_frequency': 'str',
            'locale': 'str',
            'content_types': 'NewsContentTypes',
            'ons_topic_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'status': 'status',
            'news_frequency': 'newsFrequency',
            'locale': 'locale',
            'content_types': 'contentTypes',
            'ons_topic_id': 'onsTopicId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._status = None
        self._news_frequency = None
        self._locale = None
        self._content_types = None
        self._ons_topic_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def status(self):
        """
        Gets the status of this UpdateNewsReportDetails.
        Defines if the news report will be enabled or disabled.

        Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED"


        :return: The status of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateNewsReportDetails.
        Defines if the news report will be enabled or disabled.


        :param status: The status of this UpdateNewsReportDetails.
        :type: str
        """
        allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                f"Invalid value for `status`, must be None or one of {allowed_values}"
            )
        self._status = status

    @property
    def news_frequency(self):
        """
        Gets the news_frequency of this UpdateNewsReportDetails.
        News report frequency.

        Allowed values for this property are: "WEEKLY"


        :return: The news_frequency of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._news_frequency

    @news_frequency.setter
    def news_frequency(self, news_frequency):
        """
        Sets the news_frequency of this UpdateNewsReportDetails.
        News report frequency.


        :param news_frequency: The news_frequency of this UpdateNewsReportDetails.
        :type: str
        """
        allowed_values = ["WEEKLY"]
        if not value_allowed_none_or_none_sentinel(news_frequency, allowed_values):
            raise ValueError(
                f"Invalid value for `news_frequency`, must be None or one of {allowed_values}"
            )
        self._news_frequency = news_frequency

    @property
    def locale(self):
        """
        Gets the locale of this UpdateNewsReportDetails.
        Language of the news report.

        Allowed values for this property are: "EN"


        :return: The locale of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this UpdateNewsReportDetails.
        Language of the news report.


        :param locale: The locale of this UpdateNewsReportDetails.
        :type: str
        """
        allowed_values = ["EN"]
        if not value_allowed_none_or_none_sentinel(locale, allowed_values):
            raise ValueError(
                f"Invalid value for `locale`, must be None or one of {allowed_values}"
            )
        self._locale = locale

    @property
    def content_types(self):
        """
        Gets the content_types of this UpdateNewsReportDetails.

        :return: The content_types of this UpdateNewsReportDetails.
        :rtype: oci.opsi.models.NewsContentTypes
        """
        return self._content_types

    @content_types.setter
    def content_types(self, content_types):
        """
        Sets the content_types of this UpdateNewsReportDetails.

        :param content_types: The content_types of this UpdateNewsReportDetails.
        :type: oci.opsi.models.NewsContentTypes
        """
        self._content_types = content_types

    @property
    def ons_topic_id(self):
        """
        Gets the ons_topic_id of this UpdateNewsReportDetails.
        The `OCID`__ of the ONS topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The ons_topic_id of this UpdateNewsReportDetails.
        :rtype: str
        """
        return self._ons_topic_id

    @ons_topic_id.setter
    def ons_topic_id(self, ons_topic_id):
        """
        Sets the ons_topic_id of this UpdateNewsReportDetails.
        The `OCID`__ of the ONS topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param ons_topic_id: The ons_topic_id of this UpdateNewsReportDetails.
        :type: str
        """
        self._ons_topic_id = ons_topic_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateNewsReportDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateNewsReportDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateNewsReportDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateNewsReportDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateNewsReportDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateNewsReportDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateNewsReportDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateNewsReportDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
