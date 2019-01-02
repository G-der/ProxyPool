# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 3
MIN_SCORE = 1
INITIAL_SCORE = 3

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 500

# 检查周期(秒)
TESTER_CYCLE = 20

# 获取周期(秒)
GETTER_CYCLE = 520

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://www.baidu.com'

# API配置
API_HOST = '127.0.0.1'
API_PORT = 5555

# 开关
#测试
TESTER_ENABLED = False
#获取
GETTER_ENABLED = False
#API
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10
