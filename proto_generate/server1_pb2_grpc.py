# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto_generate.server1_pb2 as server1__pb2


class Server1Stub(object):
    """服务端接口类
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.fun1 = channel.unary_unary(
                '/proto.Server1/fun1',
                request_serializer=server1__pb2.Fun1Request.SerializeToString,
                response_deserializer=server1__pb2.Fun1Reply.FromString,
                )


class Server1Servicer(object):
    """服务端接口类
    """

    def fun1(self, request, context):
        """服务端接口方法
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Server1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'fun1': grpc.unary_unary_rpc_method_handler(
                    servicer.fun1,
                    request_deserializer=server1__pb2.Fun1Request.FromString,
                    response_serializer=server1__pb2.Fun1Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.Server1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server1(object):
    """服务端接口类
    """

    @staticmethod
    def fun1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Server1/fun1',
            server1__pb2.Fun1Request.SerializeToString,
            server1__pb2.Fun1Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)