from unittest import mock

from mq_http_sdk.mq_client import MQClient
from sqlalchemy.orm import Query
from airflow.models.connection import Connection

from aliyun_rocketmq_provider.hooks.aliyun_rocketmq import AliyunRocketMQHook


class TestAliyunRocketMQHook:
    def setup_class(self):
        Query.first = mock.Mock(
            return_value=Connection(
                host="http://127.0.0.1",
                login="test",
                password="test",
                schema="test",
            )
        )

    def test_publish(self):
        hook = AliyunRocketMQHook(topic="test_topic")
        with mock.patch.object(MQClient, "publish_message"):
            response = hook.run("")
            assert response.message_id == ""
