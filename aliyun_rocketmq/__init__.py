def get_provider_info():
    return {
        "package-name": "apache-airflow-provider-aliyun-rocketmq",
        "name": "Aliyun RocketMQ Airflow Provider",
        "description": "Airflow provider for aliyun rocketmq",
        "hook-class-names": ["aliyun_rocketmq_provider.hooks.aliyun_rocketmq_hook.RocketMQHook"],
        "versions": ["0.0.1"]
    }
