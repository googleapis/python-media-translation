# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.rpc import status_pb2 as status  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.mediatranslation.v1alpha1",
    manifest={
        "TranslateSpeechConfig",
        "StreamingTranslateSpeechConfig",
        "StreamingTranslateSpeechRequest",
        "StreamingTranslateSpeechResult",
        "StreamingTranslateSpeechResponse",
    },
)


class TranslateSpeechConfig(proto.Message):
    r"""Provides information to the speech translation that specifies
    how to process the request.

    Attributes:
        audio_encoding (str):
            Required. Encoding of audio data. Supported formats:

            -  ``linear16``

               Uncompressed 16-bit signed little-endian samples (Linear
               PCM).

            -  ``flac``

               ``flac`` (Free Lossless Audio Codec) is the recommended
               encoding because it is lossless--therefore recognition is
               not compromised--and requires only about half the
               bandwidth of ``linear16``.

            -  ``mulaw``

               8-bit samples that compand 14-bit audio samples using
               G.711 PCMU/mu-law.

            -  ``amr``

               Adaptive Multi-Rate Narrowband codec.
               ``sample_rate_hertz`` must be 8000.

            -  ``amr-wb``

               Adaptive Multi-Rate Wideband codec. ``sample_rate_hertz``
               must be 16000.

            -  ``ogg-opus``

               Opus encoded audio frames in Ogg container
               (`OggOpus <https://wiki.xiph.org/OggOpus>`__).
               ``sample_rate_hertz`` must be one of 8000, 12000, 16000,
               24000, or 48000.

            -  ``mp3``

               MP3 audio. Support all standard MP3 bitrates (which range
               from 32-320 kbps). When using this encoding,
               ``sample_rate_hertz`` has to match the sample rate of the
               file being used.
        source_language_code (str):
            Required. Source language code (BCP-47) of
            the input audio.
        target_language_code (str):
            Required. Target language code (BCP-47) of
            the output.
        alternative_source_language_codes (Sequence[str]):
            Optional. A list of up to 3 additional language codes
            (BCP-47), listing possible alternative languages of the
            supplied audio. If alternative source languages are listed,
            speech translation result will translate in the most likely
            language detected including the main source_language_code.
            The translated result will include the language code of the
            language detected in the audio. Note: (1) If the provided
            alternative_source_language_code is not supported by current
            API version, we will skip that language code. (2) If user
            only provided one eligible
            alternative_source_language_codes, the translation will
            happen between source_language_code and
            alternative_source_language_codes. The target_language_code
            will be ignored. It will be useful in conversation mode.
        sample_rate_hertz (int):
            Optional. Sample rate in Hertz of the audio
            data. Valid values are: 8000-48000. 16000 is
            optimal. For best results, set the sampling rate
            of the audio source to 16000 Hz. If that's not
            possible, use the native sample rate of the
            audio source (instead of re-sampling).
        model (str):
            Optional.
    """

    audio_encoding = proto.Field(proto.STRING, number=1)
    source_language_code = proto.Field(proto.STRING, number=2)
    target_language_code = proto.Field(proto.STRING, number=3)
    alternative_source_language_codes = proto.RepeatedField(proto.STRING, number=6)
    sample_rate_hertz = proto.Field(proto.INT32, number=4)
    model = proto.Field(proto.STRING, number=5)


class StreamingTranslateSpeechConfig(proto.Message):
    r"""Config used for streaming translation.

    Attributes:
        audio_config (~.media_translation.TranslateSpeechConfig):
            Required. The common config for all the
            following audio contents.
        single_utterance (bool):
            Optional. If ``false`` or omitted, the system performs
            continuous translation (continuing to wait for and process
            audio even if the user pauses speaking) until the client
            closes the input stream (gRPC API) or until the maximum time
            limit has been reached. May return multiple
            ``StreamingTranslateSpeechResult``\ s with the ``is_final``
            flag set to ``true``.

            If ``true``, the speech translator will detect a single
            spoken utterance. When it detects that the user has paused
            or stopped speaking, it will return an
            ``END_OF_SINGLE_UTTERANCE`` event and cease translation.
            When the client receives 'END_OF_SINGLE_UTTERANCE' event,
            the client should stop sending the requests. However,
            clients should keep receiving remaining responses until the
            stream is terminated. To construct the complete sentence in
            a streaming way, one should override (if 'is_final' of
            previous response is false), or append (if 'is_final' of
            previous response is true).
        stability (str):
            Optional. Stability control for the media translation text.
            The value should be "LOW", "MEDIUM", "HIGH". It applies to
            text/text_and_audio translation only. For audio translation
            mode, we only support HIGH stability mode, low/medium
            stability mode will throw argument error. Default empty
            string will be treated as "HIGH" in audio translation mode;
            will be treated as "LOW" in other translation mode. Note
            that stability and speed would be trade off. (1) "LOW": In
            low mode, translation service will start to do translation
            right after getting recognition response. The speed will be
            faster. (2) "MEDIUM": In medium mode, translation service
            will check if the recognition response is stable enough or
            not, and only translate recognition response which is not
            likely to be changed later. (3) "HIGH": In high mode,
            translation service will wait for more stable recognition
            responses, and then start to do translation. Also, the
            following recognition responses cannot modify previous
            recognition responses. Thus it may impact quality in some
            situation. "HIGH" stability will generate "final" responses
            more frequently.
        translation_mode (str):
            Optional. Translation mode, the value should be "text",
            "audio", "text_and_audio". Default empty string will be
            treated as "text". (1)"text": The response will be text
            translation. Text translation has a field "is_final".
            Detailed definition can be found in
            ``TextTranslationResult``. (2) "audio": The response will be
            audio translation. Audio translation does not have
            "is_final" field, which means each audio translation
            response is stable and will not be changed by later
            response. Translation mode "audio" can only be used with
            "high" stability mode, (3) "text_and_audio": The response
            will have a text translation, when "is_final" is true, we
            will also output its corresponding audio translation. When
            "is_final" is false, audio_translation field will be empty.
        disable_interim_results (bool):
            Optional. If disable_interim_results is true, we will only
            return "final" responses. Otherwise, we will return all the
            responses. Default value will be false. User can only set
            disable_interim_results to be true with "high" stability
            mode.
    """

    audio_config = proto.Field(proto.MESSAGE, number=1, message=TranslateSpeechConfig,)
    single_utterance = proto.Field(proto.BOOL, number=2)
    stability = proto.Field(proto.STRING, number=3)
    translation_mode = proto.Field(proto.STRING, number=4)
    disable_interim_results = proto.Field(proto.BOOL, number=5)


