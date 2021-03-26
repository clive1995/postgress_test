from flask_restplus import Namespace, fields


class CustomerDto:

    api = Namespace('customer',description='customer operations')

    customerRegister = api.model('customerRegister',{
        'firstname':fields.String,
        'lastname':fields.String,
        'email':fields.String,
        'password':fields.String,
        'çonfirmpassword':fields.String
    })

    education = api.model('education',{
        'customer_id':fields.Integer,
        'fromdate':fields.Date,
        'todate':fields.Date,
        'school':fields.String,
        'description':fields.String,
        'fieldofstudy':fields.String,
    })
    educationupdate = api.model('educationupdate', {
        'id':fields.Integer,
        'customer_id': fields.Integer,
        'fromdate': fields.Date,
        'todate': fields.Date,
        'school': fields.String,
        'description': fields.String,
        'fieldofstudy': fields.String,
    })

    educationDelete = api.model('educationDelete',{
        'experience_id':fields.Integer,
        'customer_id':fields.Integer
    })