# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NullValueFormatEntry(FormatEntry):
    """
    The Null Value masking format replaces column data with NULL. The column
    being masked must be allowed to contain null values. To learn more,
    check Null Value in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NullValueFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.NullValueFormatEntry.type` attribute
        of this class is ``NULL_VALUE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this NullValueFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this NullValueFormatEntry.
        :type description: str

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description'
        }

        self._type = None
        self._description = None
        self._type = 'NULL_VALUE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other