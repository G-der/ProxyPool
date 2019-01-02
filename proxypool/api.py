from flask import Flask, g

from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()

@app.route('/all')
def get_all_proxy():
    """
    Get a proxy
    :return: 所有代理
    """
    conn = get_conn()
    list = conn.all()
    print(list)
    result=""
    for item in list:
        result +=  item +"<br>"
    
    return result

@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())

@app.route('/delete/<string:proxy_ip>', methods=['GET'])
def delete(proxy_ip):
    if len(proxy_ip) == 0:
        abort(404)
    
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    if conn.exists(proxy_ip):
        conn.delete(proxy_ip)
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    app.run()
