from app import app
from app.models import Employee, MenuItem, AddOnItem

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Employee': Employee, 'MenuItem': MenuItem}
