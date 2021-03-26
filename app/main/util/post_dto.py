from flask_restplus import Namespace,fields


class Posts_dto:
    api = Namespace('Posts',description='post apis')

    addposts = api.model('addposts',{
        'customer_id':fields.Integer,
        'post':fields.String
    })

    addComments = api.model('addComments',{
        'post_id':fields.Integer,
        'customer_id':fields.Integer,
        'comment':fields.String
    })