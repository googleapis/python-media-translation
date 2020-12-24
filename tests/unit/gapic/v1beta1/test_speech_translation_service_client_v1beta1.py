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

"""Unit tests."""

import mock
import pytest

from google.cloud import mediatranslation_v1beta1
from google.cloud.mediatranslation_v1beta1.proto import media_translation_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def stream_stream(
        self, method, request_serializer=None, response_deserializer=None
    ):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestSpeechTranslationServiceClient(object):
    def test_streaming_translate_speech(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = media_translation_pb2.StreamingTranslateSpeechResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[iter([expected_response])])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = mediatranslation_v1beta1.SpeechTranslationServiceClient()

        # Setup Request
        request = {}
        request = media_translation_pb2.StreamingTranslateSpeechRequest(**request)
        requests = [request]

        response = client.streaming_translate_speech(requests)
        resources = list(response)
        assert len(resources) == 1
        assert expected_response == resources[0]

        assert len(channel.requests) == 1
        actual_requests = channel.requests[0][1]
        assert len(actual_requests) == 1
        actual_request = list(actual_requests)[0]
        assert request == actual_request

    def test_streaming_translate_speech_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = mediatranslation_v1beta1.SpeechTranslationServiceClient()

        # Setup request
        request = {}

        request = media_translation_pb2.StreamingTranslateSpeechRequest(**request)
        requests = [request]

        with pytest.raises(CustomException):
            client.streaming_translate_speech(requests)
