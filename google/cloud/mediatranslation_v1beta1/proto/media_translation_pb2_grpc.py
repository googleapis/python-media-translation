# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.mediatranslation_v1beta1.proto import (
    media_translation_pb2 as google_dot_cloud_dot_mediatranslation__v1beta1_dot_proto_dot_media__translation__pb2,
)


class SpeechTranslationServiceStub(object):
    """Provides translation from/to media types.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamingTranslateSpeech = channel.stream_stream(
            "/google.cloud.mediatranslation.v1beta1.SpeechTranslationService/StreamingTranslateSpeech",
            request_serializer=google_dot_cloud_dot_mediatranslation__v1beta1_dot_proto_dot_media__translation__pb2.StreamingTranslateSpeechRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_mediatranslation__v1beta1_dot_proto_dot_media__translation__pb2.StreamingTranslateSpeechResponse.FromString,
        )


class SpeechTranslationServiceServicer(object):
    """Provides translation from/to media types.
    """

    def StreamingTranslateSpeech(self, request_iterator, context):
        """Performs bidirectional streaming speech translation: receive results while
        sending audio. This method is only available via the gRPC API (not REST).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SpeechTranslationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "StreamingTranslateSpeech": grpc.stream_stream_rpc_method_handler(
            servicer.StreamingTranslateSpeech,
            request_deserializer=google_dot_cloud_dot_mediatranslation__v1beta1_dot_proto_dot_media__translation__pb2.StreamingTranslateSpeechRequest.FromString,
            response_serializer=google_dot_cloud_dot_mediatranslation__v1beta1_dot_proto_dot_media__translation__pb2.StreamingTranslateSpeechResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.mediatranslation.v1beta1.SpeechTranslationService",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SpeechTranslationService(object):
    """Provides translation from/to media types.
    """

    @staticmethod
    def StreamingTranslateSpeech(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            "/google.cloud.mediatranslation.v1beta1.SpeechTranslationService/StreamingTranslateSpeech",
            google_dot_cloud_dot_mediatranslation__v1beta1_dot_proto_dot_media__translation__pb2.StreamingTranslateSpeechRequest.SerializeToString,
            google_dot_cloud_dot_mediatranslation__v1beta1_dot_proto_dot_media__translation__pb2.StreamingTranslateSpeechResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )