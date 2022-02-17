from flaskpitch import create_app,db
from flaskpitch.models import User,Role,Post
from flask_migrate import Migrate

app=create_app('production')
migrate=Migrate()
migrate = Migrate(app,db)

@app.cli.command()
def test():
  """
  Run unit tests
  """
  import unittest
  tests=unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def make_shell_context():
  return dict(app=app,db=db,User=User,Role=Role,Post=Post)


if __name__=='main':
  app.run()