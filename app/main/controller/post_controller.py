from flask_restplus import reqparse,Resource
from app.main import db
from flask import request
from ..model.education_model import Posts, Likes, Comments
from ..model.customer_model import PostSchema
from ..util.post_dto import Posts_dto

api = Posts_dto.api

_postDto = Posts_dto

parser = reqparse.RequestParser()
parser.add_argument('customer_id',type=str,required=True)
parser.add_argument('post_id',type=str,required=True)

@api.route('/post')
class Postser(Resource):
    @api.expect(_postDto.addposts)
    def post(self):
        data = request.json
        posts =  Posts(
            customer_id= data['customer_id'],
            post= data['post']
        )
        db.session.add(posts)
        db.session.commit()

    @api.expect(parser)
    def get(self):
        data = parser.parse_args()
        posts = db.session.query(Posts).join(Likes).join(Comments).filter_by(id=data['post_id']).all()
        print(posts)
        schema = PostSchema()
        print(schema.dump(posts,many=True))


@api.route('/like')
class Liker(Resource):
    @api.expect(parser)
    def post(self):
        data = parser.parse_args()
        likes = Likes(
            posts_id = data['post_id'],
            customer_id = data['customer_id']
        )

        db.session.add(likes)
        db.session.commit()

@api.route('/comments')
class Commenter(Resource):
    @api.expect(_postDto.addComments)
    def post(self):
        data = request.json
        comments = Comments(
            posts_id=data['post_id'],
            customer_id = data['customer_id'],
            comment=data['comment'],
        )

        db.session.add(comments)
        db.session.commit()