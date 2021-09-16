from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version", "r") as fh:
    version = fh.read()

setup(
    name='apache-airflow-provider-aliyun-rocketmq',
    version=version,
    description='Airflow x Aliyun RocketMQ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        "apache_airflow_provider": [
            "provider_info=aliyun_rocketmq.__init__:get_provider_info"
        ]
    },
    license='Apache License 2.0',
    packages=['aliyun_rocketmq', 'aliyun_rocketmq.hooks'],
    install_requires=['apache-airflow>=2.0', 'mq-http-sdk>=1.0.3'],
    setup_requires=['setuptools', 'wheel'],
    author='Ed__xu__Ed',
    author_email='m.tofu@qq.com',
    url='https://github.com/Ed-XCF/apache-airflow-provider-aliyun-rocketmq',
    python_requires='~=3.7',
)
