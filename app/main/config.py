class LocalSetup:
    SQLALCHEMY_DATABASE_URI= 'postgresql://postgres:cyclops@localhost/dev_connector'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config_by_name = dict(
    LOCAL=LocalSetup
)