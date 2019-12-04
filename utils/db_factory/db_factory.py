from utils.db_factory.mysql_db import MysqlDB
from utils.db_factory.mongo_db import MongoDB
from utils.db_factory.redis_db import RedisDB

# from zhuge.databases.pikadb.pikadb import PikaDB
# from zhuge.databases.redisdb.redisdb import RedisDB
# from zhuge.databases.mongodb.mongodb import MongoDB
# from zhuge.databases.rabbitmqdb.rabbitmq import Rabbitmq
# from zhuge.databases.esdb.esdb import EsDB
# from zhuge.databases.kafkadb.kafkadb import KafkaDB

class dbfactory():

    @staticmethod
    def create_db(**kwargs):
        db_type = kwargs.get("db_type")
        return getattr(dbfactory, db_type)(**kwargs)

    @staticmethod
    def db_mysql(*args, **kwargs):
        return MysqlDB(**kwargs)

    # @staticmethod
    # def db_tidb(*args, **kwargs):
    #     return TiDB(**kwargs)
    #
    @staticmethod
    def db_mongo(*args, **kwargs):
        return MongoDB(**kwargs)
    #
    # @staticmethod
    # def db_es(*args, **kwargs):
    #     return EsDB(**kwargs)
    #
    @staticmethod
    def db_redis(*args, **kwargs):
        return RedisDB.getRedisConn(**kwargs)
    #
    # @staticmethod
    # def db_pika(*args, **kwargs):
    #     return PikaDB.getPikaConn(**kwargs)
    #
    # @staticmethod
    # def db_rabbitmq(*args, **kwargs):
    #     return Rabbitmq(**kwargs)
    #
    # @staticmethod
    # def db_kafka(*args, **kwargs):
    #     return KafkaDB(**kwargs)