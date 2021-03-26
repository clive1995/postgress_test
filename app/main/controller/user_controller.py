from flask_restplus import Resource, reqparse
from flask import request,jsonify
from app.main.util.user_dto import CustomerDto
from datetime import datetime
from app.main.model.customer_model import Customer,CustomerSchema,EducationSchema,ExperienceSchema
from app.main.model.education_model import Education
from app.main import db

parser = reqparse.RequestParser()
parser.add_argument('customer_id',type=int,required=True,default=None)

educationparser = reqparse.RequestParser()
educationparser.add_argument('customer_id',type=int,required=True,default=None)
educationparser.add_argument('education_id',type=int,required=True,default=None)

api = CustomerDto.api


@api.route('/register')
class CustomerRegister(Resource):
    @api.expect(parser,validate=True)
    def get(self):
        data = parser.parse_args()
        customer = db.session.query(Customer).filter_by(id=data['customer_id']).first()
        print(customer)
        schema = CustomerSchema()
        # for item in customer:
        print(schema.dump([customer],many=True))
        return schema.dump([customer],many=True)

    @api.expect(CustomerDto.customerRegister)
    def post(self):
        data = request.json
        try:
            customer = Customer(
                username=data['firstname'].strip()+' '+data['lastname'].strip(),
                password=data['password'].strip(),
                email= data['email'].strip(),
                hash='###'
            )
            db.session.add(customer)
            db.session.commit()
        except Exception as e:
            print(e)
        return data

@api.route('/education')
class Educationres(Resource):
    @api.expect(CustomerDto.education)
    def post(self):
        data = request.json
        try:
            education = Education(
                customer_id =int(data['customer_id']),
                fromdate = datetime.strptime(data['fromdate'],'%Y-%d-%m'),
                todate =datetime.strptime(data['todate'],'%Y-%d-%m'),
                school = data['school'],
                description = data['description'],
                fieldofstudy = data['fieldofstudy'],
            )
            print(datetime.strptime(data['fromdate'],'%Y-%d-%m'))
            db.session.add(education)
            db.session.commit()
        except Exception as e:
            print(e)
        return data

    @api.expect(educationparser, validate=True)
    def get(self):
        data = educationparser.parse_args()
        education = Education.query.filter_by(customer_id=data['customer_id'],id=data['education_id']).all()
        schema = EducationSchema()
        return schema.dump(education,many=True)

    @api.expect(CustomerDto.educationupdate)
    def put(self):
        data = request.json
        education = Education.query.filter_by(id=data['id']).first()
        education.school = data['school']
        education.fieldofstudy = data['fieldofstudy']
        education.description = data['description']
        education.fromdate = data['fromdate']
        education.todate = data['todate']
        db.session.commit()
        return data

    @api.expect(CustomerDto.educationDelete)
    def delete(self):
        data = request.json
        print(data['experience_id'])
        try:
            Education.query.filter_by(id=data['experience_id']).delete()
            db.session.commit()
            return 'yessss'
        except Exception as e:
            print(e)





