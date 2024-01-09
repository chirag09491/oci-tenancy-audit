# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .monitor_configuration import MonitorConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DnsTraceMonitorConfiguration(MonitorConfiguration):
    """
    Request configuration details for the DNS Trace monitor type.
    """

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "A"
    RECORD_TYPE_A = "A"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "AAAA"
    RECORD_TYPE_AAAA = "AAAA"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "ANY"
    RECORD_TYPE_ANY = "ANY"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "CNAME"
    RECORD_TYPE_CNAME = "CNAME"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "DNSKEY"
    RECORD_TYPE_DNSKEY = "DNSKEY"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "DS"
    RECORD_TYPE_DS = "DS"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "MX"
    RECORD_TYPE_MX = "MX"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "NS"
    RECORD_TYPE_NS = "NS"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "NSEC"
    RECORD_TYPE_NSEC = "NSEC"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "NULL_REC"
    RECORD_TYPE_NULL_REC = "NULL_REC"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "PTR"
    RECORD_TYPE_PTR = "PTR"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "RRSIG"
    RECORD_TYPE_RRSIG = "RRSIG"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "SOA"
    RECORD_TYPE_SOA = "SOA"

    #: A constant which can be used with the record_type property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "TXT"
    RECORD_TYPE_TXT = "TXT"

    #: A constant which can be used with the protocol property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a DnsTraceMonitorConfiguration.
    #: This constant has a value of "UDP"
    PROTOCOL_UDP = "UDP"

    def __init__(self, **kwargs):
        """
        Initializes a new DnsTraceMonitorConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_synthetics.models.DnsTraceMonitorConfiguration.config_type` attribute
        of this class is ``DNS_TRACE_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this DnsTraceMonitorConfiguration.
            Allowed values for this property are: "BROWSER_CONFIG", "SCRIPTED_BROWSER_CONFIG", "REST_CONFIG", "SCRIPTED_REST_CONFIG", "NETWORK_CONFIG", "DNS_SERVER_CONFIG", "DNS_TRACE_CONFIG", "DNSSEC_CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_type: str

        :param is_failure_retried:
            The value to assign to the is_failure_retried property of this DnsTraceMonitorConfiguration.
        :type is_failure_retried: bool

        :param dns_configuration:
            The value to assign to the dns_configuration property of this DnsTraceMonitorConfiguration.
        :type dns_configuration: oci.apm_synthetics.models.DnsConfiguration

        :param record_type:
            The value to assign to the record_type property of this DnsTraceMonitorConfiguration.
            Allowed values for this property are: "A", "AAAA", "ANY", "CNAME", "DNSKEY", "DS", "MX", "NS", "NSEC", "NULL_REC", "PTR", "RRSIG", "SOA", "TXT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type record_type: str

        :param protocol:
            The value to assign to the protocol property of this DnsTraceMonitorConfiguration.
            Allowed values for this property are: "TCP", "UDP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param verify_response_content:
            The value to assign to the verify_response_content property of this DnsTraceMonitorConfiguration.
        :type verify_response_content: str

        """
        self.swagger_types = {
            'config_type': 'str',
            'is_failure_retried': 'bool',
            'dns_configuration': 'DnsConfiguration',
            'record_type': 'str',
            'protocol': 'str',
            'verify_response_content': 'str'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'is_failure_retried': 'isFailureRetried',
            'dns_configuration': 'dnsConfiguration',
            'record_type': 'recordType',
            'protocol': 'protocol',
            'verify_response_content': 'verifyResponseContent'
        }

        self._config_type = None
        self._is_failure_retried = None
        self._dns_configuration = None
        self._record_type = None
        self._protocol = None
        self._verify_response_content = None
        self._config_type = 'DNS_TRACE_CONFIG'

    @property
    def record_type(self):
        """
        Gets the record_type of this DnsTraceMonitorConfiguration.
        DNS record type.

        Allowed values for this property are: "A", "AAAA", "ANY", "CNAME", "DNSKEY", "DS", "MX", "NS", "NSEC", "NULL_REC", "PTR", "RRSIG", "SOA", "TXT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The record_type of this DnsTraceMonitorConfiguration.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """
        Sets the record_type of this DnsTraceMonitorConfiguration.
        DNS record type.


        :param record_type: The record_type of this DnsTraceMonitorConfiguration.
        :type: str
        """
        allowed_values = ["A", "AAAA", "ANY", "CNAME", "DNSKEY", "DS", "MX", "NS", "NSEC", "NULL_REC", "PTR", "RRSIG", "SOA", "TXT"]
        if not value_allowed_none_or_none_sentinel(record_type, allowed_values):
            record_type = 'UNKNOWN_ENUM_VALUE'
        self._record_type = record_type

    @property
    def protocol(self):
        """
        Gets the protocol of this DnsTraceMonitorConfiguration.
        Type of protocol.

        Allowed values for this property are: "TCP", "UDP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this DnsTraceMonitorConfiguration.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this DnsTraceMonitorConfiguration.
        Type of protocol.


        :param protocol: The protocol of this DnsTraceMonitorConfiguration.
        :type: str
        """
        allowed_values = ["TCP", "UDP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def verify_response_content(self):
        """
        Gets the verify_response_content of this DnsTraceMonitorConfiguration.
        Verify response content against regular expression based string.
        If response content does not match the verifyResponseContent value, then it will be considered a failure.


        :return: The verify_response_content of this DnsTraceMonitorConfiguration.
        :rtype: str
        """
        return self._verify_response_content

    @verify_response_content.setter
    def verify_response_content(self, verify_response_content):
        """
        Sets the verify_response_content of this DnsTraceMonitorConfiguration.
        Verify response content against regular expression based string.
        If response content does not match the verifyResponseContent value, then it will be considered a failure.


        :param verify_response_content: The verify_response_content of this DnsTraceMonitorConfiguration.
        :type: str
        """
        self._verify_response_content = verify_response_content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
