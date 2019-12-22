from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:7365728@127.0.0.1:3306/python1904'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 花生网
class Fangtx(db.Model):
    __tablename__ = 'Fangtx'
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(20), nullable=False)  # 区
    house = db.Column(db.String(20), nullable=False)  # 房子位置
    monthly = db.Column(db.Integer, nullable=False)  # 月租 int
    house_info = db.Column(db.String(80), nullable=False)  # 房子信息
    agent = db.Column(db.String(20), nullable=False)  # 房产经纪人
    imgs = db.Column(db.String(80), nullable=False)  # 房间图片
    traffic = db.Column(db.String(80), nullable=False)  # 交通
    chum = db.Column(db.String(20), nullable=True)  # 室友
    cfg = db.Column(db.String(80), nullable=False)  # 房间配置

    def __init__(self, district, house, monthly, house_info, agent, imgs, traffic, chum,cfg):
        self.district = district
        self.house = house
        self.monthly = monthly
        self.house_info = house_info
        self.agent = agent
        self.imgs = imgs
        self.traffic = traffic
        self.chum = chum
        self.cfg = cfg


# 创建表(全部)
# db.create_all()


# db.drop_all()

# 添加数据
def add_house(district, house, monthly, house_info, agent, imgs, traffic, chum,cfg):
    res = Fangtx(district, house, monthly, house_info, agent, imgs, traffic, chum,cfg)
    # print(res)
    db.session.add(res)
    db.session.commit()
    return True


# print(add_house('朝阳', '双桥某小区3居室主卧', 1900, '呼呼呼', '程雷18519314699', '急急急', '距八通线双桥地铁站A口1618米', '小区物业费1元/平米/月'))
# print(add_house('海淀', '中关村某小区3居室主卧', 1800, '呼呼呼', '程雷18519314699', '急急急', '距八通线双桥地铁站A口1618米', '小区物业费1元/平米/月'))
# print(add_house('海淀', '中关村某小区3居室主卧', 1800, '呼呼呼', '程雷18519314699', '急急急', "['距八通线双桥地铁站A口1618米','ghfdaskghjkfdh']", '小区物业费1元/平米/月'))


# 显示全部
def query_all():
    res = Fangtx.query.all
    return tuple(res())


# print(query_all())


# 根据 月租 查询
def query_by_web(monthly):
    res = Fangtx.query.filter_by(monthly=monthly).all()
    if res != []:
        return tuple(res)


# 根据 区 查询
def query_by_district(district):
    res = Fangtx.query.filter_by(district=district).all()
    # print(res)
    # print(type(res))
    if res != []:
        return tuple(res)


# print(query_by_district('朝阳'))
# print(query_by_district('朝'))


# 模糊查询 小区名
def query_by_likehouse(house):
    res = Fangtx.query.filter(Fangtx.house.like("%" + house + "%") if house is not None else "").all()
    # print(res)
    # for i in res:
    #     print(i.house)
    return tuple(res)


# query_by_likehouse('双桥')
# query_by_likehouse('中关村')

# 模糊查询 地铁名
def query_by_liketraffic(traffic):
    res = Fangtx.query.filter(Fangtx.traffic.like("%" + traffic + "%") if traffic is not None else "").all()
    # print(res)
    if res != []:
        return tuple(res)


# print(query_by_liketraffic('aaa地铁站'))


# 模糊查询 all
def query_likeall(input):
    res = Fangtx.query.filter(or_(
        Fangtx.district.like("%" + input + "%") if input is not None else "",
        Fangtx.house.like("%" + input + "%") if input is not None else "",
        Fangtx.monthly.like("%" + input + "%") if input is not None else "",
        Fangtx.house_info.like("%" + input + "%") if input is not None else "",
        Fangtx.traffic.like("%" + input + "%") if input is not None else "")).all()
    print(res)
    if res != []:
        return tuple(res)

# print(query_likeall('双桥地铁站'))
