# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180608

from .secret_content_details import SecretContentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Base64SecretContentDetails(SecretContentDetails):
    """
    Base64-encoded secret content.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Base64SecretContentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.vault.models.Base64SecretContentDetails.content_type` attribute
        of this class is ``BASE64`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content_type:
            The value to assign to the content_type property of this Base64SecretContentDetails.
            Allowed values for this property are: "BASE64"
        :type content_type: str

        :param name:
            The value to assign to the name property of this Base64SecretContentDetails.
        :type name: str

        :param stage:
            The value to assign to the stage property of this Base64SecretContentDetails.
            Allowed values for this property are: "CURRENT", "PENDING"
        :type stage: str

        :param content:
            The value to assign to the content property of this Base64SecretContentDetails.
        :type content: str

        """
        self.swagger_types = {
            'content_type': 'str',
            'name': 'str',
            'stage': 'str',
            'content': 'str'
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'name': 'name',
            'stage': 'stage',
            'content': 'content'
        }

        self._content_type = None
        self._name = None
        self._stage = None
        self._content = None
        self._content_type = 'BASE64'

    @property
    def content(self):
        """
        Gets the content of this Base64SecretContentDetails.
        The base64-encoded content of the secret.


        :return: The content of this Base64SecretContentDetails.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this Base64SecretContentDetails.
        The base64-encoded content of the secret.


        :param content: The content of this Base64SecretContentDetails.
        :type: str
        """
        self._content = content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
