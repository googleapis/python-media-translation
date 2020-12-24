# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class StreamingTranslateSpeechResponse(object):
    class SpeechEventType(enum.IntEnum):
        """
        Indicates the type of speech event.

        Attributes:
          SPEECH_EVENT_TYPE_UNSPECIFIED (int): No speech event specified.
          END_OF_SINGLE_UTTERANCE (int): This event indicates that the server has detected the end of the
          user's speech utterance and expects no additional speech. Therefore, the
          server will not process additional audio (although it may subsequently
          return additional results). When the client receives
          'END_OF_SINGLE_UTTERANCE' event, the client should stop sending the
          requests. However, clients should keep receiving remaining responses
          until the stream is terminated. To construct the complete sentence in a
          streaming way, one should override (if 'is_final' of previous response
          is false), or append (if 'is_final' of previous response is true). This
          event is only sent if ``single_utterance`` was set to ``true``, and is
          not used otherwise.
        """

        SPEECH_EVENT_TYPE_UNSPECIFIED = 0
        END_OF_SINGLE_UTTERANCE = 1
