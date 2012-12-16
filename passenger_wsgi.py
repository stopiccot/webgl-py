import sys, os
INTERP = os.path.join(os.environ['HOME'], 'flask_env', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from app import app as application
#app.app.run()

if __name__ == "__main__":
    application.run(host='0.0.0.0')