class StreamingTranslateSpeechRequest(proto.Message):
    r"""The top-level message sent by the client for the
    ``StreamingTranslateSpeech`` method. Multiple
    ``StreamingTranslateSpeechRequest`` messages are sent. The first
    message must contain a ``streaming_config`` message and must not
    contain ``audio_content`` data. All subsequent messages must contain
    ``audio_content`` data and must not contain a ``streaming_config``
    message.

    Attributes:
        streaming_config (~.media_translation.StreamingTranslateSpeechConfig):
            Provides information to the recognizer that specifies how to
            process the request. The first
            ``StreamingTranslateSpeechRequest`` message must contain a
            ``streaming_config`` message.
        audio_content (bytes):
            The audio data to be translated. Sequential chunks of audio
            data are sent in sequential
            ``StreamingTranslateSpeechRequest`` messages. The first
            ``StreamingTranslateSpeechRequest`` message must not contain
            ``audio_content`` data and all subsequent
            ``StreamingTranslateSpeechRequest`` messages must contain
            ``audio_content`` data. The audio bytes must be encoded as
            specified in ``StreamingTranslateSpeechConfig``. Note: as
            with all bytes fields, protobuffers use a pure binary
            representation (not base64).
    """

    streaming_config = proto.Field(
        proto.MESSAGE, number=1, message=StreamingTranslateSpeechConfig,
    )
    audio_content = proto.Field(proto.BYTES, number=2)


class StreamingTranslateSpeechResult(proto.Message):
    r"""A streaming speech translation result corresponding to a
    portion of the audio that is currently being processed.

    Attributes:
        text_translation_result (~.media_translation.StreamingTranslateSpeechResult.TextTranslationResult):
            Text translation result.
        audio_translation_result (~.media_translation.StreamingTranslateSpeechResult.AudioTranslationResult):
            Audio translation result.
        recognition_result (str):
            Output only. The debug only recognition
            result in original language. This field is debug
            only and will be set to empty string if not
            available. This is implementation detail and
            will not be backward compatible.
            Still need to decide whether to expose this
            field by default.
        detected_source_language_code (str):
            Output only.
    """

    class TextTranslationResult(proto.Message):
        r"""Text translation result.

        Attributes:
            translation (str):
                Output only. The translated sentence.
            is_final (bool):
                Output only. If ``false``, this
                ``StreamingTranslateSpeechResult`` represents an interim
                result that may change. If ``true``, this is the final time
                the translation service will return this particular
                ``StreamingTranslateSpeechResult``, the streaming translator
                will not return any further hypotheses for this portion of
                the transcript and corresponding audio.
        """

        translation = proto.Field(proto.STRING, number=1)
        is_final = proto.Field(proto.BOOL, number=2)

    class AudioTranslationResult(proto.Message):
        r"""Audio translation result.

        Attributes:
            audio_translation (bytes):
                Output only. The translated audio.
        """

        audio_translation = proto.Field(proto.BYTES, number=1)

    text_translation_result = proto.Field(
        proto.MESSAGE, number=1, message=TextTranslationResult,
    )
    audio_translation_result = proto.Field(
        proto.MESSAGE, number=2, message=AudioTranslationResult,
    )
    recognition_result = proto.Field(proto.STRING, number=3)
    detected_source_language_code = proto.Field(proto.STRING, number=4)


class StreamingTranslateSpeechResponse(proto.Message):
    r"""A streaming speech translation response corresponding to a
    portion of the audio currently processed.

    Attributes:
        error (~.status.Status):
            Output only. If set, returns a
            [google.rpc.Status][google.rpc.Status] message that
            specifies the error for the operation.
        result (~.media_translation.StreamingTranslateSpeechResult):
            Output only. The translation result that is currently being
            processed (For text translation, is_final could be true or
            false. For audio translation, we do not have is_final field,
            which means each audio response is stable and will not get
            changed later. For text_and_audio, we still have "is_final"
            field in text translation, but we only output corresponsding
            audio when "is_final" is true.).
        speech_event_type (~.media_translation.StreamingTranslateSpeechResponse.SpeechEventType):
            Output only. Indicates the type of speech
            event.
    """

    class SpeechEventType(proto.Enum):
        r"""Indicates the type of speech event."""
        SPEECH_EVENT_TYPE_UNSPECIFIED = 0
        END_OF_SINGLE_UTTERANCE = 1

    error = proto.Field(proto.MESSAGE, number=1, message=status.Status,)
    result = proto.Field(
        proto.MESSAGE, number=2, message=StreamingTranslateSpeechResult,
    )
    speech_event_type = proto.Field(proto.ENUM, number=3, enum=SpeechEventType,)


__all__ = tuple(sorted(__protobuf__.manifest))